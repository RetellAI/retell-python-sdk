# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = [
    "CallListParams",
    "FilterCriteria",
    "FilterCriteriaDurationMs",
    "FilterCriteriaE2ELatencyP50",
    "FilterCriteriaStartTimestamp",
]


class CallListParams(TypedDict, total=False):
    filter_criteria: FilterCriteria
    """Filter criteria for the calls to retrieve."""

    limit: int
    """Limit the number of calls returned.

    Default 50, Max 1000. To retrieve more than 1000, use pagination_key to continue
    fetching the next page.
    """

    pagination_key: str
    """The pagination key to continue fetching the next page of calls.

    Pagination key is represented by a call id here, and it's exclusive (not
    included in the fetched calls). The last call id from the list calls is usually
    used as pagination key here. If not set, will start from the beginning.
    """

    sort_order: Literal["ascending", "descending"]
    """
    The calls will be sorted by `start_timestamp`, whether to return the calls in
    ascending or descending order.
    """


class FilterCriteriaDurationMs(TypedDict, total=False):
    lower_threshold: int

    upper_threshold: int


class FilterCriteriaE2ELatencyP50(TypedDict, total=False):
    lower_threshold: int

    upper_threshold: int


class FilterCriteriaStartTimestamp(TypedDict, total=False):
    lower_threshold: int

    upper_threshold: int


class FilterCriteria(TypedDict, total=False):
    agent_id: List[str]
    """Only retrieve calls that are made with specific agent(s)."""

    call_status: List[Literal["registered", "not_connected", "ongoing", "ended", "error"]]
    """Only retrieve calls with specific call status(es)."""

    call_successful: Iterable[bool]
    """Only retrieve calls with specific call successful(s)."""

    call_type: List[Literal["web_call", "phone_call"]]
    """Only retrieve calls with specific call type(s)."""

    direction: List[Literal["inbound", "outbound"]]
    """Only retrieve calls with specific direction(s)."""

    disconnection_reason: List[
        Literal[
            "user_hangup",
            "agent_hangup",
            "call_transfer",
            "voicemail_reached",
            "inactivity",
            "max_duration_reached",
            "concurrency_limit_reached",
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
        ]
    ]
    """Only retrieve calls with specific disconnection reason(s)."""

    duration_ms: FilterCriteriaDurationMs
    """Only retrieve calls with specific range of duration(s)."""

    e2e_latency_p50: FilterCriteriaE2ELatencyP50

    from_number: List[str]
    """Only retrieve calls with specific from number(s)."""

    in_voicemail: Iterable[bool]
    """Only retrieve calls that are in voicemail or not in voicemail."""

    start_timestamp: FilterCriteriaStartTimestamp
    """Only retrieve calls with specific range of start timestamp(s)."""

    to_number: List[str]
    """Only retrieve calls with specific to number(s)."""

    user_sentiment: List[Literal["Negative", "Positive", "Neutral", "Unknown"]]
    """Only retrieve calls with specific user sentiment(s)."""

    version: Iterable[int]
    """The version of the agent to use for the call."""
