# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PhoneNumberResponse"]


class PhoneNumberResponse(BaseModel):
    area_code: int
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    phone_number: str
    """
    E.164 format of the number (+country code, then number with no space, no special
    characters), used as the unique identifier for phone number APIs.
    """

    phone_number_pretty: str
    """Pretty printed phone number, provided for your reference."""

    inbound_agent_id: Optional[str] = None
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If
    null, this number would not accept inbound call.
    """

    outbound_agent_id: Optional[str] = None
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls. If
    null, this number would not be able to initiate outbound call without agent id
    override.
    """
