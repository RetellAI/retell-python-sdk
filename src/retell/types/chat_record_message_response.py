# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ChatRecordMessageResponse"]


class ChatRecordMessageResponse(BaseModel):
    created_timestamp: int

    message_id: str
