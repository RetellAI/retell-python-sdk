# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ChatRecordMessageParams", "Variant0", "Variant1", "Variant1Metadata"]


class Variant0(TypedDict, total=False):
    idempotency_key: Required[str]

    message: Required[str]

    role: Required[Literal["user"]]


class Variant1(TypedDict, total=False):
    idempotency_key: Required[str]

    message: Required[str]

    role: Required[Literal["transfer_target"]]

    metadata: Variant1Metadata


class Variant1Metadata(TypedDict, total=False):
    transfer_target_name: str


ChatRecordMessageParams: TypeAlias = Union[Variant0, Variant1]
