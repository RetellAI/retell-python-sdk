# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["CallUpdateLiveParams", "CallControl", "FieldsToOverride"]


class CallUpdateLiveParams(TypedDict, total=False):
    call_control: CallControl
    """Live agent control.

    At least one of `additional_context` or `trigger_response` should be supplied;
    an empty object is a no-op.
    """

    fields_to_override: FieldsToOverride
    """Call fields to override on the running call.

    Each field is applied to the live call immediately; omitted fields are left
    unchanged.
    """


class CallControl(TypedDict, total=False):
    """Live agent control.

    At least one of `additional_context` or `trigger_response` should be supplied; an empty object is a no-op.
    """

    additional_context: str
    """
    Free-form text appended to the call transcript with role "injected" and injected
    into the next agent response context. Must be non-empty.
    """

    trigger_response: bool
    """Only `true` has an effect.

    When set, if the agent is currently speaking the response is interrupted and a
    new one is generated. If the agent has already finished speaking and is waiting
    silently for the user, the agent is nudged to produce another response. If the
    user is currently speaking, this field is a no-op so the agent does not talk
    over them. This field respects the agent's `interruption_sensitivity`: when
    sensitivity is `0` the agent's current speech is treated as uninterruptible, so
    `trigger_response` is a no-op while the agent is speaking. Omitting or setting
    `false` leaves the call untouched.
    """


class FieldsToOverride(TypedDict, total=False):
    """Call fields to override on the running call.

    Each field is applied to the live call immediately; omitted fields are left unchanged.
    """

    data_storage_setting: Literal["everything", "everything_except_pii", "basic_attributes_only"]
    """Data storage setting for this call.

    Overrides the agent's default setting. "everything" stores all data,
    "everything_except_pii" excludes PII when possible, "basic_attributes_only"
    stores only metadata. Cannot be downgraded from more restrictive to less
    restrictive settings.
    """

    metadata: object
    """An arbitrary object for storage purpose only.

    Overrides the metadata on the call. Size limited to 50kB max.
    """

    override_dynamic_variables: Optional[Dict[str, str]]
    """Override dynamic variables represented as key-value pairs of strings.

    Setting this will override or add the dynamic variables set in the agent during
    the call. Only need to set the delta where you want to override, no need to set
    the entire dynamic variables object. Setting this to null will remove any
    existing override.
    """
