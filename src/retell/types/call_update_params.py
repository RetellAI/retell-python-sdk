# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
