# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import crm_get_schema_params, crm_update_config_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.crm_config import CRMConfig
from ..types.crm_get_schema_response import CRMGetSchemaResponse
from ..types.crm_run_sync_job_response import CRMRunSyncJobResponse
from ..types.crm_get_sync_job_status_response import CRMGetSyncJobStatusResponse

__all__ = ["CRMResource", "AsyncCRMResource"]


class CRMResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CRMResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CRMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CRMResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return CRMResourceWithStreamingResponse(self)

    def get_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMConfig:
        """
        Get the organization's CRM configuration: which CRM app is linked, the custom
        contact fields defined for it, and how post-call analysis data is written back
        to contacts. Returns an empty configuration when nothing has been set up yet.
        """
        return self._get(
            "/get-crm-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMConfig,
        )

    def get_schema(
        self,
        *,
        app_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMGetSchemaResponse:
        """
        Get the contact schema of the connected CRM: the fields available on its contact
        object, which are the values that sync mappings can reference.

        Args:
          app_id: ID of the CRM app to read the schema from. Defaults to the app linked in the
              organization's CRM configuration. Naming a different app additionally requires
              the App.Read scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/get-crm-schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"app_id": app_id}, crm_get_schema_params.CRMGetSchemaParams),
            ),
            cast_to=CRMGetSchemaResponse,
        )

    def get_sync_job_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMGetSyncJobStatusResponse:
        """
        Get the status of the organization's contact sync, whether it was started
        manually or by the schedule. Returns status `idle` when no sync is running.
        """
        return self._get(
            "/get-sync-job-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMGetSyncJobStatusResponse,
        )

    def run_sync_job(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMRunSyncJobResponse:
        """
        Start a contact sync with the linked CRM app immediately, instead of waiting for
        the scheduled sync. One sync runs per organization at a time: starting another
        while one is in flight is rejected. Poll get-sync-job-status for progress.
        """
        return self._post(
            "/run-sync-job",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMRunSyncJobResponse,
        )

    def update_config(
        self,
        *,
        app_id: Optional[str] | Omit = omit,
        contact_columns_order: SequenceNotStr[str] | Omit = omit,
        crm_analysis_data_mappings: Iterable[crm_update_config_params.CRMAnalysisDataMapping] | Omit = omit,
        custom_fields: Iterable[crm_update_config_params.CustomField] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMConfig:
        """Update the organization's CRM configuration.

        Omitted fields stay as they are; a
        field that is sent replaces its stored value in full.

        Args:
          app_id: ID of the CRM app to link. Pass null to unlink, which stops syncing. Changing it
              resets the sync cursor, so the next sync re-reads every contact from the new
              CRM.

          contact_columns_order: Preferred display order of contact fields, for clients that render contacts as a
              table. Not used by the API itself.

          crm_analysis_data_mappings: Replaces the stored list.

          custom_fields: Replaces the stored list. Names must be snake_case and cannot collide with a
              built-in contact field or start with `contact`/`external`. Removing a field that
              an analysis data mapping still targets is rejected — send
              crm_analysis_data_mappings in the same request to retarget or drop those
              mappings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/update-crm-config",
            body=maybe_transform(
                {
                    "app_id": app_id,
                    "contact_columns_order": contact_columns_order,
                    "crm_analysis_data_mappings": crm_analysis_data_mappings,
                    "custom_fields": custom_fields,
                },
                crm_update_config_params.CRMUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMConfig,
        )


class AsyncCRMResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCRMResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCRMResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCRMResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncCRMResourceWithStreamingResponse(self)

    async def get_config(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMConfig:
        """
        Get the organization's CRM configuration: which CRM app is linked, the custom
        contact fields defined for it, and how post-call analysis data is written back
        to contacts. Returns an empty configuration when nothing has been set up yet.
        """
        return await self._get(
            "/get-crm-config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMConfig,
        )

    async def get_schema(
        self,
        *,
        app_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMGetSchemaResponse:
        """
        Get the contact schema of the connected CRM: the fields available on its contact
        object, which are the values that sync mappings can reference.

        Args:
          app_id: ID of the CRM app to read the schema from. Defaults to the app linked in the
              organization's CRM configuration. Naming a different app additionally requires
              the App.Read scope.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/get-crm-schema",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"app_id": app_id}, crm_get_schema_params.CRMGetSchemaParams),
            ),
            cast_to=CRMGetSchemaResponse,
        )

    async def get_sync_job_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMGetSyncJobStatusResponse:
        """
        Get the status of the organization's contact sync, whether it was started
        manually or by the schedule. Returns status `idle` when no sync is running.
        """
        return await self._get(
            "/get-sync-job-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMGetSyncJobStatusResponse,
        )

    async def run_sync_job(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMRunSyncJobResponse:
        """
        Start a contact sync with the linked CRM app immediately, instead of waiting for
        the scheduled sync. One sync runs per organization at a time: starting another
        while one is in flight is rejected. Poll get-sync-job-status for progress.
        """
        return await self._post(
            "/run-sync-job",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMRunSyncJobResponse,
        )

    async def update_config(
        self,
        *,
        app_id: Optional[str] | Omit = omit,
        contact_columns_order: SequenceNotStr[str] | Omit = omit,
        crm_analysis_data_mappings: Iterable[crm_update_config_params.CRMAnalysisDataMapping] | Omit = omit,
        custom_fields: Iterable[crm_update_config_params.CustomField] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CRMConfig:
        """Update the organization's CRM configuration.

        Omitted fields stay as they are; a
        field that is sent replaces its stored value in full.

        Args:
          app_id: ID of the CRM app to link. Pass null to unlink, which stops syncing. Changing it
              resets the sync cursor, so the next sync re-reads every contact from the new
              CRM.

          contact_columns_order: Preferred display order of contact fields, for clients that render contacts as a
              table. Not used by the API itself.

          crm_analysis_data_mappings: Replaces the stored list.

          custom_fields: Replaces the stored list. Names must be snake_case and cannot collide with a
              built-in contact field or start with `contact`/`external`. Removing a field that
              an analysis data mapping still targets is rejected — send
              crm_analysis_data_mappings in the same request to retarget or drop those
              mappings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/update-crm-config",
            body=await async_maybe_transform(
                {
                    "app_id": app_id,
                    "contact_columns_order": contact_columns_order,
                    "crm_analysis_data_mappings": crm_analysis_data_mappings,
                    "custom_fields": custom_fields,
                },
                crm_update_config_params.CRMUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CRMConfig,
        )


class CRMResourceWithRawResponse:
    def __init__(self, crm: CRMResource) -> None:
        self._crm = crm

        self.get_config = to_raw_response_wrapper(
            crm.get_config,
        )
        self.get_schema = to_raw_response_wrapper(
            crm.get_schema,
        )
        self.get_sync_job_status = to_raw_response_wrapper(
            crm.get_sync_job_status,
        )
        self.run_sync_job = to_raw_response_wrapper(
            crm.run_sync_job,
        )
        self.update_config = to_raw_response_wrapper(
            crm.update_config,
        )


class AsyncCRMResourceWithRawResponse:
    def __init__(self, crm: AsyncCRMResource) -> None:
        self._crm = crm

        self.get_config = async_to_raw_response_wrapper(
            crm.get_config,
        )
        self.get_schema = async_to_raw_response_wrapper(
            crm.get_schema,
        )
        self.get_sync_job_status = async_to_raw_response_wrapper(
            crm.get_sync_job_status,
        )
        self.run_sync_job = async_to_raw_response_wrapper(
            crm.run_sync_job,
        )
        self.update_config = async_to_raw_response_wrapper(
            crm.update_config,
        )


class CRMResourceWithStreamingResponse:
    def __init__(self, crm: CRMResource) -> None:
        self._crm = crm

        self.get_config = to_streamed_response_wrapper(
            crm.get_config,
        )
        self.get_schema = to_streamed_response_wrapper(
            crm.get_schema,
        )
        self.get_sync_job_status = to_streamed_response_wrapper(
            crm.get_sync_job_status,
        )
        self.run_sync_job = to_streamed_response_wrapper(
            crm.run_sync_job,
        )
        self.update_config = to_streamed_response_wrapper(
            crm.update_config,
        )


class AsyncCRMResourceWithStreamingResponse:
    def __init__(self, crm: AsyncCRMResource) -> None:
        self._crm = crm

        self.get_config = async_to_streamed_response_wrapper(
            crm.get_config,
        )
        self.get_schema = async_to_streamed_response_wrapper(
            crm.get_schema,
        )
        self.get_sync_job_status = async_to_streamed_response_wrapper(
            crm.get_sync_job_status,
        )
        self.run_sync_job = async_to_streamed_response_wrapper(
            crm.run_sync_job,
        )
        self.update_config = async_to_streamed_response_wrapper(
            crm.update_config,
        )
