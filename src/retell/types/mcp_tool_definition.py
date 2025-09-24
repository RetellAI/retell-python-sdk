# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpToolDefinition"]


class McpToolDefinition(BaseModel):
    description: str
    """Description of what the MCP tool does."""

    input_schema: Dict[str, object] = FieldInfo(alias="inputSchema")
    """JSON schema defining the input parameters for the tool."""

    name: str
    """Name of the MCP tool."""
