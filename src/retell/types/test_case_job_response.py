# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .test_case_definition_response import TestCaseDefinitionResponse

__all__ = ["TestCaseJobResponse"]


class TestCaseJobResponse(BaseModel):
    __test__ = False
    creation_timestamp: int
    """Timestamp when the test case job was created (milliseconds since epoch)"""

    status: Literal["in_progress", "pass", "fail", "error"]
    """Status of the test case job"""

    test_case_definition_id: str
    """ID of the test case definition used"""

    test_case_definition_snapshot: TestCaseDefinitionResponse
    """Snapshot of the test case definition at time of execution"""

    test_case_job_id: str
    """Unique identifier for the test case job"""

    user_modified_timestamp: int
    """Timestamp when the test case job was last modified (milliseconds since epoch)"""

    result_explanation: Optional[str] = None
    """Explanation of the test result"""

    transcript_snapshot: Optional[object] = None
    """Snapshot of the transcript generated during test execution.

    Can be either ConversationFlowPlaygroundSnapshot or
    MultiStatePromptPlaygroundSnapshot
    """
