# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import llm, call, agent, voice, concurrency, phone_number, knowledge_base
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .lib.webhook_auth import verify  # type: ignore

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Retell", "AsyncRetell", "Client", "AsyncClient"]


class Retell(SyncAPIClient):
    call: call.CallResource
    phone_number: phone_number.PhoneNumberResource
    agent: agent.AgentResource
    llm: llm.LlmResource
    knowledge_base: knowledge_base.KnowledgeBaseResource
    voice: voice.VoiceResource
    concurrency: concurrency.ConcurrencyResource
    with_raw_response: RetellWithRawResponse
    with_streaming_response: RetellWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new synchronous retell client instance."""
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

        self.call = call.CallResource(self)
        self.phone_number = phone_number.PhoneNumberResource(self)
        self.agent = agent.AgentResource(self)
        self.llm = llm.LlmResource(self)
        self.knowledge_base = knowledge_base.KnowledgeBaseResource(self)
        self.voice = voice.VoiceResource(self)
        self.concurrency = concurrency.ConcurrencyResource(self)
        self.with_raw_response = RetellWithRawResponse(self)
        self.with_streaming_response = RetellWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    call: call.AsyncCallResource
    phone_number: phone_number.AsyncPhoneNumberResource
    agent: agent.AsyncAgentResource
    llm: llm.AsyncLlmResource
    knowledge_base: knowledge_base.AsyncKnowledgeBaseResource
    voice: voice.AsyncVoiceResource
    concurrency: concurrency.AsyncConcurrencyResource
    with_raw_response: AsyncRetellWithRawResponse
    with_streaming_response: AsyncRetellWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """Construct a new async retell client instance."""
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

        self.call = call.AsyncCallResource(self)
        self.phone_number = phone_number.AsyncPhoneNumberResource(self)
        self.agent = agent.AsyncAgentResource(self)
        self.llm = llm.AsyncLlmResource(self)
        self.knowledge_base = knowledge_base.AsyncKnowledgeBaseResource(self)
        self.voice = voice.AsyncVoiceResource(self)
        self.concurrency = concurrency.AsyncConcurrencyResource(self)
        self.with_raw_response = AsyncRetellWithRawResponse(self)
        self.with_streaming_response = AsyncRetellWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def __init__(self, client: Retell) -> None:
        self.call = call.CallResourceWithRawResponse(client.call)
        self.phone_number = phone_number.PhoneNumberResourceWithRawResponse(client.phone_number)
        self.agent = agent.AgentResourceWithRawResponse(client.agent)
        self.llm = llm.LlmResourceWithRawResponse(client.llm)
        self.knowledge_base = knowledge_base.KnowledgeBaseResourceWithRawResponse(client.knowledge_base)
        self.voice = voice.VoiceResourceWithRawResponse(client.voice)
        self.concurrency = concurrency.ConcurrencyResourceWithRawResponse(client.concurrency)


class AsyncRetellWithRawResponse:
    def __init__(self, client: AsyncRetell) -> None:
        self.call = call.AsyncCallResourceWithRawResponse(client.call)
        self.phone_number = phone_number.AsyncPhoneNumberResourceWithRawResponse(client.phone_number)
        self.agent = agent.AsyncAgentResourceWithRawResponse(client.agent)
        self.llm = llm.AsyncLlmResourceWithRawResponse(client.llm)
        self.knowledge_base = knowledge_base.AsyncKnowledgeBaseResourceWithRawResponse(client.knowledge_base)
        self.voice = voice.AsyncVoiceResourceWithRawResponse(client.voice)
        self.concurrency = concurrency.AsyncConcurrencyResourceWithRawResponse(client.concurrency)


class RetellWithStreamedResponse:
    def __init__(self, client: Retell) -> None:
        self.call = call.CallResourceWithStreamingResponse(client.call)
        self.phone_number = phone_number.PhoneNumberResourceWithStreamingResponse(client.phone_number)
        self.agent = agent.AgentResourceWithStreamingResponse(client.agent)
        self.llm = llm.LlmResourceWithStreamingResponse(client.llm)
        self.knowledge_base = knowledge_base.KnowledgeBaseResourceWithStreamingResponse(client.knowledge_base)
        self.voice = voice.VoiceResourceWithStreamingResponse(client.voice)
        self.concurrency = concurrency.ConcurrencyResourceWithStreamingResponse(client.concurrency)


class AsyncRetellWithStreamedResponse:
    def __init__(self, client: AsyncRetell) -> None:
        self.call = call.AsyncCallResourceWithStreamingResponse(client.call)
        self.phone_number = phone_number.AsyncPhoneNumberResourceWithStreamingResponse(client.phone_number)
        self.agent = agent.AsyncAgentResourceWithStreamingResponse(client.agent)
        self.llm = llm.AsyncLlmResourceWithStreamingResponse(client.llm)
        self.knowledge_base = knowledge_base.AsyncKnowledgeBaseResourceWithStreamingResponse(client.knowledge_base)
        self.voice = voice.AsyncVoiceResourceWithStreamingResponse(client.voice)
        self.concurrency = concurrency.AsyncConcurrencyResourceWithStreamingResponse(client.concurrency)


Client = Retell

AsyncClient = AsyncRetell
