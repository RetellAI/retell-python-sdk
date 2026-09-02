# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["AgentRepairParams"]


class AgentRepairParams(TypedDict, total=False):
    version: Union[str, int]
    """Optional version of the agent to repair.

    Default to latest version. Published versions are immutable and cannot be
    repaired.
    """
