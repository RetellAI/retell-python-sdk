# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import test_create_batch_test_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.batch_test_response import BatchTestResponse

__all__ = ["TestsResource", "AsyncTestsResource"]


class TestsResource(SyncAPIResource):
    __test__ = False

    @cached_property
    def with_raw_response(self) -> TestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return TestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return TestsResourceWithStreamingResponse(self)

    def create_batch_test(
        self,
        *,
        response_engine: test_create_batch_test_params.ResponseEngine,
        test_case_definition_ids: SequenceNotStr[str],
        reserved_concurrency: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchTestResponse:
        """
        Create a batch test to run multiple test cases

        Args:
          response_engine: Response engine to use for the test cases. Custom LLM is not supported.

          test_case_definition_ids: Array of test case definition IDs to run

          reserved_concurrency: Number of concurrency reserved for all other calls that are not triggered by
              batch calls, such as inbound calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-batch-test",
            body=maybe_transform(
                {
                    "response_engine": response_engine,
                    "test_case_definition_ids": test_case_definition_ids,
                    "reserved_concurrency": reserved_concurrency,
                },
                test_create_batch_test_params.TestCreateBatchTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchTestResponse,
        )


class AsyncTestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncTestsResourceWithStreamingResponse(self)

    async def create_batch_test(
        self,
        *,
        response_engine: test_create_batch_test_params.ResponseEngine,
        test_case_definition_ids: SequenceNotStr[str],
        reserved_concurrency: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchTestResponse:
        """
        Create a batch test to run multiple test cases

        Args:
          response_engine: Response engine to use for the test cases. Custom LLM is not supported.

          test_case_definition_ids: Array of test case definition IDs to run

          reserved_concurrency: Number of concurrency reserved for all other calls that are not triggered by
              batch calls, such as inbound calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-batch-test",
            body=await async_maybe_transform(
                {
                    "response_engine": response_engine,
                    "test_case_definition_ids": test_case_definition_ids,
                    "reserved_concurrency": reserved_concurrency,
                },
                test_create_batch_test_params.TestCreateBatchTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchTestResponse,
        )


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create_batch_test = to_raw_response_wrapper(
            tests.create_batch_test,
        )


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create_batch_test = async_to_raw_response_wrapper(
            tests.create_batch_test,
        )


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create_batch_test = to_streamed_response_wrapper(
            tests.create_batch_test,
        )


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create_batch_test = async_to_streamed_response_wrapper(
            tests.create_batch_test,
        )
