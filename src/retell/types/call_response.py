# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .register_call_response import RegisterCallResponse

__all__ = [
    "CallResponse",
    "CallResponseCallAnalysis",
    "CallResponseE2ELatency",
    "CallResponseLlmLatency",
    "CallResponseLlmWebsocketNetworkRttLatency",
    "CallResponseTranscriptObject",
    "CallResponseTranscriptObjectWord",
    "CallResponseTranscriptWithToolCall",
    "CallResponseTranscriptWithToolCallUtterance",
    "CallResponseTranscriptWithToolCallUtteranceWord",
    "CallResponseTranscriptWithToolCallToolCallInvocationUtterance",
    "CallResponseTranscriptWithToolCallToolCallResultUtterance",
]


class CallResponseCallAnalysis(BaseModel):
    agent_sentiment: Optional[Literal["Negative", "Positive", "Neutral"]] = None
    """Sentiment of the agent in the call."""

    agent_task_completion_rating: Optional[Literal["Complete", "Incomplete", "Partial"]] = None
    """
    Evaluate agent task completion status, whether the agent has completed his task.
    """

    agent_task_completion_rating_reason: Optional[str] = None
    """Reason for the agent task completion status."""

    call_completion_rating: Optional[Literal["Complete", "Incomplete", "Partial"]] = None
    """Evaluate whether the call ended normally or was cut off."""

    call_completion_rating_reason: Optional[str] = None
    """Reason for the call completion status."""

    call_summary: Optional[str] = None
    """A high level summary of the call."""

    user_sentiment: Optional[Literal["Negative", "Positive", "Neutral"]] = None
    """Sentiment of the user in the call."""


class CallResponseE2ELatency(BaseModel):
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


class CallResponseLlmLatency(BaseModel):
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


class CallResponseLlmWebsocketNetworkRttLatency(BaseModel):
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


class CallResponseTranscriptObjectWord(BaseModel):
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


class CallResponseTranscriptObject(BaseModel):
    content: str
    """Transcript of the utterances."""

    role: Literal["agent", "user"]
    """Documents whether this utterance is spoken by agent or user."""

    words: List[CallResponseTranscriptObjectWord]
    """Array of words in the utterance with the word timestamp.

    Useful for understanding what word was spoken at what time. Note that the word
    timestamp is not guaranteed to be accurate, it's more like an approximation.
    """


class CallResponseTranscriptWithToolCallUtteranceWord(BaseModel):
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


class CallResponseTranscriptWithToolCallUtterance(BaseModel):
    content: str
    """Transcript of the utterances."""

    role: Literal["agent", "user"]
    """Documents whether this utterance is spoken by agent or user."""

    words: List[CallResponseTranscriptWithToolCallUtteranceWord]
    """Array of words in the utterance with the word timestamp.

    Useful for understanding what word was spoken at what time. Note that the word
    timestamp is not guaranteed to be accurate, it's more like an approximation.
    """


class CallResponseTranscriptWithToolCallToolCallInvocationUtterance(BaseModel):
    arguments: str
    """Arguments for this tool call, it's a stringified JSON object."""

    name: str
    """Name of the function in this tool call."""

    role: Literal["tool_call_invocation"]
    """This is a tool call invocation."""

    tool_call_id: str
    """Tool call id, globally unique."""


class CallResponseTranscriptWithToolCallToolCallResultUtterance(BaseModel):
    content: str
    """Result of the tool call, can be a string, a stringified json, etc."""

    role: Literal["tool_call_result"]
    """This is result of a tool call."""

    tool_call_id: str
    """Tool call id, globally unique."""


CallResponseTranscriptWithToolCall = Union[
    CallResponseTranscriptWithToolCallUtterance,
    CallResponseTranscriptWithToolCallToolCallInvocationUtterance,
    CallResponseTranscriptWithToolCallToolCallResultUtterance,
]


class CallResponse(RegisterCallResponse):
    call_analysis: Optional[CallResponseCallAnalysis] = None
    """- BETA feature, schema might change, might not always be populated.

    Please do not rely on this object schema for post processing. Post conversation
    evaluation of the call. Including information such as sentiment, intent, call
    completion status and other metrics. Available after call ends. Subscribe to
    `call_analyzed` webhook event type to receive it once ready.
    """

    disconnection_reason: Optional[
        Literal[
            "user_hangup",
            "agent_hangup",
            "call_transfer",
            "inactivity",
            "machine_detected",
            "concurrency_limit_reached",
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
        ]
    ] = None
    """The reason for the disconnection of the call.

    Read details desciption about reasons listed here at
    [Disconnection Reason Doc](/get-started/debug-guide#disconnection-reason).
    """

    e2e_latency: Optional[CallResponseE2ELatency] = None
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

    llm_latency: Optional[CallResponseLlmLatency] = None
    """
    LLM latency (from issue of LLM call to first token received) tracking of the
    call, available after call ends. When using custom LLM. this latency includes
    LLM websocket roundtrip time between user server and Retell server.
    """

    llm_websocket_network_rtt_latency: Optional[CallResponseLlmWebsocketNetworkRttLatency] = None
    """
    LLM websocket roundtrip latency (between user server and Retell server) tracking
    of the call, available after call ends. Only populated for calls using custom
    LLM.
    """

    public_log_url: Optional[str] = None
    """
    Public log of the call, containing details about all the requests and responses
    received in LLM WebSocket, latency tracking for each turntaking, helpful for
    debugging and tracing. Available after call ends.
    """

    recording_url: Optional[str] = None
    """Recording of the call. Available after call ends."""

    start_timestamp: Optional[int] = None
    """Begin timestamp (milliseconds since epoch) of the call.

    Available after call starts.
    """

    transcript: Optional[str] = None
    """Transcription of the call. Available after call ends."""

    transcript_object: Optional[List[CallResponseTranscriptObject]] = None
    """Transcript of the call in the format of a list of utterance, with timestamp.

    Available after call ends.
    """

    transcript_with_tool_calls: Optional[List[CallResponseTranscriptWithToolCall]] = None
    """Transcript of the call weaved with tool call invocation and results.

    It precisely captures when (at what utterance, which word) the tool was invoked
    and what was the result. Available after call ends.
    """
