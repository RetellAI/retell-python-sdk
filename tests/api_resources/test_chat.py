# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    ChatResponse,
    ChatListResponse,
    ChatCreateChatCompletionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChat:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Retell) -> None:
        chat = client.chat.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        chat = client.chat.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_version=1,
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.chat.with_raw_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.chat.with_streaming_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        chat = client.chat.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.chat.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.chat.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Retell) -> None:
        chat = client.chat.list()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.chat.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.chat.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_chat_completion(self, client: Retell) -> None:
        chat = client.chat.create_chat_completion(
            chat_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            content="hi how are you doing?",
        )
        assert_matches_type(ChatCreateChatCompletionResponse, chat, path=["response"])

    @parametrize
    def test_raw_response_create_chat_completion(self, client: Retell) -> None:
        response = client.chat.with_raw_response.create_chat_completion(
            chat_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            content="hi how are you doing?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert_matches_type(ChatCreateChatCompletionResponse, chat, path=["response"])

    @parametrize
    def test_streaming_response_create_chat_completion(self, client: Retell) -> None:
        with client.chat.with_streaming_response.create_chat_completion(
            chat_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            content="hi how are you doing?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert_matches_type(ChatCreateChatCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_end(self, client: Retell) -> None:
        chat = client.chat.end(
            "16b980523634a6dc504898cda492e939",
        )
        assert chat is None

    @parametrize
    def test_raw_response_end(self, client: Retell) -> None:
        response = client.chat.with_raw_response.end(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = response.parse()
        assert chat is None

    @parametrize
    def test_streaming_response_end(self, client: Retell) -> None:
        with client.chat.with_streaming_response.end(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_end(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            client.chat.with_raw_response.end(
                "",
            )


class TestAsyncChat:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        chat = await async_client.chat.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        chat = await async_client.chat.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_version=1,
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat.with_raw_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.chat.with_streaming_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        chat = await async_client.chat.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.chat.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        chat = await async_client.chat.list()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatListResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.chat.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatListResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_chat_completion(self, async_client: AsyncRetell) -> None:
        chat = await async_client.chat.create_chat_completion(
            chat_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            content="hi how are you doing?",
        )
        assert_matches_type(ChatCreateChatCompletionResponse, chat, path=["response"])

    @parametrize
    async def test_raw_response_create_chat_completion(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat.with_raw_response.create_chat_completion(
            chat_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            content="hi how are you doing?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert_matches_type(ChatCreateChatCompletionResponse, chat, path=["response"])

    @parametrize
    async def test_streaming_response_create_chat_completion(self, async_client: AsyncRetell) -> None:
        async with async_client.chat.with_streaming_response.create_chat_completion(
            chat_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            content="hi how are you doing?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert_matches_type(ChatCreateChatCompletionResponse, chat, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_end(self, async_client: AsyncRetell) -> None:
        chat = await async_client.chat.end(
            "16b980523634a6dc504898cda492e939",
        )
        assert chat is None

    @parametrize
    async def test_raw_response_end(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat.with_raw_response.end(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat = await response.parse()
        assert chat is None

    @parametrize
    async def test_streaming_response_end(self, async_client: AsyncRetell) -> None:
        async with async_client.chat.with_streaming_response.end(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat = await response.parse()
            assert chat is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_end(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `chat_id` but received ''"):
            await async_client.chat.with_raw_response.end(
                "",
            )
