# Provide MCP

## Goal

Provide AI assistants access to the A12 Widget documentation (~120 markdown files) via MCP (Model Context Protocol), enabling semantic search and contextual retrieval.

## Solution

Use [mcp-documentation-server](https://github.com/andrea9293/mcp-documentation-server) - a TypeScript MCP server that provides document storage with semantic search via embeddings.

## Implementation

### 1. Loader script

Created `scripts/load_docs_to_mcp.py` using the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk). The script:

1. Connects to the server via stdio transport (spawning `npx -y @andrea9293/mcp-documentation-server`)
2. **Flush**: Deletes all existing documents
3. **Fill**: Copies markdown files to the uploads folder, then calls `process_uploads`
4. **Verify**: Confirms document count (some files may be deduplicated)

### 2. README updates

Added MCP setup instructions with two options:
- Global: `claude mcp add a12-widgets-docs -- npx -y @andrea9293/mcp-documentation-server`
- Per-project: Add `.mcp.json` to project root

### 3. Document update workflow

```bash
python -m src.main                                    # scrape
python -m src.clean_markdown <version_dir>            # clean
python scripts/load_docs_to_mcp.py <version_dir>_clean  # load
```

## Tasks

- [x] Create `scripts/load_docs_to_mcp.py` loader script
- [x] Add `mcp>=1.25,<2` to `requirements.txt`
- [x] Add MCP setup instructions to README
- [x] Test with Claude Code (119 unique documents loaded)
