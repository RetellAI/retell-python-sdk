# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import ExportRequestListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExportRequest:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        export_request = client.export_request.list()
        assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        export_request = client.export_request.list(
            limit=1000,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.export_request.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_request = response.parse()
        assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.export_request.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_request = response.parse()
            assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExportRequest:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        export_request = await async_client.export_request.list()
        assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        export_request = await async_client.export_request.list(
            limit=1000,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.export_request.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        export_request = await response.parse()
        assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.export_request.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            export_request = await response.parse()
            assert_matches_type(ExportRequestListResponse, export_request, path=["response"])

        assert cast(Any, response.is_closed) is True
