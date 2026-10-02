// Search Edgepedia and read an article through its MCP server. Node 18+, no dependencies.
const URL = 'https://www.edgechat.ai/mcp';

async function call(tool, args) {
  const response = await fetch(URL, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json, text/event-stream',
      'MCP-Protocol-Version': '2025-06-18',
    },
    body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'tools/call', params: { name: tool, arguments: args } }),
  });
  const { result } = await response.json();
  return JSON.parse(result.content[0].text);
}

const subject = process.argv.slice(2).join(' ') || 'Mount Fuji';
const [first] = (await call('search', { query: subject })).results;
console.log(first.title, first.url);
const article = await call('fetch', { id: first.id, citations: false });
console.log(article.text.slice(0, 600));
console.log('\n' + article.metadata.credit);
