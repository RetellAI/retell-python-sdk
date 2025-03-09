# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import llm_create_params, llm_update_params
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
        begin_message: Optional[str] | NotGiven = NOT_GIVEN,
        general_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        general_tools: Optional[Iterable[llm_create_params.GeneralTool]] | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        model: Optional[Literal["gpt-4o", "gpt-4o-mini", "claude-3.7-sonnet", "claude-3.5-haiku"]]
        | NotGiven = NOT_GIVEN,
        model_high_priority: bool | NotGiven = NOT_GIVEN,
        model_temperature: float | NotGiven = NOT_GIVEN,
        s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime"]] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_create_params.State]] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """Create a new Retell LLM Response Engine that can be attached to an agent.

        This
        is used to generate response output for the agent.

        Args:
          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.

              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool (last option) for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions

              - Tools of LLM (no state) = general tools

          knowledge_base_ids: A list of knowledge base ids to use for this resource. Set to null to remove all
              knowledge bases.

          model: Select the underlying text LLM. If not set, would default to gpt-4o.

          model_high_priority: If set to true, will use high priority pool with more dedicated resource to
              ensure lower and more consistent latency, default to false. This feature usually
              comes with a higher cost.

          model_temperature: If set, will control the randomness of the response. Value ranging from [0,1].
              Lower value means more deterministic, while higher value means more random. If
              unset, default value 0 will apply. Note that for tool calling, a lower value is
              recommended.

          s2s_model: Select the underlying speech to speech model. Can only set this or model, not
              both.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          tool_call_strict_mode: Only applicable when model is gpt-4o or gpt-4o mini. If set to true, will use
              structured output to make sure tool call arguments follow the json schema. The
              time to save a new tool or change to a tool will be longer as additional
              processing is needed. Default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-retell-llm",
            body=maybe_transform(
                {
                    "begin_message": begin_message,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "knowledge_base_ids": knowledge_base_ids,
                    "model": model,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "s2s_model": s2s_model,
                    "starting_state": starting_state,
                    "states": states,
                    "tool_call_strict_mode": tool_call_strict_mode,
                },
                llm_create_params.LlmCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmResponse,
        )

    def retrieve(
        self,
        llm_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Retrieve details of a specific Retell LLM Response Engine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return self._get(
            f"/get-retell-llm/{llm_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmResponse,
        )

    def update(
        self,
        llm_id: str,
        *,
        begin_message: Optional[str] | NotGiven = NOT_GIVEN,
        general_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        general_tools: Optional[Iterable[llm_update_params.GeneralTool]] | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        model: Optional[Literal["gpt-4o", "gpt-4o-mini", "claude-3.7-sonnet", "claude-3.5-haiku"]]
        | NotGiven = NOT_GIVEN,
        model_high_priority: bool | NotGiven = NOT_GIVEN,
        model_temperature: float | NotGiven = NOT_GIVEN,
        s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime"]] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_update_params.State]] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Update an existing Retell LLM Response Engine

        Args:
          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.

              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool (last option) for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions

              - Tools of LLM (no state) = general tools

          knowledge_base_ids: A list of knowledge base ids to use for this resource. Set to null to remove all
              knowledge bases.

          model: Select the underlying text LLM. If not set, would default to gpt-4o.

          model_high_priority: If set to true, will use high priority pool with more dedicated resource to
              ensure lower and more consistent latency, default to false. This feature usually
              comes with a higher cost.

          model_temperature: If set, will control the randomness of the response. Value ranging from [0,1].
              Lower value means more deterministic, while higher value means more random. If
              unset, default value 0 will apply. Note that for tool calling, a lower value is
              recommended.

          s2s_model: Select the underlying speech to speech model. Can only set this or model, not
              both.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          tool_call_strict_mode: Only applicable when model is gpt-4o or gpt-4o mini. If set to true, will use
              structured output to make sure tool call arguments follow the json schema. The
              time to save a new tool or change to a tool will be longer as additional
              processing is needed. Default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return self._patch(
            f"/update-retell-llm/{llm_id}",
            body=maybe_transform(
                {
                    "begin_message": begin_message,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "knowledge_base_ids": knowledge_base_ids,
                    "model": model,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "s2s_model": s2s_model,
                    "starting_state": starting_state,
                    "states": states,
                    "tool_call_strict_mode": tool_call_strict_mode,
                },
                llm_update_params.LlmUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmResponse,
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
    ) -> LlmListResponse:
        """List all Retell LLM Response Engines that can be attached to an agent."""
        return self._get(
            "/list-retell-llms",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmListResponse,
        )

    def delete(
        self,
        llm_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing Retell LLM Response Engine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-retell-llm/{llm_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        begin_message: Optional[str] | NotGiven = NOT_GIVEN,
        general_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        general_tools: Optional[Iterable[llm_create_params.GeneralTool]] | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        model: Optional[Literal["gpt-4o", "gpt-4o-mini", "claude-3.7-sonnet", "claude-3.5-haiku"]]
        | NotGiven = NOT_GIVEN,
        model_high_priority: bool | NotGiven = NOT_GIVEN,
        model_temperature: float | NotGiven = NOT_GIVEN,
        s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime"]] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_create_params.State]] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """Create a new Retell LLM Response Engine that can be attached to an agent.

        This
        is used to generate response output for the agent.

        Args:
          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.

              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool (last option) for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions

              - Tools of LLM (no state) = general tools

          knowledge_base_ids: A list of knowledge base ids to use for this resource. Set to null to remove all
              knowledge bases.

          model: Select the underlying text LLM. If not set, would default to gpt-4o.

          model_high_priority: If set to true, will use high priority pool with more dedicated resource to
              ensure lower and more consistent latency, default to false. This feature usually
              comes with a higher cost.

          model_temperature: If set, will control the randomness of the response. Value ranging from [0,1].
              Lower value means more deterministic, while higher value means more random. If
              unset, default value 0 will apply. Note that for tool calling, a lower value is
              recommended.

          s2s_model: Select the underlying speech to speech model. Can only set this or model, not
              both.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          tool_call_strict_mode: Only applicable when model is gpt-4o or gpt-4o mini. If set to true, will use
              structured output to make sure tool call arguments follow the json schema. The
              time to save a new tool or change to a tool will be longer as additional
              processing is needed. Default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-retell-llm",
            body=await async_maybe_transform(
                {
                    "begin_message": begin_message,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "knowledge_base_ids": knowledge_base_ids,
                    "model": model,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "s2s_model": s2s_model,
                    "starting_state": starting_state,
                    "states": states,
                    "tool_call_strict_mode": tool_call_strict_mode,
                },
                llm_create_params.LlmCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmResponse,
        )

    async def retrieve(
        self,
        llm_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Retrieve details of a specific Retell LLM Response Engine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return await self._get(
            f"/get-retell-llm/{llm_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmResponse,
        )

    async def update(
        self,
        llm_id: str,
        *,
        begin_message: Optional[str] | NotGiven = NOT_GIVEN,
        general_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        general_tools: Optional[Iterable[llm_update_params.GeneralTool]] | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        model: Optional[Literal["gpt-4o", "gpt-4o-mini", "claude-3.7-sonnet", "claude-3.5-haiku"]]
        | NotGiven = NOT_GIVEN,
        model_high_priority: bool | NotGiven = NOT_GIVEN,
        model_temperature: float | NotGiven = NOT_GIVEN,
        s2s_model: Optional[Literal["gpt-4o-realtime", "gpt-4o-mini-realtime"]] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_update_params.State]] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Update an existing Retell LLM Response Engine

        Args:
          begin_message: First utterance said by the agent in the call. If not set, LLM will dynamically
              generate a message. If set to "", agent will wait for user to speak first.

          general_prompt: General prompt appended to system prompt no matter what state the agent is in.

              - System prompt (with state) = general prompt + state prompt.

              - System prompt (no state) = general prompt.

          general_tools: A list of tools the model may call (to get external knowledge, call API, etc).
              You can select from some common predefined tools like end call, transfer call,
              etc; or you can create your own custom tool (last option) for the LLM to use.

              - Tools of LLM (with state) = general tools + state tools + state transitions

              - Tools of LLM (no state) = general tools

          knowledge_base_ids: A list of knowledge base ids to use for this resource. Set to null to remove all
              knowledge bases.

          model: Select the underlying text LLM. If not set, would default to gpt-4o.

          model_high_priority: If set to true, will use high priority pool with more dedicated resource to
              ensure lower and more consistent latency, default to false. This feature usually
              comes with a higher cost.

          model_temperature: If set, will control the randomness of the response. Value ranging from [0,1].
              Lower value means more deterministic, while higher value means more random. If
              unset, default value 0 will apply. Note that for tool calling, a lower value is
              recommended.

          s2s_model: Select the underlying speech to speech model. Can only set this or model, not
              both.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

          tool_call_strict_mode: Only applicable when model is gpt-4o or gpt-4o mini. If set to true, will use
              structured output to make sure tool call arguments follow the json schema. The
              time to save a new tool or change to a tool will be longer as additional
              processing is needed. Default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        return await self._patch(
            f"/update-retell-llm/{llm_id}",
            body=await async_maybe_transform(
                {
                    "begin_message": begin_message,
                    "general_prompt": general_prompt,
                    "general_tools": general_tools,
                    "knowledge_base_ids": knowledge_base_ids,
                    "model": model,
                    "model_high_priority": model_high_priority,
                    "model_temperature": model_temperature,
                    "s2s_model": s2s_model,
                    "starting_state": starting_state,
                    "states": states,
                    "tool_call_strict_mode": tool_call_strict_mode,
                },
                llm_update_params.LlmUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmResponse,
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
    ) -> LlmListResponse:
        """List all Retell LLM Response Engines that can be attached to an agent."""
        return await self._get(
            "/list-retell-llms",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LlmListResponse,
        )

    async def delete(
        self,
        llm_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing Retell LLM Response Engine

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not llm_id:
            raise ValueError(f"Expected a non-empty value for `llm_id` but received {llm_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-retell-llm/{llm_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
