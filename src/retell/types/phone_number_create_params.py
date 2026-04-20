# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PhoneNumberCreateParams", "InboundAgent", "OutboundAgent"]


class PhoneNumberCreateParams(TypedDict, total=False):
    allowed_inbound_country_list: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.

    If not set or empty, calls from all countries are allowed.
    """

    allowed_outbound_country_list: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

    area_code: int
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    country_code: Literal["US", "CA"]
    """The ISO 3166-1 alpha-2 country code of the number you are trying to purchase.

    If left empty, will default to "US".
    """

    fallback_number: Optional[str]
    """Enterprise only.

    Phone number to transfer inbound calls to when organization is in outage mode.
    Can be either a Retell phone number or an external number. Cannot be the same as
    this phone number, and cannot be a number that already has its own fallback
    configured (prevents nested forwarding).
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

    number_provider: Literal["twilio", "telnyx"]
    """The provider to purchase the phone number from. Default to twilio."""

    outbound_agents: Optional[Iterable[OutboundAgent]]
    """Outbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound call,
    with probability proportional to the weight. Total weights must add up to 1.
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
