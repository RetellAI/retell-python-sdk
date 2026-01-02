# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    CallResponse,
    WebCallResponse,
    CallListResponse,
    PhoneCallResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCall:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Retell) -> None:
        call = client.call.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Retell) -> None:
        response = client.call.with_raw_response.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Retell) -> None:
        call = client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        call = client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
            custom_attributes={
                "custom_attribute_1": "value1",
                "custom_attribute_2": "value2",
            },
            data_storage_setting="everything_except_pii",
            metadata={
                "customer_id": "cust_123",
                "notes": "Follow-up required",
            },
            override_dynamic_variables={"additional_discount": "15%"},
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.call.with_raw_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.call.with_streaming_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.update(
                call_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        call = client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        call = client.call.list(
            filter_criteria={
                "agent_id": ["agent_oBeDLoLOeuAbiuaMFXRtDOLriT12345"],
                "batch_call_id": ["string"],
                "call_status": ["ended"],
                "call_successful": [True],
                "call_type": ["phone_call"],
                "direction": ["inbound"],
                "disconnection_reason": ["user_hangup"],
                "duration_ms": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "e2e_latency_p50": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "end_timestamp": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "from_number": ["string"],
                "in_voicemail": [True],
                "start_timestamp": {
                    "lower_threshold": 1738475411000,
                    "upper_threshold": 1738475421000,
                },
                "to_number": ["string"],
                "user_sentiment": ["Positive"],
                "version": [0],
            },
            limit=0,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.call.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.call.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        call = client.call.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert call is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.call.with_raw_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert call is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.call.with_streaming_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            client.call.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_phone_call(self, client: Retell) -> None:
        call = client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_phone_call_with_all_params(self, client: Retell) -> None:
        call = client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
            agent_override={
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
            custom_sip_headers={"X-Custom-Header": "Custom Value"},
            ignore_e164_validation=True,
            metadata={},
            override_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            override_agent_version=1,
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_phone_call(self, client: Retell) -> None:
        response = client.call.with_raw_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_phone_call(self, client: Retell) -> None:
        with client.call.with_streaming_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_web_call(self, client: Retell) -> None:
        call = client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_web_call_with_all_params(self, client: Retell) -> None:
        call = client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_override={
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
            agent_version=1,
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_web_call(self, client: Retell) -> None:
        response = client.call.with_raw_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(WebCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_web_call(self, client: Retell) -> None:
        with client.call.with_streaming_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(WebCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_phone_call(self, client: Retell) -> None:
        call = client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_phone_call_with_all_params(self, client: Retell) -> None:
        call = client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_override={
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
            agent_version=1,
            direction="inbound",
            from_number="+14157774444",
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register_phone_call(self, client: Retell) -> None:
        response = client.call.with_raw_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register_phone_call(self, client: Retell) -> None:
        with client.call.with_streaming_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCall:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.retrieve(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.update(
            call_id="call_a4441234567890777c4a4a123e6",
            custom_attributes={
                "custom_attribute_1": "value1",
                "custom_attribute_2": "value2",
            },
            data_storage_setting="everything_except_pii",
            metadata={
                "customer_id": "cust_123",
                "notes": "Follow-up required",
            },
            override_dynamic_variables={"additional_discount": "15%"},
        )
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.update(
            call_id="call_a4441234567890777c4a4a123e6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.update(
                call_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.list()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.list(
            filter_criteria={
                "agent_id": ["agent_oBeDLoLOeuAbiuaMFXRtDOLriT12345"],
                "batch_call_id": ["string"],
                "call_status": ["ended"],
                "call_successful": [True],
                "call_type": ["phone_call"],
                "direction": ["inbound"],
                "disconnection_reason": ["user_hangup"],
                "duration_ms": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "e2e_latency_p50": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "end_timestamp": {
                    "lower_threshold": 0,
                    "upper_threshold": 0,
                },
                "from_number": ["string"],
                "in_voicemail": [True],
                "start_timestamp": {
                    "lower_threshold": 1738475411000,
                    "upper_threshold": 1738475421000,
                },
                "to_number": ["string"],
                "user_sentiment": ["Positive"],
                "version": [0],
            },
            limit=0,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(CallListResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(CallListResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )
        assert call is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert call is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.delete(
            "119c3f8e47135a29e65947eeb34cf12d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert call is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `call_id` but received ''"):
            await async_client.call.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_phone_call(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_phone_call_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
            agent_override={
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
            custom_sip_headers={"X-Custom-Header": "Custom Value"},
            ignore_e164_validation=True,
            metadata={},
            override_agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            override_agent_version=1,
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_phone_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_phone_call(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.create_phone_call(
            from_number="+14157774444",
            to_number="+12137774445",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_web_call(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_web_call_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_override={
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
            agent_version=1,
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
        )
        assert_matches_type(WebCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_web_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(WebCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_web_call(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.create_web_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(WebCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_phone_call(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_phone_call_with_all_params(self, async_client: AsyncRetell) -> None:
        call = await async_client.call.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            agent_override={
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
            agent_version=1,
            direction="inbound",
            from_number="+14157774444",
            metadata={},
            retell_llm_dynamic_variables={"customer_name": "bar"},
            to_number="+12137774445",
        )
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register_phone_call(self, async_client: AsyncRetell) -> None:
        response = await async_client.call.with_raw_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        call = await response.parse()
        assert_matches_type(PhoneCallResponse, call, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register_phone_call(self, async_client: AsyncRetell) -> None:
        async with async_client.call.with_streaming_response.register_phone_call(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            call = await response.parse()
            assert_matches_type(PhoneCallResponse, call, path=["response"])

        assert cast(Any, response.is_closed) is True
