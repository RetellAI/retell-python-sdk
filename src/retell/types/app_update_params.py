# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AppUpdateParams",
    "AuthConfig",
    "AuthConfigOAuthConfigRequest",
    "AuthConfigAPIKeyAuthConfigRequest",
    "AuthConfigBasicAuthConfigRequest",
    "CRMConfig",
    "CRMConfigInboundSyncMapping",
    "CRMConfigOutboundSyncMapping",
]


class AppUpdateParams(TypedDict, total=False):
    auth_config: AuthConfig
    """Caller-managed credentials.

    Providers using the OAuth callback reject auth_config and must be authorized
    through connect-app.
    """

    crm_config: CRMConfig

    name: str

    tenant_id: str
    """
    Sub-account id, for providers that scope requests by a sub-account id on a
    shared host.
    """

    tenant_url: str
    """Per-tenant API base URL."""


class AuthConfigOAuthConfigRequest(TypedDict, total=False):
    client_id: Required[str]

    client_secret: Required[str]
    """Secret credential; stored encrypted at rest."""

    type: Required[Literal["oauth2"]]


class AuthConfigAPIKeyAuthConfigRequest(TypedDict, total=False):
    api_key: Required[str]
    """API key credential; stored encrypted at rest."""

    type: Required[Literal["api_key"]]


class AuthConfigBasicAuthConfigRequest(TypedDict, total=False):
    password: Required[str]
    """Password credential; stored encrypted at rest."""

    type: Required[Literal["basic"]]

    username: Required[str]


AuthConfig: TypeAlias = Union[
    AuthConfigOAuthConfigRequest, AuthConfigAPIKeyAuthConfigRequest, AuthConfigBasicAuthConfigRequest
]


class CRMConfigInboundSyncMapping(TypedDict, total=False):
    external_field_name: Required[str]
    """Field on the CRM's contact object to map to.

    A name that does not exist there surfaces as an error on the sync job rather
    than at configuration time.
    """

    field_name: Required[str]
    """Retell contact field, built-in or custom, to map.

    Types must be compatible with the CRM field on both sides of the sync.
    """


class CRMConfigOutboundSyncMapping(TypedDict, total=False):
    external_field_name: Required[str]
    """Field on the CRM's contact object to map to.

    A name that does not exist there surfaces as an error on the sync job rather
    than at configuration time.
    """

    field_name: Required[str]
    """Retell contact field, built-in or custom, to map.

    Types must be compatible with the CRM field on both sides of the sync.
    """


class CRMConfig(TypedDict, total=False):
    inbound_sync_mappings: Iterable[CRMConfigInboundSyncMapping]
    """Field mappings applied when syncing CRM records into Retell contacts.

    Must include phone_number, which is the field the two systems are matched on.
    """

    outbound_sync_mappings: Iterable[CRMConfigOutboundSyncMapping]
    """Field mappings applied when writing Retell contact changes back to the CRM."""

    sync_conversation_activity: bool
    """Whether to push call/chat activity to the external CRM.

    Opt-in — defaults to false when unset.
    """

    sync_new_contacts: bool
    """
    Whether to create a CRM record after a conversation when the contact is not yet
    linked to one.
    """
