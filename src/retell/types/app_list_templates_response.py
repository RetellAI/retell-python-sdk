# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AppListTemplatesResponse", "Item", "ItemTool"]


class ItemTool(BaseModel):
    description: str
    """Also the LLM-facing description when used as a mid-call tool."""

    display_name: str

    name: str
    """Unique tool name within the provider."""

    privacy_scope: Literal["standard", "pci"]
    """Privacy scope of an integration function."""

    timeout_ms: float
    """Per-invocation timeout for this tool, in milliseconds."""


class Item(BaseModel):
    description: str

    display_name: str

    provider: str
    """Provider name.

    Must be valid for the App's type; the supported providers per type are listed by
    list-app-templates.
    """

    tools: List[ItemTool]

    type: Literal["crm", "calendar", "knowledge_base", "support", "communication"]
    """App integration category."""


class AppListTemplatesResponse(BaseModel):
    has_more: bool
    """Whether more results are available."""

    items: List[Item]

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
