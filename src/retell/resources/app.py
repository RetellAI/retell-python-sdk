# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import app_list_params, app_create_params, app_delete_params, app_update_params, app_list_usages_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.app_response import AppResponse
from ..types.app_list_response import AppListResponse
from ..types.app_test_auth_response import AppTestAuthResponse
from ..types.app_list_usages_response import AppListUsagesResponse

__all__ = ["AppResource", "AsyncAppResource"]


class AppResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AppResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        provider: str,
        type: Literal["crm", "calendar", "knowledge_base", "support", "communication"],
        auth_config: app_create_params.AuthConfig | Omit = omit,
        crm_config: app_create_params.CRMConfig | Omit = omit,
        name: str | Omit = omit,
        tenant_id: str | Omit = omit,
        tenant_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """
        Create an App: the connection to one external system (a CRM, calendar, support
        desk, and so on), holding its credentials and settings. Providers that
        authenticate with a key, token, or refresh token can be connected in this one
        call by passing auth_config; the credential is stored encrypted and never
        returned. Up to 20 apps per provider.

        Args:
          provider: Provider name. Must be valid for the App's type; the supported providers per
              type are listed by list-app-templates.

          type: App integration category.

          name: Display name.

          tenant_id: Sub-account id, for providers that scope requests by a sub-account id on a
              shared host.

          tenant_url: Per-tenant API base URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-app",
            body=maybe_transform(
                {
                    "provider": provider,
                    "type": type,
                    "auth_config": auth_config,
                    "crm_config": crm_config,
                    "name": name,
                    "tenant_id": tenant_id,
                    "tenant_url": tenant_url,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    def update(
        self,
        app_id: str,
        *,
        auth_config: app_update_params.AuthConfig | Omit = omit,
        crm_config: app_update_params.CRMConfig | Omit = omit,
        name: str | Omit = omit,
        tenant_id: str | Omit = omit,
        tenant_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """Partially update an App.

        Omitted fields remain unchanged. Updating auth_config
        invalidates the cached provider token immediately.

        Args:
          tenant_id: Sub-account id, for providers that scope requests by a sub-account id on a
              shared host.

          tenant_url: Per-tenant API base URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._patch(
            path_template("/update-app/{app_id}", app_id=app_id),
            body=maybe_transform(
                {
                    "auth_config": auth_config,
                    "crm_config": crm_config,
                    "name": name,
                    "tenant_id": tenant_id,
                    "tenant_url": tenant_url,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        sort_order: Literal["ascending", "descending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListResponse:
        """
        List Apps in the organization (paginated).

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          sort_order: Sort order for results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/list-apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            cast_to=AppListResponse,
        )

    def delete(
        self,
        app_id: str,
        *,
        force_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an App.

        Fails when agents or knowledge bases still reference it, unless
        force_delete is set. If a CRM config is linked to this App, the link is cleared.

        Args:
          force_delete: Delete even when the App is still referenced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/delete-app/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"force_delete": force_delete}, app_delete_params.AppDeleteParams),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """
        Get an App by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template("/get-app/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    def list_usages(
        self,
        app_id: str,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        sort_order: Literal["ascending", "descending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListUsagesResponse:
        """
        List the agents and knowledge bases referencing an App, most recently configured
        first by default.

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          sort_order: Sort order for results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._get(
            path_template("/list-app-usages/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    app_list_usages_params.AppListUsagesParams,
                ),
            ),
            cast_to=AppListUsagesResponse,
        )

    def test_auth(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppTestAuthResponse:
        """
        Probe the App's stored credentials by making a minimal authenticated call to the
        provider. Returns success=true on a successful round-trip, and records the
        outcome on the App's connection_status either way.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return self._post(
            path_template("/test-app-auth/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppTestAuthResponse,
        )


class AsyncAppResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncAppResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        provider: str,
        type: Literal["crm", "calendar", "knowledge_base", "support", "communication"],
        auth_config: app_create_params.AuthConfig | Omit = omit,
        crm_config: app_create_params.CRMConfig | Omit = omit,
        name: str | Omit = omit,
        tenant_id: str | Omit = omit,
        tenant_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """
        Create an App: the connection to one external system (a CRM, calendar, support
        desk, and so on), holding its credentials and settings. Providers that
        authenticate with a key, token, or refresh token can be connected in this one
        call by passing auth_config; the credential is stored encrypted and never
        returned. Up to 20 apps per provider.

        Args:
          provider: Provider name. Must be valid for the App's type; the supported providers per
              type are listed by list-app-templates.

          type: App integration category.

          name: Display name.

          tenant_id: Sub-account id, for providers that scope requests by a sub-account id on a
              shared host.

          tenant_url: Per-tenant API base URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-app",
            body=await async_maybe_transform(
                {
                    "provider": provider,
                    "type": type,
                    "auth_config": auth_config,
                    "crm_config": crm_config,
                    "name": name,
                    "tenant_id": tenant_id,
                    "tenant_url": tenant_url,
                },
                app_create_params.AppCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    async def update(
        self,
        app_id: str,
        *,
        auth_config: app_update_params.AuthConfig | Omit = omit,
        crm_config: app_update_params.CRMConfig | Omit = omit,
        name: str | Omit = omit,
        tenant_id: str | Omit = omit,
        tenant_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """Partially update an App.

        Omitted fields remain unchanged. Updating auth_config
        invalidates the cached provider token immediately.

        Args:
          tenant_id: Sub-account id, for providers that scope requests by a sub-account id on a
              shared host.

          tenant_url: Per-tenant API base URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._patch(
            path_template("/update-app/{app_id}", app_id=app_id),
            body=await async_maybe_transform(
                {
                    "auth_config": auth_config,
                    "crm_config": crm_config,
                    "name": name,
                    "tenant_id": tenant_id,
                    "tenant_url": tenant_url,
                },
                app_update_params.AppUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        sort_order: Literal["ascending", "descending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListResponse:
        """
        List Apps in the organization (paginated).

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          sort_order: Sort order for results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/list-apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    app_list_params.AppListParams,
                ),
            ),
            cast_to=AppListResponse,
        )

    async def delete(
        self,
        app_id: str,
        *,
        force_delete: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete an App.

        Fails when agents or knowledge bases still reference it, unless
        force_delete is set. If a CRM config is linked to this App, the link is cleared.

        Args:
          force_delete: Delete even when the App is still referenced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/delete-app/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"force_delete": force_delete}, app_delete_params.AppDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppResponse:
        """
        Get an App by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template("/get-app/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppResponse,
        )

    async def list_usages(
        self,
        app_id: str,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        sort_order: Literal["ascending", "descending"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppListUsagesResponse:
        """
        List the agents and knowledge bases referencing an App, most recently configured
        first by default.

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          sort_order: Sort order for results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._get(
            path_template("/list-app-usages/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                        "sort_order": sort_order,
                    },
                    app_list_usages_params.AppListUsagesParams,
                ),
            ),
            cast_to=AppListUsagesResponse,
        )

    async def test_auth(
        self,
        app_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AppTestAuthResponse:
        """
        Probe the App's stored credentials by making a minimal authenticated call to the
        provider. Returns success=true on a successful round-trip, and records the
        outcome on the App's connection_status either way.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not app_id:
            raise ValueError(f"Expected a non-empty value for `app_id` but received {app_id!r}")
        return await self._post(
            path_template("/test-app-auth/{app_id}", app_id=app_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppTestAuthResponse,
        )


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.create = to_raw_response_wrapper(
            app.create,
        )
        self.update = to_raw_response_wrapper(
            app.update,
        )
        self.list = to_raw_response_wrapper(
            app.list,
        )
        self.delete = to_raw_response_wrapper(
            app.delete,
        )
        self.get = to_raw_response_wrapper(
            app.get,
        )
        self.list_usages = to_raw_response_wrapper(
            app.list_usages,
        )
        self.test_auth = to_raw_response_wrapper(
            app.test_auth,
        )


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.create = async_to_raw_response_wrapper(
            app.create,
        )
        self.update = async_to_raw_response_wrapper(
            app.update,
        )
        self.list = async_to_raw_response_wrapper(
            app.list,
        )
        self.delete = async_to_raw_response_wrapper(
            app.delete,
        )
        self.get = async_to_raw_response_wrapper(
            app.get,
        )
        self.list_usages = async_to_raw_response_wrapper(
            app.list_usages,
        )
        self.test_auth = async_to_raw_response_wrapper(
            app.test_auth,
        )


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.create = to_streamed_response_wrapper(
            app.create,
        )
        self.update = to_streamed_response_wrapper(
            app.update,
        )
        self.list = to_streamed_response_wrapper(
            app.list,
        )
        self.delete = to_streamed_response_wrapper(
            app.delete,
        )
        self.get = to_streamed_response_wrapper(
            app.get,
        )
        self.list_usages = to_streamed_response_wrapper(
            app.list_usages,
        )
        self.test_auth = to_streamed_response_wrapper(
            app.test_auth,
        )


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.create = async_to_streamed_response_wrapper(
            app.create,
        )
        self.update = async_to_streamed_response_wrapper(
            app.update,
        )
        self.list = async_to_streamed_response_wrapper(
            app.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            app.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            app.get,
        )
        self.list_usages = async_to_streamed_response_wrapper(
            app.list_usages,
        )
        self.test_auth = async_to_streamed_response_wrapper(
            app.test_auth,
        )
