# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConcurrencyRetrieveResponse"]


class ConcurrencyRetrieveResponse(BaseModel):
    concurrency_limit: Optional[int] = None
    """The concurrency limit of the user."""

    current_concurrency: Optional[int] = None
    """The current concurrency of the user."""
