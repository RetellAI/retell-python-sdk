# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["KnowledgeBaseAddSourcesParams", "KnowledgeBaseText"]


class KnowledgeBaseAddSourcesParams(TypedDict, total=False):
    knowledge_base_files: List[FileTypes]
    """Files to add to the knowledge base.

    Limit to 25 files, where each file is limited to 50MB.
    """

    knowledge_base_texts: Iterable[KnowledgeBaseText]
    """Texts to add to the knowledge base."""

    knowledge_base_urls: List[str]
    """URLs to be scraped and added to the knowledge base. Must be valid urls."""


class KnowledgeBaseText(TypedDict, total=False):
    text: Required[str]
    """Text to add to the knowledge base."""

    title: Required[str]
    """Title of the text."""
