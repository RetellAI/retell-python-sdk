# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    CallResponse,
    CallListResponse,
    RegisterCallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Retell) -> None:
        call = client.call.create(
            from_number="string",
            to_number="string",
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        call = client.call.create(
            from_number="string",
            to_number="string",
            drop_call_if_machine_detected=True,
            override_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            retell_llm_dynamic_variables={"customer_name": "John Doe"},
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.call.with_raw_response.create(
            from_number="string",
            to_number="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.call.with_streaming_response.create(
            from_number="string",
            to_number="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(RegisterCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    def test_method_list(self, client: Retell) -> None:
        call = client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        call = client.call.list(
            filter_criteria={
                "agent_id": ["oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD"],
                "before_start_timestamp": 1703302407399,
                "after_start_timestamp": 1703302407300,
                "before_end_timestamp": 1703302428899,
                "after_end_timestamp": 1703302428800,
            },
            limit=0,
            pagination_key="string",
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
    def test_method_register(self, client: Retell) -> None:
        call = client.call.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: Retell) -> None:
        call = client.call.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
            end_call_after_silence_ms=600000,
            from_number="string",
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "John Doe"},
            to_number="string",
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: Retell) -> None:
        response = client.call.with_raw_response.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: Retell) -> None:
        with client.call.with_streaming_response.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(RegisterCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCall:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create(
            from_number="string",
            to_number="string",
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create(
            from_number="string",
            to_number="string",
            drop_call_if_machine_detected=True,
            override_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            retell_llm_dynamic_variables={"customer_name": "John Doe"},
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.create(
            from_number="string",
            to_number="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.create(
            from_number="string",
            to_number="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(RegisterCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.list(
            filter_criteria={
                "agent_id": ["oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD"],
                "before_start_timestamp": 1703302407399,
                "after_start_timestamp": 1703302407300,
                "before_end_timestamp": 1703302428899,
                "after_end_timestamp": 1703302428800,
            },
            limit=0,
            pagination_key="string",
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
    async def test_method_register(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
            end_call_after_silence_ms=600000,
            from_number="string",
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "John Doe"},
            to_number="string",
        )
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(RegisterCallResponse, call, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.register(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(RegisterCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True
