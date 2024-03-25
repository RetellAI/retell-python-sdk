# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CallListParams", "FilterCriteria"]


class CallListParams(TypedDict, total=False):
    filter_criteria: FilterCriteria

    limit: int
    """Limit the number of calls returned."""

    sort_order: Literal["ascending", "descending"]
    """
    The calls will be sorted by `start_timestamp`, whether to return the calls in
    ascending or descending order.
    """


class FilterCriteria(TypedDict, total=False):
    after_end_timestamp: int
    """Inclusive. Filter calls that end on or after this timestamp."""

    after_start_timestamp: int
    """Inclusive. Filter calls that start on or after this timestamp."""

    agent_id: List[str]
    """Only retrieve calls that are made with specific agent(s)."""

    before_end_timestamp: int
    """Exclusive. Filter calls that end before this timestamp."""

    before_start_timestamp: int
    """Exclusive. Filter calls that start before this timestamp."""
