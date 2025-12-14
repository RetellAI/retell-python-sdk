# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    ConversationFlowComponentResponse,
    ConversationFlowComponentListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConversationFlowComponent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                }
            ],
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                    "display_position": {
                        "x": 0,
                        "y": 0,
                    },
                    "edges": [
                        {
                            "id": "id",
                            "transition_condition": {
                                "prompt": "prompt",
                                "type": "prompt",
                            },
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "finetune_conversation_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                        }
                    ],
                    "finetune_transition_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "global_node_setting": {
                        "condition": "condition",
                        "negative_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                        "positive_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                    },
                    "interruption_sensitivity": 0,
                    "knowledge_base_ids": ["kb_001", "kb_002"],
                    "model_choice": {
                        "model": "gpt-4.1",
                        "type": "cascading",
                        "high_priority": True,
                    },
                    "name": "name",
                    "skip_response_edge": {
                        "id": "id",
                        "transition_condition": {
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                        "destination_node_id": "destination_node_id",
                    },
                }
            ],
            begin_tag_display_position={
                "x": 100,
                "y": 200,
            },
            mcps=[
                {
                    "name": "name",
                    "url": "url",
                    "headers": {"Authorization": "Bearer 1234567890"},
                    "query_params": {
                        "index": "1",
                        "key": "value",
                    },
                    "timeout_ms": 0,
                }
            ],
            start_node_id="collect_info",
            tools=[
                {
                    "name": "get_customer_info",
                    "type": "custom",
                    "url": "https://api.example.com/customer",
                    "args_at_root": True,
                    "description": "Get customer information from database",
                    "headers": {"foo": "string"},
                    "method": "GET",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                    "query_params": {"foo": "string"},
                    "response_variables": {"foo": "string"},
                    "timeout_ms": 1000,
                    "tool_id": "tool_001",
                }
            ],
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.conversation_flow_component.with_raw_response.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = response.parse()
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.conversation_flow_component.with_streaming_response.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = response.parse()
            assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.retrieve(
            "conversation_flow_component_id",
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.conversation_flow_component.with_raw_response.retrieve(
            "conversation_flow_component_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = response.parse()
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.conversation_flow_component.with_streaming_response.retrieve(
            "conversation_flow_component_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = response.parse()
            assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `conversation_flow_component_id` but received ''"
        ):
            client.conversation_flow_component.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.update(
            conversation_flow_component_id="conversation_flow_component_id",
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.update(
            conversation_flow_component_id="conversation_flow_component_id",
            begin_tag_display_position={
                "x": 100,
                "y": 200,
            },
            mcps=[
                {
                    "name": "name",
                    "url": "url",
                    "headers": {"Authorization": "Bearer 1234567890"},
                    "query_params": {
                        "index": "1",
                        "key": "value",
                    },
                    "timeout_ms": 0,
                }
            ],
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                    "display_position": {
                        "x": 0,
                        "y": 0,
                    },
                    "edges": [
                        {
                            "id": "id",
                            "transition_condition": {
                                "prompt": "prompt",
                                "type": "prompt",
                            },
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "finetune_conversation_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                        }
                    ],
                    "finetune_transition_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "global_node_setting": {
                        "condition": "condition",
                        "negative_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                        "positive_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                    },
                    "interruption_sensitivity": 0,
                    "knowledge_base_ids": ["kb_001", "kb_002"],
                    "model_choice": {
                        "model": "gpt-4.1",
                        "type": "cascading",
                        "high_priority": True,
                    },
                    "name": "name",
                    "skip_response_edge": {
                        "id": "id",
                        "transition_condition": {
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                        "destination_node_id": "destination_node_id",
                    },
                }
            ],
            start_node_id="collect_info",
            tools=[
                {
                    "name": "get_customer_info",
                    "type": "custom",
                    "url": "https://api.example.com/customer",
                    "args_at_root": True,
                    "description": "Get customer information from database",
                    "headers": {"foo": "string"},
                    "method": "GET",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                    "query_params": {"foo": "string"},
                    "response_variables": {"foo": "string"},
                    "timeout_ms": 1000,
                    "tool_id": "tool_001",
                }
            ],
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.conversation_flow_component.with_raw_response.update(
            conversation_flow_component_id="conversation_flow_component_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = response.parse()
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.conversation_flow_component.with_streaming_response.update(
            conversation_flow_component_id="conversation_flow_component_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = response.parse()
            assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `conversation_flow_component_id` but received ''"
        ):
            client.conversation_flow_component.with_raw_response.update(
                conversation_flow_component_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.list()
        assert_matches_type(ConversationFlowComponentListResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.conversation_flow_component.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = response.parse()
        assert_matches_type(ConversationFlowComponentListResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.conversation_flow_component.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = response.parse()
            assert_matches_type(ConversationFlowComponentListResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        conversation_flow_component = client.conversation_flow_component.delete(
            "conversation_flow_component_id",
        )
        assert conversation_flow_component is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.conversation_flow_component.with_raw_response.delete(
            "conversation_flow_component_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = response.parse()
        assert conversation_flow_component is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.conversation_flow_component.with_streaming_response.delete(
            "conversation_flow_component_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = response.parse()
            assert conversation_flow_component is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `conversation_flow_component_id` but received ''"
        ):
            client.conversation_flow_component.with_raw_response.delete(
                "",
            )


class TestAsyncConversationFlowComponent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                }
            ],
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                    "display_position": {
                        "x": 0,
                        "y": 0,
                    },
                    "edges": [
                        {
                            "id": "id",
                            "transition_condition": {
                                "prompt": "prompt",
                                "type": "prompt",
                            },
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "finetune_conversation_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                        }
                    ],
                    "finetune_transition_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "global_node_setting": {
                        "condition": "condition",
                        "negative_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                        "positive_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                    },
                    "interruption_sensitivity": 0,
                    "knowledge_base_ids": ["kb_001", "kb_002"],
                    "model_choice": {
                        "model": "gpt-4.1",
                        "type": "cascading",
                        "high_priority": True,
                    },
                    "name": "name",
                    "skip_response_edge": {
                        "id": "id",
                        "transition_condition": {
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                        "destination_node_id": "destination_node_id",
                    },
                }
            ],
            begin_tag_display_position={
                "x": 100,
                "y": 200,
            },
            mcps=[
                {
                    "name": "name",
                    "url": "url",
                    "headers": {"Authorization": "Bearer 1234567890"},
                    "query_params": {
                        "index": "1",
                        "key": "value",
                    },
                    "timeout_ms": 0,
                }
            ],
            start_node_id="collect_info",
            tools=[
                {
                    "name": "get_customer_info",
                    "type": "custom",
                    "url": "https://api.example.com/customer",
                    "args_at_root": True,
                    "description": "Get customer information from database",
                    "headers": {"foo": "string"},
                    "method": "GET",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                    "query_params": {"foo": "string"},
                    "response_variables": {"foo": "string"},
                    "timeout_ms": 1000,
                    "tool_id": "tool_001",
                }
            ],
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.conversation_flow_component.with_raw_response.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = await response.parse()
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.conversation_flow_component.with_streaming_response.create(
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = await response.parse()
            assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.retrieve(
            "conversation_flow_component_id",
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.conversation_flow_component.with_raw_response.retrieve(
            "conversation_flow_component_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = await response.parse()
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.conversation_flow_component.with_streaming_response.retrieve(
            "conversation_flow_component_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = await response.parse()
            assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `conversation_flow_component_id` but received ''"
        ):
            await async_client.conversation_flow_component.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.update(
            conversation_flow_component_id="conversation_flow_component_id",
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.update(
            conversation_flow_component_id="conversation_flow_component_id",
            begin_tag_display_position={
                "x": 100,
                "y": 200,
            },
            mcps=[
                {
                    "name": "name",
                    "url": "url",
                    "headers": {"Authorization": "Bearer 1234567890"},
                    "query_params": {
                        "index": "1",
                        "key": "value",
                    },
                    "timeout_ms": 0,
                }
            ],
            name="Customer Information Collector",
            nodes=[
                {
                    "id": "collect_info",
                    "instruction": {
                        "text": "Ask the customer for their name and contact information.",
                        "type": "prompt",
                    },
                    "type": "conversation",
                    "display_position": {
                        "x": 0,
                        "y": 0,
                    },
                    "edges": [
                        {
                            "id": "id",
                            "transition_condition": {
                                "prompt": "prompt",
                                "type": "prompt",
                            },
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "finetune_conversation_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                        }
                    ],
                    "finetune_transition_examples": [
                        {
                            "id": "id",
                            "transcript": [
                                {
                                    "content": "content",
                                    "role": "agent",
                                }
                            ],
                            "destination_node_id": "destination_node_id",
                        }
                    ],
                    "global_node_setting": {
                        "condition": "condition",
                        "negative_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                        "positive_finetune_examples": [
                            {
                                "transcript": [
                                    {
                                        "content": "content",
                                        "role": "agent",
                                    }
                                ]
                            }
                        ],
                    },
                    "interruption_sensitivity": 0,
                    "knowledge_base_ids": ["kb_001", "kb_002"],
                    "model_choice": {
                        "model": "gpt-4.1",
                        "type": "cascading",
                        "high_priority": True,
                    },
                    "name": "name",
                    "skip_response_edge": {
                        "id": "id",
                        "transition_condition": {
                            "prompt": "prompt",
                            "type": "prompt",
                        },
                        "destination_node_id": "destination_node_id",
                    },
                }
            ],
            start_node_id="collect_info",
            tools=[
                {
                    "name": "get_customer_info",
                    "type": "custom",
                    "url": "https://api.example.com/customer",
                    "args_at_root": True,
                    "description": "Get customer information from database",
                    "headers": {"foo": "string"},
                    "method": "GET",
                    "parameters": {
                        "properties": {"foo": "bar"},
                        "type": "object",
                        "required": ["string"],
                    },
                    "query_params": {"foo": "string"},
                    "response_variables": {"foo": "string"},
                    "timeout_ms": 1000,
                    "tool_id": "tool_001",
                }
            ],
        )
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.conversation_flow_component.with_raw_response.update(
            conversation_flow_component_id="conversation_flow_component_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = await response.parse()
        assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.conversation_flow_component.with_streaming_response.update(
            conversation_flow_component_id="conversation_flow_component_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = await response.parse()
            assert_matches_type(ConversationFlowComponentResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `conversation_flow_component_id` but received ''"
        ):
            await async_client.conversation_flow_component.with_raw_response.update(
                conversation_flow_component_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.list()
        assert_matches_type(ConversationFlowComponentListResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.conversation_flow_component.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = await response.parse()
        assert_matches_type(ConversationFlowComponentListResponse, conversation_flow_component, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.conversation_flow_component.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = await response.parse()
            assert_matches_type(ConversationFlowComponentListResponse, conversation_flow_component, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        conversation_flow_component = await async_client.conversation_flow_component.delete(
            "conversation_flow_component_id",
        )
        assert conversation_flow_component is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.conversation_flow_component.with_raw_response.delete(
            "conversation_flow_component_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        conversation_flow_component = await response.parse()
        assert conversation_flow_component is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.conversation_flow_component.with_streaming_response.delete(
            "conversation_flow_component_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            conversation_flow_component = await response.parse()
            assert conversation_flow_component is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `conversation_flow_component_id` but received ''"
        ):
            await async_client.conversation_flow_component.with_raw_response.delete(
                "",
            )
