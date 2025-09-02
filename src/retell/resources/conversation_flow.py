# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    conversation_flow_list_params,
    conversation_flow_create_params,
    conversation_flow_update_params,
    conversation_flow_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, SequenceNotStr
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
from ..types.conversation_flow_response import ConversationFlowResponse
from ..types.conversation_flow_list_response import ConversationFlowListResponse

__all__ = ["ConversationFlowResource", "AsyncConversationFlowResource"]


class ConversationFlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConversationFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ConversationFlowResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        model_choice: conversation_flow_create_params.ModelChoice,
        nodes: Iterable[conversation_flow_create_params.Node],
        start_speaker: Literal["user", "agent"],
        begin_tag_display_position: Optional[conversation_flow_create_params.BeginTagDisplayPosition]
        | NotGiven = NOT_GIVEN,
        default_dynamic_variables: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        global_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        kb_config: conversation_flow_create_params.KBConfig | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        mcps: Optional[Iterable[conversation_flow_create_params.Mcp]] | NotGiven = NOT_GIVEN,
        model_temperature: Optional[float] | NotGiven = NOT_GIVEN,
        start_node_id: Optional[str] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[conversation_flow_create_params.Tool]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowResponse:
        """Create a new Conversation Flow that can be attached to an agent.

        This is used to
        generate response output for the agent.

        Args:
          model_choice: The model choice for the conversation flow.

          nodes: Array of nodes in the conversation flow.

          start_speaker: Who starts the conversation - user or agent.

          begin_tag_display_position: Display position for the begin tag in the frontend.

          default_dynamic_variables: Default dynamic variables that can be referenced throughout the conversation
              flow.

          global_prompt: Global prompt used in every node of the conversation flow.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: Knowledge base IDs for RAG (Retrieval-Augmented Generation).

          mcps: A list of MCP server configurations to use for this conversation flow.

          model_temperature: Controls the randomness of the model's responses. Lower values make responses
              more deterministic.

          start_node_id: ID of the start node in the conversation flow.

          tool_call_strict_mode: Whether to use strict mode for tool calls. Only applicable when using structured
              output models.

          tools: Tools available in the conversation flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-conversation-flow",
            body=maybe_transform(
                {
                    "model_choice": model_choice,
                    "nodes": nodes,
                    "start_speaker": start_speaker,
                    "begin_tag_display_position": begin_tag_display_position,
                    "default_dynamic_variables": default_dynamic_variables,
                    "global_prompt": global_prompt,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model_temperature": model_temperature,
                    "start_node_id": start_node_id,
                    "tool_call_strict_mode": tool_call_strict_mode,
                    "tools": tools,
                },
                conversation_flow_create_params.ConversationFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowResponse,
        )

    def retrieve(
        self,
        conversation_flow_id: str,
        *,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowResponse:
        """
        Retrieve details of a specific Conversation Flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_id` but received {conversation_flow_id!r}"
            )
        return self._get(
            f"/get-conversation-flow/{conversation_flow_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"version": version}, conversation_flow_retrieve_params.ConversationFlowRetrieveParams
                ),
            ),
            cast_to=ConversationFlowResponse,
        )

    def update(
        self,
        conversation_flow_id: str,
        *,
        version: str | NotGiven = NOT_GIVEN,
        begin_tag_display_position: Optional[conversation_flow_update_params.BeginTagDisplayPosition]
        | NotGiven = NOT_GIVEN,
        default_dynamic_variables: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        global_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        kb_config: conversation_flow_update_params.KBConfig | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        mcps: Optional[Iterable[conversation_flow_update_params.Mcp]] | NotGiven = NOT_GIVEN,
        model_choice: conversation_flow_update_params.ModelChoice | NotGiven = NOT_GIVEN,
        model_temperature: Optional[float] | NotGiven = NOT_GIVEN,
        nodes: Iterable[conversation_flow_update_params.Node] | NotGiven = NOT_GIVEN,
        start_node_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_speaker: Literal["user", "agent"] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[conversation_flow_update_params.Tool]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowResponse:
        """
        Update an existing conversation flow

        Args:
          version: Version of the conversation flow to update

          begin_tag_display_position: Display position for the begin tag in the frontend.

          default_dynamic_variables: Default dynamic variables that can be referenced throughout the conversation
              flow.

          global_prompt: Global prompt used in every node of the conversation flow.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: Knowledge base IDs for RAG (Retrieval-Augmented Generation).

          mcps: A list of MCP server configurations to use for this conversation flow.

          model_choice: The model choice for the conversation flow.

          model_temperature: Controls the randomness of the model's responses. Lower values make responses
              more deterministic.

          nodes: Array of nodes in the conversation flow.

          start_node_id: ID of the start node in the conversation flow.

          start_speaker: Who starts the conversation - user or agent.

          tool_call_strict_mode: Whether to use strict mode for tool calls. Only applicable when using structured
              output models.

          tools: Tools available in the conversation flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_id` but received {conversation_flow_id!r}"
            )
        return self._patch(
            f"/update-conversation-flow/{conversation_flow_id}",
            body=maybe_transform(
                {
                    "begin_tag_display_position": begin_tag_display_position,
                    "default_dynamic_variables": default_dynamic_variables,
                    "global_prompt": global_prompt,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model_choice": model_choice,
                    "model_temperature": model_temperature,
                    "nodes": nodes,
                    "start_node_id": start_node_id,
                    "start_speaker": start_speaker,
                    "tool_call_strict_mode": tool_call_strict_mode,
                    "tools": tools,
                },
                conversation_flow_update_params.ConversationFlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"version": version}, conversation_flow_update_params.ConversationFlowUpdateParams
                ),
            ),
            cast_to=ConversationFlowResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        pagination_key: str | NotGiven = NOT_GIVEN,
        pagination_key_version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowListResponse:
        """
        List all conversation flows that can be attached to an agent.

        Args:
          limit: Limit the number of conversation flows returned. Default 1000, Max 1000. To
              retrieve more than 1000, use pagination_key to continue fetching the next page.

          pagination_key: The pagination key to continue fetching the next page of conversation flows.
              Pagination key is represented by a conversation flow id here, and it's exclusive
              (not included in the fetched conversation flows). The last conversation flow id
              from the list conversation flows is usually used as pagination key here. If not
              set, will start from the beginning.

          pagination_key_version: Specifies the version of the conversation flow associated with the
              pagination_key. When paginating, both the pagination_key and its version must be
              provided to ensure consistent ordering and to fetch the next page correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/list-conversation-flows",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "pagination_key_version": pagination_key_version,
                    },
                    conversation_flow_list_params.ConversationFlowListParams,
                ),
            ),
            cast_to=ConversationFlowListResponse,
        )

    def delete(
        self,
        conversation_flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a conversation flow and all its versions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_id` but received {conversation_flow_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-conversation-flow/{conversation_flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConversationFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncConversationFlowResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        model_choice: conversation_flow_create_params.ModelChoice,
        nodes: Iterable[conversation_flow_create_params.Node],
        start_speaker: Literal["user", "agent"],
        begin_tag_display_position: Optional[conversation_flow_create_params.BeginTagDisplayPosition]
        | NotGiven = NOT_GIVEN,
        default_dynamic_variables: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        global_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        kb_config: conversation_flow_create_params.KBConfig | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        mcps: Optional[Iterable[conversation_flow_create_params.Mcp]] | NotGiven = NOT_GIVEN,
        model_temperature: Optional[float] | NotGiven = NOT_GIVEN,
        start_node_id: Optional[str] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[conversation_flow_create_params.Tool]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowResponse:
        """Create a new Conversation Flow that can be attached to an agent.

        This is used to
        generate response output for the agent.

        Args:
          model_choice: The model choice for the conversation flow.

          nodes: Array of nodes in the conversation flow.

          start_speaker: Who starts the conversation - user or agent.

          begin_tag_display_position: Display position for the begin tag in the frontend.

          default_dynamic_variables: Default dynamic variables that can be referenced throughout the conversation
              flow.

          global_prompt: Global prompt used in every node of the conversation flow.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: Knowledge base IDs for RAG (Retrieval-Augmented Generation).

          mcps: A list of MCP server configurations to use for this conversation flow.

          model_temperature: Controls the randomness of the model's responses. Lower values make responses
              more deterministic.

          start_node_id: ID of the start node in the conversation flow.

          tool_call_strict_mode: Whether to use strict mode for tool calls. Only applicable when using structured
              output models.

          tools: Tools available in the conversation flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-conversation-flow",
            body=await async_maybe_transform(
                {
                    "model_choice": model_choice,
                    "nodes": nodes,
                    "start_speaker": start_speaker,
                    "begin_tag_display_position": begin_tag_display_position,
                    "default_dynamic_variables": default_dynamic_variables,
                    "global_prompt": global_prompt,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model_temperature": model_temperature,
                    "start_node_id": start_node_id,
                    "tool_call_strict_mode": tool_call_strict_mode,
                    "tools": tools,
                },
                conversation_flow_create_params.ConversationFlowCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowResponse,
        )

    async def retrieve(
        self,
        conversation_flow_id: str,
        *,
        version: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowResponse:
        """
        Retrieve details of a specific Conversation Flow

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_id` but received {conversation_flow_id!r}"
            )
        return await self._get(
            f"/get-conversation-flow/{conversation_flow_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, conversation_flow_retrieve_params.ConversationFlowRetrieveParams
                ),
            ),
            cast_to=ConversationFlowResponse,
        )

    async def update(
        self,
        conversation_flow_id: str,
        *,
        version: str | NotGiven = NOT_GIVEN,
        begin_tag_display_position: Optional[conversation_flow_update_params.BeginTagDisplayPosition]
        | NotGiven = NOT_GIVEN,
        default_dynamic_variables: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        global_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        kb_config: conversation_flow_update_params.KBConfig | NotGiven = NOT_GIVEN,
        knowledge_base_ids: Optional[SequenceNotStr[str]] | NotGiven = NOT_GIVEN,
        mcps: Optional[Iterable[conversation_flow_update_params.Mcp]] | NotGiven = NOT_GIVEN,
        model_choice: conversation_flow_update_params.ModelChoice | NotGiven = NOT_GIVEN,
        model_temperature: Optional[float] | NotGiven = NOT_GIVEN,
        nodes: Iterable[conversation_flow_update_params.Node] | NotGiven = NOT_GIVEN,
        start_node_id: Optional[str] | NotGiven = NOT_GIVEN,
        start_speaker: Literal["user", "agent"] | NotGiven = NOT_GIVEN,
        tool_call_strict_mode: Optional[bool] | NotGiven = NOT_GIVEN,
        tools: Optional[Iterable[conversation_flow_update_params.Tool]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowResponse:
        """
        Update an existing conversation flow

        Args:
          version: Version of the conversation flow to update

          begin_tag_display_position: Display position for the begin tag in the frontend.

          default_dynamic_variables: Default dynamic variables that can be referenced throughout the conversation
              flow.

          global_prompt: Global prompt used in every node of the conversation flow.

          kb_config: Knowledge base configuration for RAG retrieval.

          knowledge_base_ids: Knowledge base IDs for RAG (Retrieval-Augmented Generation).

          mcps: A list of MCP server configurations to use for this conversation flow.

          model_choice: The model choice for the conversation flow.

          model_temperature: Controls the randomness of the model's responses. Lower values make responses
              more deterministic.

          nodes: Array of nodes in the conversation flow.

          start_node_id: ID of the start node in the conversation flow.

          start_speaker: Who starts the conversation - user or agent.

          tool_call_strict_mode: Whether to use strict mode for tool calls. Only applicable when using structured
              output models.

          tools: Tools available in the conversation flow.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_id` but received {conversation_flow_id!r}"
            )
        return await self._patch(
            f"/update-conversation-flow/{conversation_flow_id}",
            body=await async_maybe_transform(
                {
                    "begin_tag_display_position": begin_tag_display_position,
                    "default_dynamic_variables": default_dynamic_variables,
                    "global_prompt": global_prompt,
                    "kb_config": kb_config,
                    "knowledge_base_ids": knowledge_base_ids,
                    "mcps": mcps,
                    "model_choice": model_choice,
                    "model_temperature": model_temperature,
                    "nodes": nodes,
                    "start_node_id": start_node_id,
                    "start_speaker": start_speaker,
                    "tool_call_strict_mode": tool_call_strict_mode,
                    "tools": tools,
                },
                conversation_flow_update_params.ConversationFlowUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, conversation_flow_update_params.ConversationFlowUpdateParams
                ),
            ),
            cast_to=ConversationFlowResponse,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        pagination_key: str | NotGiven = NOT_GIVEN,
        pagination_key_version: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConversationFlowListResponse:
        """
        List all conversation flows that can be attached to an agent.

        Args:
          limit: Limit the number of conversation flows returned. Default 1000, Max 1000. To
              retrieve more than 1000, use pagination_key to continue fetching the next page.

          pagination_key: The pagination key to continue fetching the next page of conversation flows.
              Pagination key is represented by a conversation flow id here, and it's exclusive
              (not included in the fetched conversation flows). The last conversation flow id
              from the list conversation flows is usually used as pagination key here. If not
              set, will start from the beginning.

          pagination_key_version: Specifies the version of the conversation flow associated with the
              pagination_key. When paginating, both the pagination_key and its version must be
              provided to ensure consistent ordering and to fetch the next page correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/list-conversation-flows",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "pagination_key_version": pagination_key_version,
                    },
                    conversation_flow_list_params.ConversationFlowListParams,
                ),
            ),
            cast_to=ConversationFlowListResponse,
        )

    async def delete(
        self,
        conversation_flow_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a conversation flow and all its versions

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_id` but received {conversation_flow_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-conversation-flow/{conversation_flow_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConversationFlowResourceWithRawResponse:
    def __init__(self, conversation_flow: ConversationFlowResource) -> None:
        self._conversation_flow = conversation_flow

        self.create = to_raw_response_wrapper(
            conversation_flow.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversation_flow.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conversation_flow.update,
        )
        self.list = to_raw_response_wrapper(
            conversation_flow.list,
        )
        self.delete = to_raw_response_wrapper(
            conversation_flow.delete,
        )


class AsyncConversationFlowResourceWithRawResponse:
    def __init__(self, conversation_flow: AsyncConversationFlowResource) -> None:
        self._conversation_flow = conversation_flow

        self.create = async_to_raw_response_wrapper(
            conversation_flow.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversation_flow.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conversation_flow.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversation_flow.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conversation_flow.delete,
        )


class ConversationFlowResourceWithStreamingResponse:
    def __init__(self, conversation_flow: ConversationFlowResource) -> None:
        self._conversation_flow = conversation_flow

        self.create = to_streamed_response_wrapper(
            conversation_flow.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversation_flow.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conversation_flow.update,
        )
        self.list = to_streamed_response_wrapper(
            conversation_flow.list,
        )
        self.delete = to_streamed_response_wrapper(
            conversation_flow.delete,
        )


class AsyncConversationFlowResourceWithStreamingResponse:
    def __init__(self, conversation_flow: AsyncConversationFlowResource) -> None:
        self._conversation_flow = conversation_flow

        self.create = async_to_streamed_response_wrapper(
            conversation_flow.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversation_flow.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conversation_flow.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversation_flow.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            conversation_flow.delete,
        )
