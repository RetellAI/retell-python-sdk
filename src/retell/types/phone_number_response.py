# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberResponse"]


class PhoneNumberResponse(BaseModel):
    last_modification_timestamp: int
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    phone_number: str
    """
    E.164 format of the number (+country code, then number with no space, no special
    characters), used as the unique identifier for phone number APIs.
    """

    area_code: Optional[int] = None
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    inbound_agent_id: Optional[str] = None
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If
    null, this number would not accept inbound call.
    """

    inbound_webhook_url: Optional[str] = None
    """
    If set, will send a webhook for inbound calls, where you can to override agent
    id, set dynamic variables and other fields specific to that call.
    """

    nickname: Optional[str] = None
    """Nickname of the number. This is for your reference only."""

    outbound_agent_id: Optional[str] = None
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls. If
    null, this number would not be able to initiate outbound call without agent id
    override.
    """

    phone_number_pretty: Optional[str] = None
    """Pretty printed phone number, provided for your reference."""

    phone_number_type: Optional[Literal["retell-twilio", "retell-telnyx", "custom"]] = None
    """Type of the phone number."""
