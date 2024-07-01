# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    inbound_agent_id: str
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls.
    """

    outbound_agent_id: str
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls.
    """
