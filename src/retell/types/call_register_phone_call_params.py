# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CallRegisterPhoneCallParams"]


class CallRegisterPhoneCallParams(TypedDict, total=False):
    agent_id: Required[str]
    """The agent to use for the call."""

    direction: Literal["inbound", "outbound"]
    """Direction of the phone call. Stored for tracking purpose."""

    from_number: str
    """The number you own in E.164 format. Stored for tracking purpose."""

    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """

    to_number: str
    """The number you want to call, in E.164 format. Stored for tracking purpose."""
