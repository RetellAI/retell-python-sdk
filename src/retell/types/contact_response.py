# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ContactResponse", "ContactTag"]


class ContactTag(BaseModel):
    id: str
    """Unique identifier for the tag."""

    label: str
    """Human-readable label for the tag."""


class ContactResponse(BaseModel):
    contact_id: str
    """Unique identifier for the contact."""

    created_timestamp: float
    """Epoch milliseconds when the contact was created."""

    org_id: str
    """Organization this contact belongs to."""

    phone_number: str
    """Phone number of the contact."""

    contact_memory: Optional[str] = None
    """Running brief shared across this contact's phone calls and SMS chats.

    Omitted when unset.
    """

    contact_tags: Optional[List[ContactTag]] = None
    """Assigned tag IDs and labels from the organization's CRM config.

    IDs absent from the config are omitted.
    """

    conversation_count: Optional[float] = None
    """Number of conversations (calls and chats) associated with this contact."""

    custom_fields: Optional[object] = None
    """Custom fields defined in CRM config."""

    do_not_call: Optional[bool] = None
    """Whether this contact should not be called."""

    external_id: Optional[str] = None
    """CRM record ID from the external provider."""

    first_name: Optional[str] = None
    """First name of the contact."""

    last_conversation_timestamp: Optional[float] = None
    """Epoch milliseconds of the most recent conversation with this contact."""

    last_name: Optional[str] = None
    """Last name of the contact."""

    user_modified_timestamp: Optional[float] = None
    """Epoch milliseconds when the contact was last modified."""
