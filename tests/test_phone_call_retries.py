"""create_phone_call must not dial twice because the SDK retried it.

Without an idempotency_key the API can't tell a retry from a new call, so the SDK only
retries create_phone_call when the caller passed a key.
"""

from __future__ import annotations

import json
from typing import Any, List, Union
from unittest import mock
from typing_extensions import override

import httpx
import pytest

from retell import Retell, AsyncRetell, APIStatusError, APITimeoutError, APIConnectionError

BASE_URL = "http://127.0.0.1:4010"
PHONE_CALL = {
    "agent_id": "agent_1",
    "agent_version": 1,
    "call_id": "call_1",
    "call_status": "registered",
    "call_type": "phone_call",
    "direction": "outbound",
    "from_number": "+14155550100",
    "to_number": "+14155550199",
}
FROM, TO = "+14155550100", "+14155550199"

Reply = Union[httpx.Response, Exception]


class ScriptedTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    """Answers each request with the next scripted reply (the last one repeats) and records the bodies."""

    def __init__(self, *replies: Reply) -> None:
        self.replies = list(replies)
        self.requests: List[httpx.Request] = []

    def _reply(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        reply = self.replies[min(len(self.requests), len(self.replies)) - 1]
        if isinstance(reply, Exception):
            raise reply
        return reply

    @override
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        return self._reply(request)

    @override
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        return self._reply(request)

    def bodies(self) -> List[Any]:
        return [json.loads(r.content) for r in self.requests]


def status(code: int) -> httpx.Response:
    return httpx.Response(code, json={"message": "upstream"})


def read_timeout() -> Exception:
    return httpx.ReadTimeout("timed out")


def dropped() -> Exception:
    return httpx.RemoteProtocolError("Server disconnected without sending a response.")


AMBIGUOUS = [
    pytest.param(read_timeout, APITimeoutError, id="read-timeout"),
    pytest.param(dropped, APIConnectionError, id="dropped-connection"),
    *[pytest.param(lambda c=c: status(c), APIStatusError, id=str(c)) for c in (500, 502, 503, 504, 408, 409, 429)],
]


def _no_retry_timeout(*_args: Any, **_kwargs: Any) -> float:
    return 0


no_backoff = mock.patch("retell._base_client.BaseClient._calculate_retry_timeout", _no_retry_timeout)


def sync_client(transport: ScriptedTransport) -> Retell:
    return Retell(api_key="test", base_url=BASE_URL, http_client=httpx.Client(transport=transport))


def async_client(transport: ScriptedTransport) -> AsyncRetell:
    return AsyncRetell(api_key="test", base_url=BASE_URL, http_client=httpx.AsyncClient(transport=transport))


@no_backoff
@pytest.mark.parametrize("failure,error", AMBIGUOUS)
def test_keyless_phone_call_is_sent_once(failure: Any, error: Any) -> None:
    transport = ScriptedTransport(failure(), httpx.Response(201, json=PHONE_CALL))
    with pytest.raises(error):
        sync_client(transport).call.create_phone_call(from_number=FROM, to_number=TO)
    assert len(transport.requests) == 1


@no_backoff
def test_keyless_phone_call_ignores_client_max_retries() -> None:
    transport = ScriptedTransport(read_timeout(), httpx.Response(201, json=PHONE_CALL))
    with pytest.raises(APITimeoutError):
        sync_client(transport).with_options(max_retries=5).call.create_phone_call(from_number=FROM, to_number=TO)
    assert len(transport.requests) == 1


@no_backoff
@pytest.mark.parametrize("failure,error", AMBIGUOUS)
def test_keyed_phone_call_is_retried_with_the_same_key(failure: Any, error: Any) -> None:  # noqa: ARG001
    transport = ScriptedTransport(failure(), httpx.Response(201, json=PHONE_CALL))
    call = sync_client(transport).call.create_phone_call(
        from_number=FROM, to_number=TO, idempotency_key="order-42-attempt"
    )
    assert call.call_id == "call_1"
    assert [body["idempotency_key"] for body in transport.bodies()] == ["order-42-attempt", "order-42-attempt"]


@no_backoff
def test_other_requests_keep_their_retries() -> None:
    transport = ScriptedTransport(
        status(503),
        httpx.Response(201, json={"access_token": "t", "agent_id": "agent_1", "agent_version": 1, "call_id": "c"}),
    )
    sync_client(transport).call.create_web_call(agent_id="agent_1")
    assert len(transport.requests) == 2


@no_backoff
async def test_async_keyless_phone_call_is_sent_once() -> None:
    transport = ScriptedTransport(read_timeout(), httpx.Response(201, json=PHONE_CALL))
    with pytest.raises(APITimeoutError):
        await async_client(transport).call.create_phone_call(from_number=FROM, to_number=TO)
    assert len(transport.requests) == 1


@no_backoff
async def test_async_keyed_phone_call_is_retried_with_the_same_key() -> None:
    transport = ScriptedTransport(status(502), httpx.Response(201, json=PHONE_CALL))
    call = await async_client(transport).call.create_phone_call(
        from_number=FROM, to_number=TO, idempotency_key="order-42-attempt"
    )
    assert call.call_id == "call_1"
    assert [body["idempotency_key"] for body in transport.bodies()] == ["order-42-attempt", "order-42-attempt"]
