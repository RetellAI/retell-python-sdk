# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ChatListParams",
    "FilterCriteria",
    "FilterCriteriaAgent",
    "FilterCriteriaChatID",
    "FilterCriteriaChatStatus",
    "FilterCriteriaChatSuccessful",
    "FilterCriteriaCombinedCost",
    "FilterCriteriaCombinedCostNumberFilter",
    "FilterCriteriaCombinedCostRangeFilter",
    "FilterCriteriaCustomAnalysisData",
    "FilterCriteriaCustomAnalysisDataStringFilter",
    "FilterCriteriaCustomAnalysisDataNumberFilter",
    "FilterCriteriaCustomAnalysisDataBooleanFilter",
    "FilterCriteriaCustomAnalysisDataRangeFilter",
    "FilterCriteriaCustomAnalysisDataEnumFilter",
    "FilterCriteriaCustomAnalysisDataPresentFilter",
    "FilterCriteriaCustomAttribute",
    "FilterCriteriaCustomAttributeStringFilter",
    "FilterCriteriaCustomAttributeNumberFilter",
    "FilterCriteriaCustomAttributeBooleanFilter",
    "FilterCriteriaCustomAttributeRangeFilter",
    "FilterCriteriaCustomAttributeEnumFilter",
    "FilterCriteriaCustomAttributePresentFilter",
    "FilterCriteriaDisconnectionReason",
    "FilterCriteriaDurationMs",
    "FilterCriteriaDurationMsNumberFilter",
    "FilterCriteriaDurationMsRangeFilter",
    "FilterCriteriaEndTimestamp",
    "FilterCriteriaEndTimestampNumberFilter",
    "FilterCriteriaEndTimestampRangeFilter",
    "FilterCriteriaStartTimestamp",
    "FilterCriteriaStartTimestampNumberFilter",
    "FilterCriteriaStartTimestampRangeFilter",
    "FilterCriteriaUserSentiment",
]


class ChatListParams(TypedDict, total=False):
    filter_criteria: FilterCriteria
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


class FilterCriteriaAgent(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to filter on."""

    version: Iterable[float]
    """Specific versions to filter on. If not provided, all versions are included."""


class FilterCriteriaChatID(TypedDict, total=False):
    """Filter by chat ID."""

    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaChatStatus(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["ongoing", "ended", "error"]]]


class FilterCriteriaChatSuccessful(TypedDict, total=False):
    """Filter by whether the chat was successful."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]


class FilterCriteriaCombinedCostNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaCombinedCostRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaCombinedCost: TypeAlias = Union[
    FilterCriteriaCombinedCostNumberFilter, FilterCriteriaCombinedCostRangeFilter
]


class FilterCriteriaCustomAnalysisDataStringFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAnalysisDataNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAnalysisDataBooleanFilter(TypedDict, total=False):
    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAnalysisDataRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAnalysisDataEnumFilter(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAnalysisDataPresentFilter(TypedDict, total=False):
    op: Required[Literal["pr", "np"]]
    """pr: present (has value), np: not present"""

    type: Required[Literal["present"]]

    key: str
    """The field name to filter on."""


FilterCriteriaCustomAnalysisData: TypeAlias = Union[
    FilterCriteriaCustomAnalysisDataStringFilter,
    FilterCriteriaCustomAnalysisDataNumberFilter,
    FilterCriteriaCustomAnalysisDataBooleanFilter,
    FilterCriteriaCustomAnalysisDataRangeFilter,
    FilterCriteriaCustomAnalysisDataEnumFilter,
    FilterCriteriaCustomAnalysisDataPresentFilter,
]


class FilterCriteriaCustomAttributeStringFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAttributeNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAttributeBooleanFilter(TypedDict, total=False):
    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAttributeRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAttributeEnumFilter(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomAttributePresentFilter(TypedDict, total=False):
    op: Required[Literal["pr", "np"]]
    """pr: present (has value), np: not present"""

    type: Required[Literal["present"]]

    key: str
    """The field name to filter on."""


FilterCriteriaCustomAttribute: TypeAlias = Union[
    FilterCriteriaCustomAttributeStringFilter,
    FilterCriteriaCustomAttributeNumberFilter,
    FilterCriteriaCustomAttributeBooleanFilter,
    FilterCriteriaCustomAttributeRangeFilter,
    FilterCriteriaCustomAttributeEnumFilter,
    FilterCriteriaCustomAttributePresentFilter,
]


class FilterCriteriaDisconnectionReason(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[
        List[
            Literal[
                "user_hangup",
                "agent_hangup",
                "call_transfer",
                "voicemail_reached",
                "ivr_reached",
                "inactivity",
                "max_duration_reached",
                "concurrency_limit_reached",
                "no_concurrency_fallback",
                "no_valid_payment",
                "scam_detected",
                "dial_busy",
                "dial_failed",
                "dial_no_answer",
                "invalid_destination",
                "telephony_provider_permission_denied",
                "telephony_provider_unavailable",
                "sip_routing_error",
                "marked_as_spam",
                "user_declined",
                "error_llm_websocket_open",
                "error_llm_websocket_lost_connection",
                "error_llm_websocket_runtime",
                "error_llm_websocket_corrupt_payload",
                "error_no_audio_received",
                "error_asr",
                "error_retell",
                "error_unknown",
                "error_user_not_joined",
                "registered_call_timeout",
                "transfer_bridged",
                "transfer_cancelled",
                "manual_stopped",
            ]
        ]
    ]


class FilterCriteriaDurationMsNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaDurationMsRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaDurationMs: TypeAlias = Union[FilterCriteriaDurationMsNumberFilter, FilterCriteriaDurationMsRangeFilter]


class FilterCriteriaEndTimestampNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaEndTimestampRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaEndTimestamp: TypeAlias = Union[
    FilterCriteriaEndTimestampNumberFilter, FilterCriteriaEndTimestampRangeFilter
]


class FilterCriteriaStartTimestampNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaStartTimestampRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaStartTimestamp: TypeAlias = Union[
    FilterCriteriaStartTimestampNumberFilter, FilterCriteriaStartTimestampRangeFilter
]


class FilterCriteriaUserSentiment(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["Negative", "Positive", "Neutral", "Unknown"]]]


class FilterCriteria(TypedDict, total=False):
    """Filter criteria for chats to retrieve."""

    agent: Iterable[FilterCriteriaAgent]
    """Filter by agent(s). Agent filters are connected by OR."""

    chat_id: FilterCriteriaChatID
    """Filter by chat ID."""

    chat_status: FilterCriteriaChatStatus

    chat_successful: FilterCriteriaChatSuccessful
    """Filter by whether the chat was successful."""

    combined_cost: FilterCriteriaCombinedCost
    """Filter by combined cost of the chat."""

    custom_analysis_data: Iterable[FilterCriteriaCustomAnalysisData]
    """Filter by custom analysis data fields."""

    custom_attributes: Iterable[FilterCriteriaCustomAttribute]
    """Filter by custom attributes fields."""

    disconnection_reason: FilterCriteriaDisconnectionReason

    duration_ms: FilterCriteriaDurationMs
    """Filter by chat duration in milliseconds."""

    end_timestamp: FilterCriteriaEndTimestamp
    """Filter by chat end timestamp (epoch ms)."""

    start_timestamp: FilterCriteriaStartTimestamp
    """Filter by chat start timestamp (epoch ms)."""

    user_sentiment: FilterCriteriaUserSentiment
