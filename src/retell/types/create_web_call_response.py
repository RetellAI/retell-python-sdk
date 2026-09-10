# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CreateWebCallResponse", "IceServer"]


class IceServer(BaseModel):
    urls: Union[str, List[str]]

    credential: Optional[str] = None

    username: Optional[str] = None


class CreateWebCallResponse(BaseModel):
    access_token: str
    """Token authorizing this browser to join the web call. Pass it to your frontend."""

    call_id: str
    """Unique identifier for the web call."""

    expires_at: int
    """Unix epoch ms when the access_token expires."""

    ice_servers: List[IceServer]
    """ICE servers to configure before the browser creates its peer connection."""

    transport: Literal["gateway"]
    """Connection transport to select in the web client."""
