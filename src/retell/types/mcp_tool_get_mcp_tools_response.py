# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .mcp_tool_definition import McpToolDefinition

__all__ = ["McpToolGetMcpToolsResponse"]

McpToolGetMcpToolsResponse: TypeAlias = List[McpToolDefinition]
