# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    AgentResponse,
    AgentListResponse,
    AgentGetVersionsResponse,
    AgentCreateVersionResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgent:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Retell) -> None:
        agent = client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="retell-Cimo",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        agent = client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
                "version": 0,
            },
            voice_id="retell-Cimo",
            agent_name="Jarvis",
            allow_dtmf_interruption=False,
            allow_user_dtmf=True,
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the outcome of the conversation in two sentences.",
            analysis_user_sentiment_prompt="Evaluate the user's sentiment based on their tone and satisfaction level.",
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            call_screening_option={
                "agent_identity": "Acme Health scheduling team",
                "call_purpose": "confirming your appointment for tomorrow",
            },
            custom_stt_config={
                "endpointing_ms": 0,
                "provider": "azure",
            },
            data_storage_retention_days=30,
            data_storage_setting="everything",
            denoising_mode="noise-cancellation",
            enable_backchannel=True,
            enable_dynamic_responsiveness=True,
            enable_dynamic_voice_speed=True,
            enable_expressive_mode=True,
            end_call_after_silence_ms=600000,
            expressive_emotion_tags=["empathetic", "excited", "sigh", "clear throat", "emphasis"],
            expressive_mode_prompt="Use [sigh] for thoughtful pauses and [excited] for good news.",
            fallback_voice_ids=["cartesia-Cimo", "minimax-Cimo"],
            guardrail_config={
                "input_topics": ["platform_integrity_jailbreaking"],
                "output_topics": ["harassment"],
            },
            handbook_config={
                "ai_disclosure": True,
                "conversational_personality": True,
                "default_personality": True,
                "echo_verification": True,
                "high_empathy": True,
                "nato_phonetic_alphabet": True,
                "natural_filler_words": True,
                "scope_boundaries": True,
                "smart_matching": True,
                "speech_normalization": True,
            },
            interruption_sensitivity=1,
            ivr_option={
                "action": {"type": "hangup"},
                "detection_prompt": "detection_prompt",
            },
            language="en-US",
            max_call_duration_ms=3600000,
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "conditional_prompt": "conditional_prompt",
                    "examples": ["John Doe", "Jane Smith"],
                    "required": True,
                }
            ],
            post_call_analysis_model="gpt-4.1-mini",
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
            signed_url_expiration_ms=86400000,
            stt_mode="fast",
            timezone="America/New_York",
            user_dtmf_options={
                "digit_limit": 1,
                "termination_key": "#",
                "timeout_ms": 1000,
            },
            version_description="Customer support agent for handling product inquiries",
            version_title="Production hotfix",
            vocab_specialization="general",
            voice_emotion="calm",
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_option={
                "action": {
                    "text": "Please give us a callback tomorrow at 10am.",
                    "type": "static_text",
                },
                "detection_prompt": "detection_prompt",
            },
            volume=1,
            webhook_events=["call_started"],
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.agent.with_raw_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="retell-Cimo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.agent.with_streaming_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="retell-Cimo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        agent = client.agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Retell) -> None:
        agent = client.agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.agent.with_raw_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Retell) -> None:
        with client.agent.with_streaming_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Retell) -> None:
        agent = client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        agent = client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
            agent_name="Jarvis",
            allow_dtmf_interruption=False,
            allow_user_dtmf=True,
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the outcome of the conversation in two sentences.",
            analysis_user_sentiment_prompt="Evaluate the user's sentiment based on their tone and satisfaction level.",
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            call_screening_option={
                "agent_identity": "Acme Health scheduling team",
                "call_purpose": "confirming your appointment for tomorrow",
            },
            custom_stt_config={
                "endpointing_ms": 0,
                "provider": "azure",
            },
            data_storage_retention_days=30,
            data_storage_setting="everything",
            denoising_mode="noise-cancellation",
            enable_backchannel=True,
            enable_dynamic_responsiveness=True,
            enable_dynamic_voice_speed=True,
            enable_expressive_mode=True,
            end_call_after_silence_ms=600000,
            expressive_emotion_tags=["empathetic", "excited", "sigh", "clear throat", "emphasis"],
            expressive_mode_prompt="Use [sigh] for thoughtful pauses and [excited] for good news.",
            fallback_voice_ids=["cartesia-Cimo", "minimax-Cimo"],
            guardrail_config={
                "input_topics": ["platform_integrity_jailbreaking"],
                "output_topics": ["harassment"],
            },
            handbook_config={
                "ai_disclosure": True,
                "conversational_personality": True,
                "default_personality": True,
                "echo_verification": True,
                "high_empathy": True,
                "nato_phonetic_alphabet": True,
                "natural_filler_words": True,
                "scope_boundaries": True,
                "smart_matching": True,
                "speech_normalization": True,
            },
            interruption_sensitivity=1,
            ivr_option={
                "action": {"type": "hangup"},
                "detection_prompt": "detection_prompt",
            },
            language="en-US",
            max_call_duration_ms=3600000,
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "conditional_prompt": "conditional_prompt",
                    "examples": ["John Doe", "Jane Smith"],
                    "required": True,
                }
            ],
            post_call_analysis_model="gpt-4.1-mini",
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
                "version": 0,
            },
            responsiveness=1,
            ring_duration_ms=30000,
            signed_url_expiration_ms=86400000,
            stt_mode="fast",
            timezone="America/New_York",
            user_dtmf_options={
                "digit_limit": 1,
                "termination_key": "#",
                "timeout_ms": 1000,
            },
            version_description="Customer support agent for handling product inquiries",
            version_title="Production hotfix",
            vocab_specialization="general",
            voice_emotion="calm",
            voice_id="retell-Cimo",
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_option={
                "action": {
                    "text": "Please give us a callback tomorrow at 10am.",
                    "type": "static_text",
                },
                "detection_prompt": "detection_prompt",
            },
            volume=1,
            webhook_events=["call_started"],
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.agent.with_raw_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        with pytest.warns(DeprecationWarning):
            agent = client.agent.list()

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        with pytest.warns(DeprecationWarning):
            agent = client.agent.list(
                is_latest=True,
                limit=50,
                pagination_key="agent_1ffdb9717444d0e77346838911",
                pagination_key_version=0,
            )

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with pytest.warns(DeprecationWarning):
            with client.agent.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                agent = response.parse()
                assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        agent = client.agent.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.agent.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_version(self, client: Retell) -> None:
        agent = client.agent.create_version(
            agent_id="agent_xxx",
            base_version=12,
        )
        assert_matches_type(AgentCreateVersionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_version(self, client: Retell) -> None:
        response = client.agent.with_raw_response.create_version(
            agent_id="agent_xxx",
            base_version=12,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateVersionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_version(self, client: Retell) -> None:
        with client.agent.with_streaming_response.create_version(
            agent_id="agent_xxx",
            base_version=12,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateVersionResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_version(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.create_version(
                agent_id="",
                base_version=12,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_version(self, client: Retell) -> None:
        agent = client.agent.delete_version(
            agent_id="agent_xxx",
            version=1,
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_version(self, client: Retell) -> None:
        response = client.agent.with_raw_response.delete_version(
            agent_id="agent_xxx",
            version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_version(self, client: Retell) -> None:
        with client.agent.with_streaming_response.delete_version(
            agent_id="agent_xxx",
            version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_version(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.delete_version(
                agent_id="",
                version=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_versions(self, client: Retell) -> None:
        agent = client.agent.get_versions(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentGetVersionsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_versions(self, client: Retell) -> None:
        response = client.agent.with_raw_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentGetVersionsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_versions(self, client: Retell) -> None:
        with client.agent.with_streaming_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentGetVersionsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_versions(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.get_versions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Retell) -> None:
        agent = client.agent.publish(
            agent_id="agent_xxx",
            version=15,
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish_with_all_params(self, client: Retell) -> None:
        agent = client.agent.publish(
            agent_id="agent_xxx",
            version=15,
            version_description="Hotfix for transfer timeout",
            version_title="Hotfix",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Retell) -> None:
        response = client.agent.with_raw_response.publish(
            agent_id="agent_xxx",
            version=15,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Retell) -> None:
        with client.agent.with_streaming_response.publish(
            agent_id="agent_xxx",
            version=15,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agent.with_raw_response.publish(
                agent_id="",
                version=15,
            )


class TestAsyncAgent:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="retell-Cimo",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
                "version": 0,
            },
            voice_id="retell-Cimo",
            agent_name="Jarvis",
            allow_dtmf_interruption=False,
            allow_user_dtmf=True,
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the outcome of the conversation in two sentences.",
            analysis_user_sentiment_prompt="Evaluate the user's sentiment based on their tone and satisfaction level.",
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            call_screening_option={
                "agent_identity": "Acme Health scheduling team",
                "call_purpose": "confirming your appointment for tomorrow",
            },
            custom_stt_config={
                "endpointing_ms": 0,
                "provider": "azure",
            },
            data_storage_retention_days=30,
            data_storage_setting="everything",
            denoising_mode="noise-cancellation",
            enable_backchannel=True,
            enable_dynamic_responsiveness=True,
            enable_dynamic_voice_speed=True,
            enable_expressive_mode=True,
            end_call_after_silence_ms=600000,
            expressive_emotion_tags=["empathetic", "excited", "sigh", "clear throat", "emphasis"],
            expressive_mode_prompt="Use [sigh] for thoughtful pauses and [excited] for good news.",
            fallback_voice_ids=["cartesia-Cimo", "minimax-Cimo"],
            guardrail_config={
                "input_topics": ["platform_integrity_jailbreaking"],
                "output_topics": ["harassment"],
            },
            handbook_config={
                "ai_disclosure": True,
                "conversational_personality": True,
                "default_personality": True,
                "echo_verification": True,
                "high_empathy": True,
                "nato_phonetic_alphabet": True,
                "natural_filler_words": True,
                "scope_boundaries": True,
                "smart_matching": True,
                "speech_normalization": True,
            },
            interruption_sensitivity=1,
            ivr_option={
                "action": {"type": "hangup"},
                "detection_prompt": "detection_prompt",
            },
            language="en-US",
            max_call_duration_ms=3600000,
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "conditional_prompt": "conditional_prompt",
                    "examples": ["John Doe", "Jane Smith"],
                    "required": True,
                }
            ],
            post_call_analysis_model="gpt-4.1-mini",
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
            signed_url_expiration_ms=86400000,
            stt_mode="fast",
            timezone="America/New_York",
            user_dtmf_options={
                "digit_limit": 1,
                "termination_key": "#",
                "timeout_ms": 1000,
            },
            version_description="Customer support agent for handling product inquiries",
            version_title="Production hotfix",
            vocab_specialization="general",
            voice_emotion="calm",
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_option={
                "action": {
                    "text": "Please give us a callback tomorrow at 10am.",
                    "type": "static_text",
                },
                "detection_prompt": "detection_prompt",
            },
            volume=1,
            webhook_events=["call_started"],
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="retell-Cimo",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.create(
            response_engine={
                "llm_id": "llm_234sdertfsdsfsdf",
                "type": "retell-llm",
            },
            voice_id="retell-Cimo",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.retrieve(
            agent_id="16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.retrieve(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.update(
            agent_id="16b980523634a6dc504898cda492e939",
            version=1,
            agent_name="Jarvis",
            allow_dtmf_interruption=False,
            allow_user_dtmf=True,
            ambient_sound="coffee-shop",
            ambient_sound_volume=1,
            analysis_successful_prompt="The agent finished the task and the call was complete without being cutoff.",
            analysis_summary_prompt="Summarize the outcome of the conversation in two sentences.",
            analysis_user_sentiment_prompt="Evaluate the user's sentiment based on their tone and satisfaction level.",
            backchannel_frequency=0.9,
            backchannel_words=["yeah", "uh-huh"],
            begin_message_delay_ms=1000,
            boosted_keywords=["retell", "kroger"],
            call_screening_option={
                "agent_identity": "Acme Health scheduling team",
                "call_purpose": "confirming your appointment for tomorrow",
            },
            custom_stt_config={
                "endpointing_ms": 0,
                "provider": "azure",
            },
            data_storage_retention_days=30,
            data_storage_setting="everything",
            denoising_mode="noise-cancellation",
            enable_backchannel=True,
            enable_dynamic_responsiveness=True,
            enable_dynamic_voice_speed=True,
            enable_expressive_mode=True,
            end_call_after_silence_ms=600000,
            expressive_emotion_tags=["empathetic", "excited", "sigh", "clear throat", "emphasis"],
            expressive_mode_prompt="Use [sigh] for thoughtful pauses and [excited] for good news.",
            fallback_voice_ids=["cartesia-Cimo", "minimax-Cimo"],
            guardrail_config={
                "input_topics": ["platform_integrity_jailbreaking"],
                "output_topics": ["harassment"],
            },
            handbook_config={
                "ai_disclosure": True,
                "conversational_personality": True,
                "default_personality": True,
                "echo_verification": True,
                "high_empathy": True,
                "nato_phonetic_alphabet": True,
                "natural_filler_words": True,
                "scope_boundaries": True,
                "smart_matching": True,
                "speech_normalization": True,
            },
            interruption_sensitivity=1,
            ivr_option={
                "action": {"type": "hangup"},
                "detection_prompt": "detection_prompt",
            },
            language="en-US",
            max_call_duration_ms=3600000,
            opt_in_signed_url=True,
            pii_config={
                "categories": ["person_name"],
                "mode": "post_call",
            },
            post_call_analysis_data=[
                {
                    "description": "The name of the customer.",
                    "name": "customer_name",
                    "type": "string",
                    "conditional_prompt": "conditional_prompt",
                    "examples": ["John Doe", "Jane Smith"],
                    "required": True,
                }
            ],
            post_call_analysis_model="gpt-4.1-mini",
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
                "version": 0,
            },
            responsiveness=1,
            ring_duration_ms=30000,
            signed_url_expiration_ms=86400000,
            stt_mode="fast",
            timezone="America/New_York",
            user_dtmf_options={
                "digit_limit": 1,
                "termination_key": "#",
                "timeout_ms": 1000,
            },
            version_description="Customer support agent for handling product inquiries",
            version_title="Production hotfix",
            vocab_specialization="general",
            voice_emotion="calm",
            voice_id="retell-Cimo",
            voice_model="eleven_turbo_v2",
            voice_speed=1,
            voice_temperature=1,
            voicemail_option={
                "action": {
                    "text": "Please give us a callback tomorrow at 10am.",
                    "type": "static_text",
                },
                "detection_prompt": "detection_prompt",
            },
            volume=1,
            webhook_events=["call_started"],
            webhook_timeout_ms=10000,
            webhook_url="https://webhook-url-here",
        )
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.update(
            agent_id="16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.update(
                agent_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        with pytest.warns(DeprecationWarning):
            agent = await async_client.agent.list()

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        with pytest.warns(DeprecationWarning):
            agent = await async_client.agent.list(
                is_latest=True,
                limit=50,
                pagination_key="agent_1ffdb9717444d0e77346838911",
                pagination_key_version=0,
            )

        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.agent.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentListResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.agent.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                agent = await response.parse()
                assert_matches_type(AgentListResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.delete(
            "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_version(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.create_version(
            agent_id="agent_xxx",
            base_version=12,
        )
        assert_matches_type(AgentCreateVersionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_version(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.create_version(
            agent_id="agent_xxx",
            base_version=12,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateVersionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_version(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.create_version(
            agent_id="agent_xxx",
            base_version=12,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateVersionResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_version(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.create_version(
                agent_id="",
                base_version=12,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_version(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.delete_version(
            agent_id="agent_xxx",
            version=1,
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_version(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.delete_version(
            agent_id="agent_xxx",
            version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_version(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.delete_version(
            agent_id="agent_xxx",
            version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_version(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.delete_version(
                agent_id="",
                version=1,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_versions(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.get_versions(
            "16b980523634a6dc504898cda492e939",
        )
        assert_matches_type(AgentGetVersionsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_versions(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentGetVersionsResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_versions(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.get_versions(
            "16b980523634a6dc504898cda492e939",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentGetVersionsResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_versions(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.get_versions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.publish(
            agent_id="agent_xxx",
            version=15,
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncRetell) -> None:
        agent = await async_client.agent.publish(
            agent_id="agent_xxx",
            version=15,
            version_description="Hotfix for transfer timeout",
            version_title="Hotfix",
        )
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncRetell) -> None:
        response = await async_client.agent.with_raw_response.publish(
            agent_id="agent_xxx",
            version=15,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncRetell) -> None:
        async with async_client.agent.with_streaming_response.publish(
            agent_id="agent_xxx",
            version=15,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agent.with_raw_response.publish(
                agent_id="",
                version=15,
            )
