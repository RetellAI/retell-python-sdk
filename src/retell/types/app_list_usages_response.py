# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["AppListUsagesResponse", "Item", "ItemAgentAppUsage", "ItemKnowledgeBaseAppUsage"]


class ItemAgentAppUsage(BaseModel):
    agent_id: str

    agent_versions: List[float]
    """Agent versions referencing this app, largest first."""

    configured_timestamp: float
    """When this reference was last recorded, in milliseconds."""

    type: Literal["agent"]

    agent_name: Optional[str] = None
    """Current agent name; omitted if the agent was deleted."""


class ItemKnowledgeBaseAppUsage(BaseModel):
    configured_timestamp: float
    """When this reference was last recorded, in milliseconds."""

    knowledge_base_id: str

    type: Literal["knowledge_base"]

    knowledge_base_name: Optional[str] = None
    """Current knowledge base name; omitted if it was deleted."""


Item: TypeAlias = Union[ItemAgentAppUsage, ItemKnowledgeBaseAppUsage]


class AppListUsagesResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
