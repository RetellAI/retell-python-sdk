# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell_ai import RetellAI, AsyncRetellAI
from tests.utils import assert_matches_type
from retell_ai.types import (
    RetellLlmListResponse,
    RetellLlmCreateResponse,
    RetellLlmUpdateResponse,
    RetellLlmRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetellLlms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.create(
            general_prompt="string",
        )
        assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.create(
            general_prompt="string",
            begin_message="string",
            general_tools=[
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RetellAI) -> None:
        response = client.retell_llms.with_raw_response.create(
            general_prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = response.parse()
        assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RetellAI) -> None:
        with client.retell_llms.with_streaming_response.create(
            general_prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = response.parse()
            assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(RetellLlmRetrieveResponse, retell_llm, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: RetellAI) -> None:
        response = client.retell_llms.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = response.parse()
        assert_matches_type(RetellLlmRetrieveResponse, retell_llm, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: RetellAI) -> None:
        with client.retell_llms.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = response.parse()
            assert_matches_type(RetellLlmRetrieveResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: RetellAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.retell_llms.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
        )
        assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
            begin_message="string",
            general_tools=[
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: RetellAI) -> None:
        response = client.retell_llms.with_raw_response.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = response.parse()
        assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: RetellAI) -> None:
        with client.retell_llms.with_streaming_response.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = response.parse()
            assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: RetellAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.retell_llms.with_raw_response.update(
                "",
                general_prompt="string",
            )

    @parametrize
    def test_method_list(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.list()
        assert_matches_type(RetellLlmListResponse, retell_llm, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: RetellAI) -> None:
        response = client.retell_llms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = response.parse()
        assert_matches_type(RetellLlmListResponse, retell_llm, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: RetellAI) -> None:
        with client.retell_llms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = response.parse()
            assert_matches_type(RetellLlmListResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: RetellAI) -> None:
        retell_llm = client.retell_llms.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert retell_llm is None

    @parametrize
    def test_raw_response_delete(self, client: RetellAI) -> None:
        response = client.retell_llms.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = response.parse()
        assert retell_llm is None

    @parametrize
    def test_streaming_response_delete(self, client: RetellAI) -> None:
        with client.retell_llms.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = response.parse()
            assert retell_llm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: RetellAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            client.retell_llms.with_raw_response.delete(
                "",
            )


class TestAsyncRetellLlms:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.create(
            general_prompt="string",
        )
        assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.create(
            general_prompt="string",
            begin_message="string",
            general_tools=[
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetellAI) -> None:
        response = await async_client.retell_llms.with_raw_response.create(
            general_prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = await response.parse()
        assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetellAI) -> None:
        async with async_client.retell_llms.with_streaming_response.create(
            general_prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = await response.parse()
            assert_matches_type(RetellLlmCreateResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(RetellLlmRetrieveResponse, retell_llm, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetellAI) -> None:
        response = await async_client.retell_llms.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = await response.parse()
        assert_matches_type(RetellLlmRetrieveResponse, retell_llm, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetellAI) -> None:
        async with async_client.retell_llms.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = await response.parse()
            assert_matches_type(RetellLlmRetrieveResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetellAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.retell_llms.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
        )
        assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
            begin_message="string",
            general_tools=[
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
                {
                    "type": "pre_defined",
                    "name": "end_call",
                    "description": "string",
                },
            ],
            starting_state="string",
            states=[
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
                {
                    "name": "string",
                    "state_prompt": "string",
                    "edges": [
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                        {
                            "destination_state_name": "string",
                            "description": "string",
                            "parameters": {
                                "type": "object",
                                "properties": {"foo": "bar"},
                                "required": ["string", "string", "string"],
                            },
                            "speak_during_transition": True,
                        },
                    ],
                    "tools": [
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                        {
                            "type": "pre_defined",
                            "name": "end_call",
                            "description": "string",
                        },
                    ],
                },
            ],
        )
        assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetellAI) -> None:
        response = await async_client.retell_llms.with_raw_response.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = await response.parse()
        assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetellAI) -> None:
        async with async_client.retell_llms.with_streaming_response.update(
            "16b980523634a6dc504898cda492e939",
            general_prompt="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = await response.parse()
            assert_matches_type(RetellLlmUpdateResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetellAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.retell_llms.with_raw_response.update(
                "",
                general_prompt="string",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.list()
        assert_matches_type(RetellLlmListResponse, retell_llm, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetellAI) -> None:
        response = await async_client.retell_llms.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = await response.parse()
        assert_matches_type(RetellLlmListResponse, retell_llm, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetellAI) -> None:
        async with async_client.retell_llms.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = await response.parse()
            assert_matches_type(RetellLlmListResponse, retell_llm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetellAI) -> None:
        retell_llm = await async_client.retell_llms.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert retell_llm is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetellAI) -> None:
        response = await async_client.retell_llms.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retell_llm = await response.parse()
        assert retell_llm is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetellAI) -> None:
        async with async_client.retell_llms.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retell_llm = await response.parse()
            assert retell_llm is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetellAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `llm_id` but received ''"):
            await async_client.retell_llms.with_raw_response.delete(
                "",
            )
