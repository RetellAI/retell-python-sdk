# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    llm_websocket_url: Required[str]
    """
    The URL we will establish LLM websocket for getting response, usually your
    server. Check out [LLM WebSocket](/api-references/llm-websocket) for more about
    request format (sent from us) and response format (send to us).
    """

    voice_id: Required[str]
    """Unique voice id used for the agent.

    Find list of available voices and their preview in [Voices](/features/voices)
    and Dashboard.
    """

    agent_name: str
    """The name of the agent. Only used for your own reference."""
