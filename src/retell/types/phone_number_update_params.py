# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    inbound_agent_id: Optional[str]
    """Unique id of agent to bind to the number.

    The number will automatically use the agent when receiving inbound calls. If set
    to null, this number would not accept inbound call.
    """

    inbound_agent_version: Optional[int]
    """Version of the inbound agent to bind to the number.

    If not provided, will default to 0.
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

    If not provided, will default to 0.
    """
