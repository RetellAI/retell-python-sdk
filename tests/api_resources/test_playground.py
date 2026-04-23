# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import PlaygroundCompletionResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlayground:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_completion(self, client: Retell) -> None:
        playground = client.playground.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                },
            ],
        )
        assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_completion_with_all_params(self, client: Retell) -> None:
        playground = client.playground.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                    "created_timestamp": 1703302428855,
                    "message_id": "Jabr9TXYYJHfvl6Syypi88rdAHYHmcq6",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                    "created_timestamp": 1703302428855,
                    "message_id": "Jabr9TXYYJHfvl6Syypi88rdAHYHmcq6",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                    "created_timestamp": 1703302428855,
                    "message_id": "Jabr9TXYYJHfvl6Syypi88rdAHYHmcq6",
                },
            ],
            version=0,
            component_id="component_xyz789",
            current_node_id="start-node-abc123",
            current_state="greeting",
            dynamic_variables={
                "customer_name": "John Smith",
                "customer_phone": "444-223-3564",
            },
            tool_mocks=[
                {
                    "input_match_rule": {"type": "any"},
                    "output": "output",
                    "tool_name": "tool_name",
                    "result": True,
                }
            ],
        )
        assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_completion(self, client: Retell) -> None:
        response = client.playground.with_raw_response.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playground = response.parse()
        assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_completion(self, client: Retell) -> None:
        with client.playground.with_streaming_response.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playground = response.parse()
            assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_completion(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.playground.with_raw_response.completion(
                agent_id="",
                messages=[
                    {
                        "content": "Hi, I'd like to check my appointment.",
                        "role": "user",
                    },
                    {
                        "content": "Sure! Could you please provide your name?",
                        "role": "agent",
                    },
                    {
                        "content": "My name is John Smith.",
                        "role": "user",
                    },
                ],
            )


class TestAsyncPlayground:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_completion(self, async_client: AsyncRetell) -> None:
        playground = await async_client.playground.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                },
            ],
        )
        assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_completion_with_all_params(self, async_client: AsyncRetell) -> None:
        playground = await async_client.playground.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                    "created_timestamp": 1703302428855,
                    "message_id": "Jabr9TXYYJHfvl6Syypi88rdAHYHmcq6",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                    "created_timestamp": 1703302428855,
                    "message_id": "Jabr9TXYYJHfvl6Syypi88rdAHYHmcq6",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                    "created_timestamp": 1703302428855,
                    "message_id": "Jabr9TXYYJHfvl6Syypi88rdAHYHmcq6",
                },
            ],
            version=0,
            component_id="component_xyz789",
            current_node_id="start-node-abc123",
            current_state="greeting",
            dynamic_variables={
                "customer_name": "John Smith",
                "customer_phone": "444-223-3564",
            },
            tool_mocks=[
                {
                    "input_match_rule": {"type": "any"},
                    "output": "output",
                    "tool_name": "tool_name",
                    "result": True,
                }
            ],
        )
        assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_completion(self, async_client: AsyncRetell) -> None:
        response = await async_client.playground.with_raw_response.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playground = await response.parse()
        assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_completion(self, async_client: AsyncRetell) -> None:
        async with async_client.playground.with_streaming_response.completion(
            agent_id="agent_id",
            messages=[
                {
                    "content": "Hi, I'd like to check my appointment.",
                    "role": "user",
                },
                {
                    "content": "Sure! Could you please provide your name?",
                    "role": "agent",
                },
                {
                    "content": "My name is John Smith.",
                    "role": "user",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playground = await response.parse()
            assert_matches_type(PlaygroundCompletionResponse, playground, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_completion(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.playground.with_raw_response.completion(
                agent_id="",
                messages=[
                    {
                        "content": "Hi, I'd like to check my appointment.",
                        "role": "user",
                    },
                    {
                        "content": "Sure! Could you please provide your name?",
                        "role": "agent",
                    },
                    {
                        "content": "My name is John Smith.",
                        "role": "user",
                    },
                ],
            )
