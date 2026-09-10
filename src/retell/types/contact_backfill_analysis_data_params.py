# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ContactBackfillAnalysisDataParams",
    "BackfillCallFilter",
    "BackfillCallFilterAgent",
    "BackfillCallFilterStartTimestamp",
    "BackfillCallFilterStartTimestampNumberFilter",
    "BackfillCallFilterStartTimestampRangeFilter",
]


class ContactBackfillAnalysisDataParams(TypedDict, total=False):
    backfill_attributes: Required[SequenceNotStr[str]]

    backfill_call_filter: BackfillCallFilter


class BackfillCallFilterAgent(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to filter on."""

    version: Iterable[float]
    """Specific versions to filter on. If omitted or empty, all versions are included."""


class BackfillCallFilterStartTimestampNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class BackfillCallFilterStartTimestampRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


BackfillCallFilterStartTimestamp: TypeAlias = Union[
    BackfillCallFilterStartTimestampNumberFilter, BackfillCallFilterStartTimestampRangeFilter
]


class BackfillCallFilter(TypedDict, total=False):
    agent: Iterable[BackfillCallFilterAgent]
    """Filter calls by agent. Agents are OR-connected."""

    start_timestamp: BackfillCallFilterStartTimestamp
    """Filter calls by start timestamp (epoch ms)."""
