# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatAgentListParams", "FilterCriteria", "FilterCriteriaChannel", "FilterCriteriaIsTransferAgent"]


class ChatAgentListParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return."""

    pagination_key: str
    """Pagination key for fetching the next page."""

    sort_order: Literal["ascending", "descending"]
    """Sort order for results."""

    filter_criteria: FilterCriteria
    """Filters for listing agents. All provided filters are connected with AND."""


class FilterCriteriaChannel(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[Literal["voice", "chat"]]


class FilterCriteriaIsTransferAgent(TypedDict, total=False):
    """Filter by whether the agent is a transfer agent."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]


class FilterCriteria(TypedDict, total=False):
    """Filters for listing agents. All provided filters are connected with AND."""

    channel: FilterCriteriaChannel

    is_transfer_agent: FilterCriteriaIsTransferAgent
    """Filter by whether the agent is a transfer agent."""

    query: str
    """
    Case-insensitive substring search over agent name, plus substring search over
    agent id.
    """
