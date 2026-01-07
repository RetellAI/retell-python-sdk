# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "CallCreatePhoneCallParams",
    "AgentOverride",
    "AgentOverrideAgent",
    "AgentOverrideAgentCustomSttConfig",
    "AgentOverrideAgentPiiConfig",
    "AgentOverrideAgentPostCallAnalysisData",
    "AgentOverrideAgentPostCallAnalysisDataStringAnalysisData",
    "AgentOverrideAgentPostCallAnalysisDataEnumAnalysisData",
    "AgentOverrideAgentPostCallAnalysisDataBooleanAnalysisData",
    "AgentOverrideAgentPostCallAnalysisDataNumberAnalysisData",
    "AgentOverrideAgentPronunciationDictionary",
    "AgentOverrideAgentResponseEngine",
    "AgentOverrideAgentResponseEngineResponseEngineRetellLm",
    "AgentOverrideAgentResponseEngineResponseEngineCustomLm",
    "AgentOverrideAgentResponseEngineResponseEngineConversationFlow",
    "AgentOverrideAgentUserDtmfOptions",
    "AgentOverrideAgentVoicemailOption",
    "AgentOverrideAgentVoicemailOptionAction",
    "AgentOverrideAgentVoicemailOptionActionVoicemailActionPrompt",
    "AgentOverrideAgentVoicemailOptionActionVoicemailActionStaticText",
    "AgentOverrideAgentVoicemailOptionActionVoicemailActionHangup",
    "AgentOverrideAgentVoicemailOptionActionVoicemailActionBridgeTransfer",
    "AgentOverrideConversationFlow",
    "AgentOverrideConversationFlowKBConfig",
    "AgentOverrideConversationFlowModelChoice",
    "AgentOverrideRetellLlm",
    "AgentOverrideRetellLlmKBConfig",
]


class CallCreatePhoneCallParams(TypedDict, total=False):
    from_number: Required[str]
    """The number you own in E.164 format.

    Must be a number purchased from Retell or imported to Retell.
    """

    to_number: Required[str]
    """The number you want to call, in E.164 format.

    If using a number purchased from Retell, only US numbers are supported as
    destination.
    """

    agent_override: AgentOverride
    """For this particular call, override agent configuration with these settings.

    This allows you to customize agent behavior for individual calls without
    modifying the base agent.
    """

    custom_sip_headers: Dict[str, str]
    """Add optional custom SIP headers to the call."""

    ignore_e164_validation: bool
    """If true, the e.164 validation will be ignored for the from_number.

    This can be useful when you want to dial to internal pseudo numbers. This only
    applies when you are using custom telephony and does not apply when you are
    using Retell Telephony. If omitted, the default value is false.
    """

    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    override_agent_id: str
    """For this particular call, override the agent used with this agent id.

    This does not bind the agent to this number, this is for one time override.
    """

    override_agent_version: int
    """For this particular call, override the agent version used with this version.

    This does not bind the agent version to this number, this is for one time
    override.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """


class AgentOverrideAgentCustomSttConfig(TypedDict, total=False):
    """Custom STT configuration. Only used when stt_mode is set to custom."""

    endpointing_ms: Required[int]
    """Endpointing timeout in milliseconds. Minimum is 100 for azure, 10 for deepgram."""

    provider: Required[Literal["azure", "deepgram"]]
    """The STT provider to use."""


class AgentOverrideAgentPiiConfig(TypedDict, total=False):
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


class AgentOverrideAgentPostCallAnalysisDataStringAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["string"]]
    """Type of the variable to extract."""

    examples: SequenceNotStr[str]
    """Examples of the variable value to teach model the style and syntax."""


class AgentOverrideAgentPostCallAnalysisDataEnumAnalysisData(TypedDict, total=False):
    choices: Required[SequenceNotStr[str]]
    """The possible values of the variable, must be non empty array."""

    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["enum"]]
    """Type of the variable to extract."""


class AgentOverrideAgentPostCallAnalysisDataBooleanAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["boolean"]]
    """Type of the variable to extract."""


class AgentOverrideAgentPostCallAnalysisDataNumberAnalysisData(TypedDict, total=False):
    description: Required[str]
    """Description of the variable."""

    name: Required[str]
    """Name of the variable."""

    type: Required[Literal["number"]]
    """Type of the variable to extract."""


