# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PhoneNumberUpdateResponse"]


class PhoneNumberUpdateResponse(BaseModel):
    agent_id: str

    area_code: int

    last_modification_timestamp: int

    phone_number: str

    phone_number_pretty: str
