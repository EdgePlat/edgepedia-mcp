"""Connect a Google ADK agent to Edgepedia's keyless Streamable HTTP MCP server.

Requires:
    pip install google-adk mcp

Set GEMINI_API_KEY (or configure Vertex AI) before running the agent with an LLM.
Run with ``--check`` to verify live tool discovery against https://www.edgepedia.org/mcp
without calling an LLM.
"""

from __future__ import annotations

import asyncio
import os
import sys

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import McpToolset, StreamableHTTPConnectionParams

EDGEPEDIA_MCP_URL = "https://www.edgepedia.org/mcp"
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.7-flash")


def build_agent(model: str = DEFAULT_MODEL) -> tuple[LlmAgent, McpToolset]:
    """Create a Google ADK LlmAgent wired to Edgepedia's read-only MCP server."""
    toolset = McpToolset(
        connection_params=StreamableHTTPConnectionParams(url=EDGEPEDIA_MCP_URL),
    )
    agent = LlmAgent(
        model=model,
        name="edgepedia_assistant",
        instruction=(
            "Use Edgepedia tools to look up facts about people, places, events, "
            "and concepts across 31 languages. Pass a subject name to `search`, "
            "then call `fetch` with the article ID for full cited Markdown. "
            "Always link each article you use and include its `credit` line."
        ),
        tools=[toolset],
    )
    return agent, toolset


async def verify_mcp_connection() -> list[str]:
    """Discover tools live from https://www.edgepedia.org/mcp and close cleanly."""
    _, toolset = build_agent()
    try:
        tools = await toolset.get_tools()
        return [tool.name for tool in tools]
    finally:
        await toolset.close()


if __name__ == "__main__":
    if "--check" in sys.argv:
        tool_names = asyncio.run(verify_mcp_connection())
        print(f"Connected to {EDGEPEDIA_MCP_URL}; discovered tools: {', '.join(tool_names)}")
    else:
        agent, _ = build_agent()
        print(
            f"Initialized Google ADK agent '{agent.name}' using {EDGEPEDIA_MCP_URL}. "
            "Run with --check to test live MCP tool discovery, or wire `agent` into "
            "an ADK Runner / `adk web`."
        )
