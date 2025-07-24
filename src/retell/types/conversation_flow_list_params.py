# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConversationFlowListParams"]


class ConversationFlowListParams(TypedDict, total=False):
    limit: int
    """Limit the number of conversation flows returned.

    Default 1000, Max 1000. To retrieve more than 1000, use pagination_key to
    continue fetching the next page.
    """

    pagination_key: str
    """The pagination key to continue fetching the next page of conversation flows.

    Pagination key is represented by a conversation flow id here, and it's exclusive
    (not included in the fetched conversation flows). The last conversation flow id
    from the list conversation flows is usually used as pagination key here. If not
    set, will start from the beginning.
    """

    pagination_key_version: int
    """
    The version of the conversation flow to continue fetching the next page of
    conversation flows.
    """
