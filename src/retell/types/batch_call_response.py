# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["BatchCallResponse"]


class BatchCallResponse(BaseModel):
    batch_call_id: str
    """Unique id of the batch call."""

    from_number: str

    name: str

    scheduled_timestamp: float

    total_task_count: float
    """Number of tasks within the batch call"""
