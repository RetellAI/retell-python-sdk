# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import batch_call_create_batch_call_params
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
from .._base_client import make_request_options
from ..types.batch_call_response import BatchCallResponse

__all__ = ["BatchCallResource", "AsyncBatchCallResource"]


class BatchCallResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchCallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BatchCallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchCallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return BatchCallResourceWithStreamingResponse(self)

    def create_batch_call(
        self,
        *,
        from_number: str,
        tasks: Iterable[batch_call_create_batch_call_params.Task],
        name: str | NotGiven = NOT_GIVEN,
        trigger_timestamp: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCallResponse:
        """Create a batch call

        Args:
          from_number: The number you own in E.164 format.

        Must be a number purchased from Retell or
              imported to Retell.

          tasks: A list of individual call tasks to be executed as part of the batch call. Each
              task represents a single outbound call and includes details such as the
              recipient's phone number and optional dynamic variables to personalize the call
              content.

          name: The name of the batch call. Only used for your own reference.

          trigger_timestamp: The scheduled time for sending the batch call, represented as a Unix timestamp
              in milliseconds. If omitted, the call will be sent immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-batch-call",
            body=maybe_transform(
                {
                    "from_number": from_number,
                    "tasks": tasks,
                    "name": name,
                    "trigger_timestamp": trigger_timestamp,
                },
                batch_call_create_batch_call_params.BatchCallCreateBatchCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCallResponse,
        )


class AsyncBatchCallResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchCallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchCallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchCallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncBatchCallResourceWithStreamingResponse(self)

    async def create_batch_call(
        self,
        *,
        from_number: str,
        tasks: Iterable[batch_call_create_batch_call_params.Task],
        name: str | NotGiven = NOT_GIVEN,
        trigger_timestamp: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCallResponse:
        """Create a batch call

        Args:
          from_number: The number you own in E.164 format.

        Must be a number purchased from Retell or
              imported to Retell.

          tasks: A list of individual call tasks to be executed as part of the batch call. Each
              task represents a single outbound call and includes details such as the
              recipient's phone number and optional dynamic variables to personalize the call
              content.

          name: The name of the batch call. Only used for your own reference.

          trigger_timestamp: The scheduled time for sending the batch call, represented as a Unix timestamp
              in milliseconds. If omitted, the call will be sent immediately.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-batch-call",
            body=await async_maybe_transform(
                {
                    "from_number": from_number,
                    "tasks": tasks,
                    "name": name,
                    "trigger_timestamp": trigger_timestamp,
                },
                batch_call_create_batch_call_params.BatchCallCreateBatchCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCallResponse,
        )


class BatchCallResourceWithRawResponse:
    def __init__(self, batch_call: BatchCallResource) -> None:
        self._batch_call = batch_call

        self.create_batch_call = to_raw_response_wrapper(
            batch_call.create_batch_call,
        )


class AsyncBatchCallResourceWithRawResponse:
    def __init__(self, batch_call: AsyncBatchCallResource) -> None:
        self._batch_call = batch_call

        self.create_batch_call = async_to_raw_response_wrapper(
            batch_call.create_batch_call,
        )


class BatchCallResourceWithStreamingResponse:
    def __init__(self, batch_call: BatchCallResource) -> None:
        self._batch_call = batch_call

        self.create_batch_call = to_streamed_response_wrapper(
            batch_call.create_batch_call,
        )


class AsyncBatchCallResourceWithStreamingResponse:
    def __init__(self, batch_call: AsyncBatchCallResource) -> None:
        self._batch_call = batch_call

        self.create_batch_call = async_to_streamed_response_wrapper(
            batch_call.create_batch_call,
        )
