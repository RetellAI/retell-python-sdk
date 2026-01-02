# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ChatAgentResponse",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineCustomLm",
    "ResponseEngineResponseEngineConversationFlow",
    "PiiConfig",
    "PostChatAnalysisData",
    "PostChatAnalysisDataStringAnalysisData",
    "PostChatAnalysisDataEnumAnalysisData",
    "PostChatAnalysisDataBooleanAnalysisData",
    "PostChatAnalysisDataNumberAnalysisData",
]


class ResponseEngineResponseEngineRetellLm(BaseModel):
    llm_id: str
    """id of the Retell LLM Response Engine."""

    type: Literal["retell-llm"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Retell LLM Response Engine."""


class ResponseEngineResponseEngineCustomLm(BaseModel):
    llm_websocket_url: str
    """LLM websocket url of the custom LLM."""

    type: Literal["custom-llm"]
    """type of the Response Engine."""


class ResponseEngineResponseEngineConversationFlow(BaseModel):
    conversation_flow_id: str
    """ID of the Conversation Flow Response Engine."""

    type: Literal["conversation-flow"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Conversation Flow Response Engine."""


ResponseEngine: TypeAlias = Union[
    ResponseEngineResponseEngineRetellLm,
    ResponseEngineResponseEngineCustomLm,
    ResponseEngineResponseEngineConversationFlow,
]


class PiiConfig(BaseModel):
    """Configuration for PII scrubbing from transcripts and recordings."""

    categories: List[
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
    """List of PII categories to scrub from transcripts and recordings."""

    mode: Literal["post_call"]
    """The processing mode for PII scrubbing. Currently only post-call is supported."""


class PostChatAnalysisDataStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""


class PostChatAnalysisDataEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""


class PostChatAnalysisDataBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""


class PostChatAnalysisDataNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""


PostChatAnalysisData: TypeAlias = Union[
    PostChatAnalysisDataStringAnalysisData,
    PostChatAnalysisDataEnumAnalysisData,
    PostChatAnalysisDataBooleanAnalysisData,
    PostChatAnalysisDataNumberAnalysisData,
]


class ChatAgentResponse(BaseModel):
    agent_id: str
    """Unique id of chat agent."""

    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    response_engine: ResponseEngine
    """The Response Engine to attach to the agent.

    It is used to generate responses for the agent. You need to create a Response
    Engine first before attaching it to an agent.
    """

    agent_name: Optional[str] = None
    """The name of the chat agent. Only used for your own reference."""

    analysis_successful_prompt: Optional[str] = None
    """
    The prompt to use for post call analysis to evaluate whether the call is
    successful. Set to null to use the default prompt.
    """

    analysis_summary_prompt: Optional[str] = None
    """The prompt to use for post call analysis to summarize the call.

    Set to null to use the default prompt.
    """

    auto_close_message: Optional[str] = None
    """Message to display when the chat is automatically closed."""

    data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]] = None
    """Controls what data is stored for this agent.

    "everything" stores all data including transcripts and recordings.
    "everything_except_pii" stores data but excludes PII when possible based on PII
    configuration. "basic_attributes_only" stores only basic metadata. If not set,
    defaults to "everything".
    """

    end_chat_after_silence_ms: Optional[int] = None
    """If users stay silent for a period after agent speech, end the chat.

    The minimum value allowed is 360,000 ms (0.1 hours). The maximum value allowed
    is 259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).
    """

    is_public: Optional[bool] = None
    """Whether the agent is public.

    When set to true, the agent is available for public agent preview link.
    """

    is_published: Optional[bool] = None
    """Whether the chat agent is published."""

    language: Optional[
        Literal[
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
    ] = None
    """Specifies what language (and dialect) the chat will operate in.

    For instance, selecting `en-GB` optimizes for British English. If unset, will
    use default value `en-US`. Select `multi` for multilingual support, currently
    this supports Spanish and English.
    """

    opt_in_signed_url: Optional[bool] = None
    """Whether this agent opts in to signed url for public log.

    If not set, default value of false will apply.
    """

    pii_config: Optional[PiiConfig] = None
    """Configuration for PII scrubbing from transcripts and recordings."""

    post_chat_analysis_data: Optional[List[PostChatAnalysisData]] = None
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
    ] = None
    """The model to use for post chat analysis. Default to gpt-4.1-mini."""

    signed_url_expiration_ms: Optional[int] = None
    """The expiration time for the signed url in milliseconds.

    Only applicable when opt_in_signed_url is true. If not set, default value of
    86400000 (24 hours) will apply.
    """

    version: Optional[int] = None
    """The version of the chat agent."""

    webhook_timeout_ms: Optional[int] = None
    """The timeout for the webhook in milliseconds.

    If not set, default value of 10000 will apply.
    """

    webhook_url: Optional[str] = None
    """The webhook for agent to listen to chat events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """
