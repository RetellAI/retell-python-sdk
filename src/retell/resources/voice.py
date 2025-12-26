# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast
from typing_extensions import Literal

import httpx

from ..types import voice_clone_params, voice_search_params, voice_add_resource_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.voice_response import VoiceResponse
from ..types.voice_list_response import VoiceListResponse
from ..types.voice_search_response import VoiceSearchResponse

__all__ = ["VoiceResource", "AsyncVoiceResource"]


class VoiceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return VoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return VoiceResourceWithStreamingResponse(self)

    def retrieve(
        self,
        voice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceResponse:
        """
        Retrieve details of a specific voice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not voice_id:
            raise ValueError(f"Expected a non-empty value for `voice_id` but received {voice_id!r}")
        return self._get(
            f"/get-voice/{voice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceResponse,
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
    ) -> VoiceListResponse:
        """List all voices available to the user"""
        return self._get(
            "/list-voices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceListResponse,
        )

    def add_resource(
        self,
        *,
        provider_voice_id: str,
        voice_name: str,
        public_user_id: str | Omit = omit,
        voice_provider: Literal["elevenlabs", "cartesia", "minimax"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceResponse:
        """
        Add a community voice to the voice library

        Args:
          provider_voice_id: Voice id assigned by the provider.

          voice_name: A custom name for the voice.

          public_user_id: Required for ElevenLabs only. User id of the voice owner.

          voice_provider: Voice provider to add the voice from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/add-community-voice",
            body=maybe_transform(
                {
                    "provider_voice_id": provider_voice_id,
                    "voice_name": voice_name,
                    "public_user_id": public_user_id,
                    "voice_provider": voice_provider,
                },
                voice_add_resource_params.VoiceAddResourceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceResponse,
        )

    def clone(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        voice_name: str,
        voice_provider: Literal["elevenlabs", "cartesia", "minimax"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceResponse:
        """
        Clone a voice from audio files

        Args:
          files: Audio files to use for voice cloning. Up to 25 files allowed. For Cartesia and
              MiniMax, only 1 file is supported.

          voice_name: Name for the cloned voice

          voice_provider: Voice provider to use for cloning. Defaults to elevenlabs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "voice_name": voice_name,
                "voice_provider": voice_provider,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/clone-voice",
            body=maybe_transform(body, voice_clone_params.VoiceCloneParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceResponse,
        )

    def search(
        self,
        *,
        search_query: str,
        voice_provider: Literal["elevenlabs", "cartesia", "minimax"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSearchResponse:
        """
        Search for community voices from voice providers

        Args:
          search_query: Search query to find voices by name, description, or ID.

          voice_provider: Voice provider to search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/search-community-voice",
            body=maybe_transform(
                {
                    "search_query": search_query,
                    "voice_provider": voice_provider,
                },
                voice_search_params.VoiceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceSearchResponse,
        )


class AsyncVoiceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVoiceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVoiceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVoiceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncVoiceResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        voice_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceResponse:
        """
        Retrieve details of a specific voice

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not voice_id:
            raise ValueError(f"Expected a non-empty value for `voice_id` but received {voice_id!r}")
        return await self._get(
            f"/get-voice/{voice_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceResponse,
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
    ) -> VoiceListResponse:
        """List all voices available to the user"""
        return await self._get(
            "/list-voices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceListResponse,
        )

    async def add_resource(
        self,
        *,
        provider_voice_id: str,
        voice_name: str,
        public_user_id: str | Omit = omit,
        voice_provider: Literal["elevenlabs", "cartesia", "minimax"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceResponse:
        """
        Add a community voice to the voice library

        Args:
          provider_voice_id: Voice id assigned by the provider.

          voice_name: A custom name for the voice.

          public_user_id: Required for ElevenLabs only. User id of the voice owner.

          voice_provider: Voice provider to add the voice from.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/add-community-voice",
            body=await async_maybe_transform(
                {
                    "provider_voice_id": provider_voice_id,
                    "voice_name": voice_name,
                    "public_user_id": public_user_id,
                    "voice_provider": voice_provider,
                },
                voice_add_resource_params.VoiceAddResourceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceResponse,
        )

    async def clone(
        self,
        *,
        files: SequenceNotStr[FileTypes],
        voice_name: str,
        voice_provider: Literal["elevenlabs", "cartesia", "minimax"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceResponse:
        """
        Clone a voice from audio files

        Args:
          files: Audio files to use for voice cloning. Up to 25 files allowed. For Cartesia and
              MiniMax, only 1 file is supported.

          voice_name: Name for the cloned voice

          voice_provider: Voice provider to use for cloning. Defaults to elevenlabs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "files": files,
                "voice_name": voice_name,
                "voice_provider": voice_provider,
            }
        )
        extracted_files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/clone-voice",
            body=await async_maybe_transform(body, voice_clone_params.VoiceCloneParams),
            files=extracted_files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceResponse,
        )

    async def search(
        self,
        *,
        search_query: str,
        voice_provider: Literal["elevenlabs", "cartesia", "minimax"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VoiceSearchResponse:
        """
        Search for community voices from voice providers

        Args:
          search_query: Search query to find voices by name, description, or ID.

          voice_provider: Voice provider to search.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/search-community-voice",
            body=await async_maybe_transform(
                {
                    "search_query": search_query,
                    "voice_provider": voice_provider,
                },
                voice_search_params.VoiceSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VoiceSearchResponse,
        )


class VoiceResourceWithRawResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.retrieve = to_raw_response_wrapper(
            voice.retrieve,
        )
        self.list = to_raw_response_wrapper(
            voice.list,
        )
        self.add_resource = to_raw_response_wrapper(
            voice.add_resource,
        )
        self.clone = to_raw_response_wrapper(
            voice.clone,
        )
        self.search = to_raw_response_wrapper(
            voice.search,
        )


class AsyncVoiceResourceWithRawResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.retrieve = async_to_raw_response_wrapper(
            voice.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            voice.list,
        )
        self.add_resource = async_to_raw_response_wrapper(
            voice.add_resource,
        )
        self.clone = async_to_raw_response_wrapper(
            voice.clone,
        )
        self.search = async_to_raw_response_wrapper(
            voice.search,
        )


class VoiceResourceWithStreamingResponse:
    def __init__(self, voice: VoiceResource) -> None:
        self._voice = voice

        self.retrieve = to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            voice.list,
        )
        self.add_resource = to_streamed_response_wrapper(
            voice.add_resource,
        )
        self.clone = to_streamed_response_wrapper(
            voice.clone,
        )
        self.search = to_streamed_response_wrapper(
            voice.search,
        )


class AsyncVoiceResourceWithStreamingResponse:
    def __init__(self, voice: AsyncVoiceResource) -> None:
        self._voice = voice

        self.retrieve = async_to_streamed_response_wrapper(
            voice.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            voice.list,
        )
        self.add_resource = async_to_streamed_response_wrapper(
            voice.add_resource,
        )
        self.clone = async_to_streamed_response_wrapper(
            voice.clone,
        )
        self.search = async_to_streamed_response_wrapper(
            voice.search,
        )
