# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PhoneNumberResponse", "SipOutboundTrunkConfig"]


class SipOutboundTrunkConfig(BaseModel):
    auth_username: Optional[str] = None
    """The username used for authenticating the SIP trunk for the phone number."""

    termination_uri: Optional[str] = None
    """The termination URI for the SIP trunk for the phone number."""

    transport: Optional[str] = None
    """Outbound transport protocol for the SIP trunk for the phone number.

    Valid values are "TLS", "TCP" and "UDP". Default is "TCP".
    """


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

    phone_number_type: Literal["retell-twilio", "retell-telnyx", "custom"]
    """Type of the phone number."""

    area_code: Optional[int] = None
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    inbound_agent_id: Optional[str] = None
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If
    null, this number would not accept inbound call.
    """

    inbound_agent_version: Optional[int] = None
    """Version of the inbound agent to bind to the number.

    If not provided, will default to latest version.
    """

    inbound_allowed_countries: Optional[List[str]] = None
    """List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.

    If not set or empty, calls from all countries are allowed.
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

    outbound_agent_version: Optional[int] = None
    """Version of the outbound agent to bind to the number.

    If not provided, will default to latest version.
    """

    outbound_allowed_countries: Optional[List[str]] = None
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

    phone_number_pretty: Optional[str] = None
    """Pretty printed phone number, provided for your reference."""

    sip_outbound_trunk_config: Optional[SipOutboundTrunkConfig] = None
