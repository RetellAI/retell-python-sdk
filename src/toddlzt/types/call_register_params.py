# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

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

    audio_websocket_protocol: Required[Literal["web", "twilio", "vonage"]]
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

    - `vonage`: (Coming soon) The
      [websocket protocol](https://developer.vonage.com/en/voice/voice-api/concepts/websockets)
      defined by Vonage, used when your system uses Vonage, and supplies Retell
      audio websocket url to Vonage.
    """

    sample_rate: Required[int]
    """
    Sample rate of the conversation, the input and output audio bytes will all
    conform to this rate. Check the audio source, audio format, and voice used for
    the agent to select one that works.

    - `elevenlabs voices`: supports sample rate ranging from [8000,44100]

    - `openai voices`: supports sample rate ranging from [8000,24000]
    """
