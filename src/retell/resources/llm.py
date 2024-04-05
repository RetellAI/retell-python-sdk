# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import LlmResponse, LlmListResponse, llm_create_params, llm_update_params
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

__all__ = ["Llm", "AsyncLlm"]


class Llm(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LlmWithRawResponse:
        return LlmWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LlmWithStreamingResponse:
        return LlmWithStreamingResponse(self)

    def create(
        self,
        *,
        begin_message: Optional[str] | NotGiven = NOT_GIVEN,
        general_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        general_tools: Optional[Iterable[llm_create_params.GeneralTool]] | NotGiven = NOT_GIVEN,
        inbound_dynamic_variables_webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_create_params.State]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Create a new Retell LLM

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

          inbound_dynamic_variables_webhook_url: For inbound phone calls with Retell numbers, if this webhook is set, will POST
              to it to retrieve dynamic variables to use for the call. Without this, there's
              no way to pass dynamic variables to inbound calls of Retell numbers.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

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
                    "inbound_dynamic_variables_webhook_url": inbound_dynamic_variables_webhook_url,
                    "starting_state": starting_state,
                    "states": states,
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
        Retrieve details of a specific Retell LLM

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
        inbound_dynamic_variables_webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_update_params.State]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Update an existing Retell LLM

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

          inbound_dynamic_variables_webhook_url: For inbound phone calls with Retell numbers, if this webhook is set, will POST
              to it to retrieve dynamic variables to use for the call. Without this, there's
              no way to pass dynamic variables to inbound calls of Retell numbers.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

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
                    "inbound_dynamic_variables_webhook_url": inbound_dynamic_variables_webhook_url,
                    "starting_state": starting_state,
                    "states": states,
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
        """List all retell LLM"""
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
        Delete an existing Retell LLM

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


class AsyncLlm(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLlmWithRawResponse:
        return AsyncLlmWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLlmWithStreamingResponse:
        return AsyncLlmWithStreamingResponse(self)

    async def create(
        self,
        *,
        begin_message: Optional[str] | NotGiven = NOT_GIVEN,
        general_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        general_tools: Optional[Iterable[llm_create_params.GeneralTool]] | NotGiven = NOT_GIVEN,
        inbound_dynamic_variables_webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_create_params.State]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Create a new Retell LLM

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

          inbound_dynamic_variables_webhook_url: For inbound phone calls with Retell numbers, if this webhook is set, will POST
              to it to retrieve dynamic variables to use for the call. Without this, there's
              no way to pass dynamic variables to inbound calls of Retell numbers.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

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
                    "inbound_dynamic_variables_webhook_url": inbound_dynamic_variables_webhook_url,
                    "starting_state": starting_state,
                    "states": states,
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
        Retrieve details of a specific Retell LLM

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
        inbound_dynamic_variables_webhook_url: Optional[str] | NotGiven = NOT_GIVEN,
        starting_state: Optional[str] | NotGiven = NOT_GIVEN,
        states: Optional[Iterable[llm_update_params.State]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LlmResponse:
        """
        Update an existing Retell LLM

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

          inbound_dynamic_variables_webhook_url: For inbound phone calls with Retell numbers, if this webhook is set, will POST
              to it to retrieve dynamic variables to use for the call. Without this, there's
              no way to pass dynamic variables to inbound calls of Retell numbers.

          starting_state: Name of the starting state. Required if states is not empty.

          states: States of the LLM. This is to help reduce prompt length and tool choices when
              the call can be broken into distinct states. With shorter prompts and less
              tools, the LLM can better focus and follow the rules, minimizing hallucination.
              If this field is not set, the agent would only have general prompt and general
              tools (essentially one state).

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
                    "inbound_dynamic_variables_webhook_url": inbound_dynamic_variables_webhook_url,
                    "starting_state": starting_state,
                    "states": states,
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
        """List all retell LLM"""
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
        Delete an existing Retell LLM

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


class LlmWithRawResponse:
    def __init__(self, llm: Llm) -> None:
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


class AsyncLlmWithRawResponse:
    def __init__(self, llm: AsyncLlm) -> None:
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


class LlmWithStreamingResponse:
    def __init__(self, llm: Llm) -> None:
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


class AsyncLlmWithStreamingResponse:
    def __init__(self, llm: AsyncLlm) -> None:
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
