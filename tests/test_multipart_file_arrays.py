from __future__ import annotations

import json
from email import policy
from typing import cast
from email.parser import BytesParser
from email.message import EmailMessage
from collections.abc import Callable, Awaitable
from typing_extensions import override

import httpx

from retell import Retell, AsyncRetell
from retell.types import knowledge_base_create_params

_KNOWLEDGE_BASE_RESPONSE = {
    "knowledge_base_id": "kb_test",
    "knowledge_base_name": "Test KB",
    "status": "in_progress",
}
_VOICE_RESPONSE = {
    "gender": "female",
    "provider": "elevenlabs",
    "voice_id": "voice_test",
    "voice_name": "Test Voice",
}
_FILES = [
    ("first.txt", b"first file", "text/plain"),
    ("second.txt", b"second file", "text/plain"),
]
_TEXTS: list[knowledge_base_create_params.KnowledgeBaseText] = [{"title": "t", "text": "hello"}]
_URLS = ["https://example.com"]


class CapturingTransport(httpx.BaseTransport, httpx.AsyncBaseTransport):
    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []

    def _response_for(self, request: httpx.Request) -> httpx.Response:
        response_json = _VOICE_RESPONSE if request.url.path == "/clone-voice" else _KNOWLEDGE_BASE_RESPONSE
        return httpx.Response(200, json=response_json)

    @override
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        return self._response_for(request)

    @override
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        await request.aread()
        self.requests.append(request)
        return self._response_for(request)


def _multipart_parts(request: httpx.Request) -> list[tuple[str, str | None, bytes]]:
    content_type = request.headers["content-type"]
    assert content_type.startswith("multipart/form-data;")

    message = cast(
        EmailMessage,
        BytesParser(policy=policy.default).parsebytes(  # pyright: ignore[reportArgumentType]
            f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode() + request.content
        ),
    )
    assert message.is_multipart()

    parts: list[tuple[str, str | None, bytes]] = []
    for part in message.iter_parts():
        name = part.get_param("name", header="content-disposition")
        payload = part.get_payload(decode=True)
        assert isinstance(name, str)
        assert isinstance(payload, bytes)
        parts.append((name, part.get_filename(), payload))
    return parts


def _single_text_part(parts: list[tuple[str, str | None, bytes]], name: str) -> bytes:
    matches = [(filename, payload) for part_name, filename, payload in parts if part_name == name]
    assert len(matches) == 1
    filename, payload = matches[0]
    assert filename is None
    return payload


def _assert_knowledge_base_request(request: httpx.Request, *, path: str) -> None:
    assert request.url.path == path
    parts = _multipart_parts(request)

    file_parts = [(filename, payload) for name, filename, payload in parts if name == "knowledge_base_files"]
    assert file_parts == [("first.txt", b"first file"), ("second.txt", b"second file")]
    assert all(name != "knowledge_base_files[]" for name, _, _ in parts)
    assert all(filename is not None for name, filename, _ in parts if name == "knowledge_base_files")

    assert json.loads(_single_text_part(parts, "knowledge_base_texts")) == _TEXTS
    assert json.loads(_single_text_part(parts, "knowledge_base_urls")) == _URLS


def _assert_voice_request(request: httpx.Request) -> None:
    assert request.url.path == "/clone-voice"
    parts = _multipart_parts(request)

    file_parts = [(filename, payload) for name, filename, payload in parts if name == "files"]
    assert file_parts == [("first.txt", b"first file"), ("second.txt", b"second file")]
    assert all(name != "files[]" for name, _, _ in parts)
    assert all(filename is not None for name, filename, _ in parts if name == "files")


def _run_sync_request(call: Callable[[Retell], object]) -> httpx.Request:
    transport = CapturingTransport()
    with Retell(
        api_key="test-key",
        base_url="https://example.test",
        max_retries=0,
        http_client=httpx.Client(transport=transport),
    ) as client:
        call(client)

    assert len(transport.requests) == 1
    return transport.requests[0]


async def _run_async_request(call: Callable[[AsyncRetell], Awaitable[object]]) -> httpx.Request:
    transport = CapturingTransport()
    async with AsyncRetell(
        api_key="test-key",
        base_url="https://example.test",
        max_retries=0,
        http_client=httpx.AsyncClient(transport=transport),
    ) as client:
        await call(client)

    assert len(transport.requests) == 1
    return transport.requests[0]


def test_knowledge_base_create_uses_bare_repeated_file_parts() -> None:
    request = _run_sync_request(
        lambda client: client.knowledge_base.create(
            knowledge_base_name="Test KB",
            knowledge_base_files=_FILES,
            knowledge_base_texts=_TEXTS,
            knowledge_base_urls=_URLS,
        )
    )
    _assert_knowledge_base_request(request, path="/create-knowledge-base")


async def test_async_knowledge_base_create_uses_bare_repeated_file_parts() -> None:
    request = await _run_async_request(
        lambda client: client.knowledge_base.create(
            knowledge_base_name="Test KB",
            knowledge_base_files=_FILES,
            knowledge_base_texts=_TEXTS,
            knowledge_base_urls=_URLS,
        )
    )
    _assert_knowledge_base_request(request, path="/create-knowledge-base")


def test_knowledge_base_add_sources_uses_bare_repeated_file_parts() -> None:
    request = _run_sync_request(
        lambda client: client.knowledge_base.add_sources(
            knowledge_base_id="kb_test",
            knowledge_base_files=_FILES,
            knowledge_base_texts=_TEXTS,
            knowledge_base_urls=_URLS,
        )
    )
    _assert_knowledge_base_request(request, path="/add-knowledge-base-sources/kb_test")


async def test_async_knowledge_base_add_sources_uses_bare_repeated_file_parts() -> None:
    request = await _run_async_request(
        lambda client: client.knowledge_base.add_sources(
            knowledge_base_id="kb_test",
            knowledge_base_files=_FILES,
            knowledge_base_texts=_TEXTS,
            knowledge_base_urls=_URLS,
        )
    )
    _assert_knowledge_base_request(request, path="/add-knowledge-base-sources/kb_test")


def test_voice_clone_uses_bare_repeated_file_parts() -> None:
    request = _run_sync_request(
        lambda client: client.voice.clone(
            files=_FILES,
            voice_name="Test Voice",
            voice_provider="elevenlabs",
        )
    )
    _assert_voice_request(request)


async def test_async_voice_clone_uses_bare_repeated_file_parts() -> None:
    request = await _run_async_request(
        lambda client: client.voice.clone(
            files=_FILES,
            voice_name="Test Voice",
            voice_provider="elevenlabs",
        )
    )
    _assert_voice_request(request)
