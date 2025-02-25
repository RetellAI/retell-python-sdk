# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import BatchCallResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatchCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_batch_call(self, client: Retell) -> None:
        batch_call = client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @parametrize
    def test_method_create_batch_call_with_all_params(self, client: Retell) -> None:
        batch_call = client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[
                {
                    "to_number": "+12137774445",
                    "retell_llm_dynamic_variables": {"customer_name": "bar"},
                }
            ],
            name="First batch call",
            trigger_timestamp=1735718400000,
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @parametrize
    def test_raw_response_create_batch_call(self, client: Retell) -> None:
        response = client.batch_call.with_raw_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_call = response.parse()
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @parametrize
    def test_streaming_response_create_batch_call(self, client: Retell) -> None:
        with client.batch_call.with_streaming_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_call = response.parse()
            assert_matches_type(BatchCallResponse, batch_call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatchCall:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_batch_call(self, async_client: AsyncRetell) -> None:
        batch_call = await async_client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @parametrize
    async def test_method_create_batch_call_with_all_params(self, async_client: AsyncRetell) -> None:
        batch_call = await async_client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[
                {
                    "to_number": "+12137774445",
                    "retell_llm_dynamic_variables": {"customer_name": "bar"},
                }
            ],
            name="First batch call",
            trigger_timestamp=1735718400000,
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @parametrize
    async def test_raw_response_create_batch_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.batch_call.with_raw_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_call = await response.parse()
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @parametrize
    async def test_streaming_response_create_batch_call(self, async_client: AsyncRetell) -> None:
        async with async_client.batch_call.with_streaming_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_call = await response.parse()
            assert_matches_type(BatchCallResponse, batch_call, path=["response"])

        assert cast(Any, response.is_closed) is True