AgentOverrideAgentPostCallAnalysisData: TypeAlias = Union[
    AgentOverrideAgentPostCallAnalysisDataStringAnalysisData,
    AgentOverrideAgentPostCallAnalysisDataEnumAnalysisData,
    AgentOverrideAgentPostCallAnalysisDataBooleanAnalysisData,
    AgentOverrideAgentPostCallAnalysisDataNumberAnalysisData,
]


class AgentOverrideAgentPronunciationDictionary(TypedDict, total=False):
    alphabet: Required[Literal["ipa", "cmu"]]
    """The phonetic alphabet to be used for pronunciation."""

    phoneme: Required[str]
    """Pronunciation of the word in the format of a IPA / CMU pronunciation."""

    word: Required[str]
    """The string of word / phrase to be annotated with pronunciation."""


class AgentOverrideAgentResponseEngineResponseEngineRetellLm(TypedDict, total=False):
    llm_id: Required[str]
    """id of the Retell LLM Response Engine."""

    type: Required[Literal["retell-llm"]]
    """type of the Response Engine."""

    version: Optional[float]
    """Version of the Retell LLM Response Engine."""


class AgentOverrideAgentResponseEngineResponseEngineCustomLm(TypedDict, total=False):
    llm_websocket_url: Required[str]
    """LLM websocket url of the custom LLM."""

    type: Required[Literal["custom-llm"]]
    """type of the Response Engine."""


class AgentOverrideAgentResponseEngineResponseEngineConversationFlow(TypedDict, total=False):
    conversation_flow_id: Required[str]
    """ID of the Conversation Flow Response Engine."""

    type: Required[Literal["conversation-flow"]]
    """type of the Response Engine."""

    version: Optional[float]
    """Version of the Conversation Flow Response Engine."""


AgentOverrideAgentResponseEngine: TypeAlias = Union[
    AgentOverrideAgentResponseEngineResponseEngineRetellLm,
    AgentOverrideAgentResponseEngineResponseEngineCustomLm,
    AgentOverrideAgentResponseEngineResponseEngineConversationFlow,
]


class AgentOverrideAgentUserDtmfOptions(TypedDict, total=False):
    digit_limit: Optional[float]
    """
    The maximum number of digits allowed in the user's DTMF (Dual-Tone
    Multi-Frequency) input per turn. Once this limit is reached, the input is
    considered complete and a response will be generated immediately.
    """

    termination_key: Optional[str]
    """A single key that signals the end of DTMF input.

    Acceptable values include any digit (0-9), the pound/hash symbol (#), or the
    asterisk (\\**).
    """

    timeout_ms: int
    """The time (in milliseconds) to wait for user DTMF input before timing out.

    The timer resets with each digit received.
    """


class AgentOverrideAgentVoicemailOptionActionVoicemailActionPrompt(TypedDict, total=False):
    text: Required[str]
    """
    The prompt used to generate the text to be spoken when the call is detected to
    be in voicemail.
    """

    type: Required[Literal["prompt"]]


class AgentOverrideAgentVoicemailOptionActionVoicemailActionStaticText(TypedDict, total=False):
    text: Required[str]
    """The text to be spoken when the call is detected to be in voicemail."""

    type: Required[Literal["static_text"]]


class AgentOverrideAgentVoicemailOptionActionVoicemailActionHangup(TypedDict, total=False):
    type: Required[Literal["hangup"]]


class AgentOverrideAgentVoicemailOptionActionVoicemailActionBridgeTransfer(TypedDict, total=False):
    type: Required[Literal["bridge_transfer"]]


AgentOverrideAgentVoicemailOptionAction: TypeAlias = Union[
    AgentOverrideAgentVoicemailOptionActionVoicemailActionPrompt,
    AgentOverrideAgentVoicemailOptionActionVoicemailActionStaticText,
    AgentOverrideAgentVoicemailOptionActionVoicemailActionHangup,
    AgentOverrideAgentVoicemailOptionActionVoicemailActionBridgeTransfer,
]


class AgentOverrideAgentVoicemailOption(TypedDict, total=False):
    """
    If this option is set, the call will try to detect voicemail in the first 3 minutes of the call. Actions defined (hangup, or leave a message) will be applied when the voicemail is detected. Set this to null to disable voicemail detection.
    """

    action: Required[AgentOverrideAgentVoicemailOptionAction]


