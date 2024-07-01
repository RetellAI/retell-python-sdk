# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .phone_call_response import PhoneCallResponse

__all__ = ["CallResponse", "V2WebCallResponse"]


class V2WebCallResponse(BaseModel):
    access_token: str
    """Access token to enter the web call room.

    This needs to be passed to your frontend to join the call.
    """

    agent_id: str
    """Corresponding agent id of this call."""

    call_id: str
    """Unique id of the call.

    Used to identify in LLM websocket and used to authenticate in audio websocket.
    """

    call_status: Literal["registered", "ongoing", "ended", "error"]
    """Status of call.

    - `registered`: Call id issued, starting to make a call using this id.

    - `ongoing`: Call connected and ongoing.

    - `ended`: The underlying websocket has ended for the call. Either user or agent
      hanged up, or call transferred.

    - `error`: Call encountered error.
    """

    call_type: Literal["web_call"]
    """Type of the call. Used to distinguish between web call and phone call."""

    metadata: Optional[object] = None
    """An arbitrary object for storage purpose only.

    You can put anything here like your internal customer id associated with the
    call. Not used for processing. You can later get this field from the call
    object.
    """

    opt_out_sensitive_data_storage: Optional[bool] = None
    """
    Whether this call opts out of sensitive data storage like transcript, recording,
    logging.
    """

    retell_llm_dynamic_variables: Optional[Dict[str, object]] = None
    """
    Add optional dynamic variables in key value pairs of string that injects into
    your Retell LLM prompt and tool description. Only applicable for Retell LLM.
    """


CallResponse = Union[V2WebCallResponse, PhoneCallResponse]
