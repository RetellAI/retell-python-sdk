# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    ChatAgentResponse,
    ChatAgentListResponse,
    ChatAgentGetVersionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChatAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Retell) -> None:
        chat_agent = client.chat_agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        chat_agent = client.chat_agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
                "version": 0,
            },
            agent_name="Jarvis",
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the call in a few sentences.",
            auto_close_message="Thank you for chatting. The conversation has ended.",
            data_storage_setting="everything",
            end_chat_after_silence_ms=3600000,
            is_public=False,
            language="en-US",
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_chat_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            post_chat_analysis_model="gpt-4.1-mini",
            signed_url_expiration_ms=86400000,
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        chat_agent = client.chat_agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Retell) -> None:
        chat_agent = client.chat_agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.chat_agent.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Retell) -> None:
        chat_agent = client.chat_agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        chat_agent = client.chat_agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
            agent_name="Jarvis",
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the call in a few sentences.",
            auto_close_message="Thank you for chatting. The conversation has ended.",
            data_storage_setting="everything",
            end_chat_after_silence_ms=3600000,
            is_public=False,
            language="en-US",
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_chat_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            post_chat_analysis_model="gpt-4.1-mini",
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
                "version": 0,
            },
            signed_url_expiration_ms=86400000,
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.chat_agent.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        chat_agent = client.chat_agent.list()
        assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        chat_agent = client.chat_agent.list(
            limit=50,
            pagination_key="16b980523634a6dc504898cda492e939",
            pagination_key_version=0,
        )
        assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        chat_agent = client.chat_agent.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert chat_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.chat_agent.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_versions(self, client: Retell) -> None:
        chat_agent = client.chat_agent.get_versions(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatAgentGetVersionsResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_versions(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert_matches_type(ChatAgentGetVersionsResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_versions(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert_matches_type(ChatAgentGetVersionsResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_versions(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.chat_agent.with_raw_response.get_versions(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_publish(self, client: Retell) -> None:
        chat_agent = client.chat_agent.publish(
            "16b980523634a6dc504898cda492e939",
        )
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Retell) -> None:
        response = client.chat_agent.with_raw_response.publish(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = response.parse()
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Retell) -> None:
        with client.chat_agent.with_streaming_response.publish(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = response.parse()
            assert chat_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.chat_agent.with_raw_response.publish(
                "",
            )


class TestAsyncChatAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
                "version": 0,
            },
            agent_name="Jarvis",
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the call in a few sentences.",
            auto_close_message="Thank you for chatting. The conversation has ended.",
            data_storage_setting="everything",
            end_chat_after_silence_ms=3600000,
            is_public=False,
            language="en-US",
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_chat_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            post_chat_analysis_model="gpt-4.1-mini",
            signed_url_expiration_ms=86400000,
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.chat_agent.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
            agent_name="Jarvis",
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the call in a few sentences.",
            auto_close_message="Thank you for chatting. The conversation has ended.",
            data_storage_setting="everything",
            end_chat_after_silence_ms=3600000,
            is_public=False,
            language="en-US",
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_chat_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            post_chat_analysis_model="gpt-4.1-mini",
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
                "version": 0,
            },
            signed_url_expiration_ms=86400000,
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert_matches_type(ChatAgentResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.chat_agent.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.list()
        assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.list(
            limit=50,
            pagination_key="16b980523634a6dc504898cda492e939",
            pagination_key_version=0,
        )
        assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert_matches_type(ChatAgentListResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert chat_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.chat_agent.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_versions(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.get_versions(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(ChatAgentGetVersionsResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_versions(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert_matches_type(ChatAgentGetVersionsResponse, chat_agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_versions(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert_matches_type(ChatAgentGetVersionsResponse, chat_agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_versions(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.chat_agent.with_raw_response.get_versions(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncRetell) -> None:
        chat_agent = await async_client.chat_agent.publish(
            "16b980523634a6dc504898cda492e939",
        )
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncRetell) -> None:
        response = await async_client.chat_agent.with_raw_response.publish(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chat_agent = await response.parse()
        assert chat_agent is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncRetell) -> None:
        async with async_client.chat_agent.with_streaming_response.publish(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chat_agent = await response.parse()
            assert chat_agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.chat_agent.with_raw_response.publish(
                "",
            )
