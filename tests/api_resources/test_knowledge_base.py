# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    KnowledgeBaseResponse,
    KnowledgeBaseListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKnowledgeBase:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_method_create(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.create(
            knowledge_base_name="Sample KB",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.create(
            knowledge_base_name="Sample KB",
            enable_auto_refresh=True,
            knowledge_base_files=[b"raw file contents"],
            knowledge_base_texts=[
                {
                    "text": "text",
                    "title": "title",
                }
            ],
            knowledge_base_urls=["https://www.example.com", "https://www.retellai.com"],
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.knowledge_base.with_raw_response.create(
            knowledge_base_name="Sample KB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.knowledge_base.with_streaming_response.create(
            knowledge_base_name="Sample KB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.retrieve(
            "kb_1234567890",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.knowledge_base.with_raw_response.retrieve(
            "kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.knowledge_base.with_streaming_response.retrieve(
            "kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_base.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.knowledge_base.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.knowledge_base.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.delete(
            "kb_1234567890",
        )
        assert knowledge_base is None

    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.knowledge_base.with_raw_response.delete(
            "kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert knowledge_base is None

    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.knowledge_base.with_streaming_response.delete(
            "kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_base.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_method_add_sources(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.add_sources(
            knowledge_base_id="kb_1234567890",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_method_add_sources_with_all_params(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.add_sources(
            knowledge_base_id="kb_1234567890",
            knowledge_base_files=[b"raw file contents"],
            knowledge_base_texts=[
                {
                    "text": "text",
                    "title": "title",
                }
            ],
            knowledge_base_urls=["https://www.example.com", "https://www.retellai.com"],
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_raw_response_add_sources(self, client: Retell) -> None:
        response = client.knowledge_base.with_raw_response.add_sources(
            knowledge_base_id="kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_streaming_response_add_sources(self, client: Retell) -> None:
        with client.knowledge_base.with_streaming_response.add_sources(
            knowledge_base_id="kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="custom code")
    @parametrize
    def test_path_params_add_sources(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_base.with_raw_response.add_sources(
                knowledge_base_id="",
            )

    @parametrize
    def test_method_delete_source(self, client: Retell) -> None:
        knowledge_base = client.knowledge_base.delete_source(
            source_id="source_1234567890",
            knowledge_base_id="kb_1234567890",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    def test_raw_response_delete_source(self, client: Retell) -> None:
        response = client.knowledge_base.with_raw_response.delete_source(
            source_id="source_1234567890",
            knowledge_base_id="kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    def test_streaming_response_delete_source(self, client: Retell) -> None:
        with client.knowledge_base.with_streaming_response.delete_source(
            source_id="source_1234567890",
            knowledge_base_id="kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_source(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            client.knowledge_base.with_raw_response.delete_source(
                source_id="source_1234567890",
                knowledge_base_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            client.knowledge_base.with_raw_response.delete_source(
                source_id="",
                knowledge_base_id="kb_1234567890",
            )


class TestAsyncKnowledgeBase:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.create(
            knowledge_base_name="Sample KB",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.create(
            knowledge_base_name="Sample KB",
            enable_auto_refresh=True,
            knowledge_base_files=[b"raw file contents"],
            knowledge_base_texts=[
                {
                    "text": "text",
                    "title": "title",
                }
            ],
            knowledge_base_urls=["https://www.example.com", "https://www.retellai.com"],
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.knowledge_base.with_raw_response.create(
            knowledge_base_name="Sample KB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.knowledge_base.with_streaming_response.create(
            knowledge_base_name="Sample KB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.retrieve(
            "kb_1234567890",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.knowledge_base.with_raw_response.retrieve(
            "kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.knowledge_base.with_streaming_response.retrieve(
            "kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_base.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.list()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.knowledge_base.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.knowledge_base.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseListResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.delete(
            "kb_1234567890",
        )
        assert knowledge_base is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.knowledge_base.with_raw_response.delete(
            "kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert knowledge_base is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.knowledge_base.with_streaming_response.delete(
            "kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert knowledge_base is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_base.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_method_add_sources(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.add_sources(
            knowledge_base_id="kb_1234567890",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_method_add_sources_with_all_params(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.add_sources(
            knowledge_base_id="kb_1234567890",
            knowledge_base_files=[b"raw file contents"],
            knowledge_base_texts=[
                {
                    "text": "text",
                    "title": "title",
                }
            ],
            knowledge_base_urls=["https://www.example.com", "https://www.retellai.com"],
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_raw_response_add_sources(self, async_client: AsyncRetell) -> None:
        response = await async_client.knowledge_base.with_raw_response.add_sources(
            knowledge_base_id="kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_streaming_response_add_sources(self, async_client: AsyncRetell) -> None:
        async with async_client.knowledge_base.with_streaming_response.add_sources(
            knowledge_base_id="kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="custom code")
    @parametrize
    async def test_path_params_add_sources(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_base.with_raw_response.add_sources(
                knowledge_base_id="",
            )

    @parametrize
    async def test_method_delete_source(self, async_client: AsyncRetell) -> None:
        knowledge_base = await async_client.knowledge_base.delete_source(
            source_id="source_1234567890",
            knowledge_base_id="kb_1234567890",
        )
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    async def test_raw_response_delete_source(self, async_client: AsyncRetell) -> None:
        response = await async_client.knowledge_base.with_raw_response.delete_source(
            source_id="source_1234567890",
            knowledge_base_id="kb_1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        knowledge_base = await response.parse()
        assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

    @parametrize
    async def test_streaming_response_delete_source(self, async_client: AsyncRetell) -> None:
        async with async_client.knowledge_base.with_streaming_response.delete_source(
            source_id="source_1234567890",
            knowledge_base_id="kb_1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            knowledge_base = await response.parse()
            assert_matches_type(KnowledgeBaseResponse, knowledge_base, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_source(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `knowledge_base_id` but received ''"):
            await async_client.knowledge_base.with_raw_response.delete_source(
                source_id="source_1234567890",
                knowledge_base_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `source_id` but received ''"):
            await async_client.knowledge_base.with_raw_response.delete_source(
                source_id="",
                knowledge_base_id="kb_1234567890",
            )
