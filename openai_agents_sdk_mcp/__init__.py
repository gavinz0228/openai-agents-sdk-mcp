"""
OpenAI Agents SDK MCP Server
A Model Context Protocol server for querying OpenAI Agents SDK documentation.
"""

__version__ = "1.0.0"
__author__ = "Gavin Zhang"

from .server import start_server
from .documentation import (
    fetch_documentation_index,
    get_documentation_for_feature,
    fetch_documentation_content,
    load_or_refresh_index,
)

__all__ = [
    "start_server",
    "fetch_documentation_index",
    "get_documentation_for_feature",
    "fetch_documentation_content",
    "load_or_refresh_index",
]
