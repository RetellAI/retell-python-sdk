# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "BatchTestResponse",
    "ResponseEngine",
    "ResponseEngineResponseEngineRetellLm",
    "ResponseEngineResponseEngineCustomLm",
    "ResponseEngineResponseEngineConversationFlow",
]


class ResponseEngineResponseEngineRetellLm(BaseModel):
    llm_id: str
    """id of the Retell LLM Response Engine."""

    type: Literal["retell-llm"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Retell LLM Response Engine."""


class ResponseEngineResponseEngineCustomLm(BaseModel):
    llm_websocket_url: str
    """LLM websocket url of the custom LLM."""

    type: Literal["custom-llm"]
    """type of the Response Engine."""


class ResponseEngineResponseEngineConversationFlow(BaseModel):
    conversation_flow_id: str
    """ID of the Conversation Flow Response Engine."""

    type: Literal["conversation-flow"]
    """type of the Response Engine."""

    version: Optional[float] = None
    """Version of the Conversation Flow Response Engine."""


ResponseEngine: TypeAlias = Union[
    ResponseEngineResponseEngineRetellLm,
    ResponseEngineResponseEngineCustomLm,
    ResponseEngineResponseEngineConversationFlow,
]


class BatchTestResponse(BaseModel):
    creation_timestamp: int
    """Timestamp when the batch job was created (milliseconds since epoch)"""

    error_count: int
    """Number of test cases that encountered errors"""

    fail_count: int
    """Number of test cases that failed"""

    pass_count: int
    """Number of test cases that passed"""

    response_engine: ResponseEngine

    status: Literal["in_progress", "complete"]
    """Status of the batch job"""

    test_case_batch_job_id: str
    """Unique identifier for the test case batch job"""

    total_count: int
    """Total number of test cases in the batch"""

    user_modified_timestamp: int
    """Timestamp when the batch job was last modified (milliseconds since epoch)"""
