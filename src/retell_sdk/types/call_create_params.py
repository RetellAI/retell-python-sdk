# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CallCreateParams", "PhoneNumber"]


class CallCreateParams(TypedDict, total=False):
    phone_number: Required[PhoneNumber]

    override_agent_id: str
    """For this particular call, override the agent used with this agent id.

    This does not bind the agent to this number, this is for one time override.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Retell LLM prompt and tool description. Only applicable for Retell LLM.
    """


_PhoneNumberReservedKeywords = TypedDict(
    "_PhoneNumberReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class PhoneNumber(_PhoneNumberReservedKeywords, total=False):
    to: Required[str]
    """The number you want to call, in BCP 47 format."""
