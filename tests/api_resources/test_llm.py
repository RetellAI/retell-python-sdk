# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import LlmResponse, LlmListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLlm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Retell) -> None:
        llm = client.llm.create()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        llm = client.llm.create(
            begin_message="Hey I am a virtual assistant calling from Retell Hospital.",
            default_dynamic_variables={"customer_name": "John Doe"},
            general_prompt="You are ...",
            general_tools=[
                {
                    "name": "end_call",
                    "type": "end_call",
                    "description": "End the call with user.",
                }
            ],
            knowledge_base_ids=["string"],
            model="gpt-4o",
            model_high_priority=True,
            model_temperature=0,
            s2s_model="gpt-4o-realtime",
            starting_state="information_collection",
            states=[
                {
                    "name": "information_collection",
                    "edges": [
                        {
                            "description": "description",
                            "destination_state_name": "destination_state_name",
                            "parameters": {
                                "properties": {"foo": "bar"},
                                "type": "object",
                                "required": ["string"],
                            },
                        }
                    ],
                    "state_prompt": "## Task\nYou will follow the steps below...",
                    "tools": [
                        {
                            "name": "name",
                            "type": "end_call",
                            "description": "description",
                        }
                    ],
                }
            ],
            tool_call_strict_mode=True,
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.llm.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.llm.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        llm = client.llm.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.llm.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.llm.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.llm.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Retell) -> None:
        llm = client.llm.update(
            llm_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        llm = client.llm.update(
            llm_id="16b980523634a6dc504898cda492e939",
            begin_message="Hey I am a virtual assistant calling from Retell Hospital.",
            default_dynamic_variables={"customer_name": "John Doe"},
            general_prompt="You are ...",
            general_tools=[
                {
                    "name": "end_call",
                    "type": "end_call",
                    "description": "End the call with user.",
                }
            ],
            knowledge_base_ids=["string"],
            model="gpt-4o",
            model_high_priority=True,
            model_temperature=0,
            s2s_model="gpt-4o-realtime",
            starting_state="information_collection",
            states=[
                {
                    "name": "information_collection",
                    "edges": [
                        {
                            "description": "description",
                            "destination_state_name": "destination_state_name",
                            "parameters": {
                                "properties": {"foo": "bar"},
                                "type": "object",
                                "required": ["string"],
                            },
                        }
                    ],
                    "state_prompt": "## Task\nYou will follow the steps below...",
                    "tools": [
                        {
                            "name": "name",
                            "type": "end_call",
                            "description": "description",
                        }
                    ],
                }
            ],
            tool_call_strict_mode=True,
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.llm.with_raw_response.update(
            llm_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.llm.with_streaming_response.update(
            llm_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.llm.with_raw_response.update(
                llm_id="",
            )

    @parametrize
    def test_method_list(self, client: Retell) -> None:
        llm = client.llm.list()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.llm.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.llm.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert_matches_type(LlmListResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        llm = client.llm.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert llm is None

    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.llm.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = response.parse()
        assert llm is None

    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.llm.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = response.parse()
            assert llm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.llm.with_raw_response.delete(
                "",
            )


class TestAsyncLlm:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.create()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.create(
            begin_message="Hey I am a virtual assistant calling from Retell Hospital.",
            default_dynamic_variables={"customer_name": "John Doe"},
            general_prompt="You are ...",
            general_tools=[
                {
                    "name": "end_call",
                    "type": "end_call",
                    "description": "End the call with user.",
                }
            ],
            knowledge_base_ids=["string"],
            model="gpt-4o",
            model_high_priority=True,
            model_temperature=0,
            s2s_model="gpt-4o-realtime",
            starting_state="information_collection",
            states=[
                {
                    "name": "information_collection",
                    "edges": [
                        {
                            "description": "description",
                            "destination_state_name": "destination_state_name",
                            "parameters": {
                                "properties": {"foo": "bar"},
                                "type": "object",
                                "required": ["string"],
                            },
                        }
                    ],
                    "state_prompt": "## Task\nYou will follow the steps below...",
                    "tools": [
                        {
                            "name": "name",
                            "type": "end_call",
                            "description": "description",
                        }
                    ],
                }
            ],
            tool_call_strict_mode=True,
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.llm.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.llm.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.llm.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.llm.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.llm.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.update(
            llm_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.update(
            llm_id="16b980523634a6dc504898cda492e939",
            begin_message="Hey I am a virtual assistant calling from Retell Hospital.",
            default_dynamic_variables={"customer_name": "John Doe"},
            general_prompt="You are ...",
            general_tools=[
                {
                    "name": "end_call",
                    "type": "end_call",
                    "description": "End the call with user.",
                }
            ],
            knowledge_base_ids=["string"],
            model="gpt-4o",
            model_high_priority=True,
            model_temperature=0,
            s2s_model="gpt-4o-realtime",
            starting_state="information_collection",
            states=[
                {
                    "name": "information_collection",
                    "edges": [
                        {
                            "description": "description",
                            "destination_state_name": "destination_state_name",
                            "parameters": {
                                "properties": {"foo": "bar"},
                                "type": "object",
                                "required": ["string"],
                            },
                        }
                    ],
                    "state_prompt": "## Task\nYou will follow the steps below...",
                    "tools": [
                        {
                            "name": "name",
                            "type": "end_call",
                            "description": "description",
                        }
                    ],
                }
            ],
            tool_call_strict_mode=True,
        )
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.llm.with_raw_response.update(
            llm_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.llm.with_streaming_response.update(
            llm_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.llm.with_raw_response.update(
                llm_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.list()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.llm.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert_matches_type(LlmListResponse, llm, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.llm.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert_matches_type(LlmListResponse, llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        llm = await async_client.llm.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert llm is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.llm.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        llm = await response.parse()
        assert llm is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.llm.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            llm = await response.parse()
            assert llm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.llm.with_raw_response.delete(
                "",
            )
