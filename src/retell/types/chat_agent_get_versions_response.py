# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .chat_agent_response import ChatAgentResponse

__all__ = ["ChatAgentGetVersionsResponse"]

ChatAgentGetVersionsResponse: TypeAlias = List[ChatAgentResponse]
