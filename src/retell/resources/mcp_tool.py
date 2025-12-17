# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import mcp_tool_get_mcp_tools_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.mcp_tool_get_mcp_tools_response import McpToolGetMcpToolsResponse

__all__ = ["McpToolResource", "AsyncMcpToolResource"]


class McpToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> McpToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return McpToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return McpToolResourceWithStreamingResponse(self)

    def get_mcp_tools(
        self,
        agent_id: str,
        *,
        mcp_id: str,
        component_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpToolGetMcpToolsResponse:
        """
        Get MCP tools for a specific agent

        Args:
          mcp_id: The ID of the MCP server to get tools from.

          component_id: The ID of the component if the MCP server is configured under a component.

          version: Optional version of the agent to use for this request. Default to latest
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/get-mcp-tools/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mcp_id": mcp_id,
                        "component_id": component_id,
                        "version": version,
                    },
                    mcp_tool_get_mcp_tools_params.McpToolGetMcpToolsParams,
                ),
            ),
            cast_to=McpToolGetMcpToolsResponse,
        )


class AsyncMcpToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMcpToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncMcpToolResourceWithStreamingResponse(self)

    async def get_mcp_tools(
        self,
        agent_id: str,
        *,
        mcp_id: str,
        component_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpToolGetMcpToolsResponse:
        """
        Get MCP tools for a specific agent

        Args:
          mcp_id: The ID of the MCP server to get tools from.

          component_id: The ID of the component if the MCP server is configured under a component.

          version: Optional version of the agent to use for this request. Default to latest
              version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/get-mcp-tools/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mcp_id": mcp_id,
                        "component_id": component_id,
                        "version": version,
                    },
                    mcp_tool_get_mcp_tools_params.McpToolGetMcpToolsParams,
                ),
            ),
            cast_to=McpToolGetMcpToolsResponse,
        )


class McpToolResourceWithRawResponse:
    def __init__(self, mcp_tool: McpToolResource) -> None:
        self._mcp_tool = mcp_tool

        self.get_mcp_tools = to_raw_response_wrapper(
            mcp_tool.get_mcp_tools,
        )


class AsyncMcpToolResourceWithRawResponse:
    def __init__(self, mcp_tool: AsyncMcpToolResource) -> None:
        self._mcp_tool = mcp_tool

        self.get_mcp_tools = async_to_raw_response_wrapper(
            mcp_tool.get_mcp_tools,
        )


class McpToolResourceWithStreamingResponse:
    def __init__(self, mcp_tool: McpToolResource) -> None:
        self._mcp_tool = mcp_tool

        self.get_mcp_tools = to_streamed_response_wrapper(
            mcp_tool.get_mcp_tools,
        )


class AsyncMcpToolResourceWithStreamingResponse:
    def __init__(self, mcp_tool: AsyncMcpToolResource) -> None:
        self._mcp_tool = mcp_tool

        self.get_mcp_tools = async_to_streamed_response_wrapper(
            mcp_tool.get_mcp_tools,
        )
