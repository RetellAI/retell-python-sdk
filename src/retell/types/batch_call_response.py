# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BatchCallResponse", "CallTimeWindow", "CallTimeWindowWindow"]


class CallTimeWindowWindow(BaseModel):
    end: float
    """End time in minutes since local midnight."""

    start: float
    """Start time in minutes since local midnight."""


class CallTimeWindow(BaseModel):
    """Canonicalized minutes-based time windows.

    Present only if specified when the batch call was created or updated. See CallTimeWindow for format details ([startMin, endMin) in local minutes; no cross-midnight).
    """

    windows: List[CallTimeWindowWindow]
    """List of TimeWindow (start/end in minutes since local midnight)."""

    day: Optional[List[Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]]] = None
    """Optional list of days to which the windows apply.

    If omitted or empty, windows apply to every day.
    """

    timezone: Optional[str] = None
    """IANA timezone (e.g.

    America/Los_Angeles). Defaults to America/Los_Angeles if omitted.
    """


class BatchCallResponse(BaseModel):
    batch_call_id: str
    """Unique id of the batch call."""

    from_number: str

    name: str

    scheduled_timestamp: float

    total_task_count: float
    """Number of tasks within the batch call"""

    call_time_window: Optional[CallTimeWindow] = None
    """Canonicalized minutes-based time windows.

    Present only if specified when the batch call was created or updated. See
    CallTimeWindow for format details ([startMin, endMin) in local minutes; no
    cross-midnight).
    """
