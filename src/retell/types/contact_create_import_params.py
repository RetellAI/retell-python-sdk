# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ContactCreateImportParams", "ColumnMapping"]


class ContactCreateImportParams(TypedDict, total=False):
    column_mapping: Required[Iterable[ColumnMapping]]
    """CSV headers mapped to contact fields.

    field_name is the contact field and external_field_name is the CSV header.
    Exactly one mapping must target phone_number. Unmapped columns are ignored.
    """

    upload_id: Required[str]
    """Id returned by upload-contact-import-file."""

    default_country: str
    """Country for parsing phone numbers without a country code. Defaults to US."""

    tags: SequenceNotStr[str]
    """Tags added to every contact in this import.

    Existing tags are preserved. Omit to leave tags unchanged.
    """


class ColumnMapping(TypedDict, total=False):
    external_field_name: Required[str]
    """Field on the CRM's contact object to map to.

    A name that does not exist there surfaces as an error on the sync job rather
    than at configuration time.
    """

    field_name: Required[str]
    """Retell contact field, built-in or custom, to map.

    Types must be compatible with the CRM field on both sides of the sync.
    """
