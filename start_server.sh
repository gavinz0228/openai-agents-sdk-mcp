#!/bin/bash
# Start the OpenAI Agents SDK MCP server

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate virtual environment and run server
cd "$SCRIPT_DIR"

if [ -d ".venv" ]; then
    source .venv/bin/activate
    python server.py
else
    echo "Error: Virtual environment not found at $SCRIPT_DIR/.venv"
    echo "Please run: python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi
