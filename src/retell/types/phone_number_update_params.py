# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
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

    Phone number to transfer inbound calls to when organization is in outage mode or
    when an inbound call cannot get a concurrency slot before the fallback timeout.
    Can be either a Retell phone number or an external number. Set to null to
    remove. Cannot be the same as this phone number, and cannot be a number that
    already has its own fallback configured (prevents nested forwarding).
    """

    inbound_agents: Optional[Iterable[InboundAgent]]
    """Inbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each inbound call,
    with probability proportional to the weight. Total weights must add up to 1.
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
    If set, will send a webhook for inbound calls, where you can override agent id,
    set dynamic variables and other fields specific to that call.
    """

    nickname: Optional[str]
    """Nickname of the number. This is for your reference only."""

    outbound_agents: Optional[Iterable[OutboundAgent]]
    """Outbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound call,
    with probability proportional to the weight. Total weights must add up to 1.
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

    agent_version: Union[int, str]
    """Agent version reference.

    Supports a numeric version (for example 3) or a tag/environment name (for
    example "prod"). The string "latest" resolves to the most recently created
    version (the largest version number), and "latest_published" resolves to the
    most recently published version. When a tag is provided, resolution uses that
    exact tag assignment (including its dynamic variables). If the tag exists but is
    currently unassigned, it resolves to latest. When a numeric version, latest, or
    latest_published is provided, resolution applies dynamic variables from the
    preferred tag for that resolved version (most recently assigned), if any.
    """


class InboundSMSAgent(TypedDict, total=False):
    agent_id: Required[str]

    weight: Required[float]
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Union[int, str]
    """Agent version reference.

    Supports a numeric version (for example 3) or a tag/environment name (for
    example "prod"). The string "latest" resolves to the most recently created
    version (the largest version number), and "latest_published" resolves to the
    most recently published version. When a tag is provided, resolution uses that
    exact tag assignment (including its dynamic variables). If the tag exists but is
    currently unassigned, it resolves to latest. When a numeric version, latest, or
    latest_published is provided, resolution applies dynamic variables from the
    preferred tag for that resolved version (most recently assigned), if any.
    """


class OutboundAgent(TypedDict, total=False):
    agent_id: Required[str]

    weight: Required[float]
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Union[int, str]
    """Agent version reference.

    Supports a numeric version (for example 3) or a tag/environment name (for
    example "prod"). The string "latest" resolves to the most recently created
    version (the largest version number), and "latest_published" resolves to the
    most recently published version. When a tag is provided, resolution uses that
    exact tag assignment (including its dynamic variables). If the tag exists but is
    currently unassigned, it resolves to latest. When a numeric version, latest, or
    latest_published is provided, resolution applies dynamic variables from the
    preferred tag for that resolved version (most recently assigned), if any.
    """


class OutboundSMSAgent(TypedDict, total=False):
    agent_id: Required[str]

    weight: Required[float]
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Union[int, str]
    """Agent version reference.

    Supports a numeric version (for example 3) or a tag/environment name (for
    example "prod"). The string "latest" resolves to the most recently created
    version (the largest version number), and "latest_published" resolves to the
    most recently published version. When a tag is provided, resolution uses that
    exact tag assignment (including its dynamic variables). If the tag exists but is
    currently unassigned, it resolves to latest. When a numeric version, latest, or
    latest_published is provided, resolution applies dynamic variables from the
    preferred tag for that resolved version (most recently assigned), if any.
    """
