# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "ContactListParams",
    "FilterCriteria",
    "FilterCriteriaContactID",
    "FilterCriteriaCustomField",
    "FilterCriteriaCustomFieldStringFilter",
    "FilterCriteriaCustomFieldNumberFilter",
    "FilterCriteriaCustomFieldBooleanFilter",
    "FilterCriteriaCustomFieldRangeFilter",
    "FilterCriteriaCustomFieldEnumFilter",
    "FilterCriteriaCustomFieldPresentFilter",
    "FilterCriteriaDoNotCall",
    "FilterCriteriaExternalID",
    "FilterCriteriaExternalIDStringFilter",
    "FilterCriteriaExternalIDPresentFilter",
    "FilterCriteriaLastConversationTimestamp",
    "FilterCriteriaLastConversationTimestampNumberFilter",
    "FilterCriteriaLastConversationTimestampRangeFilter",
    "FilterCriteriaPhoneNumber",
]


class ContactListParams(TypedDict, total=False):
    filter_criteria: FilterCriteria
    """Filter criteria for contacts.

    All conditions are implicitly connected with AND. first_name and last_name are
    not filterable here; use search_query to match on those.
    """

    limit: float
    """Maximum number of contacts to return."""

    pagination_key: str
    """Base64url-encoded pagination key from a previous response."""

    search_query: str
    """
    Case-insensitive substring match against phone number, first name, last name,
    external ID, and custom field values. This is the only way to match on a
    contact's name.
    """

    skip: float
    """Number of records to skip for offset-based pagination."""

    sort_order: Literal["asc", "desc"]
    """Sort contacts by `last_conversation_timestamp` in ascending or descending order.

    Contacts that have never been contacted sort as if their timestamp were 0.
    """


class FilterCriteriaContactID(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaCustomFieldStringFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomFieldNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomFieldBooleanFilter(TypedDict, total=False):
    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomFieldRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomFieldEnumFilter(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]

    key: str
    """The field name to filter on."""


class FilterCriteriaCustomFieldPresentFilter(TypedDict, total=False):
    op: Required[Literal["pr", "np"]]
    """pr: present (has value), np: not present"""

    type: Required[Literal["present"]]

    key: str
    """The field name to filter on."""


FilterCriteriaCustomField: TypeAlias = Union[
    FilterCriteriaCustomFieldStringFilter,
    FilterCriteriaCustomFieldNumberFilter,
    FilterCriteriaCustomFieldBooleanFilter,
    FilterCriteriaCustomFieldRangeFilter,
    FilterCriteriaCustomFieldEnumFilter,
    FilterCriteriaCustomFieldPresentFilter,
]


class FilterCriteriaDoNotCall(TypedDict, total=False):
    """Filter by whether the contact is marked do-not-call."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[bool]


class FilterCriteriaExternalIDStringFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteriaExternalIDPresentFilter(TypedDict, total=False):
    op: Required[Literal["pr", "np"]]
    """pr: present (has value), np: not present"""

    type: Required[Literal["present"]]


FilterCriteriaExternalID: TypeAlias = Union[FilterCriteriaExternalIDStringFilter, FilterCriteriaExternalIDPresentFilter]


class FilterCriteriaLastConversationTimestampNumberFilter(TypedDict, total=False):
    op: Required[Literal["eq", "ne", "gt", "ge", "lt", "le"]]
    """
    eq: equal, ne: not equal, gt: greater than, ge: greater than or equal, lt: less
    than, le: less than or equal
    """

    type: Required[Literal["number"]]

    value: Required[float]


class FilterCriteriaLastConversationTimestampRangeFilter(TypedDict, total=False):
    op: Required[Literal["bt"]]
    """bt: between"""

    type: Required[Literal["range"]]

    value: Required[Iterable[float]]
    """[lower_bound, upper_bound]"""


FilterCriteriaLastConversationTimestamp: TypeAlias = Union[
    FilterCriteriaLastConversationTimestampNumberFilter, FilterCriteriaLastConversationTimestampRangeFilter
]


class FilterCriteriaPhoneNumber(TypedDict, total=False):
    """Filter by phone number.

    Stored in E.164, so an `eq` filter needs the full number.
    """

    op: Required[Literal["eq", "ne", "sw", "ew", "co"]]
    """eq: equal, ne: not equal, sw: starts with, ew: ends with, co: contains"""

    type: Required[Literal["string"]]

    value: Required[str]


class FilterCriteria(TypedDict, total=False):
    """Filter criteria for contacts.

    All conditions are implicitly connected with AND. first_name and last_name are not filterable here; use search_query to match on those.
    """

    contact_id: FilterCriteriaContactID

    custom_fields: Iterable[FilterCriteriaCustomField]
    """Filter by custom contact fields defined in CRM config."""

    do_not_call: FilterCriteriaDoNotCall
    """Filter by whether the contact is marked do-not-call."""

    external_id: FilterCriteriaExternalID
    """Filter by the record id in the connected CRM.

    Use a `present` filter to separate synced from unsynced contacts.
    """

    last_conversation_timestamp: FilterCriteriaLastConversationTimestamp
    """Filter by when the contact was last spoken to, in epoch milliseconds."""

    phone_number: FilterCriteriaPhoneNumber
    """Filter by phone number.

    Stored in E.164, so an `eq` filter needs the full number.
    """
