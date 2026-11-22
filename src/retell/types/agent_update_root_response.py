# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["AgentUpdateRootResponse", "Tags"]


class Tags(BaseModel):
    dynamic_variables: Optional[Dict[str, str]] = None
    """Dynamic variable values supplied when a call uses this tag."""

    version: Optional[int] = None
    """Version that the tag points to. Absent when the tag follows the latest version."""


class AgentUpdateRootResponse(BaseModel):
    agent_id: str
    """Unique id of the agent."""

    is_suspended: bool
    """Whether the agent is currently suspended."""

    tags: Dict[str, Tags]
    """Environment tags for this agent, keyed by tag name.

    Every agent has prod and staging tags.
    """

    user_modified_timestamp: int
    """User modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """
