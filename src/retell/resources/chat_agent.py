# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    chat_agent_list_params,
    chat_agent_create_params,
    chat_agent_update_params,
    chat_agent_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.chat_agent_response import ChatAgentResponse
from ..types.chat_agent_list_response import ChatAgentListResponse
from ..types.chat_agent_get_versions_response import ChatAgentGetVersionsResponse

__all__ = ["ChatAgentResource", "AsyncChatAgentResource"]


class ChatAgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChatAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ChatAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ChatAgentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        response_engine: chat_agent_create_params.ResponseEngine,
        agent_name: Optional[str] | Omit = omit,
        analysis_successful_prompt: Optional[str] | Omit = omit,
        analysis_summary_prompt: Optional[str] | Omit = omit,
        auto_close_message: Optional[str] | Omit = omit,
        data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]]
        | Omit = omit,
        end_chat_after_silence_ms: int | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        language: Literal[
            "en-US",
            "en-IN",
            "en-GB",
            "en-AU",
            "en-NZ",
            "de-DE",
            "es-ES",
            "es-419",
            "hi-IN",
            "fr-FR",
            "fr-CA",
            "ja-JP",
            "pt-PT",
            "pt-BR",
            "zh-CN",
            "ru-RU",
            "it-IT",
            "ko-KR",
            "nl-NL",
            "nl-BE",
            "pl-PL",
            "tr-TR",
            "th-TH",
            "vi-VN",
            "ro-RO",
            "bg-BG",
            "ca-ES",
            "da-DK",
            "fi-FI",
            "el-GR",
            "hu-HU",
            "id-ID",
            "no-NO",
            "sk-SK",
            "sv-SE",
            "lt-LT",
            "lv-LV",
            "multi",
        ]
        | Omit = omit,
        opt_in_signed_url: bool | Omit = omit,
        pii_config: chat_agent_create_params.PiiConfig | Omit = omit,
        post_chat_analysis_data: Optional[Iterable[chat_agent_create_params.PostChatAnalysisData]] | Omit = omit,
        post_chat_analysis_model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-4.1-nano",
                "gpt-5",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5-mini",
                "gpt-5-nano",
                "claude-4.5-sonnet",
                "claude-4.5-haiku",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-3.0-flash",
            ]
        ]
        | Omit = omit,
        signed_url_expiration_ms: Optional[int] | Omit = omit,
        webhook_timeout_ms: int | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentResponse:
        """
        Create a new chat agent

        Args:
          response_engine: The Response Engine to attach to the agent. It is used to generate responses for
              the agent. You need to create a Response Engine first before attaching it to an
              agent.

          agent_name: The name of the chat agent. Only used for your own reference.

          analysis_successful_prompt: The prompt to use for post call analysis to evaluate whether the call is
              successful. Set to null to use the default prompt.

          analysis_summary_prompt: The prompt to use for post call analysis to summarize the call. Set to null to
              use the default prompt.

          auto_close_message: Message to display when the chat is automatically closed.

          data_storage_setting: Controls what data is stored for this agent. "everything" stores all data
              including transcripts and recordings. "everything_except_pii" stores data but
              excludes PII when possible based on PII configuration. "basic_attributes_only"
              stores only basic metadata. If not set, defaults to "everything".

          end_chat_after_silence_ms: If users stay silent for a period after agent speech, end the chat. The minimum
              value allowed is 360,000 ms (0.1 hours). The maximum value allowed is
              259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).

          is_public: Whether the agent is public. When set to true, the agent is available for public
              agent preview link.

          language: Specifies what language (and dialect) the chat will operate in. For instance,
              selecting `en-GB` optimizes for British English. If unset, will use default
              value `en-US`. Select `multi` for multilingual support, currently this supports
              Spanish and English.

          opt_in_signed_url: Whether this agent opts in to signed url for public log. If not set, default
              value of false will apply.

          pii_config: Configuration for PII scrubbing from transcripts and recordings.

          post_chat_analysis_data: Post chat analysis data to extract from the chat. This data will augment the
              pre-defined variables extracted in the chat analysis. This will be available
              after the chat ends.

          post_chat_analysis_model: The model to use for post chat analysis. Default to gpt-4.1-mini.

          signed_url_expiration_ms: The expiration time for the signed url in milliseconds. Only applicable when
              opt_in_signed_url is true. If not set, default value of 86400000 (24 hours) will
              apply.

          webhook_timeout_ms: The timeout for the webhook in milliseconds. If not set, default value of 10000
              will apply.

          webhook_url: The webhook for agent to listen to chat events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-chat-agent",
            body=maybe_transform(
                {
                    "response_engine": response_engine,
                    "agent_name": agent_name,
                    "analysis_successful_prompt": analysis_successful_prompt,
                    "analysis_summary_prompt": analysis_summary_prompt,
                    "auto_close_message": auto_close_message,
                    "data_storage_setting": data_storage_setting,
                    "end_chat_after_silence_ms": end_chat_after_silence_ms,
                    "is_public": is_public,
                    "language": language,
                    "opt_in_signed_url": opt_in_signed_url,
                    "pii_config": pii_config,
                    "post_chat_analysis_data": post_chat_analysis_data,
                    "post_chat_analysis_model": post_chat_analysis_model,
                    "signed_url_expiration_ms": signed_url_expiration_ms,
                    "webhook_timeout_ms": webhook_timeout_ms,
                    "webhook_url": webhook_url,
                },
                chat_agent_create_params.ChatAgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAgentResponse,
        )

    def retrieve(
        self,
        agent_id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentResponse:
        """
        Retrieve details of a specific chat agent

        Args:
          version: Optional version of the API to use for this request. If not provided, will
              default to latest version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/get-chat-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, chat_agent_retrieve_params.ChatAgentRetrieveParams),
            ),
            cast_to=ChatAgentResponse,
        )

    def update(
        self,
        agent_id: str,
        *,
        version: int | Omit = omit,
        agent_name: Optional[str] | Omit = omit,
        analysis_successful_prompt: Optional[str] | Omit = omit,
        analysis_summary_prompt: Optional[str] | Omit = omit,
        auto_close_message: Optional[str] | Omit = omit,
        data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]]
        | Omit = omit,
        end_chat_after_silence_ms: int | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        language: Literal[
            "en-US",
            "en-IN",
            "en-GB",
            "en-AU",
            "en-NZ",
            "de-DE",
            "es-ES",
            "es-419",
            "hi-IN",
            "fr-FR",
            "fr-CA",
            "ja-JP",
            "pt-PT",
            "pt-BR",
            "zh-CN",
            "ru-RU",
            "it-IT",
            "ko-KR",
            "nl-NL",
            "nl-BE",
            "pl-PL",
            "tr-TR",
            "th-TH",
            "vi-VN",
            "ro-RO",
            "bg-BG",
            "ca-ES",
            "da-DK",
            "fi-FI",
            "el-GR",
            "hu-HU",
            "id-ID",
            "no-NO",
            "sk-SK",
            "sv-SE",
            "lt-LT",
            "lv-LV",
            "multi",
        ]
        | Omit = omit,
        opt_in_signed_url: bool | Omit = omit,
        pii_config: chat_agent_update_params.PiiConfig | Omit = omit,
        post_chat_analysis_data: Optional[Iterable[chat_agent_update_params.PostChatAnalysisData]] | Omit = omit,
        post_chat_analysis_model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-4.1-nano",
                "gpt-5",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5-mini",
                "gpt-5-nano",
                "claude-4.5-sonnet",
                "claude-4.5-haiku",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-3.0-flash",
            ]
        ]
        | Omit = omit,
        response_engine: chat_agent_update_params.ResponseEngine | Omit = omit,
        signed_url_expiration_ms: Optional[int] | Omit = omit,
        webhook_timeout_ms: int | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentResponse:
        """
        Update an existing chat agent

        Args:
          version: Optional version of the API to use for this request. Default to latest version.

          agent_name: The name of the chat agent. Only used for your own reference.

          analysis_successful_prompt: The prompt to use for post call analysis to evaluate whether the call is
              successful. Set to null to use the default prompt.

          analysis_summary_prompt: The prompt to use for post call analysis to summarize the call. Set to null to
              use the default prompt.

          auto_close_message: Message to display when the chat is automatically closed.

          data_storage_setting: Controls what data is stored for this agent. "everything" stores all data
              including transcripts and recordings. "everything_except_pii" stores data but
              excludes PII when possible based on PII configuration. "basic_attributes_only"
              stores only basic metadata. If not set, defaults to "everything".

          end_chat_after_silence_ms: If users stay silent for a period after agent speech, end the chat. The minimum
              value allowed is 360,000 ms (0.1 hours). The maximum value allowed is
              259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).

          is_public: Whether the agent is public. When set to true, the agent is available for public
              agent preview link.

          language: Specifies what language (and dialect) the chat will operate in. For instance,
              selecting `en-GB` optimizes for British English. If unset, will use default
              value `en-US`. Select `multi` for multilingual support, currently this supports
              Spanish and English.

          opt_in_signed_url: Whether this agent opts in to signed url for public log. If not set, default
              value of false will apply.

          pii_config: Configuration for PII scrubbing from transcripts and recordings.

          post_chat_analysis_data: Post chat analysis data to extract from the chat. This data will augment the
              pre-defined variables extracted in the chat analysis. This will be available
              after the chat ends.

          post_chat_analysis_model: The model to use for post chat analysis. Default to gpt-4.1-mini.

          response_engine: The Response Engine to attach to the agent. It is used to generate responses for
              the agent. You need to create a Response Engine first before attaching it to an
              agent.

          signed_url_expiration_ms: The expiration time for the signed url in milliseconds. Only applicable when
              opt_in_signed_url is true. If not set, default value of 86400000 (24 hours) will
              apply.

          webhook_timeout_ms: The timeout for the webhook in milliseconds. If not set, default value of 10000
              will apply.

          webhook_url: The webhook for agent to listen to chat events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._patch(
            f"/update-chat-agent/{agent_id}",
            body=maybe_transform(
                {
                    "agent_name": agent_name,
                    "analysis_successful_prompt": analysis_successful_prompt,
                    "analysis_summary_prompt": analysis_summary_prompt,
                    "auto_close_message": auto_close_message,
                    "data_storage_setting": data_storage_setting,
                    "end_chat_after_silence_ms": end_chat_after_silence_ms,
                    "is_public": is_public,
                    "language": language,
                    "opt_in_signed_url": opt_in_signed_url,
                    "pii_config": pii_config,
                    "post_chat_analysis_data": post_chat_analysis_data,
                    "post_chat_analysis_model": post_chat_analysis_model,
                    "response_engine": response_engine,
                    "signed_url_expiration_ms": signed_url_expiration_ms,
                    "webhook_timeout_ms": webhook_timeout_ms,
                    "webhook_url": webhook_url,
                },
                chat_agent_update_params.ChatAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"version": version}, chat_agent_update_params.ChatAgentUpdateParams),
            ),
            cast_to=ChatAgentResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        pagination_key_version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentListResponse:
        """
        List all chat agents

        Args:
          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              1000, and the default is 1000.

          pagination_key: The pagination key to continue fetching the next page of agents. Pagination key
              is represented by a agent id, pagination key and version pair is exclusive (not
              included in the fetched page). If not set, will start from the beginning.

          pagination_key_version: Specifies the version of the agent associated with the pagination_key. When
              paginating, both the pagination_key and its version must be provided to ensure
              consistent ordering and to fetch the next page correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/list-chat-agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "pagination_key_version": pagination_key_version,
                    },
                    chat_agent_list_params.ChatAgentListParams,
                ),
            ),
            cast_to=ChatAgentListResponse,
        )

    def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing chat agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-chat-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_versions(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentGetVersionsResponse:
        """
        Get all versions of a chat agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/get-chat-agent-versions/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAgentGetVersionsResponse,
        )

    def publish(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Publish the latest version of the chat agent and create a new draft chat agent
        with newer version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/publish-chat-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncChatAgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChatAgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncChatAgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatAgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncChatAgentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        response_engine: chat_agent_create_params.ResponseEngine,
        agent_name: Optional[str] | Omit = omit,
        analysis_successful_prompt: Optional[str] | Omit = omit,
        analysis_summary_prompt: Optional[str] | Omit = omit,
        auto_close_message: Optional[str] | Omit = omit,
        data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]]
        | Omit = omit,
        end_chat_after_silence_ms: int | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        language: Literal[
            "en-US",
            "en-IN",
            "en-GB",
            "en-AU",
            "en-NZ",
            "de-DE",
            "es-ES",
            "es-419",
            "hi-IN",
            "fr-FR",
            "fr-CA",
            "ja-JP",
            "pt-PT",
            "pt-BR",
            "zh-CN",
            "ru-RU",
            "it-IT",
            "ko-KR",
            "nl-NL",
            "nl-BE",
            "pl-PL",
            "tr-TR",
            "th-TH",
            "vi-VN",
            "ro-RO",
            "bg-BG",
            "ca-ES",
            "da-DK",
            "fi-FI",
            "el-GR",
            "hu-HU",
            "id-ID",
            "no-NO",
            "sk-SK",
            "sv-SE",
            "lt-LT",
            "lv-LV",
            "multi",
        ]
        | Omit = omit,
        opt_in_signed_url: bool | Omit = omit,
        pii_config: chat_agent_create_params.PiiConfig | Omit = omit,
        post_chat_analysis_data: Optional[Iterable[chat_agent_create_params.PostChatAnalysisData]] | Omit = omit,
        post_chat_analysis_model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-4.1-nano",
                "gpt-5",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5-mini",
                "gpt-5-nano",
                "claude-4.5-sonnet",
                "claude-4.5-haiku",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-3.0-flash",
            ]
        ]
        | Omit = omit,
        signed_url_expiration_ms: Optional[int] | Omit = omit,
        webhook_timeout_ms: int | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentResponse:
        """
        Create a new chat agent

        Args:
          response_engine: The Response Engine to attach to the agent. It is used to generate responses for
              the agent. You need to create a Response Engine first before attaching it to an
              agent.

          agent_name: The name of the chat agent. Only used for your own reference.

          analysis_successful_prompt: The prompt to use for post call analysis to evaluate whether the call is
              successful. Set to null to use the default prompt.

          analysis_summary_prompt: The prompt to use for post call analysis to summarize the call. Set to null to
              use the default prompt.

          auto_close_message: Message to display when the chat is automatically closed.

          data_storage_setting: Controls what data is stored for this agent. "everything" stores all data
              including transcripts and recordings. "everything_except_pii" stores data but
              excludes PII when possible based on PII configuration. "basic_attributes_only"
              stores only basic metadata. If not set, defaults to "everything".

          end_chat_after_silence_ms: If users stay silent for a period after agent speech, end the chat. The minimum
              value allowed is 360,000 ms (0.1 hours). The maximum value allowed is
              259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).

          is_public: Whether the agent is public. When set to true, the agent is available for public
              agent preview link.

          language: Specifies what language (and dialect) the chat will operate in. For instance,
              selecting `en-GB` optimizes for British English. If unset, will use default
              value `en-US`. Select `multi` for multilingual support, currently this supports
              Spanish and English.

          opt_in_signed_url: Whether this agent opts in to signed url for public log. If not set, default
              value of false will apply.

          pii_config: Configuration for PII scrubbing from transcripts and recordings.

          post_chat_analysis_data: Post chat analysis data to extract from the chat. This data will augment the
              pre-defined variables extracted in the chat analysis. This will be available
              after the chat ends.

          post_chat_analysis_model: The model to use for post chat analysis. Default to gpt-4.1-mini.

          signed_url_expiration_ms: The expiration time for the signed url in milliseconds. Only applicable when
              opt_in_signed_url is true. If not set, default value of 86400000 (24 hours) will
              apply.

          webhook_timeout_ms: The timeout for the webhook in milliseconds. If not set, default value of 10000
              will apply.

          webhook_url: The webhook for agent to listen to chat events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-chat-agent",
            body=await async_maybe_transform(
                {
                    "response_engine": response_engine,
                    "agent_name": agent_name,
                    "analysis_successful_prompt": analysis_successful_prompt,
                    "analysis_summary_prompt": analysis_summary_prompt,
                    "auto_close_message": auto_close_message,
                    "data_storage_setting": data_storage_setting,
                    "end_chat_after_silence_ms": end_chat_after_silence_ms,
                    "is_public": is_public,
                    "language": language,
                    "opt_in_signed_url": opt_in_signed_url,
                    "pii_config": pii_config,
                    "post_chat_analysis_data": post_chat_analysis_data,
                    "post_chat_analysis_model": post_chat_analysis_model,
                    "signed_url_expiration_ms": signed_url_expiration_ms,
                    "webhook_timeout_ms": webhook_timeout_ms,
                    "webhook_url": webhook_url,
                },
                chat_agent_create_params.ChatAgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAgentResponse,
        )

    async def retrieve(
        self,
        agent_id: str,
        *,
        version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentResponse:
        """
        Retrieve details of a specific chat agent

        Args:
          version: Optional version of the API to use for this request. If not provided, will
              default to latest version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/get-chat-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"version": version}, chat_agent_retrieve_params.ChatAgentRetrieveParams
                ),
            ),
            cast_to=ChatAgentResponse,
        )

    async def update(
        self,
        agent_id: str,
        *,
        version: int | Omit = omit,
        agent_name: Optional[str] | Omit = omit,
        analysis_successful_prompt: Optional[str] | Omit = omit,
        analysis_summary_prompt: Optional[str] | Omit = omit,
        auto_close_message: Optional[str] | Omit = omit,
        data_storage_setting: Optional[Literal["everything", "everything_except_pii", "basic_attributes_only"]]
        | Omit = omit,
        end_chat_after_silence_ms: int | Omit = omit,
        is_public: Optional[bool] | Omit = omit,
        language: Literal[
            "en-US",
            "en-IN",
            "en-GB",
            "en-AU",
            "en-NZ",
            "de-DE",
            "es-ES",
            "es-419",
            "hi-IN",
            "fr-FR",
            "fr-CA",
            "ja-JP",
            "pt-PT",
            "pt-BR",
            "zh-CN",
            "ru-RU",
            "it-IT",
            "ko-KR",
            "nl-NL",
            "nl-BE",
            "pl-PL",
            "tr-TR",
            "th-TH",
            "vi-VN",
            "ro-RO",
            "bg-BG",
            "ca-ES",
            "da-DK",
            "fi-FI",
            "el-GR",
            "hu-HU",
            "id-ID",
            "no-NO",
            "sk-SK",
            "sv-SE",
            "lt-LT",
            "lv-LV",
            "multi",
        ]
        | Omit = omit,
        opt_in_signed_url: bool | Omit = omit,
        pii_config: chat_agent_update_params.PiiConfig | Omit = omit,
        post_chat_analysis_data: Optional[Iterable[chat_agent_update_params.PostChatAnalysisData]] | Omit = omit,
        post_chat_analysis_model: Optional[
            Literal[
                "gpt-4.1",
                "gpt-4.1-mini",
                "gpt-4.1-nano",
                "gpt-5",
                "gpt-5.1",
                "gpt-5.2",
                "gpt-5-mini",
                "gpt-5-nano",
                "claude-4.5-sonnet",
                "claude-4.5-haiku",
                "gemini-2.5-flash",
                "gemini-2.5-flash-lite",
                "gemini-3.0-flash",
            ]
        ]
        | Omit = omit,
        response_engine: chat_agent_update_params.ResponseEngine | Omit = omit,
        signed_url_expiration_ms: Optional[int] | Omit = omit,
        webhook_timeout_ms: int | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentResponse:
        """
        Update an existing chat agent

        Args:
          version: Optional version of the API to use for this request. Default to latest version.

          agent_name: The name of the chat agent. Only used for your own reference.

          analysis_successful_prompt: The prompt to use for post call analysis to evaluate whether the call is
              successful. Set to null to use the default prompt.

          analysis_summary_prompt: The prompt to use for post call analysis to summarize the call. Set to null to
              use the default prompt.

          auto_close_message: Message to display when the chat is automatically closed.

          data_storage_setting: Controls what data is stored for this agent. "everything" stores all data
              including transcripts and recordings. "everything_except_pii" stores data but
              excludes PII when possible based on PII configuration. "basic_attributes_only"
              stores only basic metadata. If not set, defaults to "everything".

          end_chat_after_silence_ms: If users stay silent for a period after agent speech, end the chat. The minimum
              value allowed is 360,000 ms (0.1 hours). The maximum value allowed is
              259,200,000 ms (72 hours). By default, this is set to 3,600,000 (1 hour).

          is_public: Whether the agent is public. When set to true, the agent is available for public
              agent preview link.

          language: Specifies what language (and dialect) the chat will operate in. For instance,
              selecting `en-GB` optimizes for British English. If unset, will use default
              value `en-US`. Select `multi` for multilingual support, currently this supports
              Spanish and English.

          opt_in_signed_url: Whether this agent opts in to signed url for public log. If not set, default
              value of false will apply.

          pii_config: Configuration for PII scrubbing from transcripts and recordings.

          post_chat_analysis_data: Post chat analysis data to extract from the chat. This data will augment the
              pre-defined variables extracted in the chat analysis. This will be available
              after the chat ends.

          post_chat_analysis_model: The model to use for post chat analysis. Default to gpt-4.1-mini.

          response_engine: The Response Engine to attach to the agent. It is used to generate responses for
              the agent. You need to create a Response Engine first before attaching it to an
              agent.

          signed_url_expiration_ms: The expiration time for the signed url in milliseconds. Only applicable when
              opt_in_signed_url is true. If not set, default value of 86400000 (24 hours) will
              apply.

          webhook_timeout_ms: The timeout for the webhook in milliseconds. If not set, default value of 10000
              will apply.

          webhook_url: The webhook for agent to listen to chat events. See what events it would get at
              [webhook doc](/features/webhook). If set, will binds webhook events for this
              agent to the specified url, and will ignore the account level webhook for this
              agent. Set to `null` to remove webhook url from this agent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._patch(
            f"/update-chat-agent/{agent_id}",
            body=await async_maybe_transform(
                {
                    "agent_name": agent_name,
                    "analysis_successful_prompt": analysis_successful_prompt,
                    "analysis_summary_prompt": analysis_summary_prompt,
                    "auto_close_message": auto_close_message,
                    "data_storage_setting": data_storage_setting,
                    "end_chat_after_silence_ms": end_chat_after_silence_ms,
                    "is_public": is_public,
                    "language": language,
                    "opt_in_signed_url": opt_in_signed_url,
                    "pii_config": pii_config,
                    "post_chat_analysis_data": post_chat_analysis_data,
                    "post_chat_analysis_model": post_chat_analysis_model,
                    "response_engine": response_engine,
                    "signed_url_expiration_ms": signed_url_expiration_ms,
                    "webhook_timeout_ms": webhook_timeout_ms,
                    "webhook_url": webhook_url,
                },
                chat_agent_update_params.ChatAgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"version": version}, chat_agent_update_params.ChatAgentUpdateParams),
            ),
            cast_to=ChatAgentResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        pagination_key_version: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentListResponse:
        """
        List all chat agents

        Args:
          limit: A limit on the number of objects to be returned. Limit can range between 1 and
              1000, and the default is 1000.

          pagination_key: The pagination key to continue fetching the next page of agents. Pagination key
              is represented by a agent id, pagination key and version pair is exclusive (not
              included in the fetched page). If not set, will start from the beginning.

          pagination_key_version: Specifies the version of the agent associated with the pagination_key. When
              paginating, both the pagination_key and its version must be provided to ensure
              consistent ordering and to fetch the next page correctly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/list-chat-agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "pagination_key_version": pagination_key_version,
                    },
                    chat_agent_list_params.ChatAgentListParams,
                ),
            ),
            cast_to=ChatAgentListResponse,
        )

    async def delete(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an existing chat agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-chat-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_versions(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ChatAgentGetVersionsResponse:
        """
        Get all versions of a chat agent

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/get-chat-agent-versions/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatAgentGetVersionsResponse,
        )

    async def publish(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Publish the latest version of the chat agent and create a new draft chat agent
        with newer version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/publish-chat-agent/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ChatAgentResourceWithRawResponse:
    def __init__(self, chat_agent: ChatAgentResource) -> None:
        self._chat_agent = chat_agent

        self.create = to_raw_response_wrapper(
            chat_agent.create,
        )
        self.retrieve = to_raw_response_wrapper(
            chat_agent.retrieve,
        )
        self.update = to_raw_response_wrapper(
            chat_agent.update,
        )
        self.list = to_raw_response_wrapper(
            chat_agent.list,
        )
        self.delete = to_raw_response_wrapper(
            chat_agent.delete,
        )
        self.get_versions = to_raw_response_wrapper(
            chat_agent.get_versions,
        )
        self.publish = to_raw_response_wrapper(
            chat_agent.publish,
        )


class AsyncChatAgentResourceWithRawResponse:
    def __init__(self, chat_agent: AsyncChatAgentResource) -> None:
        self._chat_agent = chat_agent

        self.create = async_to_raw_response_wrapper(
            chat_agent.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            chat_agent.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            chat_agent.update,
        )
        self.list = async_to_raw_response_wrapper(
            chat_agent.list,
        )
        self.delete = async_to_raw_response_wrapper(
            chat_agent.delete,
        )
        self.get_versions = async_to_raw_response_wrapper(
            chat_agent.get_versions,
        )
        self.publish = async_to_raw_response_wrapper(
            chat_agent.publish,
        )


class ChatAgentResourceWithStreamingResponse:
    def __init__(self, chat_agent: ChatAgentResource) -> None:
        self._chat_agent = chat_agent

        self.create = to_streamed_response_wrapper(
            chat_agent.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            chat_agent.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            chat_agent.update,
        )
        self.list = to_streamed_response_wrapper(
            chat_agent.list,
        )
        self.delete = to_streamed_response_wrapper(
            chat_agent.delete,
        )
        self.get_versions = to_streamed_response_wrapper(
            chat_agent.get_versions,
        )
        self.publish = to_streamed_response_wrapper(
            chat_agent.publish,
        )


class AsyncChatAgentResourceWithStreamingResponse:
    def __init__(self, chat_agent: AsyncChatAgentResource) -> None:
        self._chat_agent = chat_agent

        self.create = async_to_streamed_response_wrapper(
            chat_agent.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            chat_agent.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            chat_agent.update,
        )
        self.list = async_to_streamed_response_wrapper(
            chat_agent.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            chat_agent.delete,
        )
        self.get_versions = async_to_streamed_response_wrapper(
            chat_agent.get_versions,
        )
        self.publish = async_to_streamed_response_wrapper(
            chat_agent.publish,
        )
