# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentUpdateRootParams", "Tags", "TagsProd", "TagsStaging", "Tag", "TagAgentRootTagUpdate"]


class AgentUpdateRootParams(TypedDict, total=False):
    tags: Tags
    """Environment tags to add, change, or delete, keyed by tag name.

    Set a tag to an object to add or change it, or to null to delete it. Tags you
    leave out stay as they are. The prod and staging tags cannot be deleted. An
    agent can have up to 10 tags. Tag names must be 1-20 characters, start with a
    lowercase letter, use only lowercase letters, digits, underscores, or hyphens,
    and cannot be "latest", "latest_published", or "v" followed only by digits, such
    as "v2".
    """

    if_match: Annotated[str, PropertyInfo(alias="If-Match")]


class TagsProd(TypedDict, total=False):
    dynamic_variables: Optional[Dict[str, str]]
    """Dynamic variable values supplied when a call uses this tag.

    Replaces all of the tag's current values. Set to null to remove them. If
    omitted, the tag keeps its current values.
    """

    version: Optional[int]
    """Version for the tag to point to.

    Set to null to make the tag follow the latest version. If omitted, the tag keeps
    its current version.
    """


class TagsStaging(TypedDict, total=False):
    dynamic_variables: Optional[Dict[str, str]]
    """Dynamic variable values supplied when a call uses this tag.

    Replaces all of the tag's current values. Set to null to remove them. If
    omitted, the tag keeps its current values.
    """

    version: Optional[int]
    """Version for the tag to point to.

    Set to null to make the tag follow the latest version. If omitted, the tag keeps
    its current version.
    """


class TagAgentRootTagUpdate(TypedDict, total=False):
    dynamic_variables: Optional[Dict[str, str]]
    """Dynamic variable values supplied when a call uses this tag.

    Replaces all of the tag's current values. Set to null to remove them. If
    omitted, the tag keeps its current values.
    """

    version: Optional[int]
    """Version for the tag to point to.

    Set to null to make the tag follow the latest version. If omitted, the tag keeps
    its current version.
    """


Tag: TypeAlias = Union[TagAgentRootTagUpdate, Optional[object]]


class Tags(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=Tag,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Environment tags to add, change, or delete, keyed by tag name.

    Set a tag to an object to add or change it, or to null to delete it. Tags you leave out stay as they are. The prod and staging tags cannot be deleted. An agent can have up to 10 tags. Tag names must be 1-20 characters, start with a lowercase letter, use only lowercase letters, digits, underscores, or hyphens, and cannot be "latest", "latest_published", or "v" followed only by digits, such as "v2".
    """

    prod: TagsProd

    staging: TagsStaging
