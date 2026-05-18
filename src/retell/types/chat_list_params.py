# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    filter_criteria: object
    """Filter criteria for chats to retrieve."""

    include_total: bool
    """
    Whether to include `total` (count of all chats matching `filter_criteria`,
    ignoring `limit`/`skip`/`pagination_key`) in the response. Defaults to false.
    Each enabled request triggers an additional aggregate query, so opt in only when
    the total is needed.
    """

    limit: int
    """Maximum number of chats to return."""

    pagination_key: str
    """Opaque pagination cursor from a previous response."""

    skip: int
    """Number of records to skip for pagination."""

    sort_order: Literal["ascending", "descending"]
    """Sort chats by `start_timestamp` in ascending or descending order."""
