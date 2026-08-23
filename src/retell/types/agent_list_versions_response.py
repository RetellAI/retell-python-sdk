# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentListVersionsResponse", "Item"]


class Item(BaseModel):
    is_published: bool
    """Whether the agent version is published."""

    last_modification_timestamp: int
    """Last modification timestamp in milliseconds since epoch."""

    version: int
    """Version number of the agent."""

    base_version: Optional[int] = None
    """Version that this agent version was based on."""

    version_description: Optional[str] = None
    """Optional description of the agent version."""

    version_title: Optional[str] = None
    """Optional title of the agent version."""


class AgentListVersionsResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
