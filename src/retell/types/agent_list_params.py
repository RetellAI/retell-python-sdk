# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentListParams", "FilterCriteria", "FilterCriteriaChannel"]


class AgentListParams(TypedDict, total=False):
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


class FilterCriteria(TypedDict, total=False):
    """Filters for listing agents. All provided filters are connected with AND."""

    channel: FilterCriteriaChannel

    query: str
    """
    Case-insensitive substring search over agent name, plus substring search over
    agent id.
    """
