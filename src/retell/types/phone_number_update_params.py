# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    auth_password: str
    """
    The password used for authentication for the SIP trunk to update for the phone
    number.
    """

    auth_username: str
    """
    The username used for authentication for the SIP trunk to update for the phone
    number.
    """

    inbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If set
    to null, this number would not accept inbound call.
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

    nickname: Optional[str]
    """Nickname of the number. This is for your reference only."""

    outbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when conducting outbound calls. If
    set to null, this number would not be able to initiate outbound call without
    agent id override.
    """

    outbound_agent_version: Optional[int]
    """Version of the outbound agent to bind to the number.

    If not provided, will default to latest version.
    """

    outbound_allowed_countries: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

    termination_uri: str
    """The termination uri to update for the phone number.

    This is used for outbound calls.
    """

    transport: Optional[str]
    """Outbound transport protocol to update for the phone number.

    Valid values are "TLS", "TCP" and "UDP". Default is "TCP".
    """
