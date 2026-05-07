# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentGetVersionsParams"]


class AgentGetVersionsParams(TypedDict, total=False):
    include_response_engine: bool
    """
    When true, each returned agent version includes a response_engine_data field
    with the hydrated response engine (full retell-llm or conversation-flow
    configuration) bound to that version.
    """
