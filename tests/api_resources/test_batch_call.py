# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import BatchCallResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatchCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch_call(self, client: Retell) -> None:
        batch_call = client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch_call_with_all_params(self, client: Retell) -> None:
        batch_call = client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[
                {
                    "to_number": "+12137774445",
                    "agent_override": {
                        "agent": {
                            "agent_name": "Jarvis",
                            "allow_user_dtmf": True,
                            "ambient_sound": "coffee-shop",
                            "ambient_sound_volume": 1,
                            "analysis_successful_prompt": "The agent finished the task and the call was complete without being cutoff.",
                            "analysis_summary_prompt": "Summarize the outcome of the conversation in two sentences.",
                            "backchannel_frequency": 0.9,
                            "backchannel_words": ["yeah", "uh-huh"],
                            "begin_message_delay_ms": 1000,
                            "boosted_keywords": ["retell", "kroger"],
                            "custom_stt_config": {
                                "endpointing_ms": 0,
                                "provider": "azure",
                            },
                            "data_storage_setting": "everything",
                            "denoising_mode": "noise-cancellation",
                            "enable_backchannel": True,
                            "enable_voicemail_detection": True,
                            "end_call_after_silence_ms": 600000,
                            "fallback_voice_ids": ["openai-Alloy", "deepgram-Angus"],
                            "interruption_sensitivity": 1,
                            "is_public": False,
                            "language": "en-US",
                            "max_call_duration_ms": 3600000,
                            "normalize_for_speech": True,
                            "opt_in_signed_url": True,
                            "pii_config": {
                                "categories": ["person_name"],
                                "mode": "post_call",
                            },
                            "post_call_analysis_data": [
                                {
                                    "description": "The name of the customer.",
                                    "name": "customer_name",
                                    "type": "string",
                                    "examples": ["John Doe", "Jane Smith"],
                                }
                            ],
                            "post_call_analysis_model": "gpt-4.1-mini",
                            "pronunciation_dictionary": [
                                {
                                    "alphabet": "ipa",
                                    "phoneme": "ˈæktʃuəli",
                                    "word": "actually",
                                }
                            ],
                            "reminder_max_count": 2,
                            "reminder_trigger_ms": 10000,
                            "response_engine": {
                                "llm_id": "llm_234sdertfsdsfsdf",
                                "type": "retell-llm",
                                "version": 0,
                            },
                            "responsiveness": 1,
                            "ring_duration_ms": 30000,
                            "signed_url_expiration_ms": 86400000,
                            "stt_mode": "fast",
                            "user_dtmf_options": {
                                "digit_limit": 1,
                                "termination_key": "#",
                                "timeout_ms": 1000,
                            },
                            "version_description": "Customer support agent for handling product inquiries",
                            "vocab_specialization": "general",
                            "voice_id": "11labs-Adrian",
                            "voice_model": "eleven_turbo_v2",
                            "voice_speed": 1,
                            "voice_temperature": 1,
                            "voicemail_detection_timeout_ms": 30000,
                            "voicemail_message": "Hi, please give us a callback.",
                            "voicemail_option": {
                                "action": {
                                    "text": "Please give us a callback tomorrow at 10am.",
                                    "type": "static_text",
                                }
                            },
                            "volume": 1,
                            "webhook_timeout_ms": 10000,
                            "webhook_url": "https://webhook-url-here",
                        },
                        "conversation_flow": {
                            "begin_after_user_silence_ms": 2000,
                            "kb_config": {
                                "filter_score": 0.6,
                                "top_k": 3,
                            },
                            "knowledge_base_ids": ["kb_001", "kb_002"],
                            "model_choice": {
                                "model": "gpt-4.1",
                                "type": "cascading",
                                "high_priority": True,
                            },
                            "model_temperature": 0.7,
                            "start_speaker": "agent",
                            "tool_call_strict_mode": True,
                        },
                        "retell_llm": {
                            "begin_after_user_silence_ms": 2000,
                            "begin_message": "Hey I am a virtual assistant calling from Retell Hospital.",
                            "kb_config": {
                                "filter_score": 0.6,
                                "top_k": 3,
                            },
                            "knowledge_base_ids": ["string"],
                            "model": "gpt-4.1",
                            "model_high_priority": True,
                            "model_temperature": 0,
                            "s2s_model": "gpt-4o-realtime",
                            "start_speaker": "user",
                            "tool_call_strict_mode": True,
                        },
                    },
                    "ignore_e164_validation": False,
                    "metadata": {},
                    "override_agent_id": "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
                    "override_agent_version": 1,
                    "retell_llm_dynamic_variables": {"customer_name": "bar"},
                }
            ],
            call_time_window={
                "windows": [
                    {
                        "end": 1020,
                        "start": 540,
                    }
                ],
                "day": ["Monday"],
                "timezone": "timezone",
            },
            name="First batch call",
            reserved_concurrency=0,
            trigger_timestamp=1735718400000,
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch_call(self, client: Retell) -> None:
        response = client.batch_call.with_raw_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_call = response.parse()
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch_call(self, client: Retell) -> None:
        with client.batch_call.with_streaming_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_call = response.parse()
            assert_matches_type(BatchCallResponse, batch_call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatchCall:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch_call(self, async_client: AsyncRetell) -> None:
        batch_call = await async_client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch_call_with_all_params(self, async_client: AsyncRetell) -> None:
        batch_call = await async_client.batch_call.create_batch_call(
            from_number="+14157774444",
            tasks=[
                {
                    "to_number": "+12137774445",
                    "agent_override": {
                        "agent": {
                            "agent_name": "Jarvis",
                            "allow_user_dtmf": True,
                            "ambient_sound": "coffee-shop",
                            "ambient_sound_volume": 1,
                            "analysis_successful_prompt": "The agent finished the task and the call was complete without being cutoff.",
                            "analysis_summary_prompt": "Summarize the outcome of the conversation in two sentences.",
                            "backchannel_frequency": 0.9,
                            "backchannel_words": ["yeah", "uh-huh"],
                            "begin_message_delay_ms": 1000,
                            "boosted_keywords": ["retell", "kroger"],
                            "custom_stt_config": {
                                "endpointing_ms": 0,
                                "provider": "azure",
                            },
                            "data_storage_setting": "everything",
                            "denoising_mode": "noise-cancellation",
                            "enable_backchannel": True,
                            "enable_voicemail_detection": True,
                            "end_call_after_silence_ms": 600000,
                            "fallback_voice_ids": ["openai-Alloy", "deepgram-Angus"],
                            "interruption_sensitivity": 1,
                            "is_public": False,
                            "language": "en-US",
                            "max_call_duration_ms": 3600000,
                            "normalize_for_speech": True,
                            "opt_in_signed_url": True,
                            "pii_config": {
                                "categories": ["person_name"],
                                "mode": "post_call",
                            },
                            "post_call_analysis_data": [
                                {
                                    "description": "The name of the customer.",
                                    "name": "customer_name",
                                    "type": "string",
                                    "examples": ["John Doe", "Jane Smith"],
                                }
                            ],
                            "post_call_analysis_model": "gpt-4.1-mini",
                            "pronunciation_dictionary": [
                                {
                                    "alphabet": "ipa",
                                    "phoneme": "ˈæktʃuəli",
                                    "word": "actually",
                                }
                            ],
                            "reminder_max_count": 2,
                            "reminder_trigger_ms": 10000,
                            "response_engine": {
                                "llm_id": "llm_234sdertfsdsfsdf",
                                "type": "retell-llm",
                                "version": 0,
                            },
                            "responsiveness": 1,
                            "ring_duration_ms": 30000,
                            "signed_url_expiration_ms": 86400000,
                            "stt_mode": "fast",
                            "user_dtmf_options": {
                                "digit_limit": 1,
                                "termination_key": "#",
                                "timeout_ms": 1000,
                            },
                            "version_description": "Customer support agent for handling product inquiries",
                            "vocab_specialization": "general",
                            "voice_id": "11labs-Adrian",
                            "voice_model": "eleven_turbo_v2",
                            "voice_speed": 1,
                            "voice_temperature": 1,
                            "voicemail_detection_timeout_ms": 30000,
                            "voicemail_message": "Hi, please give us a callback.",
                            "voicemail_option": {
                                "action": {
                                    "text": "Please give us a callback tomorrow at 10am.",
                                    "type": "static_text",
                                }
                            },
                            "volume": 1,
                            "webhook_timeout_ms": 10000,
                            "webhook_url": "https://webhook-url-here",
                        },
                        "conversation_flow": {
                            "begin_after_user_silence_ms": 2000,
                            "kb_config": {
                                "filter_score": 0.6,
                                "top_k": 3,
                            },
                            "knowledge_base_ids": ["kb_001", "kb_002"],
                            "model_choice": {
                                "model": "gpt-4.1",
                                "type": "cascading",
                                "high_priority": True,
                            },
                            "model_temperature": 0.7,
                            "start_speaker": "agent",
                            "tool_call_strict_mode": True,
                        },
                        "retell_llm": {
                            "begin_after_user_silence_ms": 2000,
                            "begin_message": "Hey I am a virtual assistant calling from Retell Hospital.",
                            "kb_config": {
                                "filter_score": 0.6,
                                "top_k": 3,
                            },
                            "knowledge_base_ids": ["string"],
                            "model": "gpt-4.1",
                            "model_high_priority": True,
                            "model_temperature": 0,
                            "s2s_model": "gpt-4o-realtime",
                            "start_speaker": "user",
                            "tool_call_strict_mode": True,
                        },
                    },
                    "ignore_e164_validation": False,
                    "metadata": {},
                    "override_agent_id": "oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
                    "override_agent_version": 1,
                    "retell_llm_dynamic_variables": {"customer_name": "bar"},
                }
            ],
            call_time_window={
                "windows": [
                    {
                        "end": 1020,
                        "start": 540,
                    }
                ],
                "day": ["Monday"],
                "timezone": "timezone",
            },
            name="First batch call",
            reserved_concurrency=0,
            trigger_timestamp=1735718400000,
        )
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.batch_call.with_raw_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch_call = await response.parse()
        assert_matches_type(BatchCallResponse, batch_call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch_call(self, async_client: AsyncRetell) -> None:
        async with async_client.batch_call.with_streaming_response.create_batch_call(
            from_number="+14157774444",
            tasks=[{"to_number": "+12137774445"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch_call = await response.parse()
            assert_matches_type(BatchCallResponse, batch_call, path=["response"])

        assert cast(Any, response.is_closed) is True
