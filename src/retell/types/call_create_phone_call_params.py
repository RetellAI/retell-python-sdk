# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CallCreatePhoneCallParams"]


class CallCreatePhoneCallParams(TypedDict, total=False):
    from_number: Required[str]
    """The number you own in E.164 format. Must be a Retell managed number."""

    to_number: Required[str]
    """The number you want to call, in E.164 format.

    Right now only US numbers are officially supported.
    """

    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    override_agent_id: str
    """For this particular call, override the agent used with this agent id.

    This does not bind the agent to this number, this is for one time override.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Retell LLM prompt and tool description. Only applicable for Retell LLM.
    """
