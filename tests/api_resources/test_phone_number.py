# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell_sdk import RetellSdk, AsyncRetellSdk
from tests.utils import assert_matches_type
from retell_sdk.types import (
    PhoneNumberListResponse,
    PhoneNumberCreateResponse,
    PhoneNumberUpdateResponse,
    PhoneNumberRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumber:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RetellSdk) -> None:
        phone_number = client.phone_number.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RetellSdk) -> None:
        phone_number = client.phone_number.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            area_code="string",
        )
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RetellSdk) -> None:
        response = client.phone_number.with_raw_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RetellSdk) -> None:
        with client.phone_number.with_streaming_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: RetellSdk) -> None:
        phone_number = client.phone_number.retrieve(
            "string",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RetellSdk) -> None:
        response = client.phone_number.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RetellSdk) -> None:
        with client.phone_number.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: RetellSdk) -> None:
        phone_number = client.phone_number.update(
            "string",
            agent_id="string",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: RetellSdk) -> None:
        response = client.phone_number.with_raw_response.update(
            "string",
            agent_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: RetellSdk) -> None:
        with client.phone_number.with_streaming_response.update(
            "string",
            agent_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: RetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number.with_raw_response.update(
                "",
                agent_id="string",
            )

    @parametrize
    def test_method_list(self, client: RetellSdk) -> None:
        phone_number = client.phone_number.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RetellSdk) -> None:
        response = client.phone_number.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RetellSdk) -> None:
        with client.phone_number.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RetellSdk) -> None:
        phone_number = client.phone_number.delete(
            "string",
        )
        assert phone_number is None

    @parametrize
    def test_raw_response_delete(self, client: RetellSdk) -> None:
        response = client.phone_number.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert phone_number is None

    @parametrize
    def test_streaming_response_delete(self, client: RetellSdk) -> None:
        with client.phone_number.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number.with_raw_response.delete(
                "",
            )


class TestAsyncPhoneNumber:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetellSdk) -> None:
        phone_number = await async_client.phone_number.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetellSdk) -> None:
        phone_number = await async_client.phone_number.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            area_code="string",
        )
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.phone_number.with_raw_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.phone_number.with_streaming_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberCreateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetellSdk) -> None:
        phone_number = await async_client.phone_number.retrieve(
            "string",
        )
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.phone_number.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.phone_number.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberRetrieveResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetellSdk) -> None:
        phone_number = await async_client.phone_number.update(
            "string",
            agent_id="string",
        )
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.phone_number.with_raw_response.update(
            "string",
            agent_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.phone_number.with_streaming_response.update(
            "string",
            agent_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberUpdateResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number.with_raw_response.update(
                "",
                agent_id="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetellSdk) -> None:
        phone_number = await async_client.phone_number.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.phone_number.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.phone_number.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetellSdk) -> None:
        phone_number = await async_client.phone_number.delete(
            "string",
        )
        assert phone_number is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetellSdk) -> None:
        response = await async_client.phone_number.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert phone_number is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetellSdk) -> None:
        async with async_client.phone_number.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetellSdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number.with_raw_response.delete(
                "",
            )
