# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, TypedDict

__all__ = ["CallUpdateParams"]


class CallUpdateParams(TypedDict, total=False):
    custom_attributes: Dict[str, Union[str, float, bool]]
    """Custom attributes for the call, as key-value pairs.

    Each attribute must first be defined for your organization in the Retell
    dashboard (Call History → Actions → Custom attributes) before it can be set
    here. The object key must match the id of an existing organization-level custom
    attribute; keys that do not match a defined attribute are ignored and will not
    be saved. Values must be a string, number, or boolean.
    """

    data_storage_setting: Literal["everything", "everything_except_pii", "basic_attributes_only"]
    """Data storage setting for this call.

    Overrides the agent's default setting. "everything" stores all data,
    "everything_except_pii" excludes PII when possible, "basic_attributes_only"
    stores only metadata. Cannot be downgraded from more restrictive to less
    restrictive settings.
    """

    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object. Size limited to 50kB max.
    """
