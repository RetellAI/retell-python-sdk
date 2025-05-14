import json
from retell.lib.webhook_auth import symmetric


def test_symmetric_signature() -> None:
    post_data = {
        "name": "some_function_name",
        "args": {"some_arg": "ABC123"},
    }
    body = json.dumps(post_data, separators=(",", ":"), ensure_ascii=False)
    api_key = "fake-api-key"

    signature = symmetric["sign"](body, api_key)
    assert symmetric["verify"](body, api_key, signature)
