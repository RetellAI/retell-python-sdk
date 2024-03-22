# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import RegisterCallCreateResponse, register_call_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["RegisterCalls", "AsyncRegisterCalls"]


class RegisterCalls(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegisterCallsWithRawResponse:
        return RegisterCallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegisterCallsWithStreamingResponse:
        return RegisterCallsWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        audio_encoding: Literal["s16le", "mulaw"],
        audio_websocket_protocol: Literal["web", "twilio"],
        sample_rate: int,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        from_number: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        to_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegisterCallCreateResponse:
        """
        Register Call To Get CallId To Establish Connection

        Args:
          agent_id: Unique id of agent used for the call. Your agent would contain the LLM Websocket
              url used for this call.

          audio_encoding:
              The audio encoding of the call. The following formats are supported:

              - `s16le` 16 bit linear PCM audio, the native format for web audio capture and
                playback.

              - `mulaw` non-linear audio encoding technique used in telephony. Commonly used
                by Twilio.

          audio_websocket_protocol: Where the audio websocket would connect from would determine the format /
              protocol of websocket messages, and would determine how our server read audio
              bytes and send audio bytes.:

              - `web`: The protocol defined by Retell, commonly used for connecting from web
                frontend. Also useful for those who want to manipulate audio bytes directly.

              - `twilio`: The
                [websocket protocol](https://www.twilio.com/docs/voice/twiml/stream#message-media)
                defined by Twilio, used when your system uses Twilio, and supplies Retell
                audio websocket url to Twilio.

          sample_rate: Sample rate of the conversation, the input and output audio bytes will all
              conform to this rate. Check the audio source, audio format, and voice used for
              the agent to select one that works. supports value ranging from [8000, 48000].
              Note for Twilio `mulaw` encoding, the sample rate has to be 8000.

              - `s16le` sample rate recommendation (natively supported, lowest latency):

                - elevenlabs voices: 16000, 22050, 24000, 44100.
                - openai voices: 24000.

                - deepgram voices: 8000, 16000, 24000, 32000, 48000.

          end_call_after_silence_ms: If users stay silent for a period, end the call. By default, it is set to
              600,000 ms (10 min). The minimum value allowed is 10,000 ms (10 s).

          from_number: The caller number. This field is storage purpose only, set this if you want the
              call object to contain it so that it's easier to reference it. Not used for
              processing, when we connect to your LLM websocket server, you can then get it
              from the call object.

          metadata: An abtriary object for storage purpose only. You can put anything here like your
              own id for the call, twilio SID, internal customer id. Not used for processing,
              when we connect to your LLM websocket server, you can then get it from the call
              object.

          to_number: The callee number. This field is storage purpose only, set this if you want the
              call object to contain it so that it's easier to reference it. Not used for
              processing, when we connect to your LLM websocket server, you can then get it
              from the call object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/register-call",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "audio_encoding": audio_encoding,
                    "audio_websocket_protocol": audio_websocket_protocol,
                    "sample_rate": sample_rate,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "from_number": from_number,
                    "metadata": metadata,
                    "to_number": to_number,
                },
                register_call_create_params.RegisterCallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisterCallCreateResponse,
        )


class AsyncRegisterCalls(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegisterCallsWithRawResponse:
        return AsyncRegisterCallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegisterCallsWithStreamingResponse:
        return AsyncRegisterCallsWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        audio_encoding: Literal["s16le", "mulaw"],
        audio_websocket_protocol: Literal["web", "twilio"],
        sample_rate: int,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        from_number: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        to_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegisterCallCreateResponse:
        """
        Register Call To Get CallId To Establish Connection

        Args:
          agent_id: Unique id of agent used for the call. Your agent would contain the LLM Websocket
              url used for this call.

          audio_encoding:
              The audio encoding of the call. The following formats are supported:

              - `s16le` 16 bit linear PCM audio, the native format for web audio capture and
                playback.

              - `mulaw` non-linear audio encoding technique used in telephony. Commonly used
                by Twilio.

          audio_websocket_protocol: Where the audio websocket would connect from would determine the format /
              protocol of websocket messages, and would determine how our server read audio
              bytes and send audio bytes.:

              - `web`: The protocol defined by Retell, commonly used for connecting from web
                frontend. Also useful for those who want to manipulate audio bytes directly.

              - `twilio`: The
                [websocket protocol](https://www.twilio.com/docs/voice/twiml/stream#message-media)
                defined by Twilio, used when your system uses Twilio, and supplies Retell
                audio websocket url to Twilio.

          sample_rate: Sample rate of the conversation, the input and output audio bytes will all
              conform to this rate. Check the audio source, audio format, and voice used for
              the agent to select one that works. supports value ranging from [8000, 48000].
              Note for Twilio `mulaw` encoding, the sample rate has to be 8000.

              - `s16le` sample rate recommendation (natively supported, lowest latency):

                - elevenlabs voices: 16000, 22050, 24000, 44100.
                - openai voices: 24000.

                - deepgram voices: 8000, 16000, 24000, 32000, 48000.

          end_call_after_silence_ms: If users stay silent for a period, end the call. By default, it is set to
              600,000 ms (10 min). The minimum value allowed is 10,000 ms (10 s).

          from_number: The caller number. This field is storage purpose only, set this if you want the
              call object to contain it so that it's easier to reference it. Not used for
              processing, when we connect to your LLM websocket server, you can then get it
              from the call object.

          metadata: An abtriary object for storage purpose only. You can put anything here like your
              own id for the call, twilio SID, internal customer id. Not used for processing,
              when we connect to your LLM websocket server, you can then get it from the call
              object.

          to_number: The callee number. This field is storage purpose only, set this if you want the
              call object to contain it so that it's easier to reference it. Not used for
              processing, when we connect to your LLM websocket server, you can then get it
              from the call object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/register-call",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "audio_encoding": audio_encoding,
                    "audio_websocket_protocol": audio_websocket_protocol,
                    "sample_rate": sample_rate,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "from_number": from_number,
                    "metadata": metadata,
                    "to_number": to_number,
                },
                register_call_create_params.RegisterCallCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisterCallCreateResponse,
        )


class RegisterCallsWithRawResponse:
    def __init__(self, register_calls: RegisterCalls) -> None:
        self._register_calls = register_calls

        self.create = to_raw_response_wrapper(
            register_calls.create,
        )


class AsyncRegisterCallsWithRawResponse:
    def __init__(self, register_calls: AsyncRegisterCalls) -> None:
        self._register_calls = register_calls

        self.create = async_to_raw_response_wrapper(
            register_calls.create,
        )


class RegisterCallsWithStreamingResponse:
    def __init__(self, register_calls: RegisterCalls) -> None:
        self._register_calls = register_calls

        self.create = to_streamed_response_wrapper(
            register_calls.create,
        )


class AsyncRegisterCallsWithStreamingResponse:
    def __init__(self, register_calls: AsyncRegisterCalls) -> None:
        self._register_calls = register_calls

        self.create = async_to_streamed_response_wrapper(
            register_calls.create,
        )
