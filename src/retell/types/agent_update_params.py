# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["AgentUpdateParams"]


class AgentUpdateParams(TypedDict, total=False):
    agent_name: Optional[str]
    """The name of the agent. Only used for your own reference."""

    ambient_sound: Optional[Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor"]]
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

    Set to `null` to remove ambient sound from this agent.
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

    format_text: bool
    """Whether to format the transcribed text with inverse text normalization.

    It transforms the spoken form of text into written form for entities like phone
    number, email address, street address, etc. For example, "february fourth twenty
    twenty two" can be converted into "february 4th 2022". If not set, the default
    is true.
    """

    language: Literal["en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR"]
    """`Beta feature, use with caution.`

    This setting specifies the agent's operational language, including base language
    and dialect. Speech recognition considers both elements, but text-to-speech
    currently only recognizes the base language.

    For instance, selecting `en-GB` optimizes speech recognition for British
    English, yet text-to-speech output will be in standard English. If
    dialect-specific text-to-speech is required, please contact us for support.

    If unset, will use default value `en-US`.

    - `11lab voices`: supports English(en), German(de), Spanish(es), Hindi(hi),
      Portuguese(pt)

    - `openAI voices`: supports English(en), German(de), Spanish(es), Hindi(hi),
      Portuguese(pt), Japanese(ja)

    - `deepgram voices`: supports English(en)
    """

    llm_websocket_url: str
    """
    The URL we will establish LLM websocket for getting response, usually your
    server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
    request format (sent from us) and response format (send to us).
    """

    opt_out_sensitive_data_storage: bool
    """Disable transcripts and recordings storage for enhanced privacy.

    Access transcripts securely via webhooks. If not set, default value of false
    will apply.
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
