# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AppGetToolSchemaResponse", "InputSchema", "ResponseSchema"]


class InputSchema(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

    properties: object
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Literal["object"]
    """Type must be "object" for a JSON Schema object."""

    required: Optional[List[str]] = None
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class ResponseSchema(BaseModel):
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format. Omitting parameters defines a function with an empty parameter list.
    """

    properties: object
    """
    The value of properties is an object, where each key is the name of a property
    and each value is a schema used to validate that property.
    """

    type: Literal["object"]
    """Type must be "object" for a JSON Schema object."""

    required: Optional[List[str]] = None
    """List of names of required property when generating this parameter.

    LLM will do its best to generate the required properties in its function
    arguments. Property must exist in properties.
    """


class AppGetToolSchemaResponse(BaseModel):
    complete: bool

    input_schema: Optional[InputSchema] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """

    response_schema: Optional[ResponseSchema] = None
    """The parameters the functions accepts, described as a JSON Schema object.

    See [JSON Schema reference](https://json-schema.org/understanding-json-schema/)
    for documentation about the format. Omitting parameters defines a function with
    an empty parameter list.
    """
