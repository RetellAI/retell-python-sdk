# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BatchCallCreateBatchCallParams", "Task"]


class BatchCallCreateBatchCallParams(TypedDict, total=False):
    from_number: Required[str]
    """The number you own in E.164 format.

    Must be a number purchased from Retell or imported to Retell.
    """

    tasks: Required[Iterable[Task]]
    """A list of individual call tasks to be executed as part of the batch call.

    Each task represents a single outbound call and includes details such as the
    recipient's phone number and optional dynamic variables to personalize the call
    content.
    """

    name: str
    """The name of the batch call. Only used for your own reference."""

    trigger_timestamp: float
    """
    The scheduled time for sending the batch call, represented as a Unix timestamp
    in milliseconds. If omitted, the call will be sent immediately.
    """


class Task(TypedDict, total=False):
    to_number: Required[str]
    """The The number you want to call, in E.164 format.

    If using a number purchased from Retell, only US numbers are supported as
    destination.
    """

    retell_llm_dynamic_variables: Dict[str, object]
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Response Engine prompt and tool description. Only applicable for Response
    Engine.
    """
