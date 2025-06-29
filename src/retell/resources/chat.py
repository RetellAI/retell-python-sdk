# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import chat_create_params, chat_create_chat_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_response import ChatResponse
from ..types.chat_list_response import ChatListResponse
from ..types.chat_create_chat_completion_response import ChatCreateChatCompletionResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        agent_version: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatResponse:
        """
        Create a chat session

        Args:
          agent_id: The chat agent to use for the call.

          agent_version: The version of the chat agent to use for the chat. If not provided, will default
              to latest version.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the chat. Not used for processing. You
              can later get this field from the chat object.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-chat",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_version": agent_version,
                    "metadata": metadata,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatResponse:
        """
        Retrieve details of a specific chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._get(
            f"/get-chat/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
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
    ) -> ChatListResponse:
        """List all chats"""
        return self._get(
            "/list-chat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListResponse,
        )

    def create_chat_completion(
        self,
        *,
        chat_id: str,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateChatCompletionResponse:
        """
        Create a chat completion message

        Args:
          chat_id: Unique id of the chat to create completion.

          content: user message to generate agent chat completion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-chat-completion",
            body=maybe_transform(
                {
                    "chat_id": chat_id,
                    "content": content,
                },
                chat_create_chat_completion_params.ChatCreateChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateChatCompletionResponse,
        )

    def end(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        End an ongoing chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/end-chat/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        agent_version: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatResponse:
        """
        Create a chat session

        Args:
          agent_id: The chat agent to use for the call.

          agent_version: The version of the chat agent to use for the chat. If not provided, will default
              to latest version.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the chat. Not used for processing. You
              can later get this field from the chat object.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-chat",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_version": agent_version,
                    "metadata": metadata,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                chat_create_params.ChatCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
        )

    async def retrieve(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatResponse:
        """
        Retrieve details of a specific chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._get(
            f"/get-chat/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
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
    ) -> ChatListResponse:
        """List all chats"""
        return await self._get(
            "/list-chat",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatListResponse,
        )

    async def create_chat_completion(
        self,
        *,
        chat_id: str,
        content: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCreateChatCompletionResponse:
        """
        Create a chat completion message

        Args:
          chat_id: Unique id of the chat to create completion.

          content: user message to generate agent chat completion.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-chat-completion",
            body=await async_maybe_transform(
                {
                    "chat_id": chat_id,
                    "content": content,
                },
                chat_create_chat_completion_params.ChatCreateChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCreateChatCompletionResponse,
        )

    async def end(
        self,
        chat_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        End an ongoing chat

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/end-chat/{chat_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_raw_response_wrapper(
            chat.create,
        )
        self.retrieve = to_raw_response_wrapper(
            chat.retrieve,
        )
        self.list = to_raw_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = to_raw_response_wrapper(
            chat.create_chat_completion,
        )
        self.end = to_raw_response_wrapper(
            chat.end,
        )


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_raw_response_wrapper(
            chat.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            chat.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = async_to_raw_response_wrapper(
            chat.create_chat_completion,
        )
        self.end = async_to_raw_response_wrapper(
            chat.end,
        )


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_streamed_response_wrapper(
            chat.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            chat.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = to_streamed_response_wrapper(
            chat.create_chat_completion,
        )
        self.end = to_streamed_response_wrapper(
            chat.end,
        )


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_streamed_response_wrapper(
            chat.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            chat.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = async_to_streamed_response_wrapper(
            chat.create_chat_completion,
        )
        self.end = async_to_streamed_response_wrapper(
            chat.end,
        )
