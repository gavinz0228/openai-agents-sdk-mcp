#!/usr/bin/env python3
"""
Test script for the OpenAI Agents SDK MCP server
"""

import asyncio
import json
import sys
import os
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_mcp_server():
    """Test the MCP server locally."""
    
    # Get the absolute path to the virtual environment's Python
    venv_python = Path(__file__).parent / ".venv" / "bin" / "python"
    if not venv_python.exists():
        # Fallback to system python
        venv_python = sys.executable
    
    # Server parameters
    server_params = StdioServerParameters(
        command=str(venv_python),
        args=["-m", "openai_agents_sdk_mcp.server"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            
            print("=" * 80)
            print("Testing MCP Server for OpenAI Agents SDK Documentation")
            print("=" * 80)
            
            # Test 1: List available tools
            print("\n1. Listing available tools...")
            tools = await session.list_tools()
            print(f"Found {len(tools.tools)} tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description[:100]}...")
            
            # Test 2: List documentation topics
            print("\n2. Testing 'list_documentation_topics' tool...")
            result = await session.call_tool("list_documentation_topics", {})
            print("Response preview:")
            content = result.content[0].text
            lines = content.split('\n')
            for line in lines[:20]:
                print(line)
            if len(lines) > 20:
                print(f"... ({len(lines) - 20} more lines)")
            
            # Test 3: Get documentation for a specific feature
            print("\n3. Testing 'get_documentation' tool with query 'handoffs'...")
            result = await session.call_tool("get_documentation", {
                "query": "handoffs",
                "include_content": False  # Don't include full content for test
            })
            print("Response:")
            print(result.content[0].text)
            
            # Test 4: Natural language query
            print("\n4. Testing natural language query 'how to stream responses'...")
            result = await session.call_tool("get_documentation", {
                "query": "how to stream responses",
                "include_content": False
            })
            print("Response:")
            print(result.content[0].text)
            
            print("\n" + "=" * 80)
            print("All tests completed successfully!")
            print("=" * 80)


if __name__ == "__main__":
    asyncio.run(test_mcp_server())
