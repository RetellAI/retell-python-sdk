# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["IdentityRetrieveResponse"]


class IdentityRetrieveResponse(BaseModel):
    api_key_name: Optional[str] = None
    """Display name of the API key used, if it has one."""

    org_name: str
    """Display name of the org."""
