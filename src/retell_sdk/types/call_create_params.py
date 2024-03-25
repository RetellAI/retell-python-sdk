# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CallCreateParams", "PhoneNumber"]


class CallCreateParams(TypedDict, total=False):
    phone_number: Required[PhoneNumber]

    override_agent_id: str
    """Unique id of agent used for the call.

    Your agent would contain the LLM Websocket url used for this call.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """Add optional dynamic variables that injects into your Retell LLM prompt."""


_PhoneNumberReservedKeywords = TypedDict(
    "_PhoneNumberReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class PhoneNumber(_PhoneNumberReservedKeywords, total=False):
    to: Required[str]
    """To your customer number"""
