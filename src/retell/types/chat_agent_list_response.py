# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ChatAgentListResponse", "Item", "ItemTags"]


class ItemTags(BaseModel):
    dynamic_variables: Optional[Dict[str, str]] = None

    version: Optional[int] = None


class Item(BaseModel):
    agent_id: str
    """Unique id of agent."""

    agent_name: str
    """The name of the agent. Only used for your own reference."""

    channel: Literal["voice", "chat"]

    tags: Dict[str, ItemTags]
    """Authoritative root tags for this agent, keyed by tag name."""

    user_modified_timestamp: int
    """User modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """


class ChatAgentListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
