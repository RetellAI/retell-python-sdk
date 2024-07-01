# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PhoneNumberCreateParams"]


class PhoneNumberCreateParams(TypedDict, total=False):
    area_code: int
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    inbound_agent_id: str
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If
    unset, this number would not accept inbound call.
    """

    outbound_agent_id: str
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls. If
    unset, this number would not be able to initiate inbound call without agent id
    override.
    """
