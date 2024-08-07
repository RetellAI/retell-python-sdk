# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberImportParams"]


class PhoneNumberImportParams(TypedDict, total=False):
    phone_number: Required[str]
    """
    The number you are trying to import in E.164 format of the number (+country
    code, then number with no space, no special characters), used as the unique
    identifier for phone number APIs.
    """

    termination_uri: Required[str]
    """The termination uri to uniquely identify your elastic SIP trunk.

    This is used for outbound calls. For Twilio elastic SIP trunks it always end
    with ".pstn.twilio.com".
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

    sip_trunk_auth_password: str
    """The password used for authentication for the SIP trunk."""

    sip_trunk_auth_username: str
    """The username used for authentication for the SIP trunk."""
