# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import export_request_list_params
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
from ..types.export_request_list_response import ExportRequestListResponse

__all__ = ["ExportRequestResource", "AsyncExportRequestResource"]


class ExportRequestResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ExportRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ExportRequestResourceWithStreamingResponse(self)

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
    ) -> ExportRequestListResponse:
        """
        List export requests with pagination

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
            "/v2/list-export-requests",
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
                    export_request_list_params.ExportRequestListParams,
                ),
            ),
            cast_to=ExportRequestListResponse,
        )


class AsyncExportRequestResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportRequestResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExportRequestResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportRequestResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncExportRequestResourceWithStreamingResponse(self)

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
    ) -> ExportRequestListResponse:
        """
        List export requests with pagination

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
            "/v2/list-export-requests",
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
                    export_request_list_params.ExportRequestListParams,
                ),
            ),
            cast_to=ExportRequestListResponse,
        )


class ExportRequestResourceWithRawResponse:
    def __init__(self, export_request: ExportRequestResource) -> None:
        self._export_request = export_request

        self.list = to_raw_response_wrapper(
            export_request.list,
        )


class AsyncExportRequestResourceWithRawResponse:
    def __init__(self, export_request: AsyncExportRequestResource) -> None:
        self._export_request = export_request

        self.list = async_to_raw_response_wrapper(
            export_request.list,
        )


class ExportRequestResourceWithStreamingResponse:
    def __init__(self, export_request: ExportRequestResource) -> None:
        self._export_request = export_request

        self.list = to_streamed_response_wrapper(
            export_request.list,
        )


class AsyncExportRequestResourceWithStreamingResponse:
    def __init__(self, export_request: AsyncExportRequestResource) -> None:
        self._export_request = export_request

        self.list = async_to_streamed_response_wrapper(
            export_request.list,
        )
