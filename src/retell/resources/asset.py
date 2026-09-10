# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import asset_create_params
from .._files import deepcopy_with_paths
from .._types import Body, Query, Headers, NotGiven, FileTypes, not_given
from .._utils import extract_files, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.asset_create_response import AssetCreateResponse

__all__ = ["AssetResource", "AsyncAssetResource"]


class AssetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AssetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AssetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetCreateResponse:
        """Upload an image or audio asset.

        Audio is normalized to headerless mono PCM16 at
        24 kHz and can be referenced by `custom_on_hold_music_asset_id` on warm and
        agentic-warm transfer options. Accepted audio formats are MP3, WAV, WebM, OGG,
        M4A, AAC, and FLAC. The maximum upload size is 10 MB and audio duration is
        limited to 210 seconds.

        Args:
          file: Image or audio file to upload. Images support PNG, JPEG, GIF, WebP, and SVG.
              Audio supports MP3, WAV, WebM, OGG, M4A, AAC, and FLAC. Maximum size is 10 MB;
              audio is limited to 210 seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/create-asset",
            body=maybe_transform(body, asset_create_params.AssetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetCreateResponse,
        )


class AsyncAssetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncAssetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file: FileTypes,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetCreateResponse:
        """Upload an image or audio asset.

        Audio is normalized to headerless mono PCM16 at
        24 kHz and can be referenced by `custom_on_hold_music_asset_id` on warm and
        agentic-warm transfer options. Accepted audio formats are MP3, WAV, WebM, OGG,
        M4A, AAC, and FLAC. The maximum upload size is 10 MB and audio duration is
        limited to 210 seconds.

        Args:
          file: Image or audio file to upload. Images support PNG, JPEG, GIF, WebP, and SVG.
              Audio supports MP3, WAV, WebM, OGG, M4A, AAC, and FLAC. Maximum size is 10 MB;
              audio is limited to 210 seconds.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_with_paths({"file": file}, [["file"]])
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/create-asset",
            body=await async_maybe_transform(body, asset_create_params.AssetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AssetCreateResponse,
        )


class AssetResourceWithRawResponse:
    def __init__(self, asset: AssetResource) -> None:
        self._asset = asset

        self.create = to_raw_response_wrapper(
            asset.create,
        )


class AsyncAssetResourceWithRawResponse:
    def __init__(self, asset: AsyncAssetResource) -> None:
        self._asset = asset

        self.create = async_to_raw_response_wrapper(
            asset.create,
        )


class AssetResourceWithStreamingResponse:
    def __init__(self, asset: AssetResource) -> None:
        self._asset = asset

        self.create = to_streamed_response_wrapper(
            asset.create,
        )


class AsyncAssetResourceWithStreamingResponse:
    def __init__(self, asset: AsyncAssetResource) -> None:
        self._asset = asset

        self.create = async_to_streamed_response_wrapper(
            asset.create,
        )
