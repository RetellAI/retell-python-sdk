# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "PhoneNumberResponse",
    "InboundAgent",
    "InboundSMSAgent",
    "OutboundAgent",
    "OutboundSMSAgent",
    "SipOutboundTrunkConfig",
]


class InboundAgent(BaseModel):
    agent_id: str

    weight: float
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Optional[int] = None


class InboundSMSAgent(BaseModel):
    agent_id: str

    weight: float
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Optional[int] = None


class OutboundAgent(BaseModel):
    agent_id: str

    weight: float
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Optional[int] = None


class OutboundSMSAgent(BaseModel):
    agent_id: str

    weight: float
    """The weight of the agent.

    When used in a list of agents, the total weights must add up to 1.
    """

    agent_version: Optional[int] = None


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

    allowed_inbound_country_list: Optional[List[str]] = None
    """List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.

    If not set or empty, calls from all countries are allowed.
    """

    allowed_outbound_country_list: Optional[List[str]] = None
    """List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed.

    If not set or empty, calls to all countries are allowed.
    """

    area_code: Optional[int] = None
    """Area code of the number to obtain.

    Format is a 3 digit integer. Currently only supports US area code.
    """

    fallback_number: Optional[str] = None
    """Enterprise only.

    Phone number to transfer inbound calls to when organization is in outage mode.
    Can be either a Retell phone number or an external number. Cannot be the same as
    this phone number, and cannot be a number that already has its own fallback
    configured (prevents nested forwarding).
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

    inbound_agents: Optional[List[InboundAgent]] = None
    """Inbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each inbound call,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to inbound_agent_id.
    """

    inbound_sms_agents: Optional[List[InboundSMSAgent]] = None
    """Inbound SMS agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each inbound SMS,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to inbound_sms_agent_id.
    """

    inbound_sms_webhook_url: Optional[str] = None
    """
    If set, will send a webhook for inbound SMS, where you can override agent id,
    set dynamic variables and other fields specific to that chat.
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

    outbound_agents: Optional[List[OutboundAgent]] = None
    """Outbound agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound call,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to outbound_agent_id.
    """

    outbound_sms_agents: Optional[List[OutboundSMSAgent]] = None
    """Outbound SMS agents to bind to the number with weights.

    If set and non-empty, one agent will be picked randomly for each outbound SMS,
    with probability proportional to the weight. Total weights must add up to 1. If
    not set or empty, fallback to outbound_sms_agent_id.
    """

    phone_number_pretty: Optional[str] = None
    """Pretty printed phone number, provided for your reference."""

    sip_outbound_trunk_config: Optional[SipOutboundTrunkConfig] = None
