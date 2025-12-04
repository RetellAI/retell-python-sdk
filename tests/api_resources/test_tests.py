# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import BatchTestResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch_test(self, client: Retell) -> None:
        test = client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch_test_with_all_params(self, client: Retell) -> None:
        test = client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            test_case_definition_ids=["string"],
            reserved_concurrency=0,
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch_test(self, client: Retell) -> None:
        response = client.tests.with_raw_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch_test(self, client: Retell) -> None:
        with client.tests.with_streaming_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(BatchTestResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch_test(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch_test_with_all_params(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            test_case_definition_ids=["string"],
            reserved_concurrency=0,
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch_test(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch_test(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(BatchTestResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True
