# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentUpdateParams", "PronunciationDictionary"]


class AgentUpdateParams(TypedDict, total=False):
    agent_name: Optional[str]
    """The name of the agent. Only used for your own reference."""

    ambient_sound: Optional[
        Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise"]
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

    Set to `null` to remove ambient sound from this agent.
    """

    backchannel_frequency: float
    """Only applicable when enable_backchannel is true.

    Controls how often the agent would backchannel when a backchannel is possible.
    Value ranging from [0,1]. Lower value means less frequent backchannel, while
    higher value means more frequent backchannel. If unset, default value 0.8 will
    apply.
    """

    backchannel_words: List[str]
    """Only applicable when enable_backchannel is true.

    A list of words that the agent would use as backchannel. If not set, default
    backchannel words will apply. Check out
    [backchannel default words](/agent/interaction-configuration#backchannel) for
    more details. Note that certain voices do not work too well with certain words,
    so it's recommended to expeirment before adding any words.
    """

    boosted_keywords: Optional[List[str]]
    """
    Provide a customized list of keywords to bias the transcriber model, so that
    these words are more likely to get transcribed. Commonly used for names, brands,
    street, etc.
    """

    enable_backchannel: bool
    """
    Controls whether the agent would backchannel (agent interjects the speaker with
    phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
    when enabled tends to show up more in longer user utterances. If not set, agent
    will not backchannel.
    """

    end_call_after_silence_ms: int
    """If users stay silent for a period after agent speech, end the call.

    The minimum value allowed is 10,000 ms (10 s). By default, this is set to 600000
    (10 min).
    """

    interruption_sensitivity: float
    """Controls how sensitive the agent is to user interruptions.

    Value ranging from [0,1]. Lower value means it will take longer / more words for
    user to interrupt agent, while higher value means it's easier for user to
    interrupt agent. If unset, default value 1 will apply. When this is set to 0,
    agent would never be interrupted.
    """

    language: Literal[
        "en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR", "fr-FR"
    ]
    """Specifies what language (and dialect) the speech recognition will operate in.

    For instance, selecting `en-GB` optimizes speech recognition for British
    English. If unset, will use default value `en-US`.
    """

    llm_websocket_url: str
    """
    The URL we will establish LLM websocket for getting response, usually your
    server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
    request format (sent from us) and response format (send to us).
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

    opt_out_sensitive_data_storage: bool
    """
    Whether this agent opts out of sensitive data storage like transcript,
    recording, logging. These data can still be accessed securely via webhooks. If
    not set, default value of false will apply.
    """

    pronunciation_dictionary: Optional[Iterable[PronunciationDictionary]]
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

    responsiveness: float
    """Controls how responsive is the agent.

    Value ranging from [0,1]. Lower value means less responsive agent (wait more,
    respond slower), while higher value means faster exchanges (respond when it
    can). If unset, default value 1 will apply.
    """

    voice_id: str
    """Unique voice id used for the agent.

    Find list of available voices and their preview in Dashboard.
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

    webhook_url: Optional[str]
    """The webhook for agent to listen to call events.

    See what events it would get at [webhook doc](/features/webhook). If set, will
    binds webhook events for this agent to the specified url, and will ignore the
    account level webhook for this agent. Set to `null` to remove webhook url from
    this agent.
    """


class PronunciationDictionary(TypedDict, total=False):
    alphabet: Required[Literal["ipa", "cmu"]]
    """The phonetic alphabet to be used for pronunciation."""

    phoneme: Required[str]
    """Pronunciation of the word in the format of a IPA / CMU pronunciation."""

    word: Required[str]
    """The string of word / phrase to be annotated with pronunciation."""
