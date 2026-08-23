# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ContactGetBackfillJobStatusResponse"]


class ContactGetBackfillJobStatusResponse(BaseModel):
    status: Literal["queued", "running", "idle"]

    failed: Optional[float] = None
    """Number of items that errored so far."""

    start_timestamp: Optional[float] = None
    """Epoch milliseconds when the job started."""

    succeeded: Optional[float] = None
    """Number of items processed successfully so far."""

    triggered_by: Optional[Literal["manual", "cron"]] = None
    """
    Whether the job was started by an explicit API call (`manual`) or by the
    scheduled sync (`cron`).
    """
