# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ChatAgentCreateParams",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineCustomLm",
    "ResponseEngineResponseEngineConversationFlow",
    "GuardrailConfig",
    "PiiConfig",
    "PostChatAnalysisData",
    "PostChatAnalysisDataStringAnalysisData",
    "PostChatAnalysisDataEnumAnalysisData",
    "PostChatAnalysisDataBooleanAnalysisData",
    "PostChatAnalysisDataNumberAnalysisData",
]


class ChatAgentCreateParams(TypedDict, total=False):
    response_engine: Required[ResponseEngine]
    """The Response Engine to attach to the agent.

    It is used to generate responses for the agent. You need to create a Response
    Engine first before attaching it to an agent.
    """

    agent_name: Optional[str]
    """The name of the chat agent. Only used for your own reference."""

    analysis_successful_prompt: Optional[str]
    """
    The prompt to use for post call analysis to evaluate whether the call is
    successful. Set to null to use the default prompt.
    """

    analysis_summary_prompt: Optional[str]
    """The prompt to use for post call analysis to summarize the call.

    Set to null to use the default prompt.
    """

    auto_close_message: Optional[str]
    """Message to display when the chat is automatically closed."""

    data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]]
    """Controls what data is stored for this agent.

    "everything" stores all data including transcripts and recordings.
    "everything_except_pii" stores data but excludes PII when possible based on PII
    configuration. "basic_attributes_only" stores only basic metadata. If not set,
    defaults to "everything".
    """

    end_chat_after_silence_ms: int
    """If users stay silent for a period after agent speech, end the chat.

    The minimum value allowed is 120,000 ms (2 minutes). The maximum value allowed
    is 259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).
    """

    guardrail_config: GuardrailConfig
    """
    Configuration for guardrail checks to detect and prevent prohibited topics in
    agent output and user input.
    """

    is_public: Optional[bool]
    """Whether the agent is public.

    When set to true, the agent is available for public agent preview link.
    """

    language: Literal[
        "en-US",
        "en-IN",
        "en-GB",
        "en-AU",
        "en-NZ",
        "de-DE",
        "es-ES",
        "es-419",
        "hi-IN",
        "fr-FR",
        "fr-CA",
        "ja-JP",
        "pt-PT",
        "pt-BR",
        "zh-CN",
        "ru-RU",
        "it-IT",
        "ko-KR",
        "nl-NL",
        "nl-BE",
        "pl-PL",
        "tr-TR",
        "th-TH",
        "vi-VN",
        "ro-RO",
        "bg-BG",
        "ca-ES",
        "da-DK",
        "fi-FI",
        "el-GR",
        "hu-HU",
        "id-ID",
        "no-NO",
        "sk-SK",
        "sv-SE",
        "lt-LT",
        "lv-LV",
        "multi",
    ]
    """Specifies what language (and dialect) the chat will operate in.

    For instance, selecting `en-GB` optimizes for British English. If unset, will
    use default value `en-US`. Select `multi` for multilingual support, currently
    this supports Spanish and English.
    """

    opt_in_signed_url: bool
    """Whether this agent opts in to signed url for public log.

    If not set, default value of false will apply.
    """

    pii_config: PiiConfig
    """Configuration for PII scrubbing from transcripts and recordings."""

    post_chat_analysis_data: Optional[Iterable[PostChatAnalysisData]]
    """Post chat analysis data to extract from the chat.

    This data will augment the pre-defined variables extracted in the chat analysis.
    This will be available after the chat ends.
    """

    post_chat_analysis_model: Optional[
        Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5-mini",
            "gpt-5-nano",
            "claude-4.5-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
        ]
    ]
    """The model to use for post chat analysis. Default to gpt-4.1-mini."""

    signed_url_expiration_ms: Optional[int]
    """The expiration time for the signed url in milliseconds.

    Only applicable when opt_in_signed_url is true. If not set, default value of
    86400000 (24 hours) will apply.
    """

    webhook_events: Optional[List[Literal["chat_started", "chat_ended", "chat_analyzed"]]]
    """Which webhook events this agent should receive.

    If not set, defaults to chat_started, chat_ended, chat_analyzed.
    """

    webhook_timeout_ms: int
    """The timeout for the webhook in milliseconds.

    If not set, default value of 10000 will apply.
    """

    webhook_url: Optional[str]
    """The webhook for agent to listen to chat events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """


class ResponseEngineResponseEngineRetellLm(TypedDict, total=False):
    llm_id: Required[str]
    """id of the Retell LLM Response Engine."""

    type: Required[Literal["retell-llm"]]
    """type of the Response Engine."""

    version: Optional[float]
    """Version of the Retell LLM Response Engine."""


class ResponseEngineResponseEngineCustomLm(TypedDict, total=False):
    llm_websocket_url: Required[str]
    """LLM websocket url of the custom LLM."""

    type: Required[Literal["custom-llm"]]
    """type of the Response Engine."""


class ResponseEngineResponseEngineConversationFlow(TypedDict, total=False):
    conversation_flow_id: Required[str]
    """ID of the Conversation Flow Response Engine."""

    type: Required[Literal["conversation-flow"]]
    """type of the Response Engine."""

    version: Optional[float]
    """Version of the Conversation Flow Response Engine."""


ResponseEngine: TypeAlias = Union[
    ResponseEngineResponseEngineRetellLm,
    ResponseEngineResponseEngineCustomLm,
    ResponseEngineResponseEngineConversationFlow,
]


class GuardrailConfig(TypedDict, total=False):
    """
    Configuration for guardrail checks to detect and prevent prohibited topics in agent output and user input.
    """

    input_topics: Optional[List[Literal["platform_integrity_jailbreaking"]]]
    """Selected prohibited user topic categories to check.

    When user messages contain these topics, the agent will respond with a
    placeholder message instead of processing the request.
    """

    output_topics: Optional[
        List[
            Literal[
                "harassment",
                "self_harm",
                "sexual_exploitation",
                "violence",
                "defense_and_national_security",
                "illicit_and_harmful_activity",
                "gambling",
                "regulated_professional_advice",
                "child_safety_and_exploitation",
            ]
        ]
    ]
    """Selected prohibited agent topic categories to check.

    When agent messages contain these topics, they will be replaced with a
    placeholder message.
    """


class PiiConfig(TypedDict, total=False):
    """Configuration for PII scrubbing from transcripts and recordings."""

    categories: Required[
        List[
            Literal[
                "person_name",
                "address",
                "email",
                "phone_number",
                "ssn",
                "passport",
                "driver_license",
                "credit_card",
                "bank_account",
                "password",
                "pin",
                "medical_id",
                "date_of_birth",
                "customer_account_number",
            ]
        ]
    ]
    """List of PII categories to scrub from transcripts and recordings."""

    mode: Required[Literal["post_call"]]
    """The processing mode for PII scrubbing. Currently only post-call is supported."""


class PostChatAnalysisDataStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""


class PostChatAnalysisDataEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""


class PostChatAnalysisDataBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""


class PostChatAnalysisDataNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""


PostChatAnalysisData: TypeAlias = Union[
    PostChatAnalysisDataStringAnalysisData,
    PostChatAnalysisDataEnumAnalysisData,
    PostChatAnalysisDataBooleanAnalysisData,
    PostChatAnalysisDataNumberAnalysisData,
]
