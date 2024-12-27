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
from .._base_client import make_request_options
from ..types.agent_response import AgentResponse
from ..types.agent_list_response import AgentListResponse

__all__ = ["AgentResource", "AsyncAgentResource"]


class AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AgentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        response_engine: agent_create_params.ResponseEngine,
        voice_id: str,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[
            Literal[
                "coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        ambient_sound_volume: float | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: Optional[List[str]] | NotGiven = NOT_GIVEN,
        begin_message_delay_ms: int | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        enable_transcription_formatting: bool | NotGiven = NOT_GIVEN,
        enable_voicemail_detection: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        fallback_voice_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
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
        | NotGiven = NOT_GIVEN,
        max_call_duration_ms: int | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        post_call_analysis_data: Optional[Iterable[agent_create_params.PostCallAnalysisData]] | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_create_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        voicemail_detection_timeout_ms: int | NotGiven = NOT_GIVEN,
        voicemail_message: str | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
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
          response_engine: The response engine to use for the agent.

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

              - `call-center`: Call center work noise.
                [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/call-center.wav)

              Set to `null` to remove ambient sound from this agent.

          ambient_sound_volume: If set, will control the volume of the ambient sound. Value ranging from [0,2].
              Lower value means quieter ambient sound, while higher value means louder ambient
              sound. If unset, default value 1 will apply.

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

          begin_message_delay_ms: If set, will delay the first message by the specified amount of milliseconds, so
              that it gives user more time to prepare to take the call. Valid range is [0,
              5000]. If not set or set to 0, agent will speak immediately. Only applicable
              when agent speaks first.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          enable_transcription_formatting: If set to true, will format transcription to number, date, email, etc. If set to
              false, will return transcripts in raw words. If not set, default value of true
              will apply.

          enable_voicemail_detection: If set to true, will detect whether the call enters a voicemail. Note that this
              feature is only available for phone calls.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          fallback_voice_ids: When TTS provider for the selected voice is experiencing outages, we would use
              fallback voices listed here for the agent. Voice id and the fallback voice ids
              must be from different TTS providers. The system would go through the list in
              order, if the first one in the list is also having outage, it would use the next
              one. Set to null to remove voice fallback for the agent.

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`. Select `multi` for
              multilingual support, currently this supports Spanish and English.

          max_call_duration_ms: Maximum allowed length for the call, will force end the call if reached. The
              minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
              7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging, inbound/outbound phone numbers, etc. These data can still be
              accessed securely via webhooks. If not set, default value of false will apply.

          post_call_analysis_data: Post call analysis data to extract from the call. This data will augment the
              pre-defined variables extracted in the call analysis. This will be available
              after the call ends.

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

          voice_model: Optionally set the voice model used for the selected voice. Currently only
              elevenlab voices have voice model selections. Set to null to remove voice model
              selection, and default ones will apply. Check out the dashboard for details on
              each voice model.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          voicemail_detection_timeout_ms: Configures when to stop running voicemail detection, as it becomes unlikely to
              hit voicemail after a couple minutes, and keep running it will only have
              negative impact. The minimum value allowed is 5,000 ms (5 s), and maximum value
              allowed is 180,000 (3 minutes). By default, this is set to 30,000 (30 s).

          voicemail_message: The message to be played when the call enters a voicemail. Note that this
              feature is only available for phone calls. If you want to hangup after hitting
              voicemail, set this to empty string.

          volume: If set, will control the volume of the agent. Value ranging from [0,2]. Lower
              value means quieter agent speech, while higher value means louder agent speech.
              If unset, default value 1 will apply.

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
                    "response_engine": response_engine,
                    "voice_id": voice_id,
                    "agent_name": agent_name,
                    "ambient_sound": ambient_sound,
                    "ambient_sound_volume": ambient_sound_volume,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "begin_message_delay_ms": begin_message_delay_ms,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "enable_transcription_formatting": enable_transcription_formatting,
                    "enable_voicemail_detection": enable_voicemail_detection,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "fallback_voice_ids": fallback_voice_ids,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "max_call_duration_ms": max_call_duration_ms,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "post_call_analysis_data": post_call_analysis_data,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "responsiveness": responsiveness,
                    "voice_model": voice_model,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "voicemail_detection_timeout_ms": voicemail_detection_timeout_ms,
                    "voicemail_message": voicemail_message,
                    "volume": volume,
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
            Literal[
                "coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        ambient_sound_volume: float | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: Optional[List[str]] | NotGiven = NOT_GIVEN,
        begin_message_delay_ms: int | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        enable_transcription_formatting: bool | NotGiven = NOT_GIVEN,
        enable_voicemail_detection: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        fallback_voice_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
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
        | NotGiven = NOT_GIVEN,
        max_call_duration_ms: int | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        post_call_analysis_data: Optional[Iterable[agent_update_params.PostCallAnalysisData]] | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_update_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        response_engine: agent_update_params.ResponseEngine | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
        voice_id: str | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        voicemail_detection_timeout_ms: int | NotGiven = NOT_GIVEN,
        voicemail_message: str | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
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

              - `call-center`: Call center work noise.
                [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/call-center.wav)

              Set to `null` to remove ambient sound from this agent.

          ambient_sound_volume: If set, will control the volume of the ambient sound. Value ranging from [0,2].
              Lower value means quieter ambient sound, while higher value means louder ambient
              sound. If unset, default value 1 will apply.

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

          begin_message_delay_ms: If set, will delay the first message by the specified amount of milliseconds, so
              that it gives user more time to prepare to take the call. Valid range is [0,
              5000]. If not set or set to 0, agent will speak immediately. Only applicable
              when agent speaks first.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          enable_transcription_formatting: If set to true, will format transcription to number, date, email, etc. If set to
              false, will return transcripts in raw words. If not set, default value of true
              will apply.

          enable_voicemail_detection: If set to true, will detect whether the call enters a voicemail. Note that this
              feature is only available for phone calls.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          fallback_voice_ids: When TTS provider for the selected voice is experiencing outages, we would use
              fallback voices listed here for the agent. Voice id and the fallback voice ids
              must be from different TTS providers. The system would go through the list in
              order, if the first one in the list is also having outage, it would use the next
              one. Set to null to remove voice fallback for the agent.

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`. Select `multi` for
              multilingual support, currently this supports Spanish and English.

          max_call_duration_ms: Maximum allowed length for the call, will force end the call if reached. The
              minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
              7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging, inbound/outbound phone numbers, etc. These data can still be
              accessed securely via webhooks. If not set, default value of false will apply.

          post_call_analysis_data: Post call analysis data to extract from the call. This data will augment the
              pre-defined variables extracted in the call analysis. This will be available
              after the call ends.

          pronunciation_dictionary: A list of words / phrases and their pronunciation to be used to guide the audio
              synthesize for consistent pronunciation. Currently only supported for English &
              11labs voices. Set to null to remove pronunciation dictionary from this agent.

          reminder_max_count: If set, controls how many times agent would remind user when user is
              unresponsive. Must be a non negative integer. If unset, default value of 1 will
              apply (remind once). Set to 0 to disable agent from reminding.

          reminder_trigger_ms: If set (in milliseconds), will trigger a reminder to the agent to speak if the
              user has been silent for the specified duration after some agent speech. Must be
              a positive number. If unset, default value of 10000 ms (10 s) will apply.

          response_engine: The response engine to use for the agent.

          responsiveness: Controls how responsive is the agent. Value ranging from [0,1]. Lower value
              means less responsive agent (wait more, respond slower), while higher value
              means faster exchanges (respond when it can). If unset, default value 1 will
              apply.

          voice_id: Unique voice id used for the agent. Find list of available voices and their
              preview in Dashboard.

          voice_model: Optionally set the voice model used for the selected voice. Currently only
              elevenlab voices have voice model selections. Set to null to remove voice model
              selection, and default ones will apply. Check out the dashboard for details on
              each voice model.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          voicemail_detection_timeout_ms: Configures when to stop running voicemail detection, as it becomes unlikely to
              hit voicemail after a couple minutes, and keep running it will only have
              negative impact. The minimum value allowed is 5,000 ms (5 s), and maximum value
              allowed is 180,000 (3 minutes). By default, this is set to 30,000 (30 s).

          voicemail_message: The message to be played when the call enters a voicemail. Note that this
              feature is only available for phone calls. If you want to hangup after hitting
              voicemail, set this to empty string.

          volume: If set, will control the volume of the agent. Value ranging from [0,2]. Lower
              value means quieter agent speech, while higher value means louder agent speech.
              If unset, default value 1 will apply.

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
                    "ambient_sound_volume": ambient_sound_volume,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "begin_message_delay_ms": begin_message_delay_ms,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "enable_transcription_formatting": enable_transcription_formatting,
                    "enable_voicemail_detection": enable_voicemail_detection,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "fallback_voice_ids": fallback_voice_ids,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "max_call_duration_ms": max_call_duration_ms,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "post_call_analysis_data": post_call_analysis_data,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "response_engine": response_engine,
                    "responsiveness": responsiveness,
                    "voice_id": voice_id,
                    "voice_model": voice_model,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "voicemail_detection_timeout_ms": voicemail_detection_timeout_ms,
                    "voicemail_message": voicemail_message,
                    "volume": volume,
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
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        response_engine: agent_create_params.ResponseEngine,
        voice_id: str,
        agent_name: Optional[str] | NotGiven = NOT_GIVEN,
        ambient_sound: Optional[
            Literal[
                "coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        ambient_sound_volume: float | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: Optional[List[str]] | NotGiven = NOT_GIVEN,
        begin_message_delay_ms: int | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        enable_transcription_formatting: bool | NotGiven = NOT_GIVEN,
        enable_voicemail_detection: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        fallback_voice_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
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
        | NotGiven = NOT_GIVEN,
        max_call_duration_ms: int | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        post_call_analysis_data: Optional[Iterable[agent_create_params.PostCallAnalysisData]] | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_create_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        voicemail_detection_timeout_ms: int | NotGiven = NOT_GIVEN,
        voicemail_message: str | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
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
          response_engine: The response engine to use for the agent.

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

              - `call-center`: Call center work noise.
                [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/call-center.wav)

              Set to `null` to remove ambient sound from this agent.

          ambient_sound_volume: If set, will control the volume of the ambient sound. Value ranging from [0,2].
              Lower value means quieter ambient sound, while higher value means louder ambient
              sound. If unset, default value 1 will apply.

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

          begin_message_delay_ms: If set, will delay the first message by the specified amount of milliseconds, so
              that it gives user more time to prepare to take the call. Valid range is [0,
              5000]. If not set or set to 0, agent will speak immediately. Only applicable
              when agent speaks first.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          enable_transcription_formatting: If set to true, will format transcription to number, date, email, etc. If set to
              false, will return transcripts in raw words. If not set, default value of true
              will apply.

          enable_voicemail_detection: If set to true, will detect whether the call enters a voicemail. Note that this
              feature is only available for phone calls.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          fallback_voice_ids: When TTS provider for the selected voice is experiencing outages, we would use
              fallback voices listed here for the agent. Voice id and the fallback voice ids
              must be from different TTS providers. The system would go through the list in
              order, if the first one in the list is also having outage, it would use the next
              one. Set to null to remove voice fallback for the agent.

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`. Select `multi` for
              multilingual support, currently this supports Spanish and English.

          max_call_duration_ms: Maximum allowed length for the call, will force end the call if reached. The
              minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
              7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging, inbound/outbound phone numbers, etc. These data can still be
              accessed securely via webhooks. If not set, default value of false will apply.

          post_call_analysis_data: Post call analysis data to extract from the call. This data will augment the
              pre-defined variables extracted in the call analysis. This will be available
              after the call ends.

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

          voice_model: Optionally set the voice model used for the selected voice. Currently only
              elevenlab voices have voice model selections. Set to null to remove voice model
              selection, and default ones will apply. Check out the dashboard for details on
              each voice model.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          voicemail_detection_timeout_ms: Configures when to stop running voicemail detection, as it becomes unlikely to
              hit voicemail after a couple minutes, and keep running it will only have
              negative impact. The minimum value allowed is 5,000 ms (5 s), and maximum value
              allowed is 180,000 (3 minutes). By default, this is set to 30,000 (30 s).

          voicemail_message: The message to be played when the call enters a voicemail. Note that this
              feature is only available for phone calls. If you want to hangup after hitting
              voicemail, set this to empty string.

          volume: If set, will control the volume of the agent. Value ranging from [0,2]. Lower
              value means quieter agent speech, while higher value means louder agent speech.
              If unset, default value 1 will apply.

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
                    "response_engine": response_engine,
                    "voice_id": voice_id,
                    "agent_name": agent_name,
                    "ambient_sound": ambient_sound,
                    "ambient_sound_volume": ambient_sound_volume,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "begin_message_delay_ms": begin_message_delay_ms,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "enable_transcription_formatting": enable_transcription_formatting,
                    "enable_voicemail_detection": enable_voicemail_detection,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "fallback_voice_ids": fallback_voice_ids,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "max_call_duration_ms": max_call_duration_ms,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "post_call_analysis_data": post_call_analysis_data,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "responsiveness": responsiveness,
                    "voice_model": voice_model,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "voicemail_detection_timeout_ms": voicemail_detection_timeout_ms,
                    "voicemail_message": voicemail_message,
                    "volume": volume,
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
            Literal[
                "coffee-shop", "convention-hall", "summer-outdoor", "mountain-outdoor", "static-noise", "call-center"
            ]
        ]
        | NotGiven = NOT_GIVEN,
        ambient_sound_volume: float | NotGiven = NOT_GIVEN,
        backchannel_frequency: float | NotGiven = NOT_GIVEN,
        backchannel_words: Optional[List[str]] | NotGiven = NOT_GIVEN,
        begin_message_delay_ms: int | NotGiven = NOT_GIVEN,
        boosted_keywords: Optional[List[str]] | NotGiven = NOT_GIVEN,
        enable_backchannel: bool | NotGiven = NOT_GIVEN,
        enable_transcription_formatting: bool | NotGiven = NOT_GIVEN,
        enable_voicemail_detection: bool | NotGiven = NOT_GIVEN,
        end_call_after_silence_ms: int | NotGiven = NOT_GIVEN,
        fallback_voice_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        interruption_sensitivity: float | NotGiven = NOT_GIVEN,
        language: Literal[
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
        | NotGiven = NOT_GIVEN,
        max_call_duration_ms: int | NotGiven = NOT_GIVEN,
        normalize_for_speech: bool | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        post_call_analysis_data: Optional[Iterable[agent_update_params.PostCallAnalysisData]] | NotGiven = NOT_GIVEN,
        pronunciation_dictionary: Optional[Iterable[agent_update_params.PronunciationDictionary]]
        | NotGiven = NOT_GIVEN,
        reminder_max_count: int | NotGiven = NOT_GIVEN,
        reminder_trigger_ms: float | NotGiven = NOT_GIVEN,
        response_engine: agent_update_params.ResponseEngine | NotGiven = NOT_GIVEN,
        responsiveness: float | NotGiven = NOT_GIVEN,
        voice_id: str | NotGiven = NOT_GIVEN,
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
        ]
        | NotGiven = NOT_GIVEN,
        voice_speed: float | NotGiven = NOT_GIVEN,
        voice_temperature: float | NotGiven = NOT_GIVEN,
        voicemail_detection_timeout_ms: int | NotGiven = NOT_GIVEN,
        voicemail_message: str | NotGiven = NOT_GIVEN,
        volume: float | NotGiven = NOT_GIVEN,
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

              - `call-center`: Call center work noise.
                [Listen to Ambience](https://retell-utils-public.s3.us-west-2.amazonaws.com/call-center.wav)

              Set to `null` to remove ambient sound from this agent.

          ambient_sound_volume: If set, will control the volume of the ambient sound. Value ranging from [0,2].
              Lower value means quieter ambient sound, while higher value means louder ambient
              sound. If unset, default value 1 will apply.

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

          begin_message_delay_ms: If set, will delay the first message by the specified amount of milliseconds, so
              that it gives user more time to prepare to take the call. Valid range is [0,
              5000]. If not set or set to 0, agent will speak immediately. Only applicable
              when agent speaks first.

          boosted_keywords: Provide a customized list of keywords to bias the transcriber model, so that
              these words are more likely to get transcribed. Commonly used for names, brands,
              street, etc.

          enable_backchannel: Controls whether the agent would backchannel (agent interjects the speaker with
              phrases like "yeah", "uh-huh" to signify interest and engagement). Backchannel
              when enabled tends to show up more in longer user utterances. If not set, agent
              will not backchannel.

          enable_transcription_formatting: If set to true, will format transcription to number, date, email, etc. If set to
              false, will return transcripts in raw words. If not set, default value of true
              will apply.

          enable_voicemail_detection: If set to true, will detect whether the call enters a voicemail. Note that this
              feature is only available for phone calls.

          end_call_after_silence_ms: If users stay silent for a period after agent speech, end the call. The minimum
              value allowed is 10,000 ms (10 s). By default, this is set to 600000 (10 min).

          fallback_voice_ids: When TTS provider for the selected voice is experiencing outages, we would use
              fallback voices listed here for the agent. Voice id and the fallback voice ids
              must be from different TTS providers. The system would go through the list in
              order, if the first one in the list is also having outage, it would use the next
              one. Set to null to remove voice fallback for the agent.

          interruption_sensitivity: Controls how sensitive the agent is to user interruptions. Value ranging from
              [0,1]. Lower value means it will take longer / more words for user to interrupt
              agent, while higher value means it's easier for user to interrupt agent. If
              unset, default value 1 will apply. When this is set to 0, agent would never be
              interrupted.

          language: Specifies what language (and dialect) the speech recognition will operate in.
              For instance, selecting `en-GB` optimizes speech recognition for British
              English. If unset, will use default value `en-US`. Select `multi` for
              multilingual support, currently this supports Spanish and English.

          max_call_duration_ms: Maximum allowed length for the call, will force end the call if reached. The
              minimum value allowed is 60,000 ms (1 min), and maximum value allowed is
              7,200,000 (2 hours). By default, this is set to 3,600,000 (1 hour).

          normalize_for_speech: If set to true, will normalize the some part of text (number, currency, date,
              etc) to spoken to its spoken form for more consistent speech synthesis
              (sometimes the voice synthesize system itself might read these wrong with the
              raw text). For example, it will convert "Call my number 2137112342 on Jul 5th,
              2024 for the $24.12 payment" to "Call my number two one three seven one one two
              three four two on july fifth, twenty twenty four for the twenty four dollars
              twelve cents payment" before starting audio generation.

          opt_out_sensitive_data_storage: Whether this agent opts out of sensitive data storage like transcript,
              recording, logging, inbound/outbound phone numbers, etc. These data can still be
              accessed securely via webhooks. If not set, default value of false will apply.

          post_call_analysis_data: Post call analysis data to extract from the call. This data will augment the
              pre-defined variables extracted in the call analysis. This will be available
              after the call ends.

          pronunciation_dictionary: A list of words / phrases and their pronunciation to be used to guide the audio
              synthesize for consistent pronunciation. Currently only supported for English &
              11labs voices. Set to null to remove pronunciation dictionary from this agent.

          reminder_max_count: If set, controls how many times agent would remind user when user is
              unresponsive. Must be a non negative integer. If unset, default value of 1 will
              apply (remind once). Set to 0 to disable agent from reminding.

          reminder_trigger_ms: If set (in milliseconds), will trigger a reminder to the agent to speak if the
              user has been silent for the specified duration after some agent speech. Must be
              a positive number. If unset, default value of 10000 ms (10 s) will apply.

          response_engine: The response engine to use for the agent.

          responsiveness: Controls how responsive is the agent. Value ranging from [0,1]. Lower value
              means less responsive agent (wait more, respond slower), while higher value
              means faster exchanges (respond when it can). If unset, default value 1 will
              apply.

          voice_id: Unique voice id used for the agent. Find list of available voices and their
              preview in Dashboard.

          voice_model: Optionally set the voice model used for the selected voice. Currently only
              elevenlab voices have voice model selections. Set to null to remove voice model
              selection, and default ones will apply. Check out the dashboard for details on
              each voice model.

          voice_speed: Controls speed of voice. Value ranging from [0.5,2]. Lower value means slower
              speech, while higher value means faster speech rate. If unset, default value 1
              will apply.

          voice_temperature: Controls how stable the voice is. Value ranging from [0,2]. Lower value means
              more stable, and higher value means more variant speech generation. Currently
              this setting only applies to `11labs` voices. If unset, default value 1 will
              apply.

          voicemail_detection_timeout_ms: Configures when to stop running voicemail detection, as it becomes unlikely to
              hit voicemail after a couple minutes, and keep running it will only have
              negative impact. The minimum value allowed is 5,000 ms (5 s), and maximum value
              allowed is 180,000 (3 minutes). By default, this is set to 30,000 (30 s).

          voicemail_message: The message to be played when the call enters a voicemail. Note that this
              feature is only available for phone calls. If you want to hangup after hitting
              voicemail, set this to empty string.

          volume: If set, will control the volume of the agent. Value ranging from [0,2]. Lower
              value means quieter agent speech, while higher value means louder agent speech.
              If unset, default value 1 will apply.

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
                    "ambient_sound_volume": ambient_sound_volume,
                    "backchannel_frequency": backchannel_frequency,
                    "backchannel_words": backchannel_words,
                    "begin_message_delay_ms": begin_message_delay_ms,
                    "boosted_keywords": boosted_keywords,
                    "enable_backchannel": enable_backchannel,
                    "enable_transcription_formatting": enable_transcription_formatting,
                    "enable_voicemail_detection": enable_voicemail_detection,
                    "end_call_after_silence_ms": end_call_after_silence_ms,
                    "fallback_voice_ids": fallback_voice_ids,
                    "interruption_sensitivity": interruption_sensitivity,
                    "language": language,
                    "max_call_duration_ms": max_call_duration_ms,
                    "normalize_for_speech": normalize_for_speech,
                    "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    "post_call_analysis_data": post_call_analysis_data,
                    "pronunciation_dictionary": pronunciation_dictionary,
                    "reminder_max_count": reminder_max_count,
                    "reminder_trigger_ms": reminder_trigger_ms,
                    "response_engine": response_engine,
                    "responsiveness": responsiveness,
                    "voice_id": voice_id,
                    "voice_model": voice_model,
                    "voice_speed": voice_speed,
                    "voice_temperature": voice_temperature,
                    "voicemail_detection_timeout_ms": voicemail_detection_timeout_ms,
                    "voicemail_message": voicemail_message,
                    "volume": volume,
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
