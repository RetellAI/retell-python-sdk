# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    filter_criteria: object
    """Filter criteria for chats to retrieve."""

    limit: int
    """Maximum number of chats to return."""

    pagination_key: str
    """Opaque pagination cursor from a previous response."""

    skip: int
    """Number of records to skip for pagination."""

    sort_order: Literal["ascending", "descending"]
    """Sort chats by `start_timestamp` in ascending or descending order."""
