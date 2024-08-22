# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PhoneNumberCreateParams"]


class PhoneNumberCreateParams(TypedDict, total=False):
    area_code: int
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    inbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If
    null, this number would not accept inbound call.
    """

    nickname: str
    """Nickname of the number. This is for your reference only."""

    outbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls. If
    null, this number would not be able to initiate outbound call without agent id
    override.
    """
