# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    VoiceResponse,
    VoiceListResponse,
    VoiceSearchResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVoice:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        voice = client.voice.retrieve(
            "11labs-Adrian",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.voice.with_raw_response.retrieve(
            "11labs-Adrian",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.voice.with_streaming_response.retrieve(
            "11labs-Adrian",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `voice_id` but received ''"):
            client.voice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        voice = client.voice.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.voice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.voice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_resource(self, client: Retell) -> None:
        voice = client.voice.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_resource_with_all_params(self, client: Retell) -> None:
        voice = client.voice.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
            public_user_id="public_user_id",
            voice_provider="elevenlabs",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_resource(self, client: Retell) -> None:
        response = client.voice.with_raw_response.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_resource(self, client: Retell) -> None:
        with client.voice.with_streaming_response.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone(self, client: Retell) -> None:
        voice = client.voice.clone(
            files=[b"raw file contents"],
            voice_name="x",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Retell) -> None:
        voice = client.voice.clone(
            files=[b"raw file contents"],
            voice_name="x",
            voice_provider="elevenlabs",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Retell) -> None:
        response = client.voice.with_raw_response.clone(
            files=[b"raw file contents"],
            voice_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Retell) -> None:
        with client.voice.with_streaming_response.clone(
            files=[b"raw file contents"],
            voice_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: Retell) -> None:
        voice = client.voice.search(
            search_query="search_query",
        )
        assert_matches_type(VoiceSearchResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: Retell) -> None:
        voice = client.voice.search(
            search_query="search_query",
            voice_provider="elevenlabs",
        )
        assert_matches_type(VoiceSearchResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: Retell) -> None:
        response = client.voice.with_raw_response.search(
            search_query="search_query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = response.parse()
        assert_matches_type(VoiceSearchResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: Retell) -> None:
        with client.voice.with_streaming_response.search(
            search_query="search_query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = response.parse()
            assert_matches_type(VoiceSearchResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVoice:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.retrieve(
            "11labs-Adrian",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.voice.with_raw_response.retrieve(
            "11labs-Adrian",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.voice.with_streaming_response.retrieve(
            "11labs-Adrian",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `voice_id` but received ''"):
            await async_client.voice.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.list()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.voice.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceListResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.voice.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceListResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_resource(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_resource_with_all_params(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
            public_user_id="public_user_id",
            voice_provider="elevenlabs",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_resource(self, async_client: AsyncRetell) -> None:
        response = await async_client.voice.with_raw_response.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_resource(self, async_client: AsyncRetell) -> None:
        async with async_client.voice.with_streaming_response.add_resource(
            provider_voice_id="provider_voice_id",
            voice_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.clone(
            files=[b"raw file contents"],
            voice_name="x",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.clone(
            files=[b"raw file contents"],
            voice_name="x",
            voice_provider="elevenlabs",
        )
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncRetell) -> None:
        response = await async_client.voice.with_raw_response.clone(
            files=[b"raw file contents"],
            voice_name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncRetell) -> None:
        async with async_client.voice.with_streaming_response.clone(
            files=[b"raw file contents"],
            voice_name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.search(
            search_query="search_query",
        )
        assert_matches_type(VoiceSearchResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncRetell) -> None:
        voice = await async_client.voice.search(
            search_query="search_query",
            voice_provider="elevenlabs",
        )
        assert_matches_type(VoiceSearchResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncRetell) -> None:
        response = await async_client.voice.with_raw_response.search(
            search_query="search_query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        voice = await response.parse()
        assert_matches_type(VoiceSearchResponse, voice, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncRetell) -> None:
        async with async_client.voice.with_streaming_response.search(
            search_query="search_query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            voice = await response.parse()
            assert_matches_type(VoiceSearchResponse, voice, path=["response"])

        assert cast(Any, response.is_closed) is True
