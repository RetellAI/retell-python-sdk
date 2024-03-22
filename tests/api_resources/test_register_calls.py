# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell_ai import RetellAI, AsyncRetellAI
from tests.utils import assert_matches_type
from retell_ai.types import RegisterCallCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegisterCalls:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RetellAI) -> None:
        register_call = client.register_calls.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )
        assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RetellAI) -> None:
        register_call = client.register_calls.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
            end_call_after_silence_ms=600000,
            from_number="string",
            metadata={},
            to_number="string",
        )
        assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RetellAI) -> None:
        response = client.register_calls.with_raw_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        register_call = response.parse()
        assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RetellAI) -> None:
        with client.register_calls.with_streaming_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            register_call = response.parse()
            assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRegisterCalls:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetellAI) -> None:
        register_call = await async_client.register_calls.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )
        assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetellAI) -> None:
        register_call = await async_client.register_calls.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
            end_call_after_silence_ms=600000,
            from_number="string",
            metadata={},
            to_number="string",
        )
        assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetellAI) -> None:
        response = await async_client.register_calls.with_raw_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        register_call = await response.parse()
        assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetellAI) -> None:
        async with async_client.register_calls.with_streaming_response.create(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            audio_encoding="s16le",
            audio_websocket_protocol="twilio",
            sample_rate=24000,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            register_call = await response.parse()
            assert_matches_type(RegisterCallCreateResponse, register_call, path=["response"])

        assert cast(Any, response.is_closed) is True
