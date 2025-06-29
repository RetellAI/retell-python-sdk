# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateParams"]


class ChatCreateParams(TypedDict, total=False):
    agent_id: Required[str]
    """The chat agent to use for the call."""

    agent_version: int
    """The version of the chat agent to use for the chat.

    If not provided, will default to latest version.
    """

    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    chat. Not used for processing. You can later get this field from the chat
    object.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """
