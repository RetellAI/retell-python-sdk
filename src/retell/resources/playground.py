# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import playground_completion_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import is_given, path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._constants import DEFAULT_TIMEOUT
from .._base_client import make_request_options
from ..types.playground_completion_response import PlaygroundCompletionResponse

__all__ = ["PlaygroundResource", "AsyncPlaygroundResource"]


class PlaygroundResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlaygroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PlaygroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlaygroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return PlaygroundResourceWithStreamingResponse(self)

    def completion(
        self,
        agent_id: str,
        *,
        messages: Iterable[playground_completion_params.Message],
        version: int | Omit = omit,
        component_id: str | Omit = omit,
        current_node_id: str | Omit = omit,
        current_state: str | Omit = omit,
        dynamic_variables: Dict[str, str] | Omit = omit,
        tool_mocks: Iterable[playground_completion_params.ToolMock] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaygroundCompletionResponse:
        """Stateless playground completion.

        Send the full conversation history (same shape
        as chat completion messages) and receive only the newly generated messages.
        Nothing is persisted server-side — the caller manages conversation state.

        Args:
          messages: Full conversation history, same shape as chat completion messages. message_id
              and created_timestamp are optional — server generates them if omitted.

          version: Agent version to use. Defaults to latest.

          component_id: Conversation flow component id. Required when current_node_id refers to a node
              within a component.

          current_node_id: Current node id for conversation-flow agents. Used to resume from a specific
              node. Must be provided together with component_id when testing components.

          current_state: Current state name for retell-llm agents. Used to resume from a specific state.

          dynamic_variables: Key-value pairs for dynamic variable substitution.

          tool_mocks: Optional mock responses for tools. When provided, the agent uses these instead
              of executing real tool calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        return self._post(
            path_template("/agent-playground-completion/{agent_id}", agent_id=agent_id),
            body=maybe_transform(
                {
                    "messages": messages,
                    "component_id": component_id,
                    "current_node_id": current_node_id,
                    "current_state": current_state,
                    "dynamic_variables": dynamic_variables,
                    "tool_mocks": tool_mocks,
                },
                playground_completion_params.PlaygroundCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, playground_completion_params.PlaygroundCompletionParams),
            ),
            cast_to=PlaygroundCompletionResponse,
        )


class AsyncPlaygroundResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlaygroundResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPlaygroundResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlaygroundResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncPlaygroundResourceWithStreamingResponse(self)

    async def completion(
        self,
        agent_id: str,
        *,
        messages: Iterable[playground_completion_params.Message],
        version: int | Omit = omit,
        component_id: str | Omit = omit,
        current_node_id: str | Omit = omit,
        current_state: str | Omit = omit,
        dynamic_variables: Dict[str, str] | Omit = omit,
        tool_mocks: Iterable[playground_completion_params.ToolMock] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlaygroundCompletionResponse:
        """Stateless playground completion.

        Send the full conversation history (same shape
        as chat completion messages) and receive only the newly generated messages.
        Nothing is persisted server-side — the caller manages conversation state.

        Args:
          messages: Full conversation history, same shape as chat completion messages. message_id
              and created_timestamp are optional — server generates them if omitted.

          version: Agent version to use. Defaults to latest.

          component_id: Conversation flow component id. Required when current_node_id refers to a node
              within a component.

          current_node_id: Current node id for conversation-flow agents. Used to resume from a specific
              node. Must be provided together with component_id when testing components.

          current_state: Current state name for retell-llm agents. Used to resume from a specific state.

          dynamic_variables: Key-value pairs for dynamic variable substitution.

          tool_mocks: Optional mock responses for tools. When provided, the agent uses these instead
              of executing real tool calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        return await self._post(
            path_template("/agent-playground-completion/{agent_id}", agent_id=agent_id),
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "component_id": component_id,
                    "current_node_id": current_node_id,
                    "current_state": current_state,
                    "dynamic_variables": dynamic_variables,
                    "tool_mocks": tool_mocks,
                },
                playground_completion_params.PlaygroundCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, playground_completion_params.PlaygroundCompletionParams
                ),
            ),
            cast_to=PlaygroundCompletionResponse,
        )


class PlaygroundResourceWithRawResponse:
    def __init__(self, playground: PlaygroundResource) -> None:
        self._playground = playground

        self.completion = to_raw_response_wrapper(
            playground.completion,
        )


class AsyncPlaygroundResourceWithRawResponse:
    def __init__(self, playground: AsyncPlaygroundResource) -> None:
        self._playground = playground

        self.completion = async_to_raw_response_wrapper(
            playground.completion,
        )


class PlaygroundResourceWithStreamingResponse:
    def __init__(self, playground: PlaygroundResource) -> None:
        self._playground = playground

        self.completion = to_streamed_response_wrapper(
            playground.completion,
        )


class AsyncPlaygroundResourceWithStreamingResponse:
    def __init__(self, playground: AsyncPlaygroundResource) -> None:
        self._playground = playground

        self.completion = async_to_streamed_response_wrapper(
            playground.completion,
        )
