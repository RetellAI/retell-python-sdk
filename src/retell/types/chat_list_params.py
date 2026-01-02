# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ChatListParams"]


class ChatListParams(TypedDict, total=False):
    limit: int
    """Limit the number of chats returned.

    Default 50, Max 1000. To retrieve more than 1000, use pagination_key to continue
    fetching the next page.
    """

    pagination_key: str
    """The pagination key to continue fetching the next page of chats.

    Pagination key is represented by a chat id here, and it's exclusive (not
    included in the fetched chats). The last chat id from the list chats is usually
    used as pagination key here. If not set, will start from the beginning.
    """

    sort_order: Literal["ascending", "descending"]
    """
    The chats will be sorted by `start_timestamp`, whether to return the chats in
    ascending or descending order.
    """
