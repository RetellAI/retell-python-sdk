# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "KnowledgeBaseResponse",
    "IngestionLimits",
    "RemainingIngestionQuota",
    "KnowledgeBaseSource",
    "KnowledgeBaseSourceKnowledgeBaseSourceDocument",
    "KnowledgeBaseSourceKnowledgeBaseSourceText",
    "KnowledgeBaseSourceKnowledgeBaseSourceURL",
]


class IngestionLimits(BaseModel):
    """Effective rolling 30-day ingestion limits.

    Each KB has an independent budget. Lifetime fill allowance
    and structural source-count caps are separate.
    """

    files: int
    """Shared limit for uploaded documents and all connected-file sources."""

    texts: int
    """Limit for pasted-text sources."""

    urls: int
    """Limit for URL sources."""


class RemainingIngestionQuota(BaseModel):
    """
    Ingestion quota available to this knowledge base at response time.
    Includes unused lifetime fill allowance plus remaining rolling
    30-day per-KB capacity. Pending reservations already consume
    capacity. Default per-KB rolling limits are 25 files, 50 texts,
    and 200 URLs; organization-specific increases are reflected in
    these counts.
    Legacy knowledge bases without fill allowance receive rolling
    capacity only. Deleting sources does not restore ingestion quota.
    These counts do not include the separate limits on how many sources
    a KB can hold, and do not guarantee a concurrent request will succeed.
    Create and add-source responses include reservations for accepted
    sources; background discovery and processing may change the counts.
    Returns null if current usage cannot be read. Null means unavailable,
    not zero remaining capacity. Configured ingestion_limits are still
    returned. Quota enforcement remains required for ingestion requests.
    """

    files: int
    """Remaining additions in the shared uploaded-file and connector bucket."""

    texts: int
    """Remaining pasted-text additions."""

    urls: int
    """Remaining URL additions."""


class KnowledgeBaseSourceKnowledgeBaseSourceDocument(BaseModel):
    file_size: float
    """File size in bytes."""

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
    ingestion_limits: IngestionLimits
    """Effective rolling 30-day ingestion limits.

    Each KB has an independent budget. Lifetime fill allowance and structural
    source-count caps are separate.
    """

    knowledge_base_id: str
    """Unique id of the knowledge base."""

    knowledge_base_name: str
    """Name of the knowledge base. Must be less than 40 characters."""

    remaining_ingestion_quota: Optional[RemainingIngestionQuota] = None
    """
    Ingestion quota available to this knowledge base at response time. Includes
    unused lifetime fill allowance plus remaining rolling 30-day per-KB capacity.
    Pending reservations already consume capacity. Default per-KB rolling limits are
    25 files, 50 texts, and 200 URLs; organization-specific increases are reflected
    in these counts. Legacy knowledge bases without fill allowance receive rolling
    capacity only. Deleting sources does not restore ingestion quota. These counts
    do not include the separate limits on how many sources a KB can hold, and do not
    guarantee a concurrent request will succeed. Create and add-source responses
    include reservations for accepted sources; background discovery and processing
    may change the counts. Returns null if current usage cannot be read. Null means
    unavailable, not zero remaining capacity. Configured ingestion_limits are still
    returned. Quota enforcement remains required for ingestion requests.
    """

    status: Literal["in_progress", "complete", "error", "refreshing_in_progress"]
    """Current processing state of the knowledge base:

    - `in_progress`: Initial indexing is running. Source metadata may be incomplete
      until indexing finishes.
    - `complete`: Initial indexing or the latest update or refresh finished.
      Individual source failures may still be reported in `error_messages`.
    - `error`: Initial indexing failed. Source metadata may be incomplete.
    - `refreshing_in_progress`: An existing knowledge base is being updated. This
      includes indexing newly added sources or running a manual or automatic refresh
      that re-indexes URLs, Google Drive files, Microsoft OneDrive files, and pages
      from auto-crawling paths. Previously indexed sources remain available during
      the update, and the source list may change when it finishes.
    """

    enable_auto_refresh: Optional[bool] = None
    """
    Whether eligible URL and connected-file sources refresh automatically on a daily
    cadence.
    """

    knowledge_base_sources: Optional[List[KnowledgeBaseSource]] = None
    """Sources of the knowledge base.

    Will be populated after the processing is done (when status is "complete").
    """

    last_refreshed_timestamp: Optional[int] = None
    """Last refreshed timestamp (milliseconds since epoch).

    Only applicable when enable_auto_refresh is true.
    """

    max_chunk_size: Optional[int] = None
    """Maximum number of characters per chunk when splitting knowledge base content."""

    min_chunk_size: Optional[int] = None
    """Minimum number of characters per chunk.

    Chunks smaller than this are merged with adjacent chunks.
    """
