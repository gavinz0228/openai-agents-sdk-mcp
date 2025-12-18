# Installation Guide

This guide covers different ways to install and use the OpenAI Agents SDK MCP server.

## Table of Contents

1. [Install from PyPI (Recommended)](#install-from-pypi)
2. [Install from Source](#install-from-source)
3. [Development Installation](#development-installation)
4. [Configuration](#configuration)
5. [Usage](#usage)

## Install from PyPI

Once published to PyPI, you can install with:

```bash
pip install openai-agents-sdk-mcp
```

### Quick Start

1. **Set up your API key**:
   ```bash
   export OPENAI_API_KEY="sk-your-api-key-here"
   ```

2. **Start the MCP server**:
   ```bash
   openai-agents-sdk-mcp
   ```

3. **Use the CLI tool** (optional):
   ```bash
   # List all documentation topics
   openai-agents-docs

   # Search for specific documentation
   openai-agents-docs "handoffs"
   openai-agents-docs "how to stream responses"
   ```

## Install from Source

### 1. Clone the Repository

```bash
git clone https://github.com/gavinz0228/openai-agents-sdk-mcp.git
cd openai-agents-sdk-mcp
```

### 2. Install the Package

```bash
# Install in user mode
pip install .

# Or install in editable mode (for development)
pip install -e .
```

### 3. Set Up Environment

```bash
# Create .env file
echo "OPENAI_API_KEY=sk-your-api-key-here" > .env
```

### 4. Run the Server

```bash
openai-agents-sdk-mcp
```

## Development Installation

For contributors and developers:

```bash
# Clone the repository
git clone https://github.com/gavinz0228/openai-agents-sdk-mcp.git
cd openai-agents-sdk-mcp

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with dev dependencies
pip install -e ".[dev]"

# Set up environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run tests
python test_mcp.py
```

## Configuration

### Environment Variables

The server requires an OpenAI API key. You can provide it in several ways:

1. **Environment variable**:
   ```bash
   export OPENAI_API_KEY="sk-your-api-key-here"
   ```

2. **.env file** (in the working directory):
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

3. **In MCP client config** (see below)

### MCP Client Configuration

#### Claude Desktop

Location: `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS)

```json
{
  "mcpServers": {
    "openai-agents-sdk-docs": {
      "command": "openai-agents-sdk-mcp",
      "env": {
        "OPENAI_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

**Note**: If installed in a virtual environment, use the full path:

```json
{
  "mcpServers": {
    "openai-agents-sdk-docs": {
      "command": "/path/to/.venv/bin/openai-agents-sdk-mcp"
    }
  }
}
```

#### VS Code / Cursor

Add to workspace settings:

```json
{
  "mcp.servers": {
    "openai-agents-sdk-docs": {
      "command": "openai-agents-sdk-mcp",
      "env": {
        "OPENAI_API_KEY": "sk-your-api-key-here"
      }
    }
  }
}
```

## Usage

### As an MCP Server

Once configured in your MCP client, the server provides two tools:

1. **list_documentation_topics** - List all available documentation
2. **get_documentation** - Query specific documentation

Example queries in Claude:
- "List all OpenAI Agents SDK documentation topics"
- "Get documentation for handoffs"
- "How do I use streaming in OpenAI Agents?"

### As a Python Library

```python
from openai_agents_sdk_mcp import (
    load_or_refresh_index,
    get_documentation_for_feature
)

# Load documentation index
doc_map = load_or_refresh_index()
print(f"Found {len(doc_map)} topics")

# Find documentation for a feature
topic, url = get_documentation_for_feature("handoffs")
if topic:
    print(f"Topic: {topic}")
    print(f"URL: {url}")
```

### Command Line Interface

```bash
# List all documentation topics
openai-agents-docs

# Search for specific documentation
openai-agents-docs "handoffs"
openai-agents-docs "streaming"
openai-agents-docs "how to use guardrails"
```

## Verify Installation

Test that everything is working:

```bash
# Check package is installed
pip show openai-agents-sdk-mcp

# Test the CLI
openai-agents-docs "agents"

# Test the MCP server (requires MCP client or test script)
python -m pytest test_mcp.py  # If you have the test file
```

## Troubleshooting

### Command not found

If `openai-agents-sdk-mcp` is not found:

1. Ensure the package is installed: `pip list | grep openai-agents-sdk-mcp`
2. Check your PATH includes pip's bin directory
3. Try using: `python -m openai_agents_sdk_mcp.server`

### API Key Issues

If you see "OPENAI_API_KEY environment variable not set":

1. Verify the key is set: `echo $OPENAI_API_KEY`
2. Check the .env file exists in the working directory
3. Ensure the key is valid and active

### Import Errors

If you get import errors:

```bash
# Reinstall the package
pip uninstall openai-agents-sdk-mcp
pip install openai-agents-sdk-mcp

# Or from source
pip install -e .
```

## Uninstallation

```bash
pip uninstall openai-agents-sdk-mcp
```

## Support

For issues and questions:
- GitHub Issues: https://github.com/gavinz0228/openai-agents-sdk-mcp/issues
- Documentation: https://github.com/gavinz0228/openai-agents-sdk-mcp#readme
