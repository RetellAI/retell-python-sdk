# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import ConcurrencyRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConcurrency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        concurrency = client.concurrency.retrieve()
        assert_matches_type(ConcurrencyRetrieveResponse, concurrency, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.concurrency.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        concurrency = response.parse()
        assert_matches_type(ConcurrencyRetrieveResponse, concurrency, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.concurrency.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            concurrency = response.parse()
            assert_matches_type(ConcurrencyRetrieveResponse, concurrency, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConcurrency:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        concurrency = await async_client.concurrency.retrieve()
        assert_matches_type(ConcurrencyRetrieveResponse, concurrency, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.concurrency.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        concurrency = await response.parse()
        assert_matches_type(ConcurrencyRetrieveResponse, concurrency, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.concurrency.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            concurrency = await response.parse()
            assert_matches_type(ConcurrencyRetrieveResponse, concurrency, path=["response"])

        assert cast(Any, response.is_closed) is True
