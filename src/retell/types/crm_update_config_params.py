# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CRMUpdateConfigParams", "CRMAnalysisDataMapping", "CustomField"]


class CRMUpdateConfigParams(TypedDict, total=False):
    app_id: Optional[str]
    """ID of the CRM app to link.

    Pass null to unlink, which stops syncing. Changing it resets the sync cursor, so
    the next sync re-reads every contact from the new CRM.
    """

    contact_columns_order: SequenceNotStr[str]
    """
    Preferred display order of contact fields, for clients that render contacts as a
    table. Not used by the API itself.
    """

    crm_analysis_data_mappings: Iterable[CRMAnalysisDataMapping]
    """Replaces the stored list."""

    custom_fields: Iterable[CustomField]
    """Replaces the stored list.

    Names must be snake_case and cannot collide with a built-in contact field or
    start with `contact`/`external`. Removing a field that an analysis data mapping
    still targets is rejected — send crm_analysis_data_mappings in the same request
    to retarget or drop those mappings.
    """


class CRMAnalysisDataMapping(TypedDict, total=False):
    analysis_data_name: Required[str]
    """Name of the post-call analysis field to read the value from.

    A value that does not match the contact field's type is skipped rather than
    failing the conversation.
    """

    field_name: Required[str]
    """Contact field to write to.

    Must be an existing built-in or custom contact field, and cannot be
    phone_number, which identifies the contact.
    """

    update_mode: Required[Literal["overwrite", "fill_if_empty", "merge"]]
    """How to reconcile the new value with what the contact already holds.

    `overwrite` always replaces it, `fill_if_empty` writes only when the field is
    empty, and `merge` combines the existing text with the new value. `merge` is
    available on string fields only.
    """


class CustomField(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["string", "number", "boolean", "date", "datetime", "enum"]]

    description: str

    label: str
    """Display label for the field."""

    options: SequenceNotStr[str]
    """Allowed values.

    Required when `type` is `enum`, where a value is rejected unless it appears
    here; ignored for every other type.
    """
