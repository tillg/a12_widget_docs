#!/usr/bin/env python3
"""
Load A12 Widget documentation into the MCP documentation server.

Usage:
    python scripts/load_docs_to_mcp.py <docs_directory>

Example:
    python scripts/load_docs_to_mcp.py A12_Widget_Documentation_38.1.1_clean
"""

import asyncio
import json
import re
import shutil
import sys
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def call_tool(session: ClientSession, name: str, arguments: dict = None):
    """Call an MCP tool and return the result."""
    result = await session.call_tool(name, arguments or {})
    if result.isError:
        raise RuntimeError(f"Tool {name} failed: {result.content}")
    # Extract text content from the result
    for content in result.content:
        if hasattr(content, "text"):
            return content.text
    return None


async def load_docs(docs_dir: Path):
    """Load documentation files into the MCP server."""
    if not docs_dir.exists():
        print(f"Error: Directory not found: {docs_dir}")
        sys.exit(1)

    # Find all markdown files
    md_files = list(docs_dir.rglob("*.md"))
    if not md_files:
        print(f"Error: No markdown files found in {docs_dir}")
        sys.exit(1)

    print(f"Found {len(md_files)} markdown files to load")

    # Connect to the MCP server via stdio
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@andrea9293/mcp-documentation-server"],
    )

    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the session
                await session.initialize()
                print("Connected to MCP documentation server")

                # Step 1: Flush - get all existing documents and delete them
                print("\n--- Flushing existing documents ---")
                list_result = await call_tool(session, "list_documents")

                if list_result:
                    try:
                        docs = json.loads(list_result)
                        if docs:
                            print(f"Found {len(docs)} existing documents to delete")
                            for doc in docs:
                                doc_id = doc.get("id") or doc.get("name")
                                if doc_id:
                                    await call_tool(session, "delete_document", {"id": doc_id})
                                    print(f"  Deleted: {doc_id}")
                            print(f"Deleted {len(docs)} documents")
                        else:
                            print("No existing documents to delete")
                    except json.JSONDecodeError:
                        print("No existing documents (or empty response)")
                else:
                    print("No existing documents")

                # Step 2: Fill - copy files to uploads folder and process
                print("\n--- Loading new documents ---")
                uploads_path_result = await call_tool(session, "get_uploads_path")

                if not uploads_path_result:
                    print("Error: Could not get uploads path from server")
                    sys.exit(1)

                # Parse the uploads path from the response
                # Response format: "Uploads folder path: /path/to/uploads\n\nYou can place..."
                match = re.search(r"Uploads folder path:\s*(\S+)", uploads_path_result)
                if match:
                    uploads_path = Path(match.group(1))
                else:
                    # Fallback: try first line
                    uploads_path = Path(uploads_path_result.strip().split("\n")[0].strip())
                print(f"Uploads path: {uploads_path}")

                # Create uploads directory if needed
                uploads_path.mkdir(parents=True, exist_ok=True)

                # Clear uploads folder first
                for f in uploads_path.iterdir():
                    if f.is_file():
                        f.unlink()

                # Copy markdown files to uploads folder
                print(f"Copying {len(md_files)} files to uploads folder...")
                for md_file in md_files:
                    # Create a flat filename from the relative path
                    rel_path = md_file.relative_to(docs_dir)
                    flat_name = str(rel_path).replace("/", "_").replace("\\", "_")
                    dest = uploads_path / flat_name
                    shutil.copy2(md_file, dest)

                print("Processing uploads...")
                process_result = await call_tool(session, "process_uploads")
                print("Upload processing complete")

                # Step 3: Verify - check document count
                print("\n--- Verifying ---")
                verify_result = await call_tool(session, "list_documents")

                loaded_count = 0
                if verify_result:
                    try:
                        docs = json.loads(verify_result)
                        loaded_count = len(docs) if docs else 0
                    except json.JSONDecodeError:
                        pass

                print(f"Files provided: {len(md_files)}")
                print(f"Documents loaded: {loaded_count}")

                if loaded_count == len(md_files):
                    print("\nSuccess! All documents loaded correctly.")
                elif loaded_count > 0:
                    diff = len(md_files) - loaded_count
                    print(f"\nSuccess! {loaded_count} unique documents loaded.")
                    print(f"({diff} files had duplicate content and were deduplicated)")
                else:
                    print("\nWarning: No documents appear to be loaded. Check server logs.")

    except FileNotFoundError:
        print("Error: Could not start MCP server.")
        print("Make sure you have Node.js and npx installed.")
        print("The server will be installed automatically via npx.")
        sys.exit(1)
    except Exception as e:
        print(f"Error connecting to MCP server: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)

    docs_dir = Path(sys.argv[1])
    if not docs_dir.is_absolute():
        docs_dir = Path.cwd() / docs_dir

    asyncio.run(load_docs(docs_dir))


if __name__ == "__main__":
    main()
