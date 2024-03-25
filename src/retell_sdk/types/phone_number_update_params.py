# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PhoneNumberUpdateParams"]


class PhoneNumberUpdateParams(TypedDict, total=False):
    agent_id: Required[str]
    """Unique id of agent to bind to number.

    The number will automatically use the agent when doing inbound / outbound calls.
    """
