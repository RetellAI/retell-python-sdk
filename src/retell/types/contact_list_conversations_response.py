# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ContactListConversationsResponse", "Item", "ItemContactCall", "ItemContactChat"]


class ItemContactCall(BaseModel):
    call_id: str

    type: Literal["call"]

    direction: Optional[Literal["inbound", "outbound"]] = None
    """Direction of the call."""

    disconnection_reason: Optional[str] = None
    """Reason the call ended."""

    duration_ms: Optional[float] = None
    """Duration of the call in milliseconds."""

    sentiment: Optional[Literal["Negative", "Positive", "Neutral", "Unknown"]] = None
    """User sentiment from post-call analysis."""

    start_timestamp: Optional[float] = None
    """Epoch milliseconds when the call started."""

    successful: Optional[bool] = None
    """Whether the call was deemed successful by post-call analysis."""

    summary: Optional[str] = None
    """Post-call analysis summary."""


class ItemContactChat(BaseModel):
    chat_id: str

    type: Literal["chat"]

    direction: Optional[Literal["inbound", "outbound"]] = None
    """Direction of the chat."""

    disconnection_reason: Optional[str] = None
    """Reason the chat ended."""

    duration_ms: Optional[float] = None
    """Duration of the chat in milliseconds."""

    sentiment: Optional[Literal["Negative", "Positive", "Neutral", "Unknown"]] = None
    """User sentiment from post-chat analysis."""

    start_timestamp: Optional[float] = None
    """Epoch milliseconds when the chat started."""

    successful: Optional[bool] = None
    """Whether the chat was deemed successful by post-chat analysis."""

    summary: Optional[str] = None
    """Post-chat analysis summary."""


Item: TypeAlias = Union[ItemContactCall, ItemContactChat]


class ContactListConversationsResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more conversations exist beyond the returned window."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Base64url-encoded pagination key.

    Pass as `pagination_key` query parameter to fetch the next page.
    """
