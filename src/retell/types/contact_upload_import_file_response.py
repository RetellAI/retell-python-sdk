# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ContactUploadImportFileResponse"]


class ContactUploadImportFileResponse(BaseModel):
    file_name: Optional[str] = None

    upload_id: Optional[str] = None
