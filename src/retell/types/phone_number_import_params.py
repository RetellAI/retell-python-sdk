# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PhoneNumberImportParams", "InboundAgent", "OutboundAgent"]


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

    allowed_inbound_country_list: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.

    If not set or empty, calls from all countries are allowed.
    """

    allowed_outbound_country_list: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

    ignore_e164_validation: bool
    """If true, E.164 validation for phone_number is skipped.

    This is useful for internal pseudo numbers when using custom telephony. If
    omitted, default is true. Must be a boolean literal; string values like "true"
    or "false" are invalid.
    """

    inbound_agents: Optional[Iterable[InboundAgent]]
    """Inbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each inbound call,
    with probability proportional to the weight. Total weights must add up to 1.
    """

    inbound_webhook_url: Optional[str]
    """
    If set, will send a webhook for inbound calls, where you can to override agent
    id, set dynamic variables and other fields specific to that call.
    """

    nickname: str
    """Nickname of the number. This is for your reference only."""

    outbound_agents: Optional[Iterable[OutboundAgent]]
    """Outbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound call,
    with probability proportional to the weight. Total weights must add up to 1.
    """

    sip_trunk_auth_password: str
    """The password used for authentication for the SIP trunk."""

    sip_trunk_auth_username: str
    """The username used for authentication for the SIP trunk."""

    transport: Optional[str]
    """Outbound transport protocol to update for the phone number.

    Valid values are "TLS", "TCP" and "UDP". Default is "TCP".
    """


class InboundAgent(TypedDict, total=False):
    agent_id: Required[str]

    weight: Required[float]
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: int


class OutboundAgent(TypedDict, total=False):
    agent_id: Required[str]

    weight: Required[float]
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: int
