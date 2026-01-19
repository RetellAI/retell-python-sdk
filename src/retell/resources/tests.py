# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    test_list_batch_tests_params,
    test_create_batch_test_params,
    test_list_test_case_definitions_params,
    test_create_test_case_definition_params,
    test_update_test_case_definition_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.test_case_job_response import TestCaseJobResponse
from ..types.test_list_test_runs_response import TestListTestRunsResponse
from ..types.test_case_definition_response import TestCaseDefinitionResponse
from ..types.test_list_batch_tests_response import TestListBatchTestsResponse
from ..types.test_list_test_case_definitions_response import TestListTestCaseDefinitionsResponse

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
                },
                test_create_batch_test_params.TestCreateBatchTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchTestResponse,
        )

    def create_test_case_definition(
        self,
        *,
        metrics: SequenceNotStr[str],
        name: str,
        response_engine: test_create_test_case_definition_params.ResponseEngine,
        user_prompt: str,
        dynamic_variables: Dict[str, str] | Omit = omit,
        llm_model: Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5-mini",
            "gpt-5-nano",
            "claude-4.5-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
        ]
        | Omit = omit,
        tool_mocks: Iterable[test_create_test_case_definition_params.ToolMock] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseDefinitionResponse:
        """
        Create a new test case definition

        Args:
          metrics: Array of metric names to evaluate

          name: Name of the test case definition

          response_engine: Response engine to use for the test case. Custom LLM is not supported.

          user_prompt: User prompt to simulate in the test case

          dynamic_variables: Dynamic variables to inject into the response engine

          llm_model: LLM model to use for simulation

          tool_mocks: Mock tool calls for testing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-test-case-definition",
            body=maybe_transform(
                {
                    "metrics": metrics,
                    "name": name,
                    "response_engine": response_engine,
                    "user_prompt": user_prompt,
                    "dynamic_variables": dynamic_variables,
                    "llm_model": llm_model,
                    "tool_mocks": tool_mocks,
                },
                test_create_test_case_definition_params.TestCreateTestCaseDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseDefinitionResponse,
        )

    def delete_test_case_definition(
        self,
        test_case_definition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a test case definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_definition_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_definition_id` but received {test_case_definition_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-test-case-definition/{test_case_definition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_batch_test(
        self,
        test_case_batch_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchTestResponse:
        """
        Get a batch test job by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_batch_job_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_batch_job_id` but received {test_case_batch_job_id!r}"
            )
        return self._get(
            f"/get-batch-test/{test_case_batch_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchTestResponse,
        )

    def get_test_case_definition(
        self,
        test_case_definition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseDefinitionResponse:
        """
        Get a test case definition by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_definition_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_definition_id` but received {test_case_definition_id!r}"
            )
        return self._get(
            f"/get-test-case-definition/{test_case_definition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseDefinitionResponse,
        )

    def get_test_run(
        self,
        test_case_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseJobResponse:
        """
        Get a test case job (test run) by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_job_id:
            raise ValueError(f"Expected a non-empty value for `test_case_job_id` but received {test_case_job_id!r}")
        return self._get(
            f"/get-test-run/{test_case_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseJobResponse,
        )

    def list_batch_tests(
        self,
        *,
        type: Literal["retell-llm", "conversation-flow"],
        conversation_flow_id: str | Omit = omit,
        llm_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestListBatchTestsResponse:
        """
        List batch test jobs for a response engine

        Args:
          type: Type of response engine

          conversation_flow_id: Conversation flow ID (required when type is conversation-flow)

          llm_id: LLM ID (required when type is retell-llm)

          version: Version of the response engine (defaults to latest)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/list-batch-tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "conversation_flow_id": conversation_flow_id,
                        "llm_id": llm_id,
                        "version": version,
                    },
                    test_list_batch_tests_params.TestListBatchTestsParams,
                ),
            ),
            cast_to=TestListBatchTestsResponse,
        )

    def list_test_case_definitions(
        self,
        *,
        type: Literal["retell-llm", "conversation-flow"],
        conversation_flow_id: str | Omit = omit,
        llm_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestListTestCaseDefinitionsResponse:
        """
        List test case definitions for a response engine

        Args:
          type: Type of response engine

          conversation_flow_id: Conversation flow ID (required when type is conversation-flow)

          llm_id: LLM ID (required when type is retell-llm)

          version: Version of the response engine (defaults to latest)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/list-test-case-definitions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "type": type,
                        "conversation_flow_id": conversation_flow_id,
                        "llm_id": llm_id,
                        "version": version,
                    },
                    test_list_test_case_definitions_params.TestListTestCaseDefinitionsParams,
                ),
            ),
            cast_to=TestListTestCaseDefinitionsResponse,
        )

    def list_test_runs(
        self,
        test_case_batch_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestListTestRunsResponse:
        """
        List all test case jobs (test runs) for a batch test job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_batch_job_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_batch_job_id` but received {test_case_batch_job_id!r}"
            )
        return self._get(
            f"/list-test-runs/{test_case_batch_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestListTestRunsResponse,
        )

    def update_test_case_definition(
        self,
        test_case_definition_id: str,
        *,
        dynamic_variables: Dict[str, str] | Omit = omit,
        llm_model: Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5-mini",
            "gpt-5-nano",
            "claude-4.5-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
        ]
        | Omit = omit,
        metrics: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        response_engine: test_update_test_case_definition_params.ResponseEngine | Omit = omit,
        tool_mocks: Iterable[test_update_test_case_definition_params.ToolMock] | Omit = omit,
        user_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseDefinitionResponse:
        """
        Update a test case definition

        Args:
          dynamic_variables: Dynamic variables to inject into the response engine

          llm_model: LLM model to use for simulation

          metrics: Array of metric names to evaluate

          name: Name of the test case definition

          response_engine: Response engine to use for the test case. Custom LLM is not supported.

          tool_mocks: Mock tool calls for testing

          user_prompt: User prompt to simulate in the test case

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_definition_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_definition_id` but received {test_case_definition_id!r}"
            )
        return self._put(
            f"/update-test-case-definition/{test_case_definition_id}",
            body=maybe_transform(
                {
                    "dynamic_variables": dynamic_variables,
                    "llm_model": llm_model,
                    "metrics": metrics,
                    "name": name,
                    "response_engine": response_engine,
                    "tool_mocks": tool_mocks,
                    "user_prompt": user_prompt,
                },
                test_update_test_case_definition_params.TestUpdateTestCaseDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseDefinitionResponse,
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
                },
                test_create_batch_test_params.TestCreateBatchTestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchTestResponse,
        )

    async def create_test_case_definition(
        self,
        *,
        metrics: SequenceNotStr[str],
        name: str,
        response_engine: test_create_test_case_definition_params.ResponseEngine,
        user_prompt: str,
        dynamic_variables: Dict[str, str] | Omit = omit,
        llm_model: Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5-mini",
            "gpt-5-nano",
            "claude-4.5-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
        ]
        | Omit = omit,
        tool_mocks: Iterable[test_create_test_case_definition_params.ToolMock] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseDefinitionResponse:
        """
        Create a new test case definition

        Args:
          metrics: Array of metric names to evaluate

          name: Name of the test case definition

          response_engine: Response engine to use for the test case. Custom LLM is not supported.

          user_prompt: User prompt to simulate in the test case

          dynamic_variables: Dynamic variables to inject into the response engine

          llm_model: LLM model to use for simulation

          tool_mocks: Mock tool calls for testing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-test-case-definition",
            body=await async_maybe_transform(
                {
                    "metrics": metrics,
                    "name": name,
                    "response_engine": response_engine,
                    "user_prompt": user_prompt,
                    "dynamic_variables": dynamic_variables,
                    "llm_model": llm_model,
                    "tool_mocks": tool_mocks,
                },
                test_create_test_case_definition_params.TestCreateTestCaseDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseDefinitionResponse,
        )

    async def delete_test_case_definition(
        self,
        test_case_definition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a test case definition

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_definition_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_definition_id` but received {test_case_definition_id!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-test-case-definition/{test_case_definition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_batch_test(
        self,
        test_case_batch_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchTestResponse:
        """
        Get a batch test job by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_batch_job_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_batch_job_id` but received {test_case_batch_job_id!r}"
            )
        return await self._get(
            f"/get-batch-test/{test_case_batch_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchTestResponse,
        )

    async def get_test_case_definition(
        self,
        test_case_definition_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseDefinitionResponse:
        """
        Get a test case definition by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_definition_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_definition_id` but received {test_case_definition_id!r}"
            )
        return await self._get(
            f"/get-test-case-definition/{test_case_definition_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseDefinitionResponse,
        )

    async def get_test_run(
        self,
        test_case_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseJobResponse:
        """
        Get a test case job (test run) by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_job_id:
            raise ValueError(f"Expected a non-empty value for `test_case_job_id` but received {test_case_job_id!r}")
        return await self._get(
            f"/get-test-run/{test_case_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseJobResponse,
        )

    async def list_batch_tests(
        self,
        *,
        type: Literal["retell-llm", "conversation-flow"],
        conversation_flow_id: str | Omit = omit,
        llm_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestListBatchTestsResponse:
        """
        List batch test jobs for a response engine

        Args:
          type: Type of response engine

          conversation_flow_id: Conversation flow ID (required when type is conversation-flow)

          llm_id: LLM ID (required when type is retell-llm)

          version: Version of the response engine (defaults to latest)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/list-batch-tests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "conversation_flow_id": conversation_flow_id,
                        "llm_id": llm_id,
                        "version": version,
                    },
                    test_list_batch_tests_params.TestListBatchTestsParams,
                ),
            ),
            cast_to=TestListBatchTestsResponse,
        )

    async def list_test_case_definitions(
        self,
        *,
        type: Literal["retell-llm", "conversation-flow"],
        conversation_flow_id: str | Omit = omit,
        llm_id: str | Omit = omit,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestListTestCaseDefinitionsResponse:
        """
        List test case definitions for a response engine

        Args:
          type: Type of response engine

          conversation_flow_id: Conversation flow ID (required when type is conversation-flow)

          llm_id: LLM ID (required when type is retell-llm)

          version: Version of the response engine (defaults to latest)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/list-test-case-definitions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "type": type,
                        "conversation_flow_id": conversation_flow_id,
                        "llm_id": llm_id,
                        "version": version,
                    },
                    test_list_test_case_definitions_params.TestListTestCaseDefinitionsParams,
                ),
            ),
            cast_to=TestListTestCaseDefinitionsResponse,
        )

    async def list_test_runs(
        self,
        test_case_batch_job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestListTestRunsResponse:
        """
        List all test case jobs (test runs) for a batch test job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_batch_job_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_batch_job_id` but received {test_case_batch_job_id!r}"
            )
        return await self._get(
            f"/list-test-runs/{test_case_batch_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestListTestRunsResponse,
        )

    async def update_test_case_definition(
        self,
        test_case_definition_id: str,
        *,
        dynamic_variables: Dict[str, str] | Omit = omit,
        llm_model: Literal[
            "gpt-4.1",
            "gpt-4.1-mini",
            "gpt-4.1-nano",
            "gpt-5",
            "gpt-5.1",
            "gpt-5.2",
            "gpt-5-mini",
            "gpt-5-nano",
            "claude-4.5-sonnet",
            "claude-4.5-haiku",
            "gemini-2.5-flash",
            "gemini-2.5-flash-lite",
            "gemini-3.0-flash",
        ]
        | Omit = omit,
        metrics: SequenceNotStr[str] | Omit = omit,
        name: str | Omit = omit,
        response_engine: test_update_test_case_definition_params.ResponseEngine | Omit = omit,
        tool_mocks: Iterable[test_update_test_case_definition_params.ToolMock] | Omit = omit,
        user_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestCaseDefinitionResponse:
        """
        Update a test case definition

        Args:
          dynamic_variables: Dynamic variables to inject into the response engine

          llm_model: LLM model to use for simulation

          metrics: Array of metric names to evaluate

          name: Name of the test case definition

          response_engine: Response engine to use for the test case. Custom LLM is not supported.

          tool_mocks: Mock tool calls for testing

          user_prompt: User prompt to simulate in the test case

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not test_case_definition_id:
            raise ValueError(
                f"Expected a non-empty value for `test_case_definition_id` but received {test_case_definition_id!r}"
            )
        return await self._put(
            f"/update-test-case-definition/{test_case_definition_id}",
            body=await async_maybe_transform(
                {
                    "dynamic_variables": dynamic_variables,
                    "llm_model": llm_model,
                    "metrics": metrics,
                    "name": name,
                    "response_engine": response_engine,
                    "tool_mocks": tool_mocks,
                    "user_prompt": user_prompt,
                },
                test_update_test_case_definition_params.TestUpdateTestCaseDefinitionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestCaseDefinitionResponse,
        )


class TestsResourceWithRawResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create_batch_test = to_raw_response_wrapper(
            tests.create_batch_test,
        )
        self.create_test_case_definition = to_raw_response_wrapper(
            tests.create_test_case_definition,
        )
        self.delete_test_case_definition = to_raw_response_wrapper(
            tests.delete_test_case_definition,
        )
        self.get_batch_test = to_raw_response_wrapper(
            tests.get_batch_test,
        )
        self.get_test_case_definition = to_raw_response_wrapper(
            tests.get_test_case_definition,
        )
        self.get_test_run = to_raw_response_wrapper(
            tests.get_test_run,
        )
        self.list_batch_tests = to_raw_response_wrapper(
            tests.list_batch_tests,
        )
        self.list_test_case_definitions = to_raw_response_wrapper(
            tests.list_test_case_definitions,
        )
        self.list_test_runs = to_raw_response_wrapper(
            tests.list_test_runs,
        )
        self.update_test_case_definition = to_raw_response_wrapper(
            tests.update_test_case_definition,
        )


class AsyncTestsResourceWithRawResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create_batch_test = async_to_raw_response_wrapper(
            tests.create_batch_test,
        )
        self.create_test_case_definition = async_to_raw_response_wrapper(
            tests.create_test_case_definition,
        )
        self.delete_test_case_definition = async_to_raw_response_wrapper(
            tests.delete_test_case_definition,
        )
        self.get_batch_test = async_to_raw_response_wrapper(
            tests.get_batch_test,
        )
        self.get_test_case_definition = async_to_raw_response_wrapper(
            tests.get_test_case_definition,
        )
        self.get_test_run = async_to_raw_response_wrapper(
            tests.get_test_run,
        )
        self.list_batch_tests = async_to_raw_response_wrapper(
            tests.list_batch_tests,
        )
        self.list_test_case_definitions = async_to_raw_response_wrapper(
            tests.list_test_case_definitions,
        )
        self.list_test_runs = async_to_raw_response_wrapper(
            tests.list_test_runs,
        )
        self.update_test_case_definition = async_to_raw_response_wrapper(
            tests.update_test_case_definition,
        )


class TestsResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, tests: TestsResource) -> None:
        self._tests = tests

        self.create_batch_test = to_streamed_response_wrapper(
            tests.create_batch_test,
        )
        self.create_test_case_definition = to_streamed_response_wrapper(
            tests.create_test_case_definition,
        )
        self.delete_test_case_definition = to_streamed_response_wrapper(
            tests.delete_test_case_definition,
        )
        self.get_batch_test = to_streamed_response_wrapper(
            tests.get_batch_test,
        )
        self.get_test_case_definition = to_streamed_response_wrapper(
            tests.get_test_case_definition,
        )
        self.get_test_run = to_streamed_response_wrapper(
            tests.get_test_run,
        )
        self.list_batch_tests = to_streamed_response_wrapper(
            tests.list_batch_tests,
        )
        self.list_test_case_definitions = to_streamed_response_wrapper(
            tests.list_test_case_definitions,
        )
        self.list_test_runs = to_streamed_response_wrapper(
            tests.list_test_runs,
        )
        self.update_test_case_definition = to_streamed_response_wrapper(
            tests.update_test_case_definition,
        )


class AsyncTestsResourceWithStreamingResponse:
    def __init__(self, tests: AsyncTestsResource) -> None:
        self._tests = tests

        self.create_batch_test = async_to_streamed_response_wrapper(
            tests.create_batch_test,
        )
        self.create_test_case_definition = async_to_streamed_response_wrapper(
            tests.create_test_case_definition,
        )
        self.delete_test_case_definition = async_to_streamed_response_wrapper(
            tests.delete_test_case_definition,
        )
        self.get_batch_test = async_to_streamed_response_wrapper(
            tests.get_batch_test,
        )
        self.get_test_case_definition = async_to_streamed_response_wrapper(
            tests.get_test_case_definition,
        )
        self.get_test_run = async_to_streamed_response_wrapper(
            tests.get_test_run,
        )
        self.list_batch_tests = async_to_streamed_response_wrapper(
            tests.list_batch_tests,
        )
        self.list_test_case_definitions = async_to_streamed_response_wrapper(
            tests.list_test_case_definitions,
        )
        self.list_test_runs = async_to_streamed_response_wrapper(
            tests.list_test_runs,
        )
        self.update_test_case_definition = async_to_streamed_response_wrapper(
            tests.update_test_case_definition,
        )
