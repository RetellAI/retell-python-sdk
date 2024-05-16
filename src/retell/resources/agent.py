# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import agent_create_params, agent_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.agent_response import AgentResponse
from ..types.agent_list_response import AgentListResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        return AgentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        llm_websocket_url: str,
        voice_id: str,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[
            Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise"]
        ]
        | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: List[str] | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
            "en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR", "fr-FR"
        ]
        | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_create_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentResponse:
        """
        Create a new agent

        Args:
          llm_websocket_url: The URL we will establish LLM websocket for getting response, usually your
              server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
              request format (sent from us) and response format (send to us).

          voice_id: Unique voice id used for the agent. Find list of available voices and their
              preview in Dashboard.

          agent_name: The name of the agent. Only used for your own reference.

          ambient_sound: If set, will add ambient environment sound to the call to make experience more
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

          backchannel_frequency: Only applicable when enable_backchannel is true. Controls how often the agent
              would backchannel when a backchannel is possible. Value ranging from [0,1].
              Lower value means less frequent backchannel, while higher value means more
              frequent backchannel. If unset, default value 0.8 will apply.

          backchannel_words: Only applicable when enable_backchannel is true. A list of words that the agent
              would use as backchannel. If not set, default backchannel words will apply.
              Check out
              [backchannel default words](/agent/interaction-configuration#backchannel) for
              more details. Note that certain voices do not work too well with certain words,
              so it's recommended to expeirment before adding any words.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`.

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging. These data can still be accessed securely via webhooks. If
              not set, default value of false will apply.

          pronunciation_dictionary: A list of words / phrases and their pronunciation to be used to guide the audio
              synthesize for consistent pronunciation. Currently only supported for English &
              11labs voices. Set to null to remove pronunciation dictionary from this agent.

          reminder_max_count: If set, controls how many times agent would remind user when user is
              unresponsive. Must be a non negative integer. If unset, default value of 1 will
              apply (remind once). Set to 0 to disable agent from reminding.

          reminder_trigger_ms: If set (in milliseconds), will trigger a reminder to the agent to speak if the
              user has been silent for the specified duration after some agent speech. Must be
              a positive number. If unset, default value of 10000 ms (10 s) will apply.

          responsiveness: Controls how responsive is the agent. Value ranging from [0,1]. Lower value
              means less responsive agent (wait more, respond slower), while higher value
              means faster exchanges (respond when it can). If unset, default value 1 will
              apply.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          webhook_url: The webhook for agent to listen to call events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-agent",
            body=maybe_transform(
                {
                    "llm_websocket_url": llm_websocket_url,
                    "voice_id": voice_id,
                    "agent_name": agent_name,
                    "ambient_sound": ambient_sound,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "responsiveness": responsiveness,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "webhook_url": webhook_url,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentResponse:
        """
        Retrieve details of a specific agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/get-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[
            Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise"]
        ]
        | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: List[str] | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
            "en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR", "fr-FR"
        ]
        | NotGiven = NOT_GIVEN,
        llm_websocket_url: str | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_update_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
        voice_id: str | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentResponse:
        """Update an existing agent

        Args:
          agent_name: The name of the agent.

        Only used for your own reference.

          ambient_sound: If set, will add ambient environment sound to the call to make experience more
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

          backchannel_frequency: Only applicable when enable_backchannel is true. Controls how often the agent
              would backchannel when a backchannel is possible. Value ranging from [0,1].
              Lower value means less frequent backchannel, while higher value means more
              frequent backchannel. If unset, default value 0.8 will apply.

          backchannel_words: Only applicable when enable_backchannel is true. A list of words that the agent
              would use as backchannel. If not set, default backchannel words will apply.
              Check out
              [backchannel default words](/agent/interaction-configuration#backchannel) for
              more details. Note that certain voices do not work too well with certain words,
              so it's recommended to expeirment before adding any words.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`.

          llm_websocket_url: The URL we will establish LLM websocket for getting response, usually your
              server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
              request format (sent from us) and response format (send to us).

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging. These data can still be accessed securely via webhooks. If
              not set, default value of false will apply.

          pronunciation_dictionary: A list of words / phrases and their pronunciation to be used to guide the audio
              synthesize for consistent pronunciation. Currently only supported for English &
              11labs voices. Set to null to remove pronunciation dictionary from this agent.

          reminder_max_count: If set, controls how many times agent would remind user when user is
              unresponsive. Must be a non negative integer. If unset, default value of 1 will
              apply (remind once). Set to 0 to disable agent from reminding.

          reminder_trigger_ms: If set (in milliseconds), will trigger a reminder to the agent to speak if the
              user has been silent for the specified duration after some agent speech. Must be
              a positive number. If unset, default value of 10000 ms (10 s) will apply.

          responsiveness: Controls how responsive is the agent. Value ranging from [0,1]. Lower value
              means less responsive agent (wait more, respond slower), while higher value
              means faster exchanges (respond when it can). If unset, default value 1 will
              apply.

          voice_id: Unique voice id used for the agent. Find list of available voices and their
              preview in Dashboard.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          webhook_url: The webhook for agent to listen to call events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/update-agent/{agent_id}",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "ambient_sound": ambient_sound,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "llm_websocket_url": llm_websocket_url,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "responsiveness": responsiveness,
                    "voice_id": voice_id,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "webhook_url": webhook_url,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """List all agents"""
        return self._get(
            "/list-agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentResourceWithRawResponse:
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        return AsyncAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        llm_websocket_url: str,
        voice_id: str,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[
            Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise"]
        ]
        | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: List[str] | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
            "en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR", "fr-FR"
        ]
        | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_create_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentResponse:
        """
        Create a new agent

        Args:
          llm_websocket_url: The URL we will establish LLM websocket for getting response, usually your
              server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
              request format (sent from us) and response format (send to us).

          voice_id: Unique voice id used for the agent. Find list of available voices and their
              preview in Dashboard.

          agent_name: The name of the agent. Only used for your own reference.

          ambient_sound: If set, will add ambient environment sound to the call to make experience more
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

          backchannel_frequency: Only applicable when enable_backchannel is true. Controls how often the agent
              would backchannel when a backchannel is possible. Value ranging from [0,1].
              Lower value means less frequent backchannel, while higher value means more
              frequent backchannel. If unset, default value 0.8 will apply.

          backchannel_words: Only applicable when enable_backchannel is true. A list of words that the agent
              would use as backchannel. If not set, default backchannel words will apply.
              Check out
              [backchannel default words](/agent/interaction-configuration#backchannel) for
              more details. Note that certain voices do not work too well with certain words,
              so it's recommended to expeirment before adding any words.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`.

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging. These data can still be accessed securely via webhooks. If
              not set, default value of false will apply.

          pronunciation_dictionary: A list of words / phrases and their pronunciation to be used to guide the audio
              synthesize for consistent pronunciation. Currently only supported for English &
              11labs voices. Set to null to remove pronunciation dictionary from this agent.

          reminder_max_count: If set, controls how many times agent would remind user when user is
              unresponsive. Must be a non negative integer. If unset, default value of 1 will
              apply (remind once). Set to 0 to disable agent from reminding.

          reminder_trigger_ms: If set (in milliseconds), will trigger a reminder to the agent to speak if the
              user has been silent for the specified duration after some agent speech. Must be
              a positive number. If unset, default value of 10000 ms (10 s) will apply.

          responsiveness: Controls how responsive is the agent. Value ranging from [0,1]. Lower value
              means less responsive agent (wait more, respond slower), while higher value
              means faster exchanges (respond when it can). If unset, default value 1 will
              apply.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          webhook_url: The webhook for agent to listen to call events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-agent",
            body=await async_maybe_transform(
                {
                    "llm_websocket_url": llm_websocket_url,
                    "voice_id": voice_id,
                    "agent_name": agent_name,
                    "ambient_sound": ambient_sound,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "responsiveness": responsiveness,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "webhook_url": webhook_url,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentResponse:
        """
        Retrieve details of a specific agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/get-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[
            Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise"]
        ]
        | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: List[str] | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
            "en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR", "fr-FR"
        ]
        | NotGiven = NOT_GIVEN,
        llm_websocket_url: str | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_update_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
        voice_id: str | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentResponse:
        """Update an existing agent

        Args:
          agent_name: The name of the agent.

        Only used for your own reference.

          ambient_sound: If set, will add ambient environment sound to the call to make experience more
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

          backchannel_frequency: Only applicable when enable_backchannel is true. Controls how often the agent
              would backchannel when a backchannel is possible. Value ranging from [0,1].
              Lower value means less frequent backchannel, while higher value means more
              frequent backchannel. If unset, default value 0.8 will apply.

          backchannel_words: Only applicable when enable_backchannel is true. A list of words that the agent
              would use as backchannel. If not set, default backchannel words will apply.
              Check out
              [backchannel default words](/agent/interaction-configuration#backchannel) for
              more details. Note that certain voices do not work too well with certain words,
              so it's recommended to expeirment before adding any words.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`.

          llm_websocket_url: The URL we will establish LLM websocket for getting response, usually your
              server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
              request format (sent from us) and response format (send to us).

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging. These data can still be accessed securely via webhooks. If
              not set, default value of false will apply.

          pronunciation_dictionary: A list of words / phrases and their pronunciation to be used to guide the audio
              synthesize for consistent pronunciation. Currently only supported for English &
              11labs voices. Set to null to remove pronunciation dictionary from this agent.

          reminder_max_count: If set, controls how many times agent would remind user when user is
              unresponsive. Must be a non negative integer. If unset, default value of 1 will
              apply (remind once). Set to 0 to disable agent from reminding.

          reminder_trigger_ms: If set (in milliseconds), will trigger a reminder to the agent to speak if the
              user has been silent for the specified duration after some agent speech. Must be
              a positive number. If unset, default value of 10000 ms (10 s) will apply.

          responsiveness: Controls how responsive is the agent. Value ranging from [0,1]. Lower value
              means less responsive agent (wait more, respond slower), while higher value
              means faster exchanges (respond when it can). If unset, default value 1 will
              apply.

          voice_id: Unique voice id used for the agent. Find list of available voices and their
              preview in Dashboard.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          webhook_url: The webhook for agent to listen to call events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/update-agent/{agent_id}",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "ambient_sound": ambient_sound,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "llm_websocket_url": llm_websocket_url,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "responsiveness": responsiveness,
                    "voice_id": voice_id,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "webhook_url": webhook_url,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentListResponse:
        """List all agents"""
        return await self._get(
            "/list-agents",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AgentResourceWithRawResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_raw_response_wrapper(
            agent.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agent.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agent.update,
        )
        self.list = to_raw_response_wrapper(
            agent.list,
        )
        self.delete = to_raw_response_wrapper(
            agent.delete,
        )


class AsyncAgentResourceWithRawResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_raw_response_wrapper(
            agent.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agent.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agent.update,
        )
        self.list = async_to_raw_response_wrapper(
            agent.list,
        )
        self.delete = async_to_raw_response_wrapper(
            agent.delete,
        )


class AgentResourceWithStreamingResponse:
    def __init__(self, agent: AgentResource) -> None:
        self._agent = agent

        self.create = to_streamed_response_wrapper(
            agent.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agent.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agent.update,
        )
        self.list = to_streamed_response_wrapper(
            agent.list,
        )
        self.delete = to_streamed_response_wrapper(
            agent.delete,
        )


class AsyncAgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncAgentResource) -> None:
        self._agent = agent

        self.create = async_to_streamed_response_wrapper(
            agent.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agent.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agent.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agent.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent.delete,
        )
