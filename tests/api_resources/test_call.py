# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    CallResponse,
    WebCallResponse,
    CallListResponse,
    PhoneCallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        call = client.call.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.call.with_raw_response.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.call.with_streaming_response.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Retell) -> None:
        call = client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        call = client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
            metadata={
                "customer_id": "cust_123",
                "notes": "Follow-up required",
            },
            opt_out_sensitive_data_storage=True,
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.call.with_raw_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.call.with_streaming_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.update(
                call_id="",
            )

    @parametrize
    def test_method_list(self, client: Retell) -> None:
        call = client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        call = client.call.list(
            filter_criteria={
                "agent_id": ["agent_oBeDLoLOeuAbiuaMFXRtDOLriT12345"],
                "call_status": ["ended"],
                "call_successful": [True],
                "call_type": ["phone_call"],
                "direction": ["inbound"],
                "disconnection_reason": ["user_hangup"],
                "duration_ms": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "e2e_latency_p50": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "from_number": ["string"],
                "in_voicemail": [True],
                "start_timestamp": {
                    "lower_threshold": 1738475411000,
                    "upper_threshold": 1738475421000,
                },
                "to_number": ["string"],
                "user_sentiment": ["Positive"],
                "version": [0],
            },
            limit=0,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.call.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.call.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        call = client.call.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert call is None

    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.call.with_raw_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert call is None

    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.call.with_streaming_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_create_phone_call(self, client: Retell) -> None:
        call = client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    def test_method_create_phone_call_with_all_params(self, client: Retell) -> None:
        call = client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
            custom_sip_headers={"X-Custom-Header": "Custom Value"},
            metadata={},
            override_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            override_agent_version=1,
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_create_phone_call(self, client: Retell) -> None:
        response = client.call.with_raw_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_create_phone_call(self, client: Retell) -> None:
        with client.call.with_streaming_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_web_call(self, client: Retell) -> None:
        call = client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @parametrize
    def test_method_create_web_call_with_all_params(self, client: Retell) -> None:
        call = client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_version=1,
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_create_web_call(self, client: Retell) -> None:
        response = client.call.with_raw_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(WebCallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_create_web_call(self, client: Retell) -> None:
        with client.call.with_streaming_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(WebCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register_phone_call(self, client: Retell) -> None:
        call = client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    def test_method_register_phone_call_with_all_params(self, client: Retell) -> None:
        call = client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_version=1,
            direction="inbound",
            from_number="+14157774444",
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_register_phone_call(self, client: Retell) -> None:
        response = client.call.with_raw_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_register_phone_call(self, client: Retell) -> None:
        with client.call.with_streaming_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCall:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
            metadata={
                "customer_id": "cust_123",
                "notes": "Follow-up required",
            },
            opt_out_sensitive_data_storage=True,
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.update(
                call_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.list(
            filter_criteria={
                "agent_id": ["agent_oBeDLoLOeuAbiuaMFXRtDOLriT12345"],
                "call_status": ["ended"],
                "call_successful": [True],
                "call_type": ["phone_call"],
                "direction": ["inbound"],
                "disconnection_reason": ["user_hangup"],
                "duration_ms": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "e2e_latency_p50": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "from_number": ["string"],
                "in_voicemail": [True],
                "start_timestamp": {
                    "lower_threshold": 1738475411000,
                    "upper_threshold": 1738475421000,
                },
                "to_number": ["string"],
                "user_sentiment": ["Positive"],
                "version": [0],
            },
            limit=0,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert call is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert call is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_create_phone_call(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    async def test_method_create_phone_call_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
            custom_sip_headers={"X-Custom-Header": "Custom Value"},
            metadata={},
            override_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            override_agent_version=1,
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_create_phone_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_create_phone_call(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_web_call(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @parametrize
    async def test_method_create_web_call_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_version=1,
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_create_web_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(WebCallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_create_web_call(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(WebCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register_phone_call(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    async def test_method_register_phone_call_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_version=1,
            direction="inbound",
            from_number="+14157774444",
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_register_phone_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_register_phone_call(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True
