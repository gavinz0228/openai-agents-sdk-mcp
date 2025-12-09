
# Project Goal
It's to build a MCP tool plugin that provides documentation for OpenAI Agents SDK. The documentation should be extracted from this official website: https://openai.github.io/openai-agents-python/

# What it does
This MCP tool plugin has two main functionalities:
 - It provides LLM with a list of available modules/features from the OpenAI Agents SDK documentation website.
 - It allows LLM to query specific information of a module/feature from the OpenAI Agents SDK documentation, then it request the corresponding webpage and extract the relevant information to return to the LLM.

 # Technical Details
 - Use Python to build the MCP tool, and use venv to manage dependencies.
 - Use LLM to convert the HTML content of the documentation webpage into a map, the the feature/topic as the key, and the link as value.
 - If any of the links are not working, or  docs_index.json is missing or the last updated time of docs_index.json is over 1 day, re-fetch the indices to update docs_index.json

 # Other Requirements
  - When any features are added or updated, update the read me file accordingly.
  