class AgentOverrideAgent(TypedDict, total=False):
    """Override agent configuration settings.

    Any properties specified here will override the base agent configuration for this call.
    """

    agent_name: Optional[str]
    """The name of the agent. Only used for your own reference."""

    allow_user_dtmf: bool
    """If set to true, DTMF input will be accepted and processed.

    If false, any DTMF input will be ignored. Default to true.
    """

    ambient_sound: Optional[
        Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"]
    ]
    """
    If set, will add ambient environment sound to the call to make experience more
    realistic. Currently supports the following options:

    - `coffee-shop`: Coffee shop ambience with people chatting in background.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/coffee-shop.wav)
    - `convention-hall`: Convention hall ambience, with some echo and people
      chatting in background.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/convention-hall.wav)
    - `summer-outdoor`: Summer outdoor ambience with cicada chirping.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/summer-outdoor.wav)
    - `mountain-outdoor`: Mountain outdoor ambience with birds singing.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/mountain-outdoor.wav)
    - `static-noise`: Constant static noise.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/static-noise.wav)
    - `call-center`: Call center work noise.
      [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/call-center.wav)
      Set to `null` to remove ambient sound from this agent.
    """

    ambient_sound_volume: float
    """If set, will control the volume of the ambient sound.

    Value ranging from [0,2]. Lower value means quieter ambient sound, while higher
    value means louder ambient sound. If unset, default value 1 will apply.
    """

    analysis_successful_prompt: Optional[str]
    """
    Prompt to determine whether the post call or chat analysis should mark the
    interaction as successful. Set to null to use the default prompt.
    """

    analysis_summary_prompt: Optional[str]
    """Prompt to guide how the post call or chat analysis summary should be generated.

    When unset, the default system prompt is used. Set to null to use the default
    prompt.
    """

    backchannel_frequency: float
    """Only applicable when enable_backchannel is true.

    Controls how often the agent would backchannel when a backchannel is possible.
    Value ranging from [0,1]. Lower value means less frequent backchannel, while
    higher value means more frequent backchannel. If unset, default value 0.8 will
    apply.
    """

    backchannel_words: Optional[SequenceNotStr[str]]
    """Only applicable when enable_backchannel is true.

    A list of words that the agent would use as backchannel. If not set, default
    backchannel words will apply. Check out
    [backchannel default words](/agent/interaction-configuration#backchannel) for
    more details. Note that certain voices do not work too well with certain words,
    so it's recommended to experiment before adding any words.
    """

    begin_message_delay_ms: int
    """
    If set, will delay the first message by the specified amount of milliseconds, so
    that it gives user more time to prepare to take the call. Valid range is [0,
    5000]. If not set or set to 0, agent will speak immediately. Only applicable
    when agent speaks first.
    """

    boosted_keywords: Optional[SequenceNotStr[str]]
    """
    Provide a customized list of keywords to bias the transcriber model, so that
    these words are more likely to get transcribed. Commonly used for names, brands,
    street, etc.
    """

    custom_stt_config: AgentOverrideAgentCustomSttConfig
    """Custom STT configuration. Only used when stt_mode is set to custom."""

    data_storage_setting: Literal["everything", "everything_except_pii", "basic_attributes_only"]
    """
    Granular setting to manage how Retell stores sensitive data (transcripts,
    recordings, logs, etc.). This replaces the deprecated
    `opt_out_sensitive_data_storage` field.

    - `everything`: Store all data including transcripts, recordings, and logs.
    - `everything_except_pii`: Store data without PII when PII is detected.
    - `basic_attributes_only`: Store only basic attributes; no
      transcripts/recordings/logs. If not set, default value of "everything" will
      apply.
    """

    denoising_mode: Literal["noise-cancellation", "noise-and-background-speech-cancellation"]
    """If set, determines what denoising mode to use. Default to noise-cancellation."""

    enable_backchannel: bool
    """
    Controls whether the agent would backchannel (agent interjects the speaker with
    phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
    when enabled tends to show up more in longer user utterances. If not set, agent
    will not backchannel.
    """

    enable_voicemail_detection: bool
    """If set to true, will detect whether the call enters a voicemail.

    Note that this feature is only available for phone calls.
    """

    end_call_after_silence_ms: int
    """If users stay silent for a period after agent speech, end the call.

    The minimum value allowed is 10,000 ms (10 s). By default, this is set to 600000
    (10 min).
    """

    fallback_voice_ids: Optional[SequenceNotStr[str]]
    """
    When TTS provider for the selected voice is experiencing outages, we would use
    fallback voices listed here for the agent. Voice id and the fallback voice ids
    must be from different TTS providers. The system would go through the list in
    order, if the first one in the list is also having outage, it would use the next
    one. Set to null to remove voice fallback for the agent.
    """

    interruption_sensitivity: float
    """Controls how sensitive the agent is to user interruptions.

    Value ranging from [0,1]. Lower value means it will take longer / more words for
    user to interrupt agent, while higher value means it's easier for user to
    interrupt agent. If unset, default value 1 will apply. When this is set to 0,
    agent would never be interrupted.
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
        "vi-VN",
        "ro-RO",
        "bg-BG",
        "ca-ES",
        "th-TH",
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
        "ms-MY",
        "af-ZA",
        "ar-SA",
        "az-AZ",
        "bs-BA",
        "cy-GB",
        "fa-IR",
        "fil-PH",
        "gl-ES",
        "he-IL",
        "hr-HR",
        "hy-AM",
        "is-IS",
        "kk-KZ",
        "kn-IN",
        "mk-MK",
        "mr-IN",
        "ne-NP",
        "sl-SI",
        "sr-RS",
        "sw-KE",
        "ta-IN",
        "ur-IN",
        "yue-CN",
        "uk-UA",
        "multi",
    ]
    """Specifies what language (and dialect) the speech recognition will operate in.

    For instance, selecting `en-GB` optimizes speech recognition for British
    English. If unset, will use default value `en-US`. Select `multi` for
    multilingual support.
    """

    max_call_duration_ms: int
    """Maximum allowed length for the call, will force end the call if reached.

    The minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
    7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).
    """

    normalize_for_speech: bool
    """
    If set to true, will normalize the some part of text (number, currency, date,
    etc) to spoken to its spoken form for more consistent speech synthesis
    (sometimes the voice synthesize system itself might read these wrong with the
    raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
    2024 for the $24.12 payment" to "Call my number two one three seven one one two
    three four two on july fifth, twenty twenty four for the twenty four dollars
    twelve cents payment" before starting audio generation.
    """

    opt_in_signed_url: bool
    """Whether this agent opts in for signed URLs for public logs and recordings.

    When enabled, the generated URLs will include security signatures that restrict
    access and automatically expire after 24 hours.
    """

    pii_config: AgentOverrideAgentPiiConfig
    """Configuration for PII scrubbing from transcripts and recordings."""

    post_call_analysis_data: Optional[Iterable[AgentOverrideAgentPostCallAnalysisData]]
    """Post call analysis data to extract from the call.

    This data will augment the pre-defined variables extracted in the call analysis.
    This will be available after the call ends.
    """

    post_call_analysis_model: Optional[
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
    """The model to use for post call analysis. Default to gpt-4.1-mini."""

    pronunciation_dictionary: Optional[Iterable[AgentOverrideAgentPronunciationDictionary]]
    """
    A list of words / phrases and their pronunciation to be used to guide the audio
    synthesize for consistent pronunciation. Currently only supported for English &
    11labs voices. Set to null to remove pronunciation dictionary from this agent.
    """

    reminder_max_count: int
    """
    If set, controls how many times agent would remind user when user is
    unresponsive. Must be a non negative integer. If unset, default value of 1 will
    apply (remind once). Set to 0 to disable agent from reminding.
    """

    reminder_trigger_ms: float
    """
    If set (in milliseconds), will trigger a reminder to the agent to speak if the
    user has been silent for the specified duration after some agent speech. Must be
    a positive number. If unset, default value of 10000 ms (10 s) will apply.
    """

    response_engine: AgentOverrideAgentResponseEngine
    """The Response Engine to attach to the agent.

    It is used to generate responses for the agent. You need to create a Response
    Engine first before attaching it to an agent.
    """

    responsiveness: float
    """Controls how responsive is the agent.

    Value ranging from [0,1]. Lower value means less responsive agent (wait more,
    respond slower), while higher value means faster exchanges (respond when it
    can). If unset, default value 1 will apply.
    """

    ring_duration_ms: int
    """If set, the phone ringing will last for the specified amount of milliseconds.

    This applies for both outbound call ringtime, and call transfer ringtime.
    Default to 30000 (30 s). Valid range is [5000, 90000].
    """

    signed_url_expiration_ms: Optional[int]
    """The expiration time for the signed url in milliseconds.

    Only applicable when opt_in_signed_url is true. If not set, default value of
    86400000 (24 hours) will apply.
    """

    stt_mode: Literal["fast", "accurate", "custom"]
    """If set, determines whether speech to text should focus on latency or accuracy.

    Default to fast mode. When set to custom, custom_stt_config must be provided.
    """

    user_dtmf_options: Optional[AgentOverrideAgentUserDtmfOptions]

    version_description: Optional[str]
    """Optional description of the agent version.

    Used for your own reference and documentation.
    """

    vocab_specialization: Literal["general", "medical"]
    """If set, determines the vocabulary set to use for transcription.

    This setting only applies for English agents, for non English agent, this
    setting is a no-op. Default to general.
    """

    voice_id: str
    """Unique voice id used for the agent.

    Find list of available voices and their preview in Dashboard.
    """

    voice_model: Optional[
        Literal[
            "eleven_turbo_v2",
            "eleven_flash_v2",
            "eleven_turbo_v2_5",
            "eleven_flash_v2_5",
            "eleven_multilingual_v2",
            "sonic-2",
            "sonic-3",
            "sonic-3-latest",
            "sonic-turbo",
            "tts-1",
            "gpt-4o-mini-tts",
            "speech-02-turbo",
        ]
    ]
    """Select the voice model used for the selected voice.

    Each provider has a set of available voice models. Set to null to remove voice
    model selection, and default ones will apply. Check out dashboard for more
    details of each voice model.
    """

    voice_speed: float
    """Controls speed of voice.

    Value ranging from [0.5,2]. Lower value means slower speech, while higher value
    means faster speech rate. If unset, default value 1 will apply.
    """

    voice_temperature: float
    """Controls how stable the voice is.

    Value ranging from [0,2]. Lower value means more stable, and higher value means
    more variant speech generation. Currently this setting only applies to `11labs`
    voices. If unset, default value 1 will apply.
    """

    voicemail_detection_timeout_ms: int
    """
    Configures when to stop running voicemail detection, as it becomes unlikely to
    hit voicemail after a couple minutes, and keep running it will only have
    negative impact. The minimum value allowed is 5,000 ms (5 s), and maximum value
    allowed is 180,000 (3 minutes). By default, this is set to 30,000 (30 s).
    """

    voicemail_message: str
    """The message to be played when the call enters a voicemail.

    Note that this feature is only available for phone calls. If you want to hangup
    after hitting voicemail, set this to empty string.
    """

    voicemail_option: Optional[AgentOverrideAgentVoicemailOption]
    """
    If this option is set, the call will try to detect voicemail in the first 3
    minutes of the call. Actions defined (hangup, or leave a message) will be
    applied when the voicemail is detected. Set this to null to disable voicemail
    detection.
    """

    volume: float
    """If set, will control the volume of the agent.

    Value ranging from [0,2]. Lower value means quieter agent speech, while higher
    value means louder agent speech. If unset, default value 1 will apply.
    """

    webhook_timeout_ms: int
    """The timeout for the webhook in milliseconds.

    If not set, default value of 10000 will apply.
    """

    webhook_url: Optional[str]
    """The webhook for agent to listen to call events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """


class AgentOverrideConversationFlowKBConfig(TypedDict, total=False):
    """Knowledge base configuration for RAG retrieval."""

    filter_score: float
    """Similarity threshold for filtering search results"""

    top_k: int
    """Max number of knowledge base chunks to retrieve"""


class AgentOverrideConversationFlowModelChoice(TypedDict, total=False):
    """The model choice for the conversation flow."""

    model: Required[
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
    """The LLM model to use"""

    type: Required[Literal["cascading"]]
    """Type of model choice"""

    high_priority: bool
    """Whether to use high priority pool with more dedicated resource, default false"""


class AgentOverrideConversationFlow(TypedDict, total=False):
    """Override conversation flow configuration settings.

    Only applicable when using conversation flow as the response engine. Supported attributes - model_choice, model_temperature, tool_call_strict_mode, knowledge_base_ids, kb_config, start_speaker, begin_after_user_silence_ms.
    """

    begin_after_user_silence_ms: Optional[int]
    """
    If set, the AI will begin the conversation after waiting for the user for the
    duration (in milliseconds) specified by this attribute. This only applies if the
    agent is configured to wait for the user to speak first. If not set, the agent
    will wait indefinitely for the user to speak.
    """

    kb_config: AgentOverrideConversationFlowKBConfig
    """Knowledge base configuration for RAG retrieval."""

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """Knowledge base IDs for RAG (Retrieval-Augmented Generation)."""

    model_choice: AgentOverrideConversationFlowModelChoice
    """The model choice for the conversation flow."""

    model_temperature: Optional[float]
    """Controls the randomness of the model's responses.

    Lower values make responses more deterministic.
    """

    start_speaker: Literal["user", "agent"]
    """Who starts the conversation - user or agent."""

    tool_call_strict_mode: Optional[bool]
    """Whether to use strict mode for tool calls.

    Only applicable when using certain supported models.
    """


class AgentOverrideRetellLlmKBConfig(TypedDict, total=False):
    """Knowledge base configuration for RAG retrieval."""

    filter_score: float
    """Similarity threshold for filtering search results"""

    top_k: int
    """Max number of knowledge base chunks to retrieve"""


class AgentOverrideRetellLlm(TypedDict, total=False):
    """Override Retell LLM configuration settings.

    Only applicable when using Retell LLM as the response engine. Supported attributes - model, s2s_model, model_temperature, model_high_priority, tool_call_strict_mode, knowledge_base_ids, kb_config, start_speaker, begin_after_user_silence_ms, begin_message.
    """

    begin_after_user_silence_ms: Optional[int]
    """
    If set, the AI will begin the conversation after waiting for the user for the
    duration (in milliseconds) specified by this attribute. This only applies if the
    agent is configured to wait for the user to speak first. If not set, the agent
    will wait indefinitely for the user to speak.
    """

    begin_message: Optional[str]
    """First utterance said by the agent in the call.

    If not set, LLM will dynamically generate a message. If set to "", agent will
    wait for user to speak first.
    """

    kb_config: Optional[AgentOverrideRetellLlmKBConfig]
    """Knowledge base configuration for RAG retrieval."""

    knowledge_base_ids: Optional[SequenceNotStr[str]]
    """A list of knowledge base ids to use for this resource."""

    model: Optional[
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
    """Select the underlying text LLM. If not set, would default to gpt-4.1."""

    model_high_priority: Optional[bool]
    """
    If set to true, will use high priority pool with more dedicated resource to
    ensure lower and more consistent latency, default to false. This feature usually
    comes with a higher cost.
    """

    model_temperature: float
    """If set, will control the randomness of the response.

    Value ranging from [0,1]. Lower value means more deterministic, while higher
    value means more random. If unset, default value 0 will apply. Note that for
    tool calling, a lower value is recommended.
    """

    s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime", "gpt-realtime", "gpt-realtime-mini"]]
    """Select the underlying speech to speech model.

    Can only set this or model, not both.
    """

    start_speaker: Literal["user", "agent"]
    """The speaker who starts the conversation.

    Required. Must be either 'user' or 'agent'.
    """

    tool_call_strict_mode: Optional[bool]
    """Whether to use strict mode for tool calls.

    Only applicable when using certain supported models.
    """


class AgentOverride(TypedDict, total=False):
    """For this particular call, override agent configuration with these settings.

    This allows you to customize agent behavior for individual calls without modifying the base agent.
    """

    agent: AgentOverrideAgent
    """Override agent configuration settings.

    Any properties specified here will override the base agent configuration for
    this call.
    """

    conversation_flow: AgentOverrideConversationFlow
    """Override conversation flow configuration settings.

    Only applicable when using conversation flow as the response engine. Supported
    attributes - model_choice, model_temperature, tool_call_strict_mode,
    knowledge_base_ids, kb_config, start_speaker, begin_after_user_silence_ms.
    """

    retell_llm: AgentOverrideRetellLlm
    """Override Retell LLM configuration settings.

    Only applicable when using Retell LLM as the response engine. Supported
    attributes - model, s2s_model, model_temperature, model_high_priority,
    tool_call_strict_mode, knowledge_base_ids, kb_config, start_speaker,
    begin_after_user_silence_ms, begin_message.
    """
