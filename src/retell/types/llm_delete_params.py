# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["LlmDeleteParams"]


class LlmDeleteParams(TypedDict, total=False):
    force_delete: bool
    """
    By default the deletion is rejected with a 400 if any agent still uses this
    Retell LLM as its response engine. Set to true to delete it anyway, which leaves
    those agents pointing at a Retell LLM that no longer exists.
    """
