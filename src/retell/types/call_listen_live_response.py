# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CallListenLiveResponse", "IceServer"]


class IceServer(BaseModel):
    urls: Union[str, List[str]]

    credential: Optional[str] = None

    username: Optional[str] = None


class CallListenLiveResponse(BaseModel):
    access_token: str
    """Subscribe-only JWT scoped to the call's room.

    Cannot publish. Listener participant is hidden from other participants.
    """

    expires_at: int
    """Unix epoch ms when the access_token expires."""

    participant_id: str
    """
    Identity this listener joins as, and the value to hand back to
    /v2/take-over-live-call. Returned on both transports; a `livekit` client can
    equally read it off its own room object, a `gateway` one has no equivalent to
    read.
    """

    room_name: str
    """Room name to join.

    Always the call's original room — does not follow warm transfers.
    """

    gateway_ip: Optional[str] = None
    """
    Public side of the gateway instance handling this call, for diagnostics only —
    the client's media address comes from the SDP answer's ICE candidates. `gateway`
    transport only.
    """

    ice_servers: Optional[List[IceServer]] = None
    """
    ICE servers the client must configure before creating its PeerConnection — they
    cannot be added afterwards. `gateway` transport only.
    """

    transport: Optional[Literal["livekit", "gateway"]] = None
    """
    Which media stack issued the access_token, and therefore where the client
    signals. The two tokens are indistinguishable, so a client must read this rather
    than infer it. `gateway` clients address Retell itself; `livekit` clients
    connect to the returned `url`. Optional only because a server predating the
    field omits it during a rollout; treat absent as `livekit`.
    """

    url: Optional[str] = None
    """Server URL the client should connect to with the access_token.

    Present only when `transport` is `livekit`; a `gateway` listener signals to
    Retell and needs no address.
    """
