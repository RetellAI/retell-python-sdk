# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CRMGetSchemaResponse", "Field"]


class Field(BaseModel):
    name: str

    type: Literal["string", "number", "boolean", "date", "datetime", "enum"]

    description: Optional[str] = None

    label: Optional[str] = None
    """Display label for the field."""

    options: Optional[List[str]] = None
    """Allowed values.

    Required when `type` is `enum`, where a value is rejected unless it appears
    here; ignored for every other type.
    """


class CRMGetSchemaResponse(BaseModel):
    fields: List[Field]

    provider: str
    """CRM provider name."""
