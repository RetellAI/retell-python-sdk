# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AppResponse",
    "AuthConfig",
    "AuthConfigOAuthConfigResponse",
    "AuthConfigAPIKeyAuthConfigResponse",
    "AuthConfigAccessTokenAuthConfigResponse",
    "AuthConfigBasicAuthConfigResponse",
    "AuthConfigRefreshTokenAuthConfigResponse",
    "CRMConfig",
    "CRMConfigInboundSyncMapping",
    "CRMConfigOutboundSyncMapping",
]


class AuthConfigOAuthConfigResponse(BaseModel):
    client_id: str

    type: Literal["oauth2"]


class AuthConfigAPIKeyAuthConfigResponse(BaseModel):
    type: Literal["api_key"]


class AuthConfigAccessTokenAuthConfigResponse(BaseModel):
    type: Literal["access_token"]


class AuthConfigBasicAuthConfigResponse(BaseModel):
    type: Literal["basic"]

    username: str


class AuthConfigRefreshTokenAuthConfigResponse(BaseModel):
    type: Literal["refresh_token"]


AuthConfig: TypeAlias = Union[
    AuthConfigOAuthConfigResponse,
    AuthConfigAPIKeyAuthConfigResponse,
    AuthConfigAccessTokenAuthConfigResponse,
    AuthConfigBasicAuthConfigResponse,
    AuthConfigRefreshTokenAuthConfigResponse,
]


class CRMConfigInboundSyncMapping(BaseModel):
    external_field_name: str
    """Field on the CRM's contact object to map to.

    A name that does not exist there surfaces as an error on the sync job rather
    than at configuration time.
    """

    field_name: str
    """Retell contact field, built-in or custom, to map.

    Types must be compatible with the CRM field on both sides of the sync.
    """


class CRMConfigOutboundSyncMapping(BaseModel):
    external_field_name: str
    """Field on the CRM's contact object to map to.

    A name that does not exist there surfaces as an error on the sync job rather
    than at configuration time.
    """

    field_name: str
    """Retell contact field, built-in or custom, to map.

    Types must be compatible with the CRM field on both sides of the sync.
    """


class CRMConfig(BaseModel):
    inbound_sync_mappings: Optional[List[CRMConfigInboundSyncMapping]] = None
    """Field mappings applied when syncing CRM records into Retell contacts.

    Must include phone_number, which is the field the two systems are matched on.
    """

    outbound_sync_mappings: Optional[List[CRMConfigOutboundSyncMapping]] = None
    """Field mappings applied when writing Retell contact changes back to the CRM."""

    sync_conversation_activity: Optional[bool] = None
    """Whether to push call/chat activity to the external CRM.

    Opt-in — defaults to false when unset.
    """

    sync_new_contacts: Optional[bool] = None
    """
    Whether to create a CRM record after a conversation when the contact is not yet
    linked to one.
    """


class AppResponse(BaseModel):
    app_id: str

    created_timestamp: float

    org_id: str

    provider: str
    """Provider name.

    Must be valid for the App's type; the supported providers per type are listed by
    list-app-templates.
    """

    type: Literal["crm", "calendar", "knowledge_base", "support", "communication"]
    """App integration category."""

    user_modified_timestamp: float

    auth_config: Optional[AuthConfig] = None
    """Non-secret auth metadata.

    Encrypted secret fields are never returned by the API.
    """

    connection_status: Optional[Literal["not_connected", "connected", "error"]] = None
    """Connection health of the App, server-managed.

    `not_connected` after create or a credential / tenant URL change; `connected`
    once verified via OAuth connect, an auth test, or a successful live tool call;
    `error` when the provider rejects the credentials (on connect, an auth test, or
    a live tool call).
    """

    crm_config: Optional[CRMConfig] = None

    name: Optional[str] = None

    tenant_id: Optional[str] = None
    """
    Sub-account id, for providers that scope requests by a sub-account id on a
    shared host. Omitted by every other provider.
    """

    tenant_url: Optional[str] = None
    """Per-tenant API base URL.

    Set by providers with per-org hosts; omitted by providers on a single global
    host.
    """
