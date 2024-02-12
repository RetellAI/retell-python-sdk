# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AgentListResponse", "AgentListResponseItem"]


class AgentListResponseItem(BaseModel):
    agent_id: Optional[str] = None
    """Unique id of agent."""

    agent_name: Optional[str] = None
    """The name of the agent. Only used for your own reference."""

    last_modification_timestamp: Optional[int] = None
    """Last modification timestamp (milliseconds since epoch).

    Either the time of last update or creation if no updates available.
    """

    llm_websocket_url: Optional[str] = None
    """
    The URL we will establish LLM websocket for getting response, usually your
    server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
    request format (sent from us) and response format (send to us).
    """

    voice_id: Optional[str] = None
    """Unique voice id used for the agent.

    Find list of available voices and their preview in [Voices](/features/voices)
    and Dashboard.
    """


AgentListResponse = List[AgentListResponseItem]
