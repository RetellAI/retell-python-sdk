# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import llm_list_params, llm_create_params, llm_delete_params, llm_update_params, llm_retrieve_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.llm_response import LlmResponse
from ..types.llm_list_response import LlmListResponse

__all__ = ["LlmResource", "AsyncLlmResource"]


class LlmResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return LlmResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        backup_model: llm_create_params.BackupModel | Omit = omit,
        begin_after_user_silence_ms: Optional[int] | Omit = omit,
        begin_message: Optional[str] | Omit = omit,
        default_dynamic_variables: Optional[Dict[str, str]] | Omit = omit,
        general_prompt: Optional[str] | Omit = omit,
        general_tools: Optional[Iterable[llm_create_params.GeneralTool]] | Omit = omit,
        is_transfer_llm: Optional[bool] | Omit = omit,
        kb_config: Optional[llm_create_params.KBConfig] | Omit = omit,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        mcps: Optional[Iterable[llm_create_params.Mcp]] | Omit = omit,
        model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-5",
                "gpt-5-mini",
                "gpt-5-nano",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5.4",
                "gpt-5.4-mini",
                "gpt-5.4-nano",
                "gpt-5.5",
                "gpt-5.6-terra",
                "gpt-5.6-luna",
                "gpt-6-astra",
                "gpt-6-sol",
                "gpt-6.1-sol",
                "gpt-6.1-terra",
                "gpt-6-luna",
                "claude-4.6-sonnet",
                "claude-5-opus",
                "claude-5.5-opus",
                "claude-5-sonnet",
                "claude-5.5-sonnet",
                "claude-5.5-haiku",
                "claude-4.5-haiku",
                "gemini-3.0-flash",
                "gemini-3.1-flash-lite",
                "gemini-3.5-flash",
                "gemini-3.5-flash-lite",
                "gemini-3.6-flash",
                "gemini-3.7-flash",
                "gemini-3.8-flash",
                "gemini-4-argon",
            ]
        ]
        | Omit = omit,
        model_config: llm_create_params.ModelConfig | Omit = omit,
        model_high_priority: Optional[bool] | Omit = omit,
        model_temperature: float | Omit = omit,
        model_ultrafast: Optional[bool] | Omit = omit,
        s2s_model: Optional[
            Literal[
                "gpt-realtime-2.1",
                "gpt-realtime-2.1-mini",
                "gpt-realtime-2",
                "gpt-realtime-1.5",
                "gpt-realtime",
                "gpt-realtime-mini",
                "grok-voice-3.0",
            ]
        ]
        | Omit = omit,
        start_speaker: Literal["user", "agent"] | Omit = omit,
        starting_state: Optional[str] | Omit = omit,
        states: Optional[Iterable[llm_create_params.State]] | Omit = omit,
        voice_prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmResponse:
        """Create a new Retell LLM Response Engine that can be attached to an agent.

        This
        is used to generate response output for the agent.

        Args:
          backup_model: Backup models are supported only for call agents. Response engines with a backup
              model cannot be used by chat agents.

          begin_after_user_silence_ms: If set, the AI will begin the conversation after waiting for the user for the
              duration (in milliseconds) specified by this attribute. This only applies if the
              agent is configured to wait for the user to speak first. If not set, the agent
              will wait indefinitely for the user to speak.

          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          default_dynamic_variables: Default dynamic variables represented as key-value pairs of strings. These are
              injected into your Retell LLM prompt and tool description when specific values
              are not provided in a request. Only applicable for Retell LLM.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.
              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions
              - Tools of LLM (no state) = general tools

          is_transfer_llm: Whether this Retell LLM is used for warm transfer. Can only be set at creation,
              and is ignored on update.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: A list of knowledge base ids to use for this resource.

          mcps: A list of MCPs to use for this LLM.

          model: Available LLM models for agents.

          model_config: Model settings for the response engine. type decides which models primary and
              backup accept. On update, each top-level key replaces the current one and
              omitted keys are kept; set backup to null to remove it. Changing type requires
              primary and clears backup, while temperature carries over. In agent_override,
              type is required whenever primary is set; setting backup to null disables it for
              that call only.

          model_high_priority: Deprecated, use model_config.primary.tier fast. Ignored when model_config is
              set.

          model_temperature: Deprecated, use model_config.temperature. Ignored when model_config is set.

          model_ultrafast: Deprecated, use model_config.primary.tier ultrafast. Ignored when model_config
              is set.

          s2s_model: The speech-to-speech model to use

          start_speaker: The speaker who starts the conversation. Required. Must be either 'user' or
              'agent'.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          voice_prompt: Prompt for the voice model when model_config.type is duplex, at most 15,000
              tokens. Required for duplex, where general_prompt is the backend's prompt. Kept
              when you switch models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-retell-llm",
            body=maybe_transform(
                {
                    "backup_model": backup_model,
                    "begin_after_user_silence_ms": begin_after_user_silence_ms,
                    "begin_message": begin_message,
                    "default_dynamic_variables": default_dynamic_variables,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "is_transfer_llm": is_transfer_llm,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model": model,
                    "model_config": model_config,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "model_ultrafast": model_ultrafast,
                    "s2s_model": s2s_model,
                    "start_speaker": start_speaker,
                    "starting_state": starting_state,
                    "states": states,
                    "voice_prompt": voice_prompt,
                },
                llm_create_params.LlmCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            ),
            cast_to=LlmResponse,
        )

    def retrieve(
        self,
        llm_id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmResponse:
        """
        Retrieve details of a specific Retell LLM Response Engine

        Args:
          version: Optional version of the API to use for this request. Default to latest version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return self._get(
            path_template("/get-retell-llm/{llm_id}", llm_id=llm_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=maybe_transform({"version": version}, llm_retrieve_params.LlmRetrieveParams),
            ),
            cast_to=LlmResponse,
        )

    def update(
        self,
        llm_id: str,
        *,
        version: int | Omit = omit,
        backup_model: llm_update_params.BackupModel | Omit = omit,
        begin_after_user_silence_ms: Optional[int] | Omit = omit,
        begin_message: Optional[str] | Omit = omit,
        default_dynamic_variables: Optional[Dict[str, str]] | Omit = omit,
        general_prompt: Optional[str] | Omit = omit,
        general_tools: Optional[Iterable[llm_update_params.GeneralTool]] | Omit = omit,
        is_transfer_llm: Optional[bool] | Omit = omit,
        kb_config: Optional[llm_update_params.KBConfig] | Omit = omit,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        mcps: Optional[Iterable[llm_update_params.Mcp]] | Omit = omit,
        model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-5",
                "gpt-5-mini",
                "gpt-5-nano",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5.4",
                "gpt-5.4-mini",
                "gpt-5.4-nano",
                "gpt-5.5",
                "gpt-5.6-terra",
                "gpt-5.6-luna",
                "gpt-6-astra",
                "gpt-6-sol",
                "gpt-6.1-sol",
                "gpt-6.1-terra",
                "gpt-6-luna",
                "claude-4.6-sonnet",
                "claude-5-opus",
                "claude-5.5-opus",
                "claude-5-sonnet",
                "claude-5.5-sonnet",
                "claude-5.5-haiku",
                "claude-4.5-haiku",
                "gemini-3.0-flash",
                "gemini-3.1-flash-lite",
                "gemini-3.5-flash",
                "gemini-3.5-flash-lite",
                "gemini-3.6-flash",
                "gemini-3.7-flash",
                "gemini-3.8-flash",
                "gemini-4-argon",
            ]
        ]
        | Omit = omit,
        model_config: llm_update_params.ModelConfig | Omit = omit,
        model_high_priority: Optional[bool] | Omit = omit,
        model_temperature: float | Omit = omit,
        model_ultrafast: Optional[bool] | Omit = omit,
        s2s_model: Optional[
            Literal[
                "gpt-realtime-2.1",
                "gpt-realtime-2.1-mini",
                "gpt-realtime-2",
                "gpt-realtime-1.5",
                "gpt-realtime",
                "gpt-realtime-mini",
                "grok-voice-3.0",
            ]
        ]
        | Omit = omit,
        start_speaker: Literal["user", "agent"] | Omit = omit,
        starting_state: Optional[str] | Omit = omit,
        states: Optional[Iterable[llm_update_params.State]] | Omit = omit,
        voice_prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmResponse:
        """
        Update an existing Retell LLM Response Engine

        Args:
          version: Optional version of the API to use for this request. Default to latest version.

          backup_model: Backup models are supported only for call agents. Response engines with a backup
              model cannot be used by chat agents.

          begin_after_user_silence_ms: If set, the AI will begin the conversation after waiting for the user for the
              duration (in milliseconds) specified by this attribute. This only applies if the
              agent is configured to wait for the user to speak first. If not set, the agent
              will wait indefinitely for the user to speak.

          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          default_dynamic_variables: Default dynamic variables represented as key-value pairs of strings. These are
              injected into your Retell LLM prompt and tool description when specific values
              are not provided in a request. Only applicable for Retell LLM.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.
              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions
              - Tools of LLM (no state) = general tools

          is_transfer_llm: Whether this Retell LLM is used for warm transfer. Can only be set at creation,
              and is ignored on update.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: A list of knowledge base ids to use for this resource.

          mcps: A list of MCPs to use for this LLM.

          model: Available LLM models for agents.

          model_config: Model settings for the response engine. type decides which models primary and
              backup accept. On update, each top-level key replaces the current one and
              omitted keys are kept; set backup to null to remove it. Changing type requires
              primary and clears backup, while temperature carries over. In agent_override,
              type is required whenever primary is set; setting backup to null disables it for
              that call only.

          model_high_priority: Deprecated, use model_config.primary.tier fast. Ignored when model_config is
              set.

          model_temperature: Deprecated, use model_config.temperature. Ignored when model_config is set.

          model_ultrafast: Deprecated, use model_config.primary.tier ultrafast. Ignored when model_config
              is set.

          s2s_model: The speech-to-speech model to use

          start_speaker: The speaker who starts the conversation. Required. Must be either 'user' or
              'agent'.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          voice_prompt: Prompt for the voice model when model_config.type is duplex, at most 15,000
              tokens. Required for duplex, where general_prompt is the backend's prompt. Kept
              when you switch models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return self._patch(
            path_template("/update-retell-llm/{llm_id}", llm_id=llm_id),
            body=maybe_transform(
                {
                    "backup_model": backup_model,
                    "begin_after_user_silence_ms": begin_after_user_silence_ms,
                    "begin_message": begin_message,
                    "default_dynamic_variables": default_dynamic_variables,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "is_transfer_llm": is_transfer_llm,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model": model,
                    "model_config": model_config,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "model_ultrafast": model_ultrafast,
                    "s2s_model": s2s_model,
                    "start_speaker": start_speaker,
                    "starting_state": starting_state,
                    "states": states,
                    "voice_prompt": voice_prompt,
                },
                llm_update_params.LlmUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=maybe_transform({"version": version}, llm_update_params.LlmUpdateParams),
            ),
            cast_to=LlmResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        sort_order: Literal["ascending", "descending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmListResponse:
        """
        List Retell LLM Response Engines with pagination

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          sort_order: Sort order for results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/list-retell-llms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    llm_list_params.LlmListParams,
                ),
            ),
            cast_to=LlmListResponse,
        )

    def delete(
        self,
        llm_id: str,
        *,
        force_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing Retell LLM Response Engine

        Args:
          force_delete: By default the deletion is rejected with a 400 if any agent still uses this
              Retell LLM as its response engine. Set to true to delete it anyway, which leaves
              those agents pointing at a Retell LLM that no longer exists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/delete-retell-llm/{llm_id}", llm_id=llm_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=maybe_transform({"force_delete": force_delete}, llm_delete_params.LlmDeleteParams),
            ),
            cast_to=NoneType,
        )


class AsyncLlmResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLlmResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncLlmResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        backup_model: llm_create_params.BackupModel | Omit = omit,
        begin_after_user_silence_ms: Optional[int] | Omit = omit,
        begin_message: Optional[str] | Omit = omit,
        default_dynamic_variables: Optional[Dict[str, str]] | Omit = omit,
        general_prompt: Optional[str] | Omit = omit,
        general_tools: Optional[Iterable[llm_create_params.GeneralTool]] | Omit = omit,
        is_transfer_llm: Optional[bool] | Omit = omit,
        kb_config: Optional[llm_create_params.KBConfig] | Omit = omit,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        mcps: Optional[Iterable[llm_create_params.Mcp]] | Omit = omit,
        model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-5",
                "gpt-5-mini",
                "gpt-5-nano",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5.4",
                "gpt-5.4-mini",
                "gpt-5.4-nano",
                "gpt-5.5",
                "gpt-5.6-terra",
                "gpt-5.6-luna",
                "gpt-6-astra",
                "gpt-6-sol",
                "gpt-6.1-sol",
                "gpt-6.1-terra",
                "gpt-6-luna",
                "claude-4.6-sonnet",
                "claude-5-opus",
                "claude-5.5-opus",
                "claude-5-sonnet",
                "claude-5.5-sonnet",
                "claude-5.5-haiku",
                "claude-4.5-haiku",
                "gemini-3.0-flash",
                "gemini-3.1-flash-lite",
                "gemini-3.5-flash",
                "gemini-3.5-flash-lite",
                "gemini-3.6-flash",
                "gemini-3.7-flash",
                "gemini-3.8-flash",
                "gemini-4-argon",
            ]
        ]
        | Omit = omit,
        model_config: llm_create_params.ModelConfig | Omit = omit,
        model_high_priority: Optional[bool] | Omit = omit,
        model_temperature: float | Omit = omit,
        model_ultrafast: Optional[bool] | Omit = omit,
        s2s_model: Optional[
            Literal[
                "gpt-realtime-2.1",
                "gpt-realtime-2.1-mini",
                "gpt-realtime-2",
                "gpt-realtime-1.5",
                "gpt-realtime",
                "gpt-realtime-mini",
                "grok-voice-3.0",
            ]
        ]
        | Omit = omit,
        start_speaker: Literal["user", "agent"] | Omit = omit,
        starting_state: Optional[str] | Omit = omit,
        states: Optional[Iterable[llm_create_params.State]] | Omit = omit,
        voice_prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmResponse:
        """Create a new Retell LLM Response Engine that can be attached to an agent.

        This
        is used to generate response output for the agent.

        Args:
          backup_model: Backup models are supported only for call agents. Response engines with a backup
              model cannot be used by chat agents.

          begin_after_user_silence_ms: If set, the AI will begin the conversation after waiting for the user for the
              duration (in milliseconds) specified by this attribute. This only applies if the
              agent is configured to wait for the user to speak first. If not set, the agent
              will wait indefinitely for the user to speak.

          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          default_dynamic_variables: Default dynamic variables represented as key-value pairs of strings. These are
              injected into your Retell LLM prompt and tool description when specific values
              are not provided in a request. Only applicable for Retell LLM.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.
              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions
              - Tools of LLM (no state) = general tools

          is_transfer_llm: Whether this Retell LLM is used for warm transfer. Can only be set at creation,
              and is ignored on update.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: A list of knowledge base ids to use for this resource.

          mcps: A list of MCPs to use for this LLM.

          model: Available LLM models for agents.

          model_config: Model settings for the response engine. type decides which models primary and
              backup accept. On update, each top-level key replaces the current one and
              omitted keys are kept; set backup to null to remove it. Changing type requires
              primary and clears backup, while temperature carries over. In agent_override,
              type is required whenever primary is set; setting backup to null disables it for
              that call only.

          model_high_priority: Deprecated, use model_config.primary.tier fast. Ignored when model_config is
              set.

          model_temperature: Deprecated, use model_config.temperature. Ignored when model_config is set.

          model_ultrafast: Deprecated, use model_config.primary.tier ultrafast. Ignored when model_config
              is set.

          s2s_model: The speech-to-speech model to use

          start_speaker: The speaker who starts the conversation. Required. Must be either 'user' or
              'agent'.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          voice_prompt: Prompt for the voice model when model_config.type is duplex, at most 15,000
              tokens. Required for duplex, where general_prompt is the backend's prompt. Kept
              when you switch models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-retell-llm",
            body=await async_maybe_transform(
                {
                    "backup_model": backup_model,
                    "begin_after_user_silence_ms": begin_after_user_silence_ms,
                    "begin_message": begin_message,
                    "default_dynamic_variables": default_dynamic_variables,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "is_transfer_llm": is_transfer_llm,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model": model,
                    "model_config": model_config,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "model_ultrafast": model_ultrafast,
                    "s2s_model": s2s_model,
                    "start_speaker": start_speaker,
                    "starting_state": starting_state,
                    "states": states,
                    "voice_prompt": voice_prompt,
                },
                llm_create_params.LlmCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
            ),
            cast_to=LlmResponse,
        )

    async def retrieve(
        self,
        llm_id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmResponse:
        """
        Retrieve details of a specific Retell LLM Response Engine

        Args:
          version: Optional version of the API to use for this request. Default to latest version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return await self._get(
            path_template("/get-retell-llm/{llm_id}", llm_id=llm_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=await async_maybe_transform({"version": version}, llm_retrieve_params.LlmRetrieveParams),
            ),
            cast_to=LlmResponse,
        )

    async def update(
        self,
        llm_id: str,
        *,
        version: int | Omit = omit,
        backup_model: llm_update_params.BackupModel | Omit = omit,
        begin_after_user_silence_ms: Optional[int] | Omit = omit,
        begin_message: Optional[str] | Omit = omit,
        default_dynamic_variables: Optional[Dict[str, str]] | Omit = omit,
        general_prompt: Optional[str] | Omit = omit,
        general_tools: Optional[Iterable[llm_update_params.GeneralTool]] | Omit = omit,
        is_transfer_llm: Optional[bool] | Omit = omit,
        kb_config: Optional[llm_update_params.KBConfig] | Omit = omit,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        mcps: Optional[Iterable[llm_update_params.Mcp]] | Omit = omit,
        model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-5",
                "gpt-5-mini",
                "gpt-5-nano",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5.4",
                "gpt-5.4-mini",
                "gpt-5.4-nano",
                "gpt-5.5",
                "gpt-5.6-terra",
                "gpt-5.6-luna",
                "gpt-6-astra",
                "gpt-6-sol",
                "gpt-6.1-sol",
                "gpt-6.1-terra",
                "gpt-6-luna",
                "claude-4.6-sonnet",
                "claude-5-opus",
                "claude-5.5-opus",
                "claude-5-sonnet",
                "claude-5.5-sonnet",
                "claude-5.5-haiku",
                "claude-4.5-haiku",
                "gemini-3.0-flash",
                "gemini-3.1-flash-lite",
                "gemini-3.5-flash",
                "gemini-3.5-flash-lite",
                "gemini-3.6-flash",
                "gemini-3.7-flash",
                "gemini-3.8-flash",
                "gemini-4-argon",
            ]
        ]
        | Omit = omit,
        model_config: llm_update_params.ModelConfig | Omit = omit,
        model_high_priority: Optional[bool] | Omit = omit,
        model_temperature: float | Omit = omit,
        model_ultrafast: Optional[bool] | Omit = omit,
        s2s_model: Optional[
            Literal[
                "gpt-realtime-2.1",
                "gpt-realtime-2.1-mini",
                "gpt-realtime-2",
                "gpt-realtime-1.5",
                "gpt-realtime",
                "gpt-realtime-mini",
                "grok-voice-3.0",
            ]
        ]
        | Omit = omit,
        start_speaker: Literal["user", "agent"] | Omit = omit,
        starting_state: Optional[str] | Omit = omit,
        states: Optional[Iterable[llm_update_params.State]] | Omit = omit,
        voice_prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmResponse:
        """
        Update an existing Retell LLM Response Engine

        Args:
          version: Optional version of the API to use for this request. Default to latest version.

          backup_model: Backup models are supported only for call agents. Response engines with a backup
              model cannot be used by chat agents.

          begin_after_user_silence_ms: If set, the AI will begin the conversation after waiting for the user for the
              duration (in milliseconds) specified by this attribute. This only applies if the
              agent is configured to wait for the user to speak first. If not set, the agent
              will wait indefinitely for the user to speak.

          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          default_dynamic_variables: Default dynamic variables represented as key-value pairs of strings. These are
              injected into your Retell LLM prompt and tool description when specific values
              are not provided in a request. Only applicable for Retell LLM.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.
              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions
              - Tools of LLM (no state) = general tools

          is_transfer_llm: Whether this Retell LLM is used for warm transfer. Can only be set at creation,
              and is ignored on update.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: A list of knowledge base ids to use for this resource.

          mcps: A list of MCPs to use for this LLM.

          model: Available LLM models for agents.

          model_config: Model settings for the response engine. type decides which models primary and
              backup accept. On update, each top-level key replaces the current one and
              omitted keys are kept; set backup to null to remove it. Changing type requires
              primary and clears backup, while temperature carries over. In agent_override,
              type is required whenever primary is set; setting backup to null disables it for
              that call only.

          model_high_priority: Deprecated, use model_config.primary.tier fast. Ignored when model_config is
              set.

          model_temperature: Deprecated, use model_config.temperature. Ignored when model_config is set.

          model_ultrafast: Deprecated, use model_config.primary.tier ultrafast. Ignored when model_config
              is set.

          s2s_model: The speech-to-speech model to use

          start_speaker: The speaker who starts the conversation. Required. Must be either 'user' or
              'agent'.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          voice_prompt: Prompt for the voice model when model_config.type is duplex, at most 15,000
              tokens. Required for duplex, where general_prompt is the backend's prompt. Kept
              when you switch models.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return await self._patch(
            path_template("/update-retell-llm/{llm_id}", llm_id=llm_id),
            body=await async_maybe_transform(
                {
                    "backup_model": backup_model,
                    "begin_after_user_silence_ms": begin_after_user_silence_ms,
                    "begin_message": begin_message,
                    "default_dynamic_variables": default_dynamic_variables,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "is_transfer_llm": is_transfer_llm,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model": model,
                    "model_config": model_config,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "model_ultrafast": model_ultrafast,
                    "s2s_model": s2s_model,
                    "start_speaker": start_speaker,
                    "starting_state": starting_state,
                    "states": states,
                    "voice_prompt": voice_prompt,
                },
                llm_update_params.LlmUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=await async_maybe_transform({"version": version}, llm_update_params.LlmUpdateParams),
            ),
            cast_to=LlmResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        sort_order: Literal["ascending", "descending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> LlmListResponse:
        """
        List Retell LLM Response Engines with pagination

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          sort_order: Sort order for results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/list-retell-llms",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    llm_list_params.LlmListParams,
                ),
            ),
            cast_to=LlmListResponse,
        )

    async def delete(
        self,
        llm_id: str,
        *,
        force_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
        max_retries: int | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing Retell LLM Response Engine

        Args:
          force_delete: By default the deletion is rejected with a 400 if any agent still uses this
              Retell LLM as its response engine. Set to true to delete it anyway, which leaves
              those agents pointing at a Retell LLM that no longer exists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/delete-retell-llm/{llm_id}", llm_id=llm_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                max_retries=max_retries,
                query=await async_maybe_transform({"force_delete": force_delete}, llm_delete_params.LlmDeleteParams),
            ),
            cast_to=NoneType,
        )


class LlmResourceWithRawResponse:
    def __init__(self, llm: LlmResource) -> None:
        self._llm = llm

        self.create = to_raw_response_wrapper(
            llm.create,
        )
        self.retrieve = to_raw_response_wrapper(
            llm.retrieve,
        )
        self.update = to_raw_response_wrapper(
            llm.update,
        )
        self.list = to_raw_response_wrapper(
            llm.list,
        )
        self.delete = to_raw_response_wrapper(
            llm.delete,
        )


class AsyncLlmResourceWithRawResponse:
    def __init__(self, llm: AsyncLlmResource) -> None:
        self._llm = llm

        self.create = async_to_raw_response_wrapper(
            llm.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            llm.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            llm.update,
        )
        self.list = async_to_raw_response_wrapper(
            llm.list,
        )
        self.delete = async_to_raw_response_wrapper(
            llm.delete,
        )


class LlmResourceWithStreamingResponse:
    def __init__(self, llm: LlmResource) -> None:
        self._llm = llm

        self.create = to_streamed_response_wrapper(
            llm.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            llm.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            llm.update,
        )
        self.list = to_streamed_response_wrapper(
            llm.list,
        )
        self.delete = to_streamed_response_wrapper(
            llm.delete,
        )


class AsyncLlmResourceWithStreamingResponse:
    def __init__(self, llm: AsyncLlmResource) -> None:
        self._llm = llm

        self.create = async_to_streamed_response_wrapper(
            llm.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            llm.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            llm.update,
        )
        self.list = async_to_streamed_response_wrapper(
            llm.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            llm.delete,
        )
