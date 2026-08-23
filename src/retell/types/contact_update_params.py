# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ContactUpdateParams"]


class ContactUpdateParams(TypedDict, total=False):
    custom_fields: object
    """Values must match the types defined in CRM config custom fields.

    Set a value to null to clear it.
    """

    do_not_call: bool

    first_name: str
    """First name of the contact."""

    last_name: str
    """Last name of the contact."""
