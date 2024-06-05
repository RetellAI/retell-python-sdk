# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CallRegisterParams"]


class CallRegisterParams(TypedDict, total=False):
    agent_id: Required[str]
    """Unique id of agent used for the call.

    Your agent would contain the LLM Websocket url used for this call.
    """

    audio_encoding: Required[Literal["s16le", "mulaw"]]
    """The audio encoding of the call. The following formats are supported:

    - `s16le` 16 bit linear PCM audio, the native format for web audio capture and
      playback.

    - `mulaw` non-linear audio encoding technique used in telephony. Commonly used
      by Twilio.
    """

    audio_websocket_protocol: Required[Literal["web", "twilio"]]
    """
    Where the audio websocket would connect from would determine the format /
    protocol of websocket messages, and would determine how our server read audio
    bytes and send audio bytes.:

    - `web`: The protocol defined by Retell, commonly used for connecting from web
      frontend. Also useful for those who want to manipulate audio bytes directly.

    - `twilio`: The
      [websocket protocol](https://www.twilio.com/docs/voice/twiml/stream#message-media)
      defined by Twilio, used when your system uses Twilio, and supplies Retell
      audio websocket url to Twilio.
    """

    sample_rate: Required[int]
    """
    Sample rate of the conversation, the input and output audio bytes will all
    conform to this rate. Check the audio source, audio format, and voice used for
    the agent to select one that works. supports value ranging from [8000, 48000].
    Note for Twilio `mulaw` encoding, the sample rate has to be 8000.

    - `s16le` sample rate recommendation (natively supported, lowest latency):

      - elevenlabs voices: 16000, 22050, 24000, 44100.
      - openai voices: 24000.

      - deepgram voices: 8000, 16000, 24000, 32000, 48000.
    """

    direction: Literal["inbound", "outbound"]
    """Direction of the phone call.

    Not populated for web call. When you are using custom Twilio, we don't have this
    information, so you would need to specify this field if you want this
    information in the call history.
    """

    end_call_after_silence_ms: int
    """If users stay silent for a period after agent speech, end the call.

    The minimum value allowed is 10,000 ms (10 s). This value, if set, would
    overwrite the agent level end_call_after_silence_ms parameter.
    """

    from_number: str
    """The caller number.

    When you are using custom Twilio, we don't have this information, so you would
    need to specify this field if you want this information in the call history.
    """

    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Retell LLM prompt and tool description. Only applicable for Retell LLM.
    """

    to_number: str
    """The callee number.

    When you are using custom Twilio, we don't have this information, so you would
    need to specify this field if you want this information in the call history.
    """
