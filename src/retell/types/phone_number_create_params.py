# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from .._types import SequenceNotStr

__all__ = ["PhoneNumberCreateParams"]


class PhoneNumberCreateParams(TypedDict, total=False):
    area_code: int
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    country_code: Literal["US", "CA"]
    """The ISO 3166-1 alpha-2 country code of the number you are trying to purchase.

    If left empty, will default to "US".
    """

    inbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If
    null, this number would not accept inbound call.
    """

    inbound_agent_version: Optional[int]
    """Version of the inbound agent to bind to the number.

    If not provided, will default to latest version.
    """

    inbound_allowed_countries: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.

    If not set or empty, calls from all countries are allowed.
    """

    inbound_webhook_url: Optional[str]
    """
    If set, will send a webhook for inbound calls, where you can to override agent
    id, set dynamic variables and other fields specific to that call.
    """

    nickname: str
    """Nickname of the number. This is for your reference only."""

    number_provider: Literal["twilio", "telnyx"]
    """The provider to purchase the phone number from. Default to twilio."""

    outbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls. If
    null, this number would not be able to initiate outbound call without agent id
    override.
    """

    outbound_agent_version: Optional[int]
    """Version of the outbound agent to bind to the number.

    If not provided, will default to latest version.
    """

    outbound_allowed_countries: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

    phone_number: str
    """
    The number you are trying to purchase in E.164 format of the number (+country
    code then number with no space and no special characters).
    """

    toll_free: bool
    """Whether to purchase a toll-free number. Toll-free numbers incur higher costs."""

    transport: Optional[str]
    """Outbound transport protocol to use for the phone number.

    Valid values are "TLS", "TCP" and "UDP". Default is "TCP".
    """
