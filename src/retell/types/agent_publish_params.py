# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentPublishParams"]


class AgentPublishParams(TypedDict, total=False):
    version: Required[int]

    version_description: str
