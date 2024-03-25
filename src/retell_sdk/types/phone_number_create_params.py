# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberCreateParams"]


class PhoneNumberCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    """Unique id of agent used for the call.

    Your agent would contain the LLM Websocket url used for this call.
    """

    area_code: str
    """Area code of the number"""
