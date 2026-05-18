# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .chat_response import ChatResponse

__all__ = ["ChatListResponse", "Item"]


class Item(ChatResponse):
    """V3 list chats response. Transcript fields are intentionally omitted."""

    pass


class ChatListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""

    total: Optional[int] = None
    """Total number of chats matching `filter_criteria`.

    Only present when `include_total` is true.
    """
