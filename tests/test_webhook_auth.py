from __future__ import annotations

from typing import cast
from collections.abc import Callable

import pytest

from retell import Retell
from retell.lib import webhook_auth

BODY = '{"event":"call_ended"}'
API_KEY = "test-api-key"
TIMESTAMP = 1_700_000_000_000
TIMEOUT = 5 * 60 * 1000
EXPECTED_DIGEST = "07024cabe7dd8f6d1c6e4a8324ca92c812e6ad4a7ee506c04f7e462e3321823e"
_sign_webhook = cast(Callable[..., str], webhook_auth.symmetric["sign"])  # pyright: ignore[reportUnknownMemberType]
_verify_webhook = cast(Callable[..., bool], webhook_auth.symmetric["verify"])  # pyright: ignore[reportUnknownMemberType]


def _sign(*, timestamp: int = TIMESTAMP) -> str:
    return _sign_webhook(BODY, API_KEY, timestamp)


def _verify(
    signature: str,
    *,
    body: str = BODY,
    api_key: str = API_KEY,
    timestamp: int = TIMESTAMP,
    timeout: int = TIMEOUT,
) -> bool:
    return _verify_webhook(
        body,
        api_key,
        signature,
        {"timestamp": timestamp, "timeout": timeout},
    )


def test_signs_with_hmac_sha256_using_documented_format() -> None:
    assert _sign() == f"v={TIMESTAMP},d={EXPECTED_DIGEST}"


def test_verifies_valid_signature() -> None:
    assert _verify(_sign()) is True


def test_retell_verify_synchronously_returns_bool() -> None:
    signature = _sign_webhook(BODY, API_KEY)

    with Retell(api_key=API_KEY) as client:
        valid = client.verify(BODY, API_KEY, signature)  # type: ignore
        tampered = client.verify(f"{BODY} ", API_KEY, signature)  # type: ignore
        malformed = client.verify(BODY, API_KEY, f"prefix-{signature}")  # type: ignore

    assert valid is True
    assert tampered is False
    assert malformed is False
    assert isinstance(valid, bool)


def test_rejects_tampered_body_and_incorrect_secret() -> None:
    signature = _sign()

    assert _verify(signature, body=f"{BODY} ") is False
    assert _verify(signature, api_key="wrong-api-key") is False


@pytest.mark.parametrize(
    "signature",
    [
        "",
        f"v={TIMESTAMP}",
        f"d={EXPECTED_DIGEST},v={TIMESTAMP}",
        f"prefix-v={TIMESTAMP},d={EXPECTED_DIGEST}",
        f"v={TIMESTAMP},d={EXPECTED_DIGEST}-suffix",
        f"v={TIMESTAMP},d=not-hex",
        f"v={TIMESTAMP},d={EXPECTED_DIGEST[2:]}",
        f"v=-{TIMESTAMP},d={EXPECTED_DIGEST}",
        f"v={TIMESTAMP},d={EXPECTED_DIGEST},extra=value",
    ],
)
def test_rejects_malformed_signature(signature: str) -> None:
    assert _verify(signature) is False


def test_rejects_expired_timestamp_outside_tolerance() -> None:
    signature = _sign()

    assert _verify(signature, timestamp=TIMESTAMP + TIMEOUT) is True
    assert _verify(signature, timestamp=TIMESTAMP + TIMEOUT + 1) is False


def test_rejects_future_timestamp_outside_tolerance() -> None:
    signature = _sign()

    assert _verify(signature, timestamp=TIMESTAMP - TIMEOUT) is True
    assert _verify(signature, timestamp=TIMESTAMP - TIMEOUT - 1) is False


def test_verification_uses_constant_time_digest_comparison(monkeypatch: pytest.MonkeyPatch) -> None:
    comparisons: list[tuple[str, str]] = []

    def compare_digest(actual: str, supplied: str) -> bool:
        comparisons.append((actual, supplied))
        return True

    monkeypatch.setattr(webhook_auth.hmac, "compare_digest", compare_digest)

    assert _verify(_sign()) is True
    assert comparisons == [(EXPECTED_DIGEST, EXPECTED_DIGEST)]
