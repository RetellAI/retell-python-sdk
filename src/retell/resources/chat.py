# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    chat_list_params,
    chat_create_params,
    chat_update_params,
    chat_create_sms_chat_params,
    chat_create_chat_completion_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import is_given, maybe_transform, async_maybe_transform
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
        agent_version: int | Omit = omit,
        metadata: object | Omit = omit,
        retell_llm_dynamic_variables: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def update(
        self,
        chat_id: str,
        *,
        custom_attributes: Dict[str, Union[str, float, bool]] | Omit = omit,
        data_storage_setting: Literal["everything", "basic_attributes_only"] | Omit = omit,
        metadata: object | Omit = omit,
        override_dynamic_variables: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatResponse:
        """
        Update metadata and sensitive data storage settings for an existing chat.

        Args:
          custom_attributes: Custom attributes for the chat

          data_storage_setting: Data storage setting for this chat. Overrides the agent's default setting.
              "everything" stores all data, "basic_attributes_only" stores only metadata.
              Cannot be downgraded from more restrictive to less restrictive settings.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the chat. Not used for processing. You
              can later get this field from the chat object. Size limited to 50kB max.

          override_dynamic_variables: Override dynamic varaibles represented as key-value pairs of strings. Setting
              this will override or add the dynamic variables set in the agent during the
              call. Only need to set the delta where you want to override, no need to set the
              entire dynamic variables object. Setting this to null will remove any existing
              override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return self._patch(
            f"/update-chat/{chat_id}",
            body=maybe_transform(
                {
                    "custom_attributes": custom_attributes,
                    "data_storage_setting": data_storage_setting,
                    "metadata": metadata,
                    "override_dynamic_variables": override_dynamic_variables,
                },
                chat_update_params.ChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
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
    ) -> ChatListResponse:
        """List all chats

        Args:
          limit: Limit the number of chats returned.

        Default 50, Max 1000. To retrieve more than
              1000, use pagination_key to continue fetching the next page.

          pagination_key: The pagination key to continue fetching the next page of chats. Pagination key
              is represented by a chat id here, and it's exclusive (not included in the
              fetched chats). The last chat id from the list chats is usually used as
              pagination key here. If not set, will start from the beginning.

          sort_order: The chats will be sorted by `start_timestamp`, whether to return the chats in
              ascending or descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        return self._get(
            "/list-chat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    chat_list_params.ChatListParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
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

    def create_sms_chat(
        self,
        *,
        from_number: str,
        to_number: str,
        metadata: object | Omit = omit,
        override_agent_id: str | Omit = omit,
        override_agent_version: int | Omit = omit,
        retell_llm_dynamic_variables: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatResponse:
        """
        Start an outbound SMS chat conversation with a phone number using the specified
        agent. The agent must be configured for chat mode. The initial SMS message will
        be automatically generated and sent based on the agent's configuration.

        Args:
          from_number: The phone number to send SMS from in E.164 format. Must be a number purchased
              from Retell or imported to Retell with SMS capability.

          to_number: The phone number to send SMS to in E.164 format

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the chat. Not used for processing. You
              can later get this field from the chat object.

          override_agent_id: For this particular chat, override the agent used with this agent id. This does
              not bind the agent to this number, this is for one time override.

          override_agent_version: For this particular chat, override the agent version used with this version.
              This does not bind the agent version to this number, this is for one time
              override.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-sms-chat",
            body=maybe_transform(
                {
                    "from_number": from_number,
                    "to_number": to_number,
                    "metadata": metadata,
                    "override_agent_id": override_agent_id,
                    "override_agent_version": override_agent_version,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                chat_create_sms_chat_params.ChatCreateSMSChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        agent_version: int | Omit = omit,
        metadata: object | Omit = omit,
        retell_llm_dynamic_variables: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    async def update(
        self,
        chat_id: str,
        *,
        custom_attributes: Dict[str, Union[str, float, bool]] | Omit = omit,
        data_storage_setting: Literal["everything", "basic_attributes_only"] | Omit = omit,
        metadata: object | Omit = omit,
        override_dynamic_variables: Optional[Dict[str, str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatResponse:
        """
        Update metadata and sensitive data storage settings for an existing chat.

        Args:
          custom_attributes: Custom attributes for the chat

          data_storage_setting: Data storage setting for this chat. Overrides the agent's default setting.
              "everything" stores all data, "basic_attributes_only" stores only metadata.
              Cannot be downgraded from more restrictive to less restrictive settings.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the chat. Not used for processing. You
              can later get this field from the chat object. Size limited to 50kB max.

          override_dynamic_variables: Override dynamic varaibles represented as key-value pairs of strings. Setting
              this will override or add the dynamic variables set in the agent during the
              call. Only need to set the delta where you want to override, no need to set the
              entire dynamic variables object. Setting this to null will remove any existing
              override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not chat_id:
            raise ValueError(f"Expected a non-empty value for `chat_id` but received {chat_id!r}")
        return await self._patch(
            f"/update-chat/{chat_id}",
            body=await async_maybe_transform(
                {
                    "custom_attributes": custom_attributes,
                    "data_storage_setting": data_storage_setting,
                    "metadata": metadata,
                    "override_dynamic_variables": override_dynamic_variables,
                },
                chat_update_params.ChatUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
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
    ) -> ChatListResponse:
        """List all chats

        Args:
          limit: Limit the number of chats returned.

        Default 50, Max 1000. To retrieve more than
              1000, use pagination_key to continue fetching the next page.

          pagination_key: The pagination key to continue fetching the next page of chats. Pagination key
              is represented by a chat id here, and it's exclusive (not included in the
              fetched chats). The last chat id from the list chats is usually used as
              pagination key here. If not set, will start from the beginning.

          sort_order: The chats will be sorted by `start_timestamp`, whether to return the chats in
              ascending or descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
        return await self._get(
            "/list-chat",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    chat_list_params.ChatListParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        if not is_given(timeout) and self._client.timeout == DEFAULT_TIMEOUT:
            timeout = 300
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

    async def create_sms_chat(
        self,
        *,
        from_number: str,
        to_number: str,
        metadata: object | Omit = omit,
        override_agent_id: str | Omit = omit,
        override_agent_version: int | Omit = omit,
        retell_llm_dynamic_variables: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatResponse:
        """
        Start an outbound SMS chat conversation with a phone number using the specified
        agent. The agent must be configured for chat mode. The initial SMS message will
        be automatically generated and sent based on the agent's configuration.

        Args:
          from_number: The phone number to send SMS from in E.164 format. Must be a number purchased
              from Retell or imported to Retell with SMS capability.

          to_number: The phone number to send SMS to in E.164 format

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the chat. Not used for processing. You
              can later get this field from the chat object.

          override_agent_id: For this particular chat, override the agent used with this agent id. This does
              not bind the agent to this number, this is for one time override.

          override_agent_version: For this particular chat, override the agent version used with this version.
              This does not bind the agent version to this number, this is for one time
              override.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-sms-chat",
            body=await async_maybe_transform(
                {
                    "from_number": from_number,
                    "to_number": to_number,
                    "metadata": metadata,
                    "override_agent_id": override_agent_id,
                    "override_agent_version": override_agent_version,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                chat_create_sms_chat_params.ChatCreateSMSChatParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        self.update = to_raw_response_wrapper(
            chat.update,
        )
        self.list = to_raw_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = to_raw_response_wrapper(
            chat.create_chat_completion,
        )
        self.create_sms_chat = to_raw_response_wrapper(
            chat.create_sms_chat,
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
        self.update = async_to_raw_response_wrapper(
            chat.update,
        )
        self.list = async_to_raw_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = async_to_raw_response_wrapper(
            chat.create_chat_completion,
        )
        self.create_sms_chat = async_to_raw_response_wrapper(
            chat.create_sms_chat,
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
        self.update = to_streamed_response_wrapper(
            chat.update,
        )
        self.list = to_streamed_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = to_streamed_response_wrapper(
            chat.create_chat_completion,
        )
        self.create_sms_chat = to_streamed_response_wrapper(
            chat.create_sms_chat,
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
        self.update = async_to_streamed_response_wrapper(
            chat.update,
        )
        self.list = async_to_streamed_response_wrapper(
            chat.list,
        )
        self.create_chat_completion = async_to_streamed_response_wrapper(
            chat.create_chat_completion,
        )
        self.create_sms_chat = async_to_streamed_response_wrapper(
            chat.create_sms_chat,
        )
        self.end = async_to_streamed_response_wrapper(
            chat.end,
        )
