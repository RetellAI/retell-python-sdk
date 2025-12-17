# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .lib.webhook_auth import verify  # type: ignore

if TYPE_CHECKING:
    from .resources import (
        llm,
        call,
        chat,
        agent,
        tests,
        voice,
        mcp_tool,
        batch_call,
        chat_agent,
        concurrency,
        phone_number,
        knowledge_base,
        conversation_flow,
        conversation_flow_component,
    )
    from .resources.llm import LlmResource, AsyncLlmResource
    from .resources.call import CallResource, AsyncCallResource
    from .resources.chat import ChatResource, AsyncChatResource
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.tests import TestsResource, AsyncTestsResource
    from .resources.voice import VoiceResource, AsyncVoiceResource
    from .resources.mcp_tool import McpToolResource, AsyncMcpToolResource
    from .resources.batch_call import BatchCallResource, AsyncBatchCallResource
    from .resources.chat_agent import ChatAgentResource, AsyncChatAgentResource
    from .resources.concurrency import ConcurrencyResource, AsyncConcurrencyResource
    from .resources.phone_number import PhoneNumberResource, AsyncPhoneNumberResource
    from .resources.knowledge_base import KnowledgeBaseResource, AsyncKnowledgeBaseResource
    from .resources.conversation_flow import ConversationFlowResource, AsyncConversationFlowResource
    from .resources.conversation_flow_component import (
        ConversationFlowComponentResource,
        AsyncConversationFlowComponentResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Retell", "AsyncRetell", "Client", "AsyncClient"]


class Retell(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Retell client instance."""
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("RETELL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.retellai.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def call(self) -> CallResource:
        from .resources.call import CallResource

        return CallResource(self)

    @cached_property
    def chat(self) -> ChatResource:
        from .resources.chat import ChatResource

        return ChatResource(self)

    @cached_property
    def phone_number(self) -> PhoneNumberResource:
        from .resources.phone_number import PhoneNumberResource

        return PhoneNumberResource(self)

    @cached_property
    def agent(self) -> AgentResource:
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def chat_agent(self) -> ChatAgentResource:
        from .resources.chat_agent import ChatAgentResource

        return ChatAgentResource(self)

    @cached_property
    def llm(self) -> LlmResource:
        from .resources.llm import LlmResource

        return LlmResource(self)

    @cached_property
    def conversation_flow(self) -> ConversationFlowResource:
        from .resources.conversation_flow import ConversationFlowResource

        return ConversationFlowResource(self)

    @cached_property
    def conversation_flow_component(self) -> ConversationFlowComponentResource:
        from .resources.conversation_flow_component import ConversationFlowComponentResource

        return ConversationFlowComponentResource(self)

    @cached_property
    def knowledge_base(self) -> KnowledgeBaseResource:
        from .resources.knowledge_base import KnowledgeBaseResource

        return KnowledgeBaseResource(self)

    @cached_property
    def voice(self) -> VoiceResource:
        from .resources.voice import VoiceResource

        return VoiceResource(self)

    @cached_property
    def concurrency(self) -> ConcurrencyResource:
        from .resources.concurrency import ConcurrencyResource

        return ConcurrencyResource(self)

    @cached_property
    def batch_call(self) -> BatchCallResource:
        from .resources.batch_call import BatchCallResource

        return BatchCallResource(self)

    @cached_property
    def tests(self) -> TestsResource:
        from .resources.tests import TestsResource

        return TestsResource(self)

    @cached_property
    def mcp_tool(self) -> McpToolResource:
        from .resources.mcp_tool import McpToolResource

        return McpToolResource(self)

    @cached_property
    def with_raw_response(self) -> RetellWithRawResponse:
        return RetellWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetellWithStreamedResponse:
        return RetellWithStreamedResponse(self)

        self.verify = verify  # type: ignore

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncRetell(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncRetell client instance."""
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("RETELL_BASE_URL")
        if base_url is None:
            base_url = f"https://api.retellai.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def call(self) -> AsyncCallResource:
        from .resources.call import AsyncCallResource

        return AsyncCallResource(self)

    @cached_property
    def chat(self) -> AsyncChatResource:
        from .resources.chat import AsyncChatResource

        return AsyncChatResource(self)

    @cached_property
    def phone_number(self) -> AsyncPhoneNumberResource:
        from .resources.phone_number import AsyncPhoneNumberResource

        return AsyncPhoneNumberResource(self)

    @cached_property
    def agent(self) -> AsyncAgentResource:
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def chat_agent(self) -> AsyncChatAgentResource:
        from .resources.chat_agent import AsyncChatAgentResource

        return AsyncChatAgentResource(self)

    @cached_property
    def llm(self) -> AsyncLlmResource:
        from .resources.llm import AsyncLlmResource

        return AsyncLlmResource(self)

    @cached_property
    def conversation_flow(self) -> AsyncConversationFlowResource:
        from .resources.conversation_flow import AsyncConversationFlowResource

        return AsyncConversationFlowResource(self)

    @cached_property
    def conversation_flow_component(self) -> AsyncConversationFlowComponentResource:
        from .resources.conversation_flow_component import AsyncConversationFlowComponentResource

        return AsyncConversationFlowComponentResource(self)

    @cached_property
    def knowledge_base(self) -> AsyncKnowledgeBaseResource:
        from .resources.knowledge_base import AsyncKnowledgeBaseResource

        return AsyncKnowledgeBaseResource(self)

    @cached_property
    def voice(self) -> AsyncVoiceResource:
        from .resources.voice import AsyncVoiceResource

        return AsyncVoiceResource(self)

    @cached_property
    def concurrency(self) -> AsyncConcurrencyResource:
        from .resources.concurrency import AsyncConcurrencyResource

        return AsyncConcurrencyResource(self)

    @cached_property
    def batch_call(self) -> AsyncBatchCallResource:
        from .resources.batch_call import AsyncBatchCallResource

        return AsyncBatchCallResource(self)

    @cached_property
    def tests(self) -> AsyncTestsResource:
        from .resources.tests import AsyncTestsResource

        return AsyncTestsResource(self)

    @cached_property
    def mcp_tool(self) -> AsyncMcpToolResource:
        from .resources.mcp_tool import AsyncMcpToolResource

        return AsyncMcpToolResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncRetellWithRawResponse:
        return AsyncRetellWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetellWithStreamedResponse:
        return AsyncRetellWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="brackets")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class RetellWithRawResponse:
    _client: Retell

    def __init__(self, client: Retell) -> None:
        self._client = client

    @cached_property
    def call(self) -> call.CallResourceWithRawResponse:
        from .resources.call import CallResourceWithRawResponse

        return CallResourceWithRawResponse(self._client.call)

    @cached_property
    def chat(self) -> chat.ChatResourceWithRawResponse:
        from .resources.chat import ChatResourceWithRawResponse

        return ChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def phone_number(self) -> phone_number.PhoneNumberResourceWithRawResponse:
        from .resources.phone_number import PhoneNumberResourceWithRawResponse

        return PhoneNumberResourceWithRawResponse(self._client.phone_number)

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def chat_agent(self) -> chat_agent.ChatAgentResourceWithRawResponse:
        from .resources.chat_agent import ChatAgentResourceWithRawResponse

        return ChatAgentResourceWithRawResponse(self._client.chat_agent)

    @cached_property
    def llm(self) -> llm.LlmResourceWithRawResponse:
        from .resources.llm import LlmResourceWithRawResponse

        return LlmResourceWithRawResponse(self._client.llm)

    @cached_property
    def conversation_flow(self) -> conversation_flow.ConversationFlowResourceWithRawResponse:
        from .resources.conversation_flow import ConversationFlowResourceWithRawResponse

        return ConversationFlowResourceWithRawResponse(self._client.conversation_flow)

    @cached_property
    def conversation_flow_component(
        self,
    ) -> conversation_flow_component.ConversationFlowComponentResourceWithRawResponse:
        from .resources.conversation_flow_component import ConversationFlowComponentResourceWithRawResponse

        return ConversationFlowComponentResourceWithRawResponse(self._client.conversation_flow_component)

    @cached_property
    def knowledge_base(self) -> knowledge_base.KnowledgeBaseResourceWithRawResponse:
        from .resources.knowledge_base import KnowledgeBaseResourceWithRawResponse

        return KnowledgeBaseResourceWithRawResponse(self._client.knowledge_base)

    @cached_property
    def voice(self) -> voice.VoiceResourceWithRawResponse:
        from .resources.voice import VoiceResourceWithRawResponse

        return VoiceResourceWithRawResponse(self._client.voice)

    @cached_property
    def concurrency(self) -> concurrency.ConcurrencyResourceWithRawResponse:
        from .resources.concurrency import ConcurrencyResourceWithRawResponse

        return ConcurrencyResourceWithRawResponse(self._client.concurrency)

    @cached_property
    def batch_call(self) -> batch_call.BatchCallResourceWithRawResponse:
        from .resources.batch_call import BatchCallResourceWithRawResponse

        return BatchCallResourceWithRawResponse(self._client.batch_call)

    @cached_property
    def tests(self) -> tests.TestsResourceWithRawResponse:
        from .resources.tests import TestsResourceWithRawResponse

        return TestsResourceWithRawResponse(self._client.tests)

    @cached_property
    def mcp_tool(self) -> mcp_tool.McpToolResourceWithRawResponse:
        from .resources.mcp_tool import McpToolResourceWithRawResponse

        return McpToolResourceWithRawResponse(self._client.mcp_tool)


class AsyncRetellWithRawResponse:
    _client: AsyncRetell

    def __init__(self, client: AsyncRetell) -> None:
        self._client = client

    @cached_property
    def call(self) -> call.AsyncCallResourceWithRawResponse:
        from .resources.call import AsyncCallResourceWithRawResponse

        return AsyncCallResourceWithRawResponse(self._client.call)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithRawResponse:
        from .resources.chat import AsyncChatResourceWithRawResponse

        return AsyncChatResourceWithRawResponse(self._client.chat)

    @cached_property
    def phone_number(self) -> phone_number.AsyncPhoneNumberResourceWithRawResponse:
        from .resources.phone_number import AsyncPhoneNumberResourceWithRawResponse

        return AsyncPhoneNumberResourceWithRawResponse(self._client.phone_number)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def chat_agent(self) -> chat_agent.AsyncChatAgentResourceWithRawResponse:
        from .resources.chat_agent import AsyncChatAgentResourceWithRawResponse

        return AsyncChatAgentResourceWithRawResponse(self._client.chat_agent)

    @cached_property
    def llm(self) -> llm.AsyncLlmResourceWithRawResponse:
        from .resources.llm import AsyncLlmResourceWithRawResponse

        return AsyncLlmResourceWithRawResponse(self._client.llm)

    @cached_property
    def conversation_flow(self) -> conversation_flow.AsyncConversationFlowResourceWithRawResponse:
        from .resources.conversation_flow import AsyncConversationFlowResourceWithRawResponse

        return AsyncConversationFlowResourceWithRawResponse(self._client.conversation_flow)

    @cached_property
    def conversation_flow_component(
        self,
    ) -> conversation_flow_component.AsyncConversationFlowComponentResourceWithRawResponse:
        from .resources.conversation_flow_component import AsyncConversationFlowComponentResourceWithRawResponse

        return AsyncConversationFlowComponentResourceWithRawResponse(self._client.conversation_flow_component)

    @cached_property
    def knowledge_base(self) -> knowledge_base.AsyncKnowledgeBaseResourceWithRawResponse:
        from .resources.knowledge_base import AsyncKnowledgeBaseResourceWithRawResponse

        return AsyncKnowledgeBaseResourceWithRawResponse(self._client.knowledge_base)

    @cached_property
    def voice(self) -> voice.AsyncVoiceResourceWithRawResponse:
        from .resources.voice import AsyncVoiceResourceWithRawResponse

        return AsyncVoiceResourceWithRawResponse(self._client.voice)

    @cached_property
    def concurrency(self) -> concurrency.AsyncConcurrencyResourceWithRawResponse:
        from .resources.concurrency import AsyncConcurrencyResourceWithRawResponse

        return AsyncConcurrencyResourceWithRawResponse(self._client.concurrency)

    @cached_property
    def batch_call(self) -> batch_call.AsyncBatchCallResourceWithRawResponse:
        from .resources.batch_call import AsyncBatchCallResourceWithRawResponse

        return AsyncBatchCallResourceWithRawResponse(self._client.batch_call)

    @cached_property
    def tests(self) -> tests.AsyncTestsResourceWithRawResponse:
        from .resources.tests import AsyncTestsResourceWithRawResponse

        return AsyncTestsResourceWithRawResponse(self._client.tests)

    @cached_property
    def mcp_tool(self) -> mcp_tool.AsyncMcpToolResourceWithRawResponse:
        from .resources.mcp_tool import AsyncMcpToolResourceWithRawResponse

        return AsyncMcpToolResourceWithRawResponse(self._client.mcp_tool)


class RetellWithStreamedResponse:
    _client: Retell

    def __init__(self, client: Retell) -> None:
        self._client = client

    @cached_property
    def call(self) -> call.CallResourceWithStreamingResponse:
        from .resources.call import CallResourceWithStreamingResponse

        return CallResourceWithStreamingResponse(self._client.call)

    @cached_property
    def chat(self) -> chat.ChatResourceWithStreamingResponse:
        from .resources.chat import ChatResourceWithStreamingResponse

        return ChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def phone_number(self) -> phone_number.PhoneNumberResourceWithStreamingResponse:
        from .resources.phone_number import PhoneNumberResourceWithStreamingResponse

        return PhoneNumberResourceWithStreamingResponse(self._client.phone_number)

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def chat_agent(self) -> chat_agent.ChatAgentResourceWithStreamingResponse:
        from .resources.chat_agent import ChatAgentResourceWithStreamingResponse

        return ChatAgentResourceWithStreamingResponse(self._client.chat_agent)

    @cached_property
    def llm(self) -> llm.LlmResourceWithStreamingResponse:
        from .resources.llm import LlmResourceWithStreamingResponse

        return LlmResourceWithStreamingResponse(self._client.llm)

    @cached_property
    def conversation_flow(self) -> conversation_flow.ConversationFlowResourceWithStreamingResponse:
        from .resources.conversation_flow import ConversationFlowResourceWithStreamingResponse

        return ConversationFlowResourceWithStreamingResponse(self._client.conversation_flow)

    @cached_property
    def conversation_flow_component(
        self,
    ) -> conversation_flow_component.ConversationFlowComponentResourceWithStreamingResponse:
        from .resources.conversation_flow_component import ConversationFlowComponentResourceWithStreamingResponse

        return ConversationFlowComponentResourceWithStreamingResponse(self._client.conversation_flow_component)

    @cached_property
    def knowledge_base(self) -> knowledge_base.KnowledgeBaseResourceWithStreamingResponse:
        from .resources.knowledge_base import KnowledgeBaseResourceWithStreamingResponse

        return KnowledgeBaseResourceWithStreamingResponse(self._client.knowledge_base)

    @cached_property
    def voice(self) -> voice.VoiceResourceWithStreamingResponse:
        from .resources.voice import VoiceResourceWithStreamingResponse

        return VoiceResourceWithStreamingResponse(self._client.voice)

    @cached_property
    def concurrency(self) -> concurrency.ConcurrencyResourceWithStreamingResponse:
        from .resources.concurrency import ConcurrencyResourceWithStreamingResponse

        return ConcurrencyResourceWithStreamingResponse(self._client.concurrency)

    @cached_property
    def batch_call(self) -> batch_call.BatchCallResourceWithStreamingResponse:
        from .resources.batch_call import BatchCallResourceWithStreamingResponse

        return BatchCallResourceWithStreamingResponse(self._client.batch_call)

    @cached_property
    def tests(self) -> tests.TestsResourceWithStreamingResponse:
        from .resources.tests import TestsResourceWithStreamingResponse

        return TestsResourceWithStreamingResponse(self._client.tests)

    @cached_property
    def mcp_tool(self) -> mcp_tool.McpToolResourceWithStreamingResponse:
        from .resources.mcp_tool import McpToolResourceWithStreamingResponse

        return McpToolResourceWithStreamingResponse(self._client.mcp_tool)


class AsyncRetellWithStreamedResponse:
    _client: AsyncRetell

    def __init__(self, client: AsyncRetell) -> None:
        self._client = client

    @cached_property
    def call(self) -> call.AsyncCallResourceWithStreamingResponse:
        from .resources.call import AsyncCallResourceWithStreamingResponse

        return AsyncCallResourceWithStreamingResponse(self._client.call)

    @cached_property
    def chat(self) -> chat.AsyncChatResourceWithStreamingResponse:
        from .resources.chat import AsyncChatResourceWithStreamingResponse

        return AsyncChatResourceWithStreamingResponse(self._client.chat)

    @cached_property
    def phone_number(self) -> phone_number.AsyncPhoneNumberResourceWithStreamingResponse:
        from .resources.phone_number import AsyncPhoneNumberResourceWithStreamingResponse

        return AsyncPhoneNumberResourceWithStreamingResponse(self._client.phone_number)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def chat_agent(self) -> chat_agent.AsyncChatAgentResourceWithStreamingResponse:
        from .resources.chat_agent import AsyncChatAgentResourceWithStreamingResponse

        return AsyncChatAgentResourceWithStreamingResponse(self._client.chat_agent)

    @cached_property
    def llm(self) -> llm.AsyncLlmResourceWithStreamingResponse:
        from .resources.llm import AsyncLlmResourceWithStreamingResponse

        return AsyncLlmResourceWithStreamingResponse(self._client.llm)

    @cached_property
    def conversation_flow(self) -> conversation_flow.AsyncConversationFlowResourceWithStreamingResponse:
        from .resources.conversation_flow import AsyncConversationFlowResourceWithStreamingResponse

        return AsyncConversationFlowResourceWithStreamingResponse(self._client.conversation_flow)

    @cached_property
    def conversation_flow_component(
        self,
    ) -> conversation_flow_component.AsyncConversationFlowComponentResourceWithStreamingResponse:
        from .resources.conversation_flow_component import AsyncConversationFlowComponentResourceWithStreamingResponse

        return AsyncConversationFlowComponentResourceWithStreamingResponse(self._client.conversation_flow_component)

    @cached_property
    def knowledge_base(self) -> knowledge_base.AsyncKnowledgeBaseResourceWithStreamingResponse:
        from .resources.knowledge_base import AsyncKnowledgeBaseResourceWithStreamingResponse

        return AsyncKnowledgeBaseResourceWithStreamingResponse(self._client.knowledge_base)

    @cached_property
    def voice(self) -> voice.AsyncVoiceResourceWithStreamingResponse:
        from .resources.voice import AsyncVoiceResourceWithStreamingResponse

        return AsyncVoiceResourceWithStreamingResponse(self._client.voice)

    @cached_property
    def concurrency(self) -> concurrency.AsyncConcurrencyResourceWithStreamingResponse:
        from .resources.concurrency import AsyncConcurrencyResourceWithStreamingResponse

        return AsyncConcurrencyResourceWithStreamingResponse(self._client.concurrency)

    @cached_property
    def batch_call(self) -> batch_call.AsyncBatchCallResourceWithStreamingResponse:
        from .resources.batch_call import AsyncBatchCallResourceWithStreamingResponse

        return AsyncBatchCallResourceWithStreamingResponse(self._client.batch_call)

    @cached_property
    def tests(self) -> tests.AsyncTestsResourceWithStreamingResponse:
        from .resources.tests import AsyncTestsResourceWithStreamingResponse

        return AsyncTestsResourceWithStreamingResponse(self._client.tests)

    @cached_property
    def mcp_tool(self) -> mcp_tool.AsyncMcpToolResourceWithStreamingResponse:
        from .resources.mcp_tool import AsyncMcpToolResourceWithStreamingResponse

        return AsyncMcpToolResourceWithStreamingResponse(self._client.mcp_tool)


Client = Retell

AsyncClient = AsyncRetell
