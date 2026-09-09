# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CallTakeOverLiveParams"]


class CallTakeOverLiveParams(TypedDict, total=False):
    participant_id: Required[str]
    """
    The id of the live-listen participant to upgrade, obtained when joining via
    /v2/listen-live-call.
    """
