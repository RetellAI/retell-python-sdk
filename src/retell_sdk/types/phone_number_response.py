# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PhoneNumberResponse"]


class PhoneNumberResponse(BaseModel):
    agent_id: str
    """Unique id of agent to bind to newly obtained number.

    The number will automatically use the agent when doing inbound / outbound calls.
    """

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
    BCP 47 format of the number (+country code, then number with no space, no
    special characters), used as the unique identifier for phone number APIs.
    """

    phone_number_pretty: str
    """Pretty printed phone number, provided for your reference."""
