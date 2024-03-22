# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import CallListResponse, CallRetrieveResponse, call_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["Calls", "AsyncCalls"]


class Calls(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallsWithRawResponse:
        return CallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallsWithStreamingResponse:
        return CallsWithStreamingResponse(self)

    def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallRetrieveResponse:
        """
        Retrieve details of a specific call

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return self._get(
            f"/get-call/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    def list(
        self,
        *,
        filter_criteria: call_list_params.FilterCriteria | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        sort_order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallListResponse:
        """
        Retrieve call details

        Args:
          limit: Limit the number of calls returned.

          sort_order: The calls will be sorted by `start_timestamp`, whether to return the calls in
              ascending or descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/list-calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_criteria": filter_criteria,
                        "limit": limit,
                        "sort_order": sort_order,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )


class AsyncCalls(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallsWithRawResponse:
        return AsyncCallsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallsWithStreamingResponse:
        return AsyncCallsWithStreamingResponse(self)

    async def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallRetrieveResponse:
        """
        Retrieve details of a specific call

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return await self._get(
            f"/get-call/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter_criteria: call_list_params.FilterCriteria | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        sort_order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallListResponse:
        """
        Retrieve call details

        Args:
          limit: Limit the number of calls returned.

          sort_order: The calls will be sorted by `start_timestamp`, whether to return the calls in
              ascending or descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/list-calls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter_criteria": filter_criteria,
                        "limit": limit,
                        "sort_order": sort_order,
                    },
                    call_list_params.CallListParams,
                ),
            ),
            cast_to=CallListResponse,
        )


class CallsWithRawResponse:
    def __init__(self, calls: Calls) -> None:
        self._calls = calls

        self.retrieve = to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = to_raw_response_wrapper(
            calls.list,
        )


class AsyncCallsWithRawResponse:
    def __init__(self, calls: AsyncCalls) -> None:
        self._calls = calls

        self.retrieve = async_to_raw_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            calls.list,
        )


class CallsWithStreamingResponse:
    def __init__(self, calls: Calls) -> None:
        self._calls = calls

        self.retrieve = to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            calls.list,
        )


class AsyncCallsWithStreamingResponse:
    def __init__(self, calls: AsyncCalls) -> None:
        self._calls = calls

        self.retrieve = async_to_streamed_response_wrapper(
            calls.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            calls.list,
        )
