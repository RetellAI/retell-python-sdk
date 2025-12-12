# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import conversation_flow_component_create_params, conversation_flow_component_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.conversation_flow_component_response import ConversationFlowComponentResponse
from ..types.conversation_flow_component_list_response import ConversationFlowComponentListResponse

__all__ = ["ConversationFlowComponentResource", "AsyncConversationFlowComponentResource"]


class ConversationFlowComponentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationFlowComponentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConversationFlowComponentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationFlowComponentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ConversationFlowComponentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        nodes: Iterable[conversation_flow_component_create_params.Node],
        begin_tag_display_position: Optional[conversation_flow_component_create_params.BeginTagDisplayPosition]
        | Omit = omit,
        mcps: Optional[Iterable[conversation_flow_component_create_params.Mcp]] | Omit = omit,
        start_node_id: Optional[str] | Omit = omit,
        tools: Optional[Iterable[conversation_flow_component_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentResponse:
        """
        Create a new shared conversation flow component

        Args:
          name: Name of the component

          nodes: Nodes that make up the component

          begin_tag_display_position: Display position for the begin tag in the frontend

          mcps: A list of MCP server configurations to use for this component

          start_node_id: ID of the starting node

          tools: Tools available within the component

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-conversation-flow-component",
            body=maybe_transform(
                {
                    "name": name,
                    "nodes": nodes,
                    "begin_tag_display_position": begin_tag_display_position,
                    "mcps": mcps,
                    "start_node_id": start_node_id,
                    "tools": tools,
                },
                conversation_flow_component_create_params.ConversationFlowComponentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentResponse,
        )

    def retrieve(
        self,
        conversation_flow_component_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentResponse:
        """
        Get a shared conversation flow component

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_component_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_component_id` but received {conversation_flow_component_id!r}"
            )
        return self._get(
            f"/get-conversation-flow-component/{conversation_flow_component_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentResponse,
        )

    def update(
        self,
        conversation_flow_component_id: str,
        *,
        begin_tag_display_position: Optional[conversation_flow_component_update_params.BeginTagDisplayPosition]
        | Omit = omit,
        mcps: Optional[Iterable[conversation_flow_component_update_params.Mcp]] | Omit = omit,
        name: str | Omit = omit,
        nodes: Iterable[conversation_flow_component_update_params.Node] | Omit = omit,
        start_node_id: Optional[str] | Omit = omit,
        tools: Optional[Iterable[conversation_flow_component_update_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentResponse:
        """
        Update an existing shared conversation flow component

        Args:
          begin_tag_display_position: Display position for the begin tag in the frontend

          mcps: A list of MCP server configurations to use for this component

          name: Name of the component

          nodes: Nodes that make up the component

          start_node_id: ID of the starting node

          tools: Tools available within the component

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_component_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_component_id` but received {conversation_flow_component_id!r}"
            )
        return self._patch(
            f"/update-conversation-flow-component/{conversation_flow_component_id}",
            body=maybe_transform(
                {
                    "begin_tag_display_position": begin_tag_display_position,
                    "mcps": mcps,
                    "name": name,
                    "nodes": nodes,
                    "start_node_id": start_node_id,
                    "tools": tools,
                },
                conversation_flow_component_update_params.ConversationFlowComponentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentListResponse:
        """List shared conversation flow components"""
        return self._get(
            "/list-conversation-flow-components",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentListResponse,
        )

    def delete(
        self,
        conversation_flow_component_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a shared conversation flow component.

        When deleting a shared component,
        creates local copies for all linked conversation flows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_component_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_component_id` but received {conversation_flow_component_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-conversation-flow-component/{conversation_flow_component_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncConversationFlowComponentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationFlowComponentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationFlowComponentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationFlowComponentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncConversationFlowComponentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        nodes: Iterable[conversation_flow_component_create_params.Node],
        begin_tag_display_position: Optional[conversation_flow_component_create_params.BeginTagDisplayPosition]
        | Omit = omit,
        mcps: Optional[Iterable[conversation_flow_component_create_params.Mcp]] | Omit = omit,
        start_node_id: Optional[str] | Omit = omit,
        tools: Optional[Iterable[conversation_flow_component_create_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentResponse:
        """
        Create a new shared conversation flow component

        Args:
          name: Name of the component

          nodes: Nodes that make up the component

          begin_tag_display_position: Display position for the begin tag in the frontend

          mcps: A list of MCP server configurations to use for this component

          start_node_id: ID of the starting node

          tools: Tools available within the component

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-conversation-flow-component",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "nodes": nodes,
                    "begin_tag_display_position": begin_tag_display_position,
                    "mcps": mcps,
                    "start_node_id": start_node_id,
                    "tools": tools,
                },
                conversation_flow_component_create_params.ConversationFlowComponentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentResponse,
        )

    async def retrieve(
        self,
        conversation_flow_component_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentResponse:
        """
        Get a shared conversation flow component

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_component_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_component_id` but received {conversation_flow_component_id!r}"
            )
        return await self._get(
            f"/get-conversation-flow-component/{conversation_flow_component_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentResponse,
        )

    async def update(
        self,
        conversation_flow_component_id: str,
        *,
        begin_tag_display_position: Optional[conversation_flow_component_update_params.BeginTagDisplayPosition]
        | Omit = omit,
        mcps: Optional[Iterable[conversation_flow_component_update_params.Mcp]] | Omit = omit,
        name: str | Omit = omit,
        nodes: Iterable[conversation_flow_component_update_params.Node] | Omit = omit,
        start_node_id: Optional[str] | Omit = omit,
        tools: Optional[Iterable[conversation_flow_component_update_params.Tool]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentResponse:
        """
        Update an existing shared conversation flow component

        Args:
          begin_tag_display_position: Display position for the begin tag in the frontend

          mcps: A list of MCP server configurations to use for this component

          name: Name of the component

          nodes: Nodes that make up the component

          start_node_id: ID of the starting node

          tools: Tools available within the component

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_component_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_component_id` but received {conversation_flow_component_id!r}"
            )
        return await self._patch(
            f"/update-conversation-flow-component/{conversation_flow_component_id}",
            body=await async_maybe_transform(
                {
                    "begin_tag_display_position": begin_tag_display_position,
                    "mcps": mcps,
                    "name": name,
                    "nodes": nodes,
                    "start_node_id": start_node_id,
                    "tools": tools,
                },
                conversation_flow_component_update_params.ConversationFlowComponentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationFlowComponentListResponse:
        """List shared conversation flow components"""
        return await self._get(
            "/list-conversation-flow-components",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationFlowComponentListResponse,
        )

    async def delete(
        self,
        conversation_flow_component_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a shared conversation flow component.

        When deleting a shared component,
        creates local copies for all linked conversation flows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conversation_flow_component_id:
            raise ValueError(
                f"Expected a non-empty value for `conversation_flow_component_id` but received {conversation_flow_component_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-conversation-flow-component/{conversation_flow_component_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ConversationFlowComponentResourceWithRawResponse:
    def __init__(self, conversation_flow_component: ConversationFlowComponentResource) -> None:
        self._conversation_flow_component = conversation_flow_component

        self.create = to_raw_response_wrapper(
            conversation_flow_component.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conversation_flow_component.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conversation_flow_component.update,
        )
        self.list = to_raw_response_wrapper(
            conversation_flow_component.list,
        )
        self.delete = to_raw_response_wrapper(
            conversation_flow_component.delete,
        )


class AsyncConversationFlowComponentResourceWithRawResponse:
    def __init__(self, conversation_flow_component: AsyncConversationFlowComponentResource) -> None:
        self._conversation_flow_component = conversation_flow_component

        self.create = async_to_raw_response_wrapper(
            conversation_flow_component.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conversation_flow_component.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conversation_flow_component.update,
        )
        self.list = async_to_raw_response_wrapper(
            conversation_flow_component.list,
        )
        self.delete = async_to_raw_response_wrapper(
            conversation_flow_component.delete,
        )


class ConversationFlowComponentResourceWithStreamingResponse:
    def __init__(self, conversation_flow_component: ConversationFlowComponentResource) -> None:
        self._conversation_flow_component = conversation_flow_component

        self.create = to_streamed_response_wrapper(
            conversation_flow_component.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conversation_flow_component.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conversation_flow_component.update,
        )
        self.list = to_streamed_response_wrapper(
            conversation_flow_component.list,
        )
        self.delete = to_streamed_response_wrapper(
            conversation_flow_component.delete,
        )


class AsyncConversationFlowComponentResourceWithStreamingResponse:
    def __init__(self, conversation_flow_component: AsyncConversationFlowComponentResource) -> None:
        self._conversation_flow_component = conversation_flow_component

        self.create = async_to_streamed_response_wrapper(
            conversation_flow_component.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conversation_flow_component.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conversation_flow_component.update,
        )
        self.list = async_to_streamed_response_wrapper(
            conversation_flow_component.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            conversation_flow_component.delete,
        )
