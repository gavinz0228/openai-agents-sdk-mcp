# OpenAI Agents SDK MCP Tool

A Model Context Protocol (MCP) tool plugin that provides documentation for the OpenAI Agents SDK by extracting and indexing content from the official documentation website: https://openai.github.io/openai-agents-python/

## Features

### 1. **Automatic Documentation Indexing**
- Fetches and parses the OpenAI Agents SDK documentation website
- Extracts all navigation links and topics
- Creates a structured JSON map of topics to URLs
- Saves to `docs_index.json` for quick access

### 2. **Smart Index Management**
The tool automatically manages the documentation index with intelligent caching:

- **Missing Index Detection**: Automatically fetches fresh index if `docs_index.json` doesn't exist
- **Staleness Check**: Refreshes index if older than 1 day (configurable)
- **Link Validation**: Verifies all documentation links are working
- **Broken Link Recovery**: Automatically re-fetches index if any links are broken

### 3. **AI-Powered Feature Search**
Uses OpenAI's GPT-4o-mini to intelligently match user queries to documentation:

- Accepts natural language queries (e.g., "how do I trace my agent")
- Finds the closest matching documentation topic
- Fetches and displays relevant documentation content
- Works with fuzzy matching and conversational queries

## Installation

1. **Clone the repository**:
```bash
cd /Users/gavin/Projects/openai-agent-sdk-mcp
```

2. **Set up Python virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure API key**:
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=sk-your-api-key-here
```

## Usage

### Generate/Refresh Documentation Index

```bash
python openai_agents_sdk_mcp.py
```

This will:
- Fetch the latest documentation structure
- Extract all topics and links
- Save to `docs_index.json`
- Display all available topics

### Search for Documentation

```bash
python openai_agents_sdk_mcp.py "feature name or query"
```

**Examples**:
```bash
# Simple feature name
python openai_agents_sdk_mcp.py "handoffs"

# Natural language query
python openai_agents_sdk_mcp.py "how do I stream responses"

# Topic search
python openai_agents_sdk_mcp.py "tracing and debugging"

# Multiple words
python openai_agents_sdk_mcp.py "realtime voice"
```

The tool will:
1. Load or refresh the documentation index (if stale)
2. Use AI to find the best matching topic
3. Display the matched topic and URL
4. Fetch and show a preview of the documentation content

## How It Works

### Index Management

```python
# The index is automatically managed:
# 1. Checks if docs_index.json exists
if not exists:
    fetch_fresh_index()

# 2. Checks if index is older than 1 day
if age > 1_day:
    fetch_fresh_index()

# 3. Validates all links are working
if broken_links_found:
    fetch_fresh_index()
```

### AI-Powered Matching

The tool uses OpenAI's GPT-4o-mini to match user queries to documentation topics:

1. Loads all available topics from the index
2. Sends user query + topic list to the LLM
3. LLM identifies the most relevant topic
4. Returns the matching topic and URL

This provides intelligent matching even for:
- Typos and misspellings
- Natural language questions
- Partial or fuzzy matches
- Related concepts

## Configuration

### Constants (in `openai_agents_sdk_mcp.py`)

```python
DOCS_INDEX_FILE = "docs_index.json"  # Index file name
INDEX_MAX_AGE_DAYS = 1               # Maximum age before refresh
```

### Environment Variables

- `OPENAI_API_KEY` - Required for AI-powered search functionality

## Files

- `openai_agents_sdk_mcp.py` - Main script
- `docs_index.json` - Cached documentation index (auto-generated)
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this)
- `.gitignore` - Git ignore rules (protects API key)

## Dependencies

- `requests` - HTTP requests for fetching web pages
- `beautifulsoup4` - HTML parsing
- `lxml` - XML/HTML parser
- `openai` - OpenAI API client for AI-powered search
- `python-dotenv` - Environment variable management

## Example Output

### Index Generation
```
Fetching OpenAI Agents SDK documentation index...
Fetching fresh documentation index...
Index refreshed with 80 topics and saved to 'docs_index.json'.

Found 80 documentation topics/features:
...
```

### Feature Search
```
Searching for documentation on: handoffs

Loaded existing index with 80 topics.
Verifying documentation links...
  ✓ All links are valid
✓ Found matching topic: Handoffs
  URL: https://openai.github.io/openai-agents-python/handoffs/

Fetching documentation content...
================================================================================
Handoffs - OpenAI Agents SDK
...
```

## License

This project is designed to work with the OpenAI Agents SDK documentation. Please refer to OpenAI's terms of service for API usage.
