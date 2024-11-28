# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ConcurrencyRetrieveResponse"]


class ConcurrencyRetrieveResponse(BaseModel):
    base_concurrency: Optional[int] = None
    """The free concurrency limit of the org."""

    concurrency_limit: Optional[int] = None
    """
    The total concurrency limit (at max how many ongoing calls one can make) of the
    org. This should be the sum of `base_concurrency` and `purchased_concurrency`.
    """

    concurrency_purchase_limit: Optional[int] = None
    """The maximum amount of concurrency that the org can purchase."""

    current_concurrency: Optional[int] = None
    """The current concurrency (amount of ongoing calls) of the org."""

    purchased_concurrency: Optional[int] = None
    """The amount of concurrency that the org has already purchased."""

    remaining_purchase_limit: Optional[int] = None
    """The remaining amount of concurrency that the org can purchase.

    This is the difference between `concurrency_purchase_limit` and
    `purchased_concurrency`.
    """
