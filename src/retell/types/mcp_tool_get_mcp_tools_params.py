# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["McpToolGetMcpToolsParams"]


class McpToolGetMcpToolsParams(TypedDict, total=False):
    mcp_id: Required[str]
    """The ID of the MCP server to get tools from."""

    component_id: str
    """The ID of the component if the MCP server is configured under a component."""

    version: int
    """Optional version of the agent to use for this request.

    Default to latest version.
    """
