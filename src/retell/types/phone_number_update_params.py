# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PhoneNumberUpdateParams", "InboundAgent", "InboundSMSAgent", "OutboundAgent", "OutboundSMSAgent"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    allowed_inbound_country_list: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.

    If not set or empty, calls from all countries are allowed.
    """

    allowed_outbound_country_list: Optional[SequenceNotStr[str]]
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

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

    fallback_number: Optional[str]
    """Enterprise only.

    Phone number to transfer inbound calls to when organization is in outage mode.
    Can be either a Retell phone number or an external number. Set to null to
    remove. Cannot be the same as this phone number, and cannot be a number that
    already has its own fallback configured (prevents nested forwarding).
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

    inbound_agents: Optional[Iterable[InboundAgent]]
    """Inbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each inbound call,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to inbound_agent_id.
    """

    inbound_sms_agents: Optional[Iterable[InboundSMSAgent]]
    """Inbound SMS agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each inbound SMS,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to inbound_sms_agent_id.
    """

    inbound_sms_webhook_url: Optional[str]
    """
    If set, will send a webhook for inbound SMS, where you can override agent id,
    set dynamic variables and other fields specific to that chat.
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

    outbound_agents: Optional[Iterable[OutboundAgent]]
    """Outbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound call,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to outbound_agent_id.
    """

    outbound_sms_agents: Optional[Iterable[OutboundSMSAgent]]
    """Outbound SMS agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound SMS,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to outbound_sms_agent_id.
    """

    termination_uri: str
    """The termination uri to update for the phone number.

    This is used for outbound calls.
    """

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


class InboundSMSAgent(TypedDict, total=False):
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


class OutboundSMSAgent(TypedDict, total=False):
    agent_id: Required[str]

    weight: Required[float]
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: int
