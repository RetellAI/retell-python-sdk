# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Mapping, Iterable, cast

import httpx

from ..types import knowledge_base_create_params, knowledge_base_add_sources_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from .._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ..types.knowledge_base_response import KnowledgeBaseResponse
from ..types.knowledge_base_list_response import KnowledgeBaseListResponse

__all__ = ["KnowledgeBaseResource", "AsyncKnowledgeBaseResource"]


class KnowledgeBaseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KnowledgeBaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return KnowledgeBaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KnowledgeBaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return KnowledgeBaseResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        knowledge_base_name: str,
        enable_auto_refresh: bool | NotGiven = NOT_GIVEN,
        knowledge_base_files: List[FileTypes] | NotGiven = NOT_GIVEN,
        knowledge_base_texts: Iterable[knowledge_base_create_params.KnowledgeBaseText] | NotGiven = NOT_GIVEN,
        knowledge_base_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Create a new knowledge base

        Args:
          knowledge_base_name: Name of the knowledge base. Must be less than 40 characters.

          enable_auto_refresh: Whether to enable auto refresh for the knowledge base urls. If set to true, will
              retrieve the data from the specified url every 12 hours.

          knowledge_base_files: Files to add to the knowledge base. Limit to 25 files, where each file is
              limited to 50MB.

          knowledge_base_texts: Texts to add to the knowledge base.

          knowledge_base_urls: URLs to be scraped and added to the knowledge base. Must be valid urls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "knowledge_base_name": knowledge_base_name,
                "enable_auto_refresh": enable_auto_refresh,
                "knowledge_base_files": knowledge_base_files,
                "knowledge_base_texts": knowledge_base_texts,
                "knowledge_base_urls": knowledge_base_urls,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["knowledge_base_files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/create-knowledge-base",
            body=maybe_transform(body, knowledge_base_create_params.KnowledgeBaseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )

    def retrieve(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Retrieve details of a specific knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return self._get(
            f"/get-knowledge-base/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseListResponse:
        """List all knowledge bases"""
        return self._get(
            "/list-knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseListResponse,
        )

    def delete(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-knowledge-base/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def add_sources(
        self,
        knowledge_base_id: str,
        *,
        knowledge_base_files: List[FileTypes] | NotGiven = NOT_GIVEN,
        knowledge_base_texts: Iterable[knowledge_base_add_sources_params.KnowledgeBaseText] | NotGiven = NOT_GIVEN,
        knowledge_base_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Add sources to a knowledge base

        Args:
          knowledge_base_files: Files to add to the knowledge base. Limit to 25 files, where each file is
              limited to 50MB.

          knowledge_base_texts: Texts to add to the knowledge base.

          knowledge_base_urls: URLs to be scraped and added to the knowledge base. Must be valid urls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        body = deepcopy_minimal(
            {
                "knowledge_base_files": knowledge_base_files,
                "knowledge_base_texts": knowledge_base_texts,
                "knowledge_base_urls": knowledge_base_urls,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["knowledge_base_files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/add-knowledge-base-sources/{knowledge_base_id}",
            body=maybe_transform(body, knowledge_base_add_sources_params.KnowledgeBaseAddSourcesParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )

    def delete_source(
        self,
        source_id: str,
        *,
        knowledge_base_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Delete an existing source from knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return self._delete(
            f"/delete-knowledge-base-source/{knowledge_base_id}/source/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )


class AsyncKnowledgeBaseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKnowledgeBaseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKnowledgeBaseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKnowledgeBaseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncKnowledgeBaseResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        knowledge_base_name: str,
        enable_auto_refresh: bool | NotGiven = NOT_GIVEN,
        knowledge_base_files: List[FileTypes] | NotGiven = NOT_GIVEN,
        knowledge_base_texts: Iterable[knowledge_base_create_params.KnowledgeBaseText] | NotGiven = NOT_GIVEN,
        knowledge_base_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Create a new knowledge base

        Args:
          knowledge_base_name: Name of the knowledge base. Must be less than 40 characters.

          enable_auto_refresh: Whether to enable auto refresh for the knowledge base urls. If set to true, will
              retrieve the data from the specified url every 12 hours.

          knowledge_base_files: Files to add to the knowledge base. Limit to 25 files, where each file is
              limited to 50MB.

          knowledge_base_texts: Texts to add to the knowledge base.

          knowledge_base_urls: URLs to be scraped and added to the knowledge base. Must be valid urls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "knowledge_base_name": knowledge_base_name,
                "enable_auto_refresh": enable_auto_refresh,
                "knowledge_base_files": knowledge_base_files,
                "knowledge_base_texts": knowledge_base_texts,
                "knowledge_base_urls": knowledge_base_urls,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["knowledge_base_files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/create-knowledge-base",
            body=await async_maybe_transform(body, knowledge_base_create_params.KnowledgeBaseCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )

    async def retrieve(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Retrieve details of a specific knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        return await self._get(
            f"/get-knowledge-base/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseListResponse:
        """List all knowledge bases"""
        return await self._get(
            "/list-knowledge-bases",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseListResponse,
        )

    async def delete(
        self,
        knowledge_base_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-knowledge-base/{knowledge_base_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def add_sources(
        self,
        knowledge_base_id: str,
        *,
        knowledge_base_files: List[FileTypes] | NotGiven = NOT_GIVEN,
        knowledge_base_texts: Iterable[knowledge_base_add_sources_params.KnowledgeBaseText] | NotGiven = NOT_GIVEN,
        knowledge_base_urls: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Add sources to a knowledge base

        Args:
          knowledge_base_files: Files to add to the knowledge base. Limit to 25 files, where each file is
              limited to 50MB.

          knowledge_base_texts: Texts to add to the knowledge base.

          knowledge_base_urls: URLs to be scraped and added to the knowledge base. Must be valid urls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        body = deepcopy_minimal(
            {
                "knowledge_base_files": knowledge_base_files,
                "knowledge_base_texts": knowledge_base_texts,
                "knowledge_base_urls": knowledge_base_urls,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["knowledge_base_files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/add-knowledge-base-sources/{knowledge_base_id}",
            body=await async_maybe_transform(body, knowledge_base_add_sources_params.KnowledgeBaseAddSourcesParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )

    async def delete_source(
        self,
        source_id: str,
        *,
        knowledge_base_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KnowledgeBaseResponse:
        """
        Delete an existing source from knowledge base

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not knowledge_base_id:
            raise ValueError(f"Expected a non-empty value for `knowledge_base_id` but received {knowledge_base_id!r}")
        if not source_id:
            raise ValueError(f"Expected a non-empty value for `source_id` but received {source_id!r}")
        return await self._delete(
            f"/delete-knowledge-base-source/{knowledge_base_id}/source/{source_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KnowledgeBaseResponse,
        )


class KnowledgeBaseResourceWithRawResponse:
    def __init__(self, knowledge_base: KnowledgeBaseResource) -> None:
        self._knowledge_base = knowledge_base

        self.create = to_raw_response_wrapper(
            knowledge_base.create,
        )
        self.retrieve = to_raw_response_wrapper(
            knowledge_base.retrieve,
        )
        self.list = to_raw_response_wrapper(
            knowledge_base.list,
        )
        self.delete = to_raw_response_wrapper(
            knowledge_base.delete,
        )
        self.add_sources = to_raw_response_wrapper(
            knowledge_base.add_sources,
        )
        self.delete_source = to_raw_response_wrapper(
            knowledge_base.delete_source,
        )


class AsyncKnowledgeBaseResourceWithRawResponse:
    def __init__(self, knowledge_base: AsyncKnowledgeBaseResource) -> None:
        self._knowledge_base = knowledge_base

        self.create = async_to_raw_response_wrapper(
            knowledge_base.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            knowledge_base.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            knowledge_base.list,
        )
        self.delete = async_to_raw_response_wrapper(
            knowledge_base.delete,
        )
        self.add_sources = async_to_raw_response_wrapper(
            knowledge_base.add_sources,
        )
        self.delete_source = async_to_raw_response_wrapper(
            knowledge_base.delete_source,
        )


class KnowledgeBaseResourceWithStreamingResponse:
    def __init__(self, knowledge_base: KnowledgeBaseResource) -> None:
        self._knowledge_base = knowledge_base

        self.create = to_streamed_response_wrapper(
            knowledge_base.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            knowledge_base.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            knowledge_base.list,
        )
        self.delete = to_streamed_response_wrapper(
            knowledge_base.delete,
        )
        self.add_sources = to_streamed_response_wrapper(
            knowledge_base.add_sources,
        )
        self.delete_source = to_streamed_response_wrapper(
            knowledge_base.delete_source,
        )


class AsyncKnowledgeBaseResourceWithStreamingResponse:
    def __init__(self, knowledge_base: AsyncKnowledgeBaseResource) -> None:
        self._knowledge_base = knowledge_base

        self.create = async_to_streamed_response_wrapper(
            knowledge_base.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            knowledge_base.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            knowledge_base.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            knowledge_base.delete,
        )
        self.add_sources = async_to_streamed_response_wrapper(
            knowledge_base.add_sources,
        )
        self.delete_source = async_to_streamed_response_wrapper(
            knowledge_base.delete_source,
        )
