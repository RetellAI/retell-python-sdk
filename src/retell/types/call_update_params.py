# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

__all__ = ["CallUpdateParams"]


class CallUpdateParams(TypedDict, total=False):
    metadata: object
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object. Size limited to 50kB max.
    """

    opt_out_sensitive_data_storage: bool
    """
    Whether this call opts out of sensitive data storage like transcript, recording,
    logging. Can only be changed from false to true.
    """

    override_dynamic_variables: Optional[Dict[str, str]]
    """Override dynamic varaibles represented as key-value pairs of strings.

    Setting this will override or add the dynamic variables set in the agent during
    the call. Only need to set the delta where you want to override, no need to set
    the entire dynamic variables object.
    """
