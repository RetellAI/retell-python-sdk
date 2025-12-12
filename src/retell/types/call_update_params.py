# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["CallUpdateParams"]


class CallUpdateParams(TypedDict, total=False):
    custom_attributes: Dict[str, Union[str, float, bool]]
    """Custom attributes for the call"""

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

    override_dynamic_variables: Optional[Dict[str, str]]
    """Override dynamic varaibles represented as key-value pairs of strings.

    Setting this will override or add the dynamic variables set in the agent during
    the call. Only need to set the delta where you want to override, no need to set
    the entire dynamic variables object. Setting this to null will remove any
    existing override.
    """
