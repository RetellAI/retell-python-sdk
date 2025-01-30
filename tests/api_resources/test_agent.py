# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import AgentResponse, AgentListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Retell) -> None:
        agent = client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        agent = client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
            agent_name="Jarvis",
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            enable_backchannel=True,
            enable_transcription_formatting=True,
            enable_voicemail_detection=True,
            end_call_after_silence_ms=600000,
            fallback_voice_ids=["openai-Alloy", "deepgram-Angus"],
            interruption_sensitivity=1,
            language="en-US",
            max_call_duration_ms=3600000,
            normalize_for_speech=True,
            opt_out_sensitive_data_storage=True,
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            pronunciation_dictionary=[
                {
                    "alphabet": "ipa",
                    "phoneme": "ˈæktʃuəli",
                    "word": "actually",
                }
            ],
            reminder_max_count=2,
            reminder_trigger_ms=10000,
            responsiveness=1,
            ring_duration_ms=30000,
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_detection_timeout_ms=30000,
            voicemail_message="Hi, please give us a callback.",
            volume=1,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.agent.with_raw_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.agent.with_streaming_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        agent = client.agent.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.agent.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.agent.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Retell) -> None:
        agent = client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        agent = client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
            agent_name="Jarvis",
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            enable_backchannel=True,
            enable_transcription_formatting=True,
            enable_voicemail_detection=True,
            end_call_after_silence_ms=600000,
            fallback_voice_ids=["openai-Alloy", "deepgram-Angus"],
            interruption_sensitivity=1,
            language="en-US",
            max_call_duration_ms=3600000,
            normalize_for_speech=True,
            opt_out_sensitive_data_storage=True,
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            pronunciation_dictionary=[
                {
                    "alphabet": "ipa",
                    "phoneme": "ˈæktʃuəli",
                    "word": "actually",
                }
            ],
            reminder_max_count=2,
            reminder_trigger_ms=10000,
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            responsiveness=1,
            ring_duration_ms=30000,
            voice_id="11labs-Adrian",
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_detection_timeout_ms=30000,
            voicemail_message="Hi, please give us a callback.",
            volume=1,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.agent.with_raw_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.agent.with_streaming_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    def test_method_list(self, client: Retell) -> None:
        agent = client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        agent = client.agent.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert agent is None

    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.agent.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.agent.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.delete(
                "",
            )


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
            agent_name="Jarvis",
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            enable_backchannel=True,
            enable_transcription_formatting=True,
            enable_voicemail_detection=True,
            end_call_after_silence_ms=600000,
            fallback_voice_ids=["openai-Alloy", "deepgram-Angus"],
            interruption_sensitivity=1,
            language="en-US",
            max_call_duration_ms=3600000,
            normalize_for_speech=True,
            opt_out_sensitive_data_storage=True,
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            pronunciation_dictionary=[
                {
                    "alphabet": "ipa",
                    "phoneme": "ˈæktʃuəli",
                    "word": "actually",
                }
            ],
            reminder_max_count=2,
            reminder_trigger_ms=10000,
            responsiveness=1,
            ring_duration_ms=30000,
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_detection_timeout_ms=30000,
            voicemail_message="Hi, please give us a callback.",
            volume=1,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="11labs-Adrian",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.retrieve(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.retrieve(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
            agent_name="Jarvis",
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            enable_backchannel=True,
            enable_transcription_formatting=True,
            enable_voicemail_detection=True,
            end_call_after_silence_ms=600000,
            fallback_voice_ids=["openai-Alloy", "deepgram-Angus"],
            interruption_sensitivity=1,
            language="en-US",
            max_call_duration_ms=3600000,
            normalize_for_speech=True,
            opt_out_sensitive_data_storage=True,
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "examples": ["John Doe", "Jane Smith"],
                }
            ],
            pronunciation_dictionary=[
                {
                    "alphabet": "ipa",
                    "phoneme": "ˈæktʃuəli",
                    "word": "actually",
                }
            ],
            reminder_max_count=2,
            reminder_trigger_ms=10000,
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            responsiveness=1,
            ring_duration_ms=30000,
            voice_id="11labs-Adrian",
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_detection_timeout_ms=30000,
            voicemail_message="Hi, please give us a callback.",
            volume=1,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.update(
                agent_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.list()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.delete(
                "",
            )
