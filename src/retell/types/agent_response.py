# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AgentResponse",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineCustomLm",
    "PostCallAnalysisData",
    "PostCallAnalysisDataStringAnalysisData",
    "PostCallAnalysisDataEnumAnalysisData",
    "PostCallAnalysisDataBooleanAnalysisData",
    "PostCallAnalysisDataNumberAnalysisData",
    "PronunciationDictionary",
]


class ResponseEngineResponseEngineRetellLm(BaseModel):
    llm_id: str
    """id of the Retell LLM to use."""

    type: Literal["retell-llm"]
    """type of the response engine."""


class ResponseEngineResponseEngineCustomLm(BaseModel):
    llm_websocket_url: str
    """LLM websocket url of the custom LLM."""

    type: Literal["custom-llm"]
    """type of the response engine."""


ResponseEngine: TypeAlias = Union[ResponseEngineResponseEngineRetellLm, ResponseEngineResponseEngineCustomLm]


class PostCallAnalysisDataStringAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["string"]
    """Type of the variable to extract."""

    examples: Optional[List[str]] = None
    """Examples of the variable value to teach model the style and syntax."""


class PostCallAnalysisDataEnumAnalysisData(BaseModel):
    choices: List[str]
    """The possible values of the variable, must be non empty array."""

    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["enum"]
    """Type of the variable to extract."""


class PostCallAnalysisDataBooleanAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["boolean"]
    """Type of the variable to extract."""


class PostCallAnalysisDataNumberAnalysisData(BaseModel):
    description: str
    """Description of the variable."""

    name: str
    """Name of the variable."""

    type: Literal["number"]
    """Type of the variable to extract."""


PostCallAnalysisData: TypeAlias = Union[
    PostCallAnalysisDataStringAnalysisData,
    PostCallAnalysisDataEnumAnalysisData,
    PostCallAnalysisDataBooleanAnalysisData,
    PostCallAnalysisDataNumberAnalysisData,
]


class PronunciationDictionary(BaseModel):
    alphabet: Literal["ipa", "cmu"]
    """The phonetic alphabet to be used for pronunciation."""

    phoneme: str
    """Pronunciation of the word in the format of a IPA / CMU pronunciation."""

    word: str
    """The string of word / phrase to be annotated with pronunciation."""


