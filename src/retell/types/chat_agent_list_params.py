# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChatAgentListParams"]


class ChatAgentListParams(TypedDict, total=False):
    limit: int
    """A limit on the number of objects to be returned.

    Limit can range between 1 and 1000, and the default is 1000.
    """

    pagination_key: str
    """The pagination key to continue fetching the next page of agents.

    Pagination key is represented by a agent id, pagination key and version pair is
    exclusive (not included in the fetched page). If not set, will start from the
    beginning.
    """

    pagination_key_version: int
    """Specifies the version of the agent associated with the pagination_key.

    When paginating, both the pagination_key and its version must be provided to
    ensure consistent ordering and to fetch the next page correctly.
    """
