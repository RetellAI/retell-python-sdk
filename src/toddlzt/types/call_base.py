# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CallBase"]


class CallBase(BaseModel):
    agent_id: str
    """Corresponding agent id of this call."""

    audio_encoding: Literal["s16le", "mulaw"]
    """The audio encoding of the call. The following formats are supported:

    - `s16le` 16 bit linear PCM audio, the native format for web audio capture and
      playback.

    - `mulaw` non-linear audio encoding technique used in telephony. Commonly used
      by Twilio.
    """

    audio_websocket_protocol: Literal["web", "twilio", "vonage"]
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

    call_id: str
    """Unique id of the call.

    Used to identify in LLM websocket and used to authenticate in audio websocket.
    """

    call_status: Literal["registered", "ongoing", "ended", "error"]
    """Status of call.

    - `registered`: Call id issued, ready to make a call using this id.

    - `ongoing`: Call connected and ongoing.

    - `ended`: The underlying websocket has ended for the call. Either user or agent
      hanged up, or call transferred.

    - `error`: Call encountered error.
    """

    sample_rate: int
    """
    Sample rate of the conversation, the input and output audio bytes will all
    conform to this rate. Check the audio source, audio format, and voice used for
    the agent to select one that works.

    - `elevenlabs voices`: supports sample rate ranging from [8000,44100]

    - `openai voices`: supports sample rate ranging from [8000,24000]
    """

    start_timestamp: int
    """Begin timestamp (milliseconds since epoch) of the call."""
