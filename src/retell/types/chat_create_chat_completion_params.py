# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ChatCreateChatCompletionParams"]


class ChatCreateChatCompletionParams(TypedDict, total=False):
    chat_id: Required[str]
    """Unique id of the chat to create completion."""

    content: Required[str]
    """user message to generate agent chat completion."""
