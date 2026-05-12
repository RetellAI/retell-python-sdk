# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "CallListResponse",
    "Item",
    "ItemV3WebCallResponse",
    "ItemV3WebCallResponseCallAnalysis",
    "ItemV3WebCallResponseCallCost",
    "ItemV3WebCallResponseCallCostProductCost",
    "ItemV3WebCallResponseLatency",
    "ItemV3WebCallResponseLatencyAsr",
    "ItemV3WebCallResponseLatencyE2E",
    "ItemV3WebCallResponseLatencyKnowledgeBase",
    "ItemV3WebCallResponseLatencyLlm",
    "ItemV3WebCallResponseLatencyLlmWebsocketNetworkRtt",
    "ItemV3WebCallResponseLatencyS2s",
    "ItemV3WebCallResponseLatencyTts",
    "ItemV3WebCallResponseLlmTokenUsage",
    "ItemV3PhoneCallResponse",
    "ItemV3PhoneCallResponseCallAnalysis",
    "ItemV3PhoneCallResponseCallCost",
    "ItemV3PhoneCallResponseCallCostProductCost",
    "ItemV3PhoneCallResponseLatency",
    "ItemV3PhoneCallResponseLatencyAsr",
    "ItemV3PhoneCallResponseLatencyE2E",
    "ItemV3PhoneCallResponseLatencyKnowledgeBase",
    "ItemV3PhoneCallResponseLatencyLlm",
    "ItemV3PhoneCallResponseLatencyLlmWebsocketNetworkRtt",
    "ItemV3PhoneCallResponseLatencyS2s",
    "ItemV3PhoneCallResponseLatencyTts",
    "ItemV3PhoneCallResponseLlmTokenUsage",
    "ItemV3PhoneCallResponseTelephonyIdentifier",
]


class ItemV3WebCallResponseCallAnalysis(BaseModel):
    """
    Post call analysis that includes information such as sentiment, status, summary, and custom defined data to extract. Available after call ends. Subscribe to `call_analyzed` webhook event type to receive it once ready.
    """

    call_successful: Optional[bool] = None
    """
    Whether the agent seems to have a successful call with the user, where the agent
    finishes the task, and the call was complete without being cutoff.
    """

    call_summary: Optional[str] = None
    """A high level summary of the call."""

    custom_analysis_data: Optional[object] = None
    """
    Custom analysis data that was extracted based on the schema defined in agent
    post call analysis data. Can be empty if nothing is specified.
    """

    in_voicemail: Optional[bool] = None
    """Whether the call is entered voicemail."""

    user_sentiment: Optional[Literal["Negative", "Positive", "Neutral", "Unknown"]] = None
    """Sentiment of the user in the call."""


class ItemV3WebCallResponseCallCostProductCost(BaseModel):
    cost: float
    """Cost for the product in cents for the duration of the call."""

    product: str
    """Product name that has a cost associated with it."""

    is_transfer_leg_cost: Optional[bool] = None
    """True if this cost item is for a transfer segment."""

    unit_price: Optional[float] = None
    """Unit price of the product in cents per second."""


class ItemV3WebCallResponseCallCost(BaseModel):
    """Cost of the call, including all the products and their costs and discount."""

    combined_cost: float
    """Combined cost of all individual costs in cents"""

    product_costs: List[ItemV3WebCallResponseCallCostProductCost]
    """List of products with their unit prices and costs in cents"""

    total_duration_seconds: float
    """Total duration of the call in seconds"""

    total_duration_unit_price: float
    """Total unit duration price of all products in cents per second"""


