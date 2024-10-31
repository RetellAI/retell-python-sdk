# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "KnowledgeBaseResponse",
    "KnowledgeBaseSource",
    "KnowledgeBaseSourceKnowledgeBaseSourceDocument",
    "KnowledgeBaseSourceKnowledgeBaseSourceText",
    "KnowledgeBaseSourceKnowledgeBaseSourceURL",
]


class KnowledgeBaseSourceKnowledgeBaseSourceDocument(BaseModel):
    file_url: str
    """URL of the document stored."""

    filename: str
    """Filename of the document."""

    source_id: str
    """Unique id of the knowledge base source."""

    type: Literal["document"]
    """Type of the knowledge base source."""


class KnowledgeBaseSourceKnowledgeBaseSourceText(BaseModel):
    content_url: str
    """URL of the text content stored."""

    source_id: str
    """Unique id of the knowledge base source."""

    title: str
    """Title of the text."""

    type: Literal["text"]
    """Type of the knowledge base source."""


class KnowledgeBaseSourceKnowledgeBaseSourceURL(BaseModel):
    source_id: str
    """Unique id of the knowledge base source."""

    type: Literal["url"]
    """Type of the knowledge base source."""

    url: str
    """URL used to be scraped and added to the knowledge base."""


KnowledgeBaseSource: TypeAlias = Union[
    KnowledgeBaseSourceKnowledgeBaseSourceDocument,
    KnowledgeBaseSourceKnowledgeBaseSourceText,
    KnowledgeBaseSourceKnowledgeBaseSourceURL,
]


class KnowledgeBaseResponse(BaseModel):
    knowledge_base_id: str
    """Unique id of the knowledge base."""

    knowledge_base_name: str
    """Name of the knowledge base. Must be less than 40 characters."""

    status: Literal["in_progress", "complete", "error"]
    """Status of the knowledge base.

    When it's created and being processed, it's "in_progress". When the processing
    is done, it's "complete". When there's an error in processing, it's "error".
    """

    enable_auto_refresh: Optional[bool] = None
    """Whether to enable auto refresh for the knowledge base urls.

    If set to true, will retrieve the data from the specified url every 12 hours.
    """

    knowledge_base_sources: Optional[List[KnowledgeBaseSource]] = None
    """Sources of the knowledge base.

    Will be populated after the processing is done (when status is "complete").
    """

    last_refreshed_timestamp: Optional[int] = None
    """Last refreshed timestamp (milliseconds since epoch).

    Only applicable when enable_auto_refresh is true.
    """
