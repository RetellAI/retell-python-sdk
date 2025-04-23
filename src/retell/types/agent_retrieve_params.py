# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AgentRetrieveParams"]


class AgentRetrieveParams(TypedDict, total=False):
    version: int
    """Optional version of the API to use for this request. Default to latest version."""
