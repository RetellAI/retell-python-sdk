# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "PhoneNumberSearchParams",
    "FilterCriteria",
    "FilterCriteriaBrandedCall",
    "FilterCriteriaInboundAgentTags",
    "FilterCriteriaInboundAgent",
    "FilterCriteriaOutboundAgentTags",
    "FilterCriteriaOutboundAgent",
    "FilterCriteriaPhoneNumberType",
    "FilterCriteriaSMS",
    "FilterCriteriaSpamStatus",
    "FilterCriteriaVerifiedNumber",
]


class PhoneNumberSearchParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return."""

    pagination_key: str
    """Pagination key for fetching the next page."""

    sort_order: Literal["ascending", "descending"]
    """Sort order for results."""

    filter_criteria: FilterCriteria
    """Filters for listing phone numbers. All provided filters are connected with AND."""


class FilterCriteriaBrandedCall(TypedDict, total=False):
    """Matches numbers that have an active branded call registration."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[Literal[True]]


class FilterCriteriaInboundAgentTags(TypedDict, total=False):
    """Agent version tags, such as `production`.

    Without `inbound_agents`, matches numbers whose inbound agent is bound through one of these tags.
    """

    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]


class FilterCriteriaInboundAgent(TypedDict, total=False):
    agent_id: Required[str]

    version: Iterable[float]


class FilterCriteriaOutboundAgentTags(TypedDict, total=False):
    """Agent version tags, such as `production`.

    Without `outbound_agents`, matches numbers whose outbound agent is bound through one of these tags.
    """

    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[SequenceNotStr[str]]


class FilterCriteriaOutboundAgent(TypedDict, total=False):
    agent_id: Required[str]

    version: Iterable[float]


class FilterCriteriaPhoneNumberType(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["retell-twilio", "retell-telnyx", "retell-bandwidth", "custom"]]]


class FilterCriteriaSMS(TypedDict, total=False):
    """
    Matches numbers that have a custom SMS configuration or an approved A2P application.
    """

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[Literal[True]]


class FilterCriteriaSpamStatus(TypedDict, total=False):
    op: Required[Literal["in"]]
    """in: value is one of the listed values"""

    type: Required[Literal["enum"]]

    value: Required[List[Literal["clean", "spam", "unknown", "not_enrolled"]]]


class FilterCriteriaVerifiedNumber(TypedDict, total=False):
    """Matches numbers that have an active phone verification."""

    op: Required[Literal["eq"]]

    type: Required[Literal["boolean"]]

    value: Required[Literal[True]]


class FilterCriteria(TypedDict, total=False):
    """Filters for listing phone numbers. All provided filters are connected with AND."""

    branded_call: FilterCriteriaBrandedCall
    """Matches numbers that have an active branded call registration."""

    inbound_agent_tags: FilterCriteriaInboundAgentTags
    """Agent version tags, such as `production`.

    Without `inbound_agents`, matches numbers whose inbound agent is bound through
    one of these tags.
    """

    inbound_agents: Iterable[FilterCriteriaInboundAgent]
    """Matches numbers with any listed agent among their inbound agents.

    For an agent with `version`, a number matches when it is bound to a listed
    version or to a tag in `inbound_agent_tags`.
    """

    outbound_agent_tags: FilterCriteriaOutboundAgentTags
    """Agent version tags, such as `production`.

    Without `outbound_agents`, matches numbers whose outbound agent is bound through
    one of these tags.
    """

    outbound_agents: Iterable[FilterCriteriaOutboundAgent]
    """Matches numbers with any listed agent among their outbound agents.

    For an agent with `version`, a number matches when it is bound to a listed
    version or to a tag in `outbound_agent_tags`.
    """

    phone_number_type: FilterCriteriaPhoneNumberType

    query: str
    """Substring match against the phone number, pretty phone number, or nickname.

    The nickname match ignores case.
    """

    sms: FilterCriteriaSMS
    """
    Matches numbers that have a custom SMS configuration or an approved A2P
    application.
    """

    spam_status: FilterCriteriaSpamStatus

    verified_number: FilterCriteriaVerifiedNumber
    """Matches numbers that have an active phone verification."""
