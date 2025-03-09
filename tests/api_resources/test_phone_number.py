# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    PhoneNumberResponse,
    PhoneNumberListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPhoneNumber:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Retell) -> None:
        phone_number = client.phone_number.create()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        phone_number = client.phone_number.create(
            area_code=415,
            inbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            inbound_webhook_url="https://example.com/inbound-webhook",
            nickname="Frontdesk Number",
            number_provider="twilio",
            outbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.phone_number.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.phone_number.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        phone_number = client.phone_number.retrieve(
            "+14157774444",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.phone_number.with_raw_response.retrieve(
            "+14157774444",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.phone_number.with_streaming_response.retrieve(
            "+14157774444",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Retell) -> None:
        phone_number = client.phone_number.update(
            phone_number="+14157774444",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        phone_number = client.phone_number.update(
            phone_number="+14157774444",
            inbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            inbound_webhook_url="https://example.com/inbound-webhook",
            nickname="Frontdesk Number",
            outbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.phone_number.with_raw_response.update(
            phone_number="+14157774444",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.phone_number.with_streaming_response.update(
            phone_number="+14157774444",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number.with_raw_response.update(
                phone_number="",
            )

    @parametrize
    def test_method_list(self, client: Retell) -> None:
        phone_number = client.phone_number.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.phone_number.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.phone_number.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        phone_number = client.phone_number.delete(
            "+14157774444",
        )
        assert phone_number is None

    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.phone_number.with_raw_response.delete(
            "+14157774444",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert phone_number is None

    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.phone_number.with_streaming_response.delete(
            "+14157774444",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.phone_number.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_import(self, client: Retell) -> None:
        phone_number = client.phone_number.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_method_import_with_all_params(self, client: Retell) -> None:
        phone_number = client.phone_number.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
            inbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            inbound_webhook_url="https://example.com/inbound-webhook",
            nickname="Frontdesk Number",
            outbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            sip_trunk_auth_password="123456",
            sip_trunk_auth_username="username",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_raw_response_import(self, client: Retell) -> None:
        response = client.phone_number.with_raw_response.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    def test_streaming_response_import(self, client: Retell) -> None:
        with client.phone_number.with_streaming_response.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPhoneNumber:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.create()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.create(
            area_code=415,
            inbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            inbound_webhook_url="https://example.com/inbound-webhook",
            nickname="Frontdesk Number",
            number_provider="twilio",
            outbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.phone_number.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.phone_number.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.retrieve(
            "+14157774444",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.phone_number.with_raw_response.retrieve(
            "+14157774444",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.phone_number.with_streaming_response.retrieve(
            "+14157774444",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.update(
            phone_number="+14157774444",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.update(
            phone_number="+14157774444",
            inbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            inbound_webhook_url="https://example.com/inbound-webhook",
            nickname="Frontdesk Number",
            outbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.phone_number.with_raw_response.update(
            phone_number="+14157774444",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.phone_number.with_streaming_response.update(
            phone_number="+14157774444",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number.with_raw_response.update(
                phone_number="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.list()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.phone_number.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.phone_number.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberListResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.delete(
            "+14157774444",
        )
        assert phone_number is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.phone_number.with_raw_response.delete(
            "+14157774444",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert phone_number is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.phone_number.with_streaming_response.delete(
            "+14157774444",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert phone_number is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.phone_number.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_import(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_method_import_with_all_params(self, async_client: AsyncRetell) -> None:
        phone_number = await async_client.phone_number.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
            inbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            inbound_webhook_url="https://example.com/inbound-webhook",
            nickname="Frontdesk Number",
            outbound_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            sip_trunk_auth_password="123456",
            sip_trunk_auth_username="username",
        )
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_raw_response_import(self, async_client: AsyncRetell) -> None:
        response = await async_client.phone_number.with_raw_response.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        phone_number = await response.parse()
        assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

    @parametrize
    async def test_streaming_response_import(self, async_client: AsyncRetell) -> None:
        async with async_client.phone_number.with_streaming_response.import_(
            phone_number="+14157774444",
            termination_uri="someuri.pstn.twilio.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            phone_number = await response.parse()
            assert_matches_type(PhoneNumberResponse, phone_number, path=["response"])

        assert cast(Any, response.is_closed) is True
