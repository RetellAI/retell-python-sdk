# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import AgentResponse, AgentListResponse, agent_create_params, agent_update_params
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

__all__ = ["Agent", "AsyncAgent"]


class Agent(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentWithRawResponse:
        return AgentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentWithStreamingResponse:
        return AgentWithStreamingResponse(self)

    def create(
        self,
        *,
        llm_websocket_url: str,
        voice_id: str,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor"]]
        | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        language: Literal["en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR"]
        | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
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

              Set to `null` to remove ambient sound from this agent.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          language: `Beta feature, use with caution.`

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

          opt_out_sensitive_data_storage: Disable transcripts and recordings storage for enhanced privacy. Access
              transcripts securely via webhooks. If not set, default value of false will
              apply.

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
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "language": language,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
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
        ambient_sound: Optional[Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor"]]
        | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        language: Literal["en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR"]
        | NotGiven = NOT_GIVEN,
        llm_websocket_url: str | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
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

              Set to `null` to remove ambient sound from this agent.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          language: `Beta feature, use with caution.`

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

          llm_websocket_url: The URL we will establish LLM websocket for getting response, usually your
              server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
              request format (sent from us) and response format (send to us).

          opt_out_sensitive_data_storage: Disable transcripts and recordings storage for enhanced privacy. Access
              transcripts securely via webhooks. If not set, default value of false will
              apply.

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
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "language": language,
                    "llm_websocket_url": llm_websocket_url,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
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


class AsyncAgent(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentWithRawResponse:
        return AsyncAgentWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentWithStreamingResponse:
        return AsyncAgentWithStreamingResponse(self)

    async def create(
        self,
        *,
        llm_websocket_url: str,
        voice_id: str,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor"]]
        | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        language: Literal["en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR"]
        | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
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

              Set to `null` to remove ambient sound from this agent.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          language: `Beta feature, use with caution.`

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

          opt_out_sensitive_data_storage: Disable transcripts and recordings storage for enhanced privacy. Access
              transcripts securely via webhooks. If not set, default value of false will
              apply.

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
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "language": language,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
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
        ambient_sound: Optional[Literal["coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor"]]
        | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        language: Literal["en-US", "en-IN", "en-GB", "de-DE", "es-ES", "es-419", "hi-IN", "ja-JP", "pt-PT", "pt-BR"]
        | NotGiven = NOT_GIVEN,
        llm_websocket_url: str | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
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

              Set to `null` to remove ambient sound from this agent.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          language: `Beta feature, use with caution.`

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

          llm_websocket_url: The URL we will establish LLM websocket for getting response, usually your
              server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
              request format (sent from us) and response format (send to us).

          opt_out_sensitive_data_storage: Disable transcripts and recordings storage for enhanced privacy. Access
              transcripts securely via webhooks. If not set, default value of false will
              apply.

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
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "language": language,
                    "llm_websocket_url": llm_websocket_url,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
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


class AgentWithRawResponse:
    def __init__(self, agent: Agent) -> None:
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


class AsyncAgentWithRawResponse:
    def __init__(self, agent: AsyncAgent) -> None:
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


class AgentWithStreamingResponse:
    def __init__(self, agent: Agent) -> None:
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


class AsyncAgentWithStreamingResponse:
    def __init__(self, agent: AsyncAgent) -> None:
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
