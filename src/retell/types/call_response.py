# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .web_call_response import WebCallResponse
from .phone_call_response import PhoneCallResponse

__all__ = ["CallResponse"]

CallResponse: TypeAlias = Union[WebCallResponse, PhoneCallResponse]