class ItemV3WebCallResponseLatencyAsr(BaseModel):
    """
    Transcription latency (diff between the duration of the chunks streamed and the durations of the transcribed part) tracking of the call.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatencyE2E(BaseModel):
    """
    End to end latency (from user stops talking to agent start talking) tracking of the call. This latency does not account for the network trip time from Retell server to user frontend. The latency is tracked every time turn change between user and agent.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatencyKnowledgeBase(BaseModel):
    """
    Knowledge base latency (from the triggering of knowledge base retrival to all relevant context received) tracking of the call. Only populated when using knowledge base feature for the agent of the call.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatencyLlm(BaseModel):
    """
    LLM latency (from issue of LLM call to first speakable chunk received) tracking of the call. When using custom LLM. this latency includes LLM websocket roundtrip time between user server and Retell server.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatencyLlmWebsocketNetworkRtt(BaseModel):
    """
    LLM websocket roundtrip latency (between user server and Retell server) tracking of the call. Only populated for calls using custom LLM.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatencyS2s(BaseModel):
    """
    Speech-to-speech latency (from requesting responses of a S2S model to first byte received) tracking of the call. Only populated for calls that uses S2S model like Realtime API.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatencyTts(BaseModel):
    """
    Text-to-speech latency (from the triggering of TTS to first byte received) tracking of the call.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3WebCallResponseLatency(BaseModel):
    """Latency tracking of the call, available after call ends.

    Not all fields here will be available, as it depends on the type of call and feature used.
    """

    asr: Optional[ItemV3WebCallResponseLatencyAsr] = None
    """
    Transcription latency (diff between the duration of the chunks streamed and the
    durations of the transcribed part) tracking of the call.
    """

    e2e: Optional[ItemV3WebCallResponseLatencyE2E] = None
    """
    End to end latency (from user stops talking to agent start talking) tracking of
    the call. This latency does not account for the network trip time from Retell
    server to user frontend. The latency is tracked every time turn change between
    user and agent.
    """

    knowledge_base: Optional[ItemV3WebCallResponseLatencyKnowledgeBase] = None
    """
    Knowledge base latency (from the triggering of knowledge base retrival to all
    relevant context received) tracking of the call. Only populated when using
    knowledge base feature for the agent of the call.
    """

    llm: Optional[ItemV3WebCallResponseLatencyLlm] = None
    """
    LLM latency (from issue of LLM call to first speakable chunk received) tracking
    of the call. When using custom LLM. this latency includes LLM websocket
    roundtrip time between user server and Retell server.
    """

    llm_websocket_network_rtt: Optional[ItemV3WebCallResponseLatencyLlmWebsocketNetworkRtt] = None
    """
    LLM websocket roundtrip latency (between user server and Retell server) tracking
    of the call. Only populated for calls using custom LLM.
    """

    s2s: Optional[ItemV3WebCallResponseLatencyS2s] = None
    """
    Speech-to-speech latency (from requesting responses of a S2S model to first byte
    received) tracking of the call. Only populated for calls that uses S2S model
    like Realtime API.
    """

    tts: Optional[ItemV3WebCallResponseLatencyTts] = None
    """
    Text-to-speech latency (from the triggering of TTS to first byte received)
    tracking of the call.
    """


class ItemV3WebCallResponseLlmTokenUsage(BaseModel):
    """LLM token usage of the call, available after call ends.

    Not populated if using custom LLM, realtime API, or no LLM call is made.
    """

    average: float
    """Average token count of the call."""

    num_requests: float
    """Number of requests made to the LLM."""

    values: List[float]
    """All the token count values in the call."""


class ItemV3WebCallResponse(BaseModel):
    access_token: str
    """Access token to enter the web call room.

    This needs to be passed to your frontend to join the call.
    """

    agent_id: str
    """Corresponding agent id of this call."""

    agent_version: int
    """The version of the agent."""

    call_id: str
    """Unique id of the call.

    Used to identify the call in the LLM websocket and used to authenticate in the
    audio websocket.
    """

    call_status: Literal["registered", "not_connected", "ongoing", "ended", "error"]
    """Status of call.

    - `registered`: Call id issued, starting to make a call using this id.
    - `ongoing`: Call connected and ongoing.
    - `ended`: The underlying websocket has ended for the call. Either user or agent
      hung up, or call transferred.
    - `error`: Call encountered error.
    """

    call_type: Literal["web_call"]
    """Type of the call. Used to distinguish between web call and phone call."""

    agent_name: Optional[str] = None
    """Name of the agent."""

    call_analysis: Optional[ItemV3WebCallResponseCallAnalysis] = None
    """
    Post call analysis that includes information such as sentiment, status, summary,
    and custom defined data to extract. Available after call ends. Subscribe to
    `call_analyzed` webhook event type to receive it once ready.
    """

    call_cost: Optional[ItemV3WebCallResponseCallCost] = None
    """Cost of the call, including all the products and their costs and discount."""

    collected_dynamic_variables: Optional[Dict[str, str]] = None
    """Dynamic variables collected from the call. Only available after the call ends."""

    custom_sip_headers: Optional[Dict[str, str]] = None
    """Custom SIP headers to be added to the call."""

    data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]] = None
    """Data storage setting for this call's agent.

    "everything" stores all data, "everything_except_pii" excludes PII when
    possible, "basic_attributes_only" stores only metadata.
    """

    disconnection_reason: Optional[
        Literal[
            "user_hangup",
            "agent_hangup",
            "call_transfer",
            "voicemail_reached",
            "ivr_reached",
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
            "transfer_bridged",
            "transfer_cancelled",
            "manual_stopped",
        ]
    ] = None
    """The reason for the disconnection of the call.

    Read detailed description about reasons listed here at
    [Disconnection Reason Doc](/reliability/debug-call-disconnect#understanding-disconnection-reasons).
    """

    duration_ms: Optional[int] = None
    """Duration of the call in milliseconds. Available after call ends."""

    end_timestamp: Optional[int] = None
    """End timestamp (milliseconds since epoch) of the call.

    Available after call ends.
    """

    knowledge_base_retrieved_contents_url: Optional[str] = None
    """URL to the knowledge base retrieved contents of the call.

    Available after call ends if the call utilizes knowledge base feature. It
    consists of the respond id and the retrieved contents related to that response.
    It's already rendered in call history tab of dashboard, and you can also
    manually download and check against the transcript to view the knowledge base
    retrieval results.
    """

    latency: Optional[ItemV3WebCallResponseLatency] = None
    """Latency tracking of the call, available after call ends.

    Not all fields here will be available, as it depends on the type of call and
    feature used.
    """

    llm_token_usage: Optional[ItemV3WebCallResponseLlmTokenUsage] = None
    """LLM token usage of the call, available after call ends.

    Not populated if using custom LLM, realtime API, or no LLM call is made.
    """

    metadata: Optional[object] = None
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    opt_in_signed_url: Optional[bool] = None
    """Whether this agent opts in for signed URLs for public logs and recordings.

    When enabled, the generated URLs will include security signatures that restrict
    access and automatically expire after 24 hours.
    """

    public_log_url: Optional[str] = None
    """
    Public log of the call, containing details about all the requests and responses
    received in LLM WebSocket, latency tracking for each turntaking, helpful for
    debugging and tracing. Available after call ends.
    """

    recording_multi_channel_url: Optional[str] = None
    """Recording of the call, with each party's audio stored in a separate channel.

    Available after the call ends.
    """

    recording_url: Optional[str] = None
    """Recording of the call. Available after call ends."""

    retell_llm_dynamic_variables: Optional[Dict[str, str]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """

    scrubbed_recording_multi_channel_url: Optional[str] = None
    """
    Recording of the call without PII, with each party's audio stored in a separate
    channel. Available after the call ends.
    """

    scrubbed_recording_url: Optional[str] = None
    """Recording of the call without PII. Available after call ends."""

    start_timestamp: Optional[int] = None
    """Begin timestamp (milliseconds since epoch) of the call.

    Available after call starts.
    """

    transfer_destination: Optional[str] = None
    """The destination number or identifier where the call was transferred to.

    Only populated when the disconnection reason was `call_transfer`. Can be a phone
    number or a SIP URI. SIP URIs are prefixed with "sip:" and may include a
    ";transport=..." portion (if transport is known) where the transport type can be
    "tls", "tcp" or "udp".
    """

    transfer_end_timestamp: Optional[int] = None
    """Transfer end timestamp (milliseconds since epoch) of the call.

    Available after transfer call ends.
    """


class ItemV3PhoneCallResponseCallAnalysis(BaseModel):
    """
    Post call analysis that includes information such as sentiment, status, summary, and custom defined data to extract. Available after call ends. Subscribe to `call_analyzed` webhook event type to receive it once ready.
    """

    call_successful: Optional[bool] = None
    """
    Whether the agent seems to have a successful call with the user, where the agent
    finishes the task, and the call was complete without being cutoff.
    """

    call_summary: Optional[str] = None
    """A high level summary of the call."""

    custom_analysis_data: Optional[object] = None
    """
    Custom analysis data that was extracted based on the schema defined in agent
    post call analysis data. Can be empty if nothing is specified.
    """

    in_voicemail: Optional[bool] = None
    """Whether the call is entered voicemail."""

    user_sentiment: Optional[Literal["Negative", "Positive", "Neutral", "Unknown"]] = None
    """Sentiment of the user in the call."""


class ItemV3PhoneCallResponseCallCostProductCost(BaseModel):
    cost: float
    """Cost for the product in cents for the duration of the call."""

    product: str
    """Product name that has a cost associated with it."""

    is_transfer_leg_cost: Optional[bool] = None
    """True if this cost item is for a transfer segment."""

    unit_price: Optional[float] = None
    """Unit price of the product in cents per second."""


class ItemV3PhoneCallResponseCallCost(BaseModel):
    """Cost of the call, including all the products and their costs and discount."""

    combined_cost: float
    """Combined cost of all individual costs in cents"""

    product_costs: List[ItemV3PhoneCallResponseCallCostProductCost]
    """List of products with their unit prices and costs in cents"""

    total_duration_seconds: float
    """Total duration of the call in seconds"""

    total_duration_unit_price: float
    """Total unit duration price of all products in cents per second"""


class ItemV3PhoneCallResponseLatencyAsr(BaseModel):
    """
    Transcription latency (diff between the duration of the chunks streamed and the durations of the transcribed part) tracking of the call.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatencyE2E(BaseModel):
    """
    End to end latency (from user stops talking to agent start talking) tracking of the call. This latency does not account for the network trip time from Retell server to user frontend. The latency is tracked every time turn change between user and agent.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatencyKnowledgeBase(BaseModel):
    """
    Knowledge base latency (from the triggering of knowledge base retrival to all relevant context received) tracking of the call. Only populated when using knowledge base feature for the agent of the call.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatencyLlm(BaseModel):
    """
    LLM latency (from issue of LLM call to first speakable chunk received) tracking of the call. When using custom LLM. this latency includes LLM websocket roundtrip time between user server and Retell server.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatencyLlmWebsocketNetworkRtt(BaseModel):
    """
    LLM websocket roundtrip latency (between user server and Retell server) tracking of the call. Only populated for calls using custom LLM.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatencyS2s(BaseModel):
    """
    Speech-to-speech latency (from requesting responses of a S2S model to first byte received) tracking of the call. Only populated for calls that uses S2S model like Realtime API.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatencyTts(BaseModel):
    """
    Text-to-speech latency (from the triggering of TTS to first byte received) tracking of the call.
    """

    max: Optional[float] = None
    """Maximum latency in the call, measured in milliseconds."""

    min: Optional[float] = None
    """Minimum latency in the call, measured in milliseconds."""

    num: Optional[float] = None
    """Number of data points (number of times latency is tracked)."""

    p50: Optional[float] = None
    """50 percentile of latency, measured in milliseconds."""

    p90: Optional[float] = None
    """90 percentile of latency, measured in milliseconds."""

    p95: Optional[float] = None
    """95 percentile of latency, measured in milliseconds."""

    p99: Optional[float] = None
    """99 percentile of latency, measured in milliseconds."""

    values: Optional[List[float]] = None
    """All the latency data points in the call, measured in milliseconds."""


class ItemV3PhoneCallResponseLatency(BaseModel):
    """Latency tracking of the call, available after call ends.

    Not all fields here will be available, as it depends on the type of call and feature used.
    """

    asr: Optional[ItemV3PhoneCallResponseLatencyAsr] = None
    """
    Transcription latency (diff between the duration of the chunks streamed and the
    durations of the transcribed part) tracking of the call.
    """

    e2e: Optional[ItemV3PhoneCallResponseLatencyE2E] = None
    """
    End to end latency (from user stops talking to agent start talking) tracking of
    the call. This latency does not account for the network trip time from Retell
    server to user frontend. The latency is tracked every time turn change between
    user and agent.
    """

    knowledge_base: Optional[ItemV3PhoneCallResponseLatencyKnowledgeBase] = None
    """
    Knowledge base latency (from the triggering of knowledge base retrival to all
    relevant context received) tracking of the call. Only populated when using
    knowledge base feature for the agent of the call.
    """

    llm: Optional[ItemV3PhoneCallResponseLatencyLlm] = None
    """
    LLM latency (from issue of LLM call to first speakable chunk received) tracking
    of the call. When using custom LLM. this latency includes LLM websocket
    roundtrip time between user server and Retell server.
    """

    llm_websocket_network_rtt: Optional[ItemV3PhoneCallResponseLatencyLlmWebsocketNetworkRtt] = None
    """
    LLM websocket roundtrip latency (between user server and Retell server) tracking
    of the call. Only populated for calls using custom LLM.
    """

    s2s: Optional[ItemV3PhoneCallResponseLatencyS2s] = None
    """
    Speech-to-speech latency (from requesting responses of a S2S model to first byte
    received) tracking of the call. Only populated for calls that uses S2S model
    like Realtime API.
    """

    tts: Optional[ItemV3PhoneCallResponseLatencyTts] = None
    """
    Text-to-speech latency (from the triggering of TTS to first byte received)
    tracking of the call.
    """


class ItemV3PhoneCallResponseLlmTokenUsage(BaseModel):
    """LLM token usage of the call, available after call ends.

    Not populated if using custom LLM, realtime API, or no LLM call is made.
    """

    average: float
    """Average token count of the call."""

    num_requests: float
    """Number of requests made to the LLM."""

    values: List[float]
    """All the token count values in the call."""


class ItemV3PhoneCallResponseTelephonyIdentifier(BaseModel):
    """Telephony identifier of the call, populated when available.

    Tracking purposes only.
    """

    twilio_call_sid: Optional[str] = None
    """Twilio call sid."""


class ItemV3PhoneCallResponse(BaseModel):
    agent_id: str
    """Corresponding agent id of this call."""

    agent_version: int
    """The version of the agent."""

    call_id: str
    """Unique id of the call.

    Used to identify the call in the LLM websocket and used to authenticate in the
    audio websocket.
    """

    call_status: Literal["registered", "not_connected", "ongoing", "ended", "error"]
    """Status of call.

    - `registered`: Call id issued, starting to make a call using this id.
    - `ongoing`: Call connected and ongoing.
    - `ended`: The underlying websocket has ended for the call. Either user or agent
      hung up, or call transferred.
    - `error`: Call encountered error.
    """

    call_type: Literal["phone_call"]
    """Type of the call. Used to distinguish between web call and phone call."""

    direction: Literal["inbound", "outbound"]
    """Direction of the phone call."""

    from_number: str
    """The caller number."""

    to_number: str
    """The callee number."""

    agent_name: Optional[str] = None
    """Name of the agent."""

    call_analysis: Optional[ItemV3PhoneCallResponseCallAnalysis] = None
    """
    Post call analysis that includes information such as sentiment, status, summary,
    and custom defined data to extract. Available after call ends. Subscribe to
    `call_analyzed` webhook event type to receive it once ready.
    """

    call_cost: Optional[ItemV3PhoneCallResponseCallCost] = None
    """Cost of the call, including all the products and their costs and discount."""

    collected_dynamic_variables: Optional[Dict[str, str]] = None
    """Dynamic variables collected from the call. Only available after the call ends."""

    custom_sip_headers: Optional[Dict[str, str]] = None
    """Custom SIP headers to be added to the call."""

    data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]] = None
    """Data storage setting for this call's agent.

    "everything" stores all data, "everything_except_pii" excludes PII when
    possible, "basic_attributes_only" stores only metadata.
    """

    disconnection_reason: Optional[
        Literal[
            "user_hangup",
            "agent_hangup",
            "call_transfer",
            "voicemail_reached",
            "ivr_reached",
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
            "transfer_bridged",
            "transfer_cancelled",
            "manual_stopped",
        ]
    ] = None
    """The reason for the disconnection of the call.

    Read detailed description about reasons listed here at
    [Disconnection Reason Doc](/reliability/debug-call-disconnect#understanding-disconnection-reasons).
    """

    duration_ms: Optional[int] = None
    """Duration of the call in milliseconds. Available after call ends."""

    end_timestamp: Optional[int] = None
    """End timestamp (milliseconds since epoch) of the call.

    Available after call ends.
    """

    knowledge_base_retrieved_contents_url: Optional[str] = None
    """URL to the knowledge base retrieved contents of the call.

    Available after call ends if the call utilizes knowledge base feature. It
    consists of the respond id and the retrieved contents related to that response.
    It's already rendered in call history tab of dashboard, and you can also
    manually download and check against the transcript to view the knowledge base
    retrieval results.
    """

    latency: Optional[ItemV3PhoneCallResponseLatency] = None
    """Latency tracking of the call, available after call ends.

    Not all fields here will be available, as it depends on the type of call and
    feature used.
    """

    llm_token_usage: Optional[ItemV3PhoneCallResponseLlmTokenUsage] = None
    """LLM token usage of the call, available after call ends.

    Not populated if using custom LLM, realtime API, or no LLM call is made.
    """

    metadata: Optional[object] = None
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    opt_in_signed_url: Optional[bool] = None
    """Whether this agent opts in for signed URLs for public logs and recordings.

    When enabled, the generated URLs will include security signatures that restrict
    access and automatically expire after 24 hours.
    """

    public_log_url: Optional[str] = None
    """
    Public log of the call, containing details about all the requests and responses
    received in LLM WebSocket, latency tracking for each turntaking, helpful for
    debugging and tracing. Available after call ends.
    """

    recording_multi_channel_url: Optional[str] = None
    """Recording of the call, with each party's audio stored in a separate channel.

    Available after the call ends.
    """

    recording_url: Optional[str] = None
    """Recording of the call. Available after call ends."""

    retell_llm_dynamic_variables: Optional[Dict[str, str]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """

    scrubbed_recording_multi_channel_url: Optional[str] = None
    """
    Recording of the call without PII, with each party's audio stored in a separate
    channel. Available after the call ends.
    """

    scrubbed_recording_url: Optional[str] = None
    """Recording of the call without PII. Available after call ends."""

    start_timestamp: Optional[int] = None
    """Begin timestamp (milliseconds since epoch) of the call.

    Available after call starts.
    """

    telephony_identifier: Optional[ItemV3PhoneCallResponseTelephonyIdentifier] = None
    """Telephony identifier of the call, populated when available.

    Tracking purposes only.
    """

    transfer_destination: Optional[str] = None
    """The destination number or identifier where the call was transferred to.

    Only populated when the disconnection reason was `call_transfer`. Can be a phone
    number or a SIP URI. SIP URIs are prefixed with "sip:" and may include a
    ";transport=..." portion (if transport is known) where the transport type can be
    "tls", "tcp" or "udp".
    """

    transfer_end_timestamp: Optional[int] = None
    """Transfer end timestamp (milliseconds since epoch) of the call.

    Available after transfer call ends.
    """


Item: TypeAlias = Union[ItemV3WebCallResponse, ItemV3PhoneCallResponse]


class CallListResponse(BaseModel):
    has_more: Optional[bool] = None
    """Whether more results are available."""

    items: Optional[List[Item]] = None

    pagination_key: Optional[str] = None
    """Pagination key for the next page."""
