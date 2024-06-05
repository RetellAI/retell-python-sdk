# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RegisterCallResponse"]


class RegisterCallResponse(BaseModel):
    agent_id: str
    """Corresponding agent id of this call."""

    audio_encoding: Literal["s16le", "mulaw"]
    """The audio encoding of the call. The following formats are supported:

    - `s16le` 16 bit linear PCM audio, the native format for web audio capture and
      playback.

    - `mulaw` non-linear audio encoding technique used in telephony. Commonly used
      by Twilio.
    """

    audio_websocket_protocol: Literal["web", "twilio"]
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
    the agent to select one that works. supports value ranging from [8000, 48000].
    Note for Twilio `mulaw` encoding, the sample rate has to be 8000.

    - `s16le` sample rate recommendation (natively supported, lowest latency):

      - elevenlabs voices: 16000, 22050, 24000, 44100.
      - openai voices: 24000.

      - deepgram voices: 8000, 16000, 24000, 32000, 48000.
    """

    direction: Optional[Literal["inbound", "outbound"]] = None
    """Direction of the phone call. Not populated for web call."""

    drop_call_if_machine_detected: Optional[bool] = None
    """If set, will drop the call if machine (voicemail, IVR) is detected.

    If not set, default value of false will apply.
    """

    end_call_after_silence_ms: Optional[int] = None
    """If users stay silent for a period after agent speech, end the call.

    The minimum value allowed is 10,000 ms (10 s). This value, if set, would
    overwrite the agent level end_call_after_silence_ms parameter.
    """

    from_number: Optional[str] = None
    """The caller number."""

    metadata: Optional[object] = None
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    opt_out_sensitive_data_storage: Optional[bool] = None
    """
    Whether this call opts out of sensitive data storage like transcript, recording,
    logging.
    """

    retell_llm_dynamic_variables: Optional[Dict[str, object]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Retell LLM prompt and tool description. Only applicable for Retell LLM.
    """

    to_number: Optional[str] = None
    """The callee number."""
