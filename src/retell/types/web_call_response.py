# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "WebCallResponse",
    "CallAnalysis",
    "E2ELatency",
    "LlmLatency",
    "LlmWebsocketNetworkRttLatency",
    "TranscriptObject",
    "TranscriptObjectWord",
    "TranscriptWithToolCall",
    "TranscriptWithToolCallUtterance",
    "TranscriptWithToolCallUtteranceWord",
    "TranscriptWithToolCallToolCallInvocationUtterance",
    "TranscriptWithToolCallToolCallResultUtterance",
]


class CallAnalysis(BaseModel):
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


class E2ELatency(BaseModel):
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


class LlmLatency(BaseModel):
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


class LlmWebsocketNetworkRttLatency(BaseModel):
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


class TranscriptObjectWord(BaseModel):
    end: Optional[float] = None
    """End time of the word in the call in second.

    This is relative audio time, not wall time.
    """

    start: Optional[float] = None
    """Start time of the word in the call in second.

    This is relative audio time, not wall time.
    """

    word: Optional[str] = None
    """Word transcript (with punctuation if applicable)."""


class TranscriptObject(BaseModel):
    content: str
    """Transcript of the utterances."""

    role: Literal["agent", "user"]
    """Documents whether this utterance is spoken by agent or user."""

    words: List[TranscriptObjectWord]
    """Array of words in the utterance with the word timestamp.

    Useful for understanding what word was spoken at what time. Note that the word
    timestamp is not guaranteed to be accurate, it's more like an approximation.
    """


class TranscriptWithToolCallUtteranceWord(BaseModel):
    end: Optional[float] = None
    """End time of the word in the call in second.

    This is relative audio time, not wall time.
    """

    start: Optional[float] = None
    """Start time of the word in the call in second.

    This is relative audio time, not wall time.
    """

    word: Optional[str] = None
    """Word transcript (with punctuation if applicable)."""


class TranscriptWithToolCallUtterance(BaseModel):
    content: str
    """Transcript of the utterances."""

    role: Literal["agent", "user"]
    """Documents whether this utterance is spoken by agent or user."""

    words: List[TranscriptWithToolCallUtteranceWord]
    """Array of words in the utterance with the word timestamp.

    Useful for understanding what word was spoken at what time. Note that the word
    timestamp is not guaranteed to be accurate, it's more like an approximation.
    """


class TranscriptWithToolCallToolCallInvocationUtterance(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""


class TranscriptWithToolCallToolCallResultUtterance(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""


TranscriptWithToolCall: TypeAlias = Union[
    TranscriptWithToolCallUtterance,
    TranscriptWithToolCallToolCallInvocationUtterance,
    TranscriptWithToolCallToolCallResultUtterance,
]


class WebCallResponse(BaseModel):
    access_token: str
    """Access token to enter the web call room.

    This needs to be passed to your frontend to join the call.
    """

    agent_id: str
    """Corresponding agent id of this call."""

    call_id: str
    """Unique id of the call.

    Used to identify in LLM websocket and used to authenticate in audio websocket.
    """

    call_status: Literal["registered", "ongoing", "ended", "error"]
    """Status of call.

    - `registered`: Call id issued, starting to make a call using this id.

    - `ongoing`: Call connected and ongoing.

    - `ended`: The underlying websocket has ended for the call. Either user or agent
      hanged up, or call transferred.

    - `error`: Call encountered error.
    """

    call_type: Literal["web_call"]
    """Type of the call. Used to distinguish between web call and phone call."""

    call_analysis: Optional[CallAnalysis] = None
    """
    Post call analysis that includes information such as sentiment, status, summary,
    and custom defined data to extract. Available after call ends. Subscribe to
    `call_analyzed` webhook event type to receive it once ready.
    """

    disconnection_reason: Optional[
        Literal[
            "user_hangup",
            "agent_hangup",
            "call_transfer",
            "voicemail_reached",
            "inactivity",
            "machine_detected",
            "max_duration_reached",
            "concurrency_limit_reached",
            "no_valid_payment",
            "scam_detected",
            "error_inbound_webhook",
            "dial_busy",
            "dial_failed",
            "dial_no_answer",
            "error_llm_websocket_open",
            "error_llm_websocket_lost_connection",
            "error_llm_websocket_runtime",
            "error_llm_websocket_corrupt_payload",
            "error_frontend_corrupted_payload",
            "error_twilio",
            "error_no_audio_received",
            "error_asr",
            "error_retell",
            "error_unknown",
            "error_user_not_joined",
            "registered_call_timeout",
        ]
    ] = None
    """The reason for the disconnection of the call.

    Read details desciption about reasons listed here at
    [Disconnection Reason Doc](/get-started/debug-guide#disconnection-reason).
    """

    e2e_latency: Optional[E2ELatency] = None
    """
    End to end latency (from user stops talking to agent start talking) tracking of
    the call, available after call ends. This latency does not account for the
    network trip time from Retell server to user frontend. The latency is tracked
    every time turn change between user and agent.
    """

    end_timestamp: Optional[int] = None
    """End timestamp (milliseconds since epoch) of the call.

    Available after call ends.
    """

    llm_latency: Optional[LlmLatency] = None
    """
    LLM latency (from issue of LLM call to first token received) tracking of the
    call, available after call ends. When using custom LLM. this latency includes
    LLM websocket roundtrip time between user server and Retell server.
    """

    llm_websocket_network_rtt_latency: Optional[LlmWebsocketNetworkRttLatency] = None
    """
    LLM websocket roundtrip latency (between user server and Retell server) tracking
    of the call, available after call ends. Only populated for calls using custom
    LLM.
    """

    metadata: Optional[object] = None
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    opt_out_sensitive_data_storage: Optional[bool] = None
    """
    Whether this call opts out of sensitive data storage like transcript, recording,
    logging.
    """

    public_log_url: Optional[str] = None
    """
    Public log of the call, containing details about all the requests and responses
    received in LLM WebSocket, latency tracking for each turntaking, helpful for
    debugging and tracing. Available after call ends.
    """

    recording_url: Optional[str] = None
    """Recording of the call. Available after call ends."""

    retell_llm_dynamic_variables: Optional[Dict[str, object]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Retell LLM prompt and tool description. Only applicable for Retell LLM.
    """

    start_timestamp: Optional[int] = None
    """Begin timestamp (milliseconds since epoch) of the call.

    Available after call starts.
    """

    transcript: Optional[str] = None
    """Transcription of the call. Available after call ends."""

    transcript_object: Optional[List[TranscriptObject]] = None
    """Transcript of the call in the format of a list of utterance, with timestamp.

    Available after call ends.
    """

    transcript_with_tool_calls: Optional[List[TranscriptWithToolCall]] = None
    """Transcript of the call weaved with tool call invocation and results.

    It precisely captures when (at what utterance, which word) the tool was invoked
    and what was the result. Available after call ends.
    """
