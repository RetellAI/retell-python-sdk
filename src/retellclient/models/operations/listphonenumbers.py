"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import phonenumber as components_phonenumber
from typing import List, Optional


@dataclasses.dataclass
class ListPhoneNumbersResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    phone_numbers: Optional[List[components_phonenumber.PhoneNumber]] = dataclasses.field(default=None)
    r"""Successfully retrieved all phone number objects."""
    

