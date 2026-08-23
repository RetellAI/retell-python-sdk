# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CRMConfig", "CRMAnalysisDataMapping", "CustomField"]


class CRMAnalysisDataMapping(BaseModel):
    analysis_data_name: str
    """Name of the post-call analysis field to read the value from.

    A value that does not match the contact field's type is skipped rather than
    failing the conversation.
    """

    field_name: str
    """Contact field to write to.

    Must be an existing built-in or custom contact field, and cannot be
    phone_number, which identifies the contact.
    """

    update_mode: Literal["overwrite", "fill_if_empty", "merge"]
    """How to reconcile the new value with what the contact already holds.

    `overwrite` always replaces it, `fill_if_empty` writes only when the field is
    empty, and `merge` combines the existing text with the new value. `merge` is
    available on string fields only.
    """


class CustomField(BaseModel):
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


class CRMConfig(BaseModel):
    org_id: str

    app_id: Optional[str] = None
    """The connected CRM integration app ID."""

    contact_columns_order: Optional[List[str]] = None
    """
    Preferred display order of contact fields, for clients that render contacts as a
    table. Not used by the API itself.
    """

    crm_analysis_data_mappings: Optional[List[CRMAnalysisDataMapping]] = None

    custom_fields: Optional[List[CustomField]] = None

    last_sync_timestamp: Optional[float] = None
    """Epoch milliseconds of the last successful sync."""
