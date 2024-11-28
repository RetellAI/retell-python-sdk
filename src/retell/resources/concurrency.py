# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.concurrency_retrieve_response import ConcurrencyRetrieveResponse

__all__ = ["ConcurrencyResource", "AsyncConcurrencyResource"]


class ConcurrencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConcurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ConcurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConcurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ConcurrencyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConcurrencyRetrieveResponse:
        """Get the current concurrency and concurrency limit of the org"""
        return self._get(
            "/get-concurrency",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConcurrencyRetrieveResponse,
        )


class AsyncConcurrencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConcurrencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConcurrencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConcurrencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncConcurrencyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConcurrencyRetrieveResponse:
        """Get the current concurrency and concurrency limit of the org"""
        return await self._get(
            "/get-concurrency",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConcurrencyRetrieveResponse,
        )


class ConcurrencyResourceWithRawResponse:
    def __init__(self, concurrency: ConcurrencyResource) -> None:
        self._concurrency = concurrency

        self.retrieve = to_raw_response_wrapper(
            concurrency.retrieve,
        )


class AsyncConcurrencyResourceWithRawResponse:
    def __init__(self, concurrency: AsyncConcurrencyResource) -> None:
        self._concurrency = concurrency

        self.retrieve = async_to_raw_response_wrapper(
            concurrency.retrieve,
        )


class ConcurrencyResourceWithStreamingResponse:
    def __init__(self, concurrency: ConcurrencyResource) -> None:
        self._concurrency = concurrency

        self.retrieve = to_streamed_response_wrapper(
            concurrency.retrieve,
        )


class AsyncConcurrencyResourceWithStreamingResponse:
    def __init__(self, concurrency: AsyncConcurrencyResource) -> None:
        self._concurrency = concurrency

        self.retrieve = async_to_streamed_response_wrapper(
            concurrency.retrieve,
        )
