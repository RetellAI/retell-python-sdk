# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CRMGetSchemaParams"]


class CRMGetSchemaParams(TypedDict, total=False):
    app_id: str
    """ID of the CRM app to read the schema from.

    Defaults to the app linked in the organization's CRM configuration. Naming a
    different app additionally requires the App.Read scope.
    """