class AgentResponse(BaseModel):
    agent_id: str
    """Unique id of agent."""

    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    response_engine: ResponseEngine
    """The response engine to use for the agent."""

    voice_id: str
    """Unique voice id used for the agent.

    Find list of available voices and their preview in Dashboard.
    """

    agent_name: Optional[str] = None
    """The name of the agent. Only used for your own reference."""

    ambient_sound: Optional[
        Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"]
    ] = None
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

    ambient_sound_volume: Optional[float] = None
    """If set, will control the volume of the ambient sound.

    Value ranging from [0,2]. Lower value means quieter ambient sound, while higher
    value means louder ambient sound. If unset, default value 1 will apply.
    """

    backchannel_frequency: Optional[float] = None
    """Only applicable when enable_backchannel is true.

    Controls how often the agent would backchannel when a backchannel is possible.
    Value ranging from [0,1]. Lower value means less frequent backchannel, while
    higher value means more frequent backchannel. If unset, default value 0.8 will
    apply.
    """

    backchannel_words: Optional[List[str]] = None
    """Only applicable when enable_backchannel is true.

    A list of words that the agent would use as backchannel. If not set, default
    backchannel words will apply. Check out
    [backchannel default words](/agent/interaction-configuration#backchannel) for
    more details. Note that certain voices do not work too well with certain words,
    so it's recommended to expeirment before adding any words.
    """

    begin_message_delay_ms: Optional[int] = None
    """
    If set, will delay the first message by the specified amount of milliseconds, so
    that it gives user more time to prepare to take the call. Valid range is [0,
    5000]. If not set or set to 0, agent will speak immediately. Only applicable
    when agent speaks first.
    """

    boosted_keywords: Optional[List[str]] = None
    """
    Provide a customized list of keywords to bias the transcriber model, so that
    these words are more likely to get transcribed. Commonly used for names, brands,
    street, etc.
    """

    enable_backchannel: Optional[bool] = None
    """
    Controls whether the agent would backchannel (agent interjects the speaker with
    phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
    when enabled tends to show up more in longer user utterances. If not set, agent
    will not backchannel.
    """

    enable_transcription_formatting: Optional[bool] = None
    """If set to true, will format transcription to number, date, email, etc.

    If set to false, will return transcripts in raw words. If not set, default value
    of true will apply.
    """

    enable_voicemail_detection: Optional[bool] = None
    """If set to true, will detect whether the call enters a voicemail.

    Note that this feature is only available for phone calls.
    """

    end_call_after_silence_ms: Optional[int] = None
    """If users stay silent for a period after agent speech, end the call.

    The minimum value allowed is 10,000 ms (10 s). By default, this is set to 600000
    (10 min).
    """

    fallback_voice_ids: Optional[List[str]] = None
    """
    When TTS provider for the selected voice is experiencing outages, we would use
    fallback voices listed here for the agent. Voice id and the fallback voice ids
    must be from different TTS providers. The system would go through the list in
    order, if the first one in the list is also having outage, it would use the next
    one. Set to null to remove voice fallback for the agent.
    """

    interruption_sensitivity: Optional[float] = None
    """Controls how sensitive the agent is to user interruptions.

    Value ranging from [0,1]. Lower value means it will take longer / more words for
    user to interrupt agent, while higher value means it's easier for user to
    interrupt agent. If unset, default value 1 will apply. When this is set to 0,
    agent would never be interrupted.
    """

    language: Optional[
        Literal[
            "en-US",
            "en-IN",
            "en-GB",
            "de-DE",
            "es-ES",
            "es-419",
            "hi-IN",
            "ja-JP",
            "pt-PT",
            "pt-BR",
            "fr-FR",
            "zh-CN",
            "ru-RU",
            "it-IT",
            "ko-KR",
            "nl-NL",
            "pl-PL",
            "tr-TR",
            "vi-VN",
            "multi",
        ]
    ] = None
    """Specifies what language (and dialect) the speech recognition will operate in.

    For instance, selecting `en-GB` optimizes speech recognition for British
    English. If unset, will use default value `en-US`. Select `multi` for
    multilingual support, currently this supports Spanish and English.
    """

    max_call_duration_ms: Optional[int] = None
    """Maximum allowed length for the call, will force end the call if reached.

    The minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
    7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).
    """

    normalize_for_speech: Optional[bool] = None
    """
    If set to true, will normalize the some part of text (number, currency, date,
    etc) to spoken to its spoken form for more consistent speech synthesis
    (sometimes the voice synthesize system itself might read these wrong with the
    raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
    2024 for the $24.12 payment" to "Call my number two one three seven one one two
    three four two on july fifth, twenty twenty four for the twenty four dollars
    twelve cents payment" before starting audio generation.
    """

    opt_out_sensitive_data_storage: Optional[bool] = None
    """
    Whether this agent opts out of sensitive data storage like transcript,
    recording, logging, inbound/outbound phone numbers, etc. These data can still be
    accessed securely via webhooks. If not set, default value of false will apply.
    """

    post_call_analysis_data: Optional[List[PostCallAnalysisData]] = None
    """Post call analysis data to extract from the call.

    This data will augment the pre-defined variables extracted in the call analysis.
    This will be available after the call ends.
    """

    pronunciation_dictionary: Optional[List[PronunciationDictionary]] = None
    """
    A list of words / phrases and their pronunciation to be used to guide the audio
    synthesize for consistent pronunciation. Currently only supported for English &
    11labs voices. Set to null to remove pronunciation dictionary from this agent.
    """

    reminder_max_count: Optional[int] = None
    """
    If set, controls how many times agent would remind user when user is
    unresponsive. Must be a non negative integer. If unset, default value of 1 will
    apply (remind once). Set to 0 to disable agent from reminding.
    """

    reminder_trigger_ms: Optional[float] = None
    """
    If set (in milliseconds), will trigger a reminder to the agent to speak if the
    user has been silent for the specified duration after some agent speech. Must be
    a positive number. If unset, default value of 10000 ms (10 s) will apply.
    """

    responsiveness: Optional[float] = None
    """Controls how responsive is the agent.

    Value ranging from [0,1]. Lower value means less responsive agent (wait more,
    respond slower), while higher value means faster exchanges (respond when it
    can). If unset, default value 1 will apply.
    """

    voice_model: Optional[
        Literal[
            "eleven_turbo_v2",
            "eleven_flash_v2",
            "eleven_turbo_v2_5",
            "eleven_flash_v2_5",
            "eleven_multilingual_v2",
            "Play3.0-mini",
            "PlayDialog",
        ]
    ] = None
    """Optionally set the voice model used for the selected voice.

    Currently only elevenlab voices have voice model selections. Set to null to
    remove voice model selection, and default ones will apply. Check out the
    dashboard for details on each voice model.
    """

    voice_speed: Optional[float] = None
    """Controls speed of voice.

    Value ranging from [0.5,2]. Lower value means slower speech, while higher value
    means faster speech rate. If unset, default value 1 will apply.
    """

    voice_temperature: Optional[float] = None
    """Controls how stable the voice is.

    Value ranging from [0,2]. Lower value means more stable, and higher value means
    more variant speech generation. Currently this setting only applies to `11labs`
    voices. If unset, default value 1 will apply.
    """

    voicemail_detection_timeout_ms: Optional[int] = None
    """
    Configures when to stop running voicemail detection, as it becomes unlikely to
    hit voicemail after a couple minutes, and keep running it will only have
    negative impact. The minimum value allowed is 5,000 ms (5 s), and maximum value
    allowed is 180,000 (3 minutes). By default, this is set to 30,000 (30 s).
    """

    voicemail_message: Optional[str] = None
    """The message to be played when the call enters a voicemail.

    Note that this feature is only available for phone calls. If you want to hangup
    after hitting voicemail, set this to empty string.
    """

    volume: Optional[float] = None
    """If set, will control the volume of the agent.

    Value ranging from [0,2]. Lower value means quieter agent speech, while higher
    value means louder agent speech. If unset, default value 1 will apply.
    """

    webhook_url: Optional[str] = None
    """The webhook for agent to listen to call events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """
