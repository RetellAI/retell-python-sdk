# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "CallListParams",
    "FilterCriteria",
    "FilterCriteriaAgent",
    "FilterCriteriaBatchCallID",
    "FilterCriteriaCallID",
    "FilterCriteriaCallIDStringFilter",
    "FilterCriteriaCallIDEnumFilter",
    "FilterCriteriaCallStatus",
    "FilterCriteriaCallSuccessful",
    "FilterCriteriaCallType",
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
    "FilterCriteriaDataStorageSetting",
    "FilterCriteriaDirection",
    "FilterCriteriaDisconnectionReason",
    "FilterCriteriaDurationMs",
    "FilterCriteriaDurationMsNumberFilter",
    "FilterCriteriaDurationMsRangeFilter",
    "FilterCriteriaDynamicVariable",
    "FilterCriteriaE2ELatencyP50",
    "FilterCriteriaE2ELatencyP50NumberFilter",
    "FilterCriteriaE2ELatencyP50RangeFilter",
    "FilterCriteriaEndTimestamp",
    "FilterCriteriaEndTimestampNumberFilter",
    "FilterCriteriaEndTimestampRangeFilter",
    "FilterCriteriaFromNumber",
    "FilterCriteriaInVoicemail",
    "FilterCriteriaMetadata",
    "FilterCriteriaMetadataStringFilter",
    "FilterCriteriaMetadataNumberFilter",
    "FilterCriteriaMetadataBooleanFilter",
    "FilterCriteriaMetadataRangeFilter",
    "FilterCriteriaMetadataEnumFilter",
    "FilterCriteriaMetadataPresentFilter",
    "FilterCriteriaStartTimestamp",
    "FilterCriteriaStartTimestampNumberFilter",
    "FilterCriteriaStartTimestampRangeFilter",
    "FilterCriteriaToNumber",
    "FilterCriteriaToolCall",
    "FilterCriteriaToolCallLatencyMs",
    "FilterCriteriaToolCallLatencyMsNumberFilter",
    "FilterCriteriaToolCallLatencyMsRangeFilter",
    "FilterCriteriaToolCallSuccess",
    "FilterCriteriaUserSentiment",
]


class CallListParams(TypedDict, total=False):
    filter_criteria: FilterCriteria
    """Filter criteria for calls. All conditions are implicitly connected with AND."""

    include_total: bool
    """
    Whether to include `total` (count of all calls matching `filter_criteria`,
    ignoring `limit`/`skip`/`pagination_key`) in the response. Defaults to false.
    Each enabled request triggers an additional aggregate query, so opt in only when
    the total is needed.
    """

    limit: int
    """Maximum number of calls to return."""

    pagination_key: str
    """Opaque pagination cursor from a previous response."""

    skip: int
    """Number of records to skip for pagination."""

    sort_order: Literal["ascending", "descending"]
    """Sort calls by `start_timestamp` in ascending or descending order."""


class FilterCriteriaAgent(TypedDict, total=False):
    agent_id: Required[str]
    """The agent ID to filter on."""

    version: Iterable[float]
    """Specific versions to filter on. If not provided, all versions are included."""


class FilterCriteriaBatchCallID(TypedDict, total=False):
    """Filter by batch call ID."""

    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaCallIDStringFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaCallIDEnumFilter(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]


FilterCriteriaCallID: TypeAlias = Union[FilterCriteriaCallIDStringFilter, FilterCriteriaCallIDEnumFilter]


class FilterCriteriaCallStatus(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["not_connected", "ongoing", "ended", "error"]]]


class FilterCriteriaCallSuccessful(TypedDict, total=False):
    """Filter by whether the call was successful."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]


class FilterCriteriaCallType(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["web_call", "phone_call"]]]


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


class FilterCriteriaDataStorageSetting(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["everything", "everything_except_pii", "basic_attributes_only"]]]


class FilterCriteriaDirection(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["inbound", "outbound"]]]


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
                "call_take_over",
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


class FilterCriteriaDynamicVariable(TypedDict, total=False):
    key: Required[str]
    """The dynamic variable name to filter on."""

    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaE2ELatencyP50NumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaE2ELatencyP50RangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaE2ELatencyP50: TypeAlias = Union[
    FilterCriteriaE2ELatencyP50NumberFilter, FilterCriteriaE2ELatencyP50RangeFilter
]


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


class FilterCriteriaFromNumber(TypedDict, total=False):
    """Filter by from number."""

    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaInVoicemail(TypedDict, total=False):
    """Filter by whether the call is in voicemail."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]


class FilterCriteriaMetadataStringFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]

    key: str
    """The field name to filter on."""


class FilterCriteriaMetadataNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]

    key: str
    """The field name to filter on."""


class FilterCriteriaMetadataBooleanFilter(TypedDict, total=False):
    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]

    key: str
    """The field name to filter on."""


class FilterCriteriaMetadataRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""

    key: str
    """The field name to filter on."""


class FilterCriteriaMetadataEnumFilter(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]

    key: str
    """The field name to filter on."""


class FilterCriteriaMetadataPresentFilter(TypedDict, total=False):
    op: Required[Literal["pr", "np"]]
    """pr: present (has value), np: not present"""

    type: Required[Literal["present"]]

    key: str
    """The field name to filter on."""


FilterCriteriaMetadata: TypeAlias = Union[
    FilterCriteriaMetadataStringFilter,
    FilterCriteriaMetadataNumberFilter,
    FilterCriteriaMetadataBooleanFilter,
    FilterCriteriaMetadataRangeFilter,
    FilterCriteriaMetadataEnumFilter,
    FilterCriteriaMetadataPresentFilter,
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


class FilterCriteriaToNumber(TypedDict, total=False):
    """Filter by to number."""

    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaToolCallLatencyMsNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaToolCallLatencyMsRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaToolCallLatencyMs: TypeAlias = Union[
    FilterCriteriaToolCallLatencyMsNumberFilter, FilterCriteriaToolCallLatencyMsRangeFilter
]


class FilterCriteriaToolCallSuccess(TypedDict, total=False):
    """Filter by tool call success status."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]


class FilterCriteriaToolCall(TypedDict, total=False):
    latency_ms: FilterCriteriaToolCallLatencyMs
    """Filter by tool call latency in milliseconds."""

    name: str
    """The tool call name to filter on."""

    success: FilterCriteriaToolCallSuccess
    """Filter by tool call success status."""

    type: str
    """The tool call type to filter on."""


class FilterCriteriaUserSentiment(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["Negative", "Positive", "Neutral", "Unknown"]]]


class FilterCriteria(TypedDict, total=False):
    """Filter criteria for calls. All conditions are implicitly connected with AND."""

    agent: Iterable[FilterCriteriaAgent]
    """Filter by agent(s). Agent filters are connected by OR."""

    batch_call_id: FilterCriteriaBatchCallID
    """Filter by batch call ID."""

    call_id: FilterCriteriaCallID
    """Filter by call ID."""

    call_status: FilterCriteriaCallStatus

    call_successful: FilterCriteriaCallSuccessful
    """Filter by whether the call was successful."""

    call_type: FilterCriteriaCallType

    combined_cost: FilterCriteriaCombinedCost
    """Filter by combined cost of the call."""

    custom_analysis_data: Iterable[FilterCriteriaCustomAnalysisData]
    """Filter by custom analysis data fields."""

    custom_attributes: Iterable[FilterCriteriaCustomAttribute]
    """Filter by custom attributes fields."""

    data_storage_setting: FilterCriteriaDataStorageSetting

    direction: FilterCriteriaDirection

    disconnection_reason: FilterCriteriaDisconnectionReason

    duration_ms: FilterCriteriaDurationMs
    """Filter by call duration in milliseconds."""

    dynamic_variables: Iterable[FilterCriteriaDynamicVariable]
    """Filter by dynamic variables."""

    e2e_latency_p50: FilterCriteriaE2ELatencyP50
    """Filter by end-to-end latency p50."""

    end_timestamp: FilterCriteriaEndTimestamp
    """Filter by call end timestamp (epoch ms)."""

    from_number: FilterCriteriaFromNumber
    """Filter by from number."""

    in_voicemail: FilterCriteriaInVoicemail
    """Filter by whether the call is in voicemail."""

    metadata: Iterable[FilterCriteriaMetadata]
    """Filter by metadata fields."""

    start_timestamp: FilterCriteriaStartTimestamp
    """Filter by call start timestamp (epoch ms)."""

    to_number: FilterCriteriaToNumber
    """Filter by to number."""

    tool_calls: Iterable[FilterCriteriaToolCall]
    """Filter by tool call criteria. Tool call filters are connected by AND."""

    user_sentiment: FilterCriteriaUserSentiment
