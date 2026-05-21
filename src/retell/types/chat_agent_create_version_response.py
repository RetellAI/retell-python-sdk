# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .agent_response import AgentResponse
from .chat_agent_response import ChatAgentResponse

__all__ = ["ChatAgentCreateVersionResponse"]

ChatAgentCreateVersionResponse: TypeAlias = Union[AgentResponse, ChatAgentResponse]
