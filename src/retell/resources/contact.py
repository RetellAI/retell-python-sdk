# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    contact_list_params,
    contact_create_params,
    contact_update_params,
    contact_list_conversations_params,
    contact_backfill_analysis_data_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.contact_response import ContactResponse
from ..types.contact_list_response import ContactListResponse
from ..types.contact_list_conversations_response import ContactListConversationsResponse
from ..types.contact_backfill_analysis_data_response import ContactBackfillAnalysisDataResponse
from ..types.contact_get_backfill_job_status_response import ContactGetBackfillJobStatusResponse

__all__ = ["ContactResource", "AsyncContactResource"]


class ContactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return ContactResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        phone_number: str,
        custom_fields: object | Omit = omit,
        do_not_call: bool | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """
        Create a new contact.

        Args:
          phone_number: Phone number of the contact.

          custom_fields: Values must match the types defined in CRM config custom fields. Set a value to
              null to clear it.

          first_name: First name of the contact.

          last_name: Last name of the contact.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-contact",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "custom_fields": custom_fields,
                    "do_not_call": do_not_call,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    def update(
        self,
        contact_id: str,
        *,
        custom_fields: object | Omit = omit,
        do_not_call: bool | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """
        Update an existing contact.

        Args:
          custom_fields: Values must match the types defined in CRM config custom fields. Set a value to
              null to clear it.

          first_name: First name of the contact.

          last_name: Last name of the contact.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._patch(
            path_template("/update-contact/{contact_id}", contact_id=contact_id),
            body=maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "do_not_call": do_not_call,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    def list(
        self,
        *,
        filter_criteria: contact_list_params.FilterCriteria | Omit = omit,
        limit: float | Omit = omit,
        pagination_key: str | Omit = omit,
        search_query: str | Omit = omit,
        skip: float | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        List contacts, newest conversation first by default, with the total count of
        matches alongside the page. Page through results with `pagination_key`; `skip`
        is available for offset-style paging but is slower on large contact sets and can
        repeat or miss rows as contacts are updated.

        Args:
          filter_criteria: Filter criteria for contacts. All conditions are implicitly connected with AND.
              first_name and last_name are not filterable here; use search_query to match on
              those.

          limit: Maximum number of contacts to return.

          pagination_key: Base64url-encoded pagination key from a previous response.

          search_query: Case-insensitive substring match against phone number, first name, last name,
              external ID, and custom field values. This is the only way to match on a
              contact's name.

          skip: Number of records to skip for offset-based pagination.

          sort_order: Sort contacts by `last_conversation_timestamp` in ascending or descending order.
              Contacts that have never been contacted sort as if their timestamp were 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/list-contacts",
            body=maybe_transform(
                {
                    "filter_criteria": filter_criteria,
                    "limit": limit,
                    "pagination_key": pagination_key,
                    "search_query": search_query,
                    "skip": skip,
                    "sort_order": sort_order,
                },
                contact_list_params.ContactListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactListResponse,
        )

    def delete(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a contact.

        A contact linked to a record in a connected CRM cannot be
        deleted while two-way sync is active — unlink the CRM app first, otherwise the
        next sync would recreate it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/delete-contact/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def backfill_analysis_data(
        self,
        *,
        backfill_attributes: SequenceNotStr[str],
        backfill_call_filter: contact_backfill_analysis_data_params.BackfillCallFilter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBackfillAnalysisDataResponse:
        """
        Trigger a backfill job that re-applies analysis data mappings to contacts using
        historical call data. Only one backfill job can run per organization at a time.

        Args:
          backfill_attributes: Contact fields to recompute. Each one must still exist as a contact field and
              have an analysis data mapping configured, otherwise the request is rejected
              rather than running a job that writes nothing.

          backfill_call_filter: Optional call filter to scope which calls are processed. Supports agent and
              start_timestamp from the standard call filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/backfill-contact-analysis-data",
            body=maybe_transform(
                {
                    "backfill_attributes": backfill_attributes,
                    "backfill_call_filter": backfill_call_filter,
                },
                contact_backfill_analysis_data_params.ContactBackfillAnalysisDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactBackfillAnalysisDataResponse,
        )

    def get(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """
        Retrieve a contact by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            path_template("/get-contact/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    def get_backfill_job_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactGetBackfillJobStatusResponse:
        """Get the status of the contact analysis data backfill job."""
        return self._get(
            "/get-backfill-contact-job-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactGetBackfillJobStatusResponse,
        )

    def get_by_phone(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """Retrieve a contact by phone number.

        At most one contact exists per phone number
        in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template("/get-contact-by-phone/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    def list_conversations(
        self,
        contact_id: str,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListConversationsResponse:
        """
        List a contact's conversations (inbound calls, outbound calls, and chats) merged
        into a single timeline, most recent first. Results are matched by the contact's
        phone number. Use the returned `pagination_key` to fetch the next page.

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return self._get(
            path_template("/list-contact-conversations/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                    },
                    contact_list_conversations_params.ContactListConversationsParams,
                ),
            ),
            cast_to=ContactListConversationsResponse,
        )


class AsyncContactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncContactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncContactResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        phone_number: str,
        custom_fields: object | Omit = omit,
        do_not_call: bool | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """
        Create a new contact.

        Args:
          phone_number: Phone number of the contact.

          custom_fields: Values must match the types defined in CRM config custom fields. Set a value to
              null to clear it.

          first_name: First name of the contact.

          last_name: Last name of the contact.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-contact",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "custom_fields": custom_fields,
                    "do_not_call": do_not_call,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                contact_create_params.ContactCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    async def update(
        self,
        contact_id: str,
        *,
        custom_fields: object | Omit = omit,
        do_not_call: bool | Omit = omit,
        first_name: str | Omit = omit,
        last_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """
        Update an existing contact.

        Args:
          custom_fields: Values must match the types defined in CRM config custom fields. Set a value to
              null to clear it.

          first_name: First name of the contact.

          last_name: Last name of the contact.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._patch(
            path_template("/update-contact/{contact_id}", contact_id=contact_id),
            body=await async_maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "do_not_call": do_not_call,
                    "first_name": first_name,
                    "last_name": last_name,
                },
                contact_update_params.ContactUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    async def list(
        self,
        *,
        filter_criteria: contact_list_params.FilterCriteria | Omit = omit,
        limit: float | Omit = omit,
        pagination_key: str | Omit = omit,
        search_query: str | Omit = omit,
        skip: float | Omit = omit,
        sort_order: Literal["asc", "desc"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListResponse:
        """
        List contacts, newest conversation first by default, with the total count of
        matches alongside the page. Page through results with `pagination_key`; `skip`
        is available for offset-style paging but is slower on large contact sets and can
        repeat or miss rows as contacts are updated.

        Args:
          filter_criteria: Filter criteria for contacts. All conditions are implicitly connected with AND.
              first_name and last_name are not filterable here; use search_query to match on
              those.

          limit: Maximum number of contacts to return.

          pagination_key: Base64url-encoded pagination key from a previous response.

          search_query: Case-insensitive substring match against phone number, first name, last name,
              external ID, and custom field values. This is the only way to match on a
              contact's name.

          skip: Number of records to skip for offset-based pagination.

          sort_order: Sort contacts by `last_conversation_timestamp` in ascending or descending order.
              Contacts that have never been contacted sort as if their timestamp were 0.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/list-contacts",
            body=await async_maybe_transform(
                {
                    "filter_criteria": filter_criteria,
                    "limit": limit,
                    "pagination_key": pagination_key,
                    "search_query": search_query,
                    "skip": skip,
                    "sort_order": sort_order,
                },
                contact_list_params.ContactListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactListResponse,
        )

    async def delete(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete a contact.

        A contact linked to a record in a connected CRM cannot be
        deleted while two-way sync is active — unlink the CRM app first, otherwise the
        next sync would recreate it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/delete-contact/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def backfill_analysis_data(
        self,
        *,
        backfill_attributes: SequenceNotStr[str],
        backfill_call_filter: contact_backfill_analysis_data_params.BackfillCallFilter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactBackfillAnalysisDataResponse:
        """
        Trigger a backfill job that re-applies analysis data mappings to contacts using
        historical call data. Only one backfill job can run per organization at a time.

        Args:
          backfill_attributes: Contact fields to recompute. Each one must still exist as a contact field and
              have an analysis data mapping configured, otherwise the request is rejected
              rather than running a job that writes nothing.

          backfill_call_filter: Optional call filter to scope which calls are processed. Supports agent and
              start_timestamp from the standard call filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/backfill-contact-analysis-data",
            body=await async_maybe_transform(
                {
                    "backfill_attributes": backfill_attributes,
                    "backfill_call_filter": backfill_call_filter,
                },
                contact_backfill_analysis_data_params.ContactBackfillAnalysisDataParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactBackfillAnalysisDataResponse,
        )

    async def get(
        self,
        contact_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """
        Retrieve a contact by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            path_template("/get-contact/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    async def get_backfill_job_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactGetBackfillJobStatusResponse:
        """Get the status of the contact analysis data backfill job."""
        return await self._get(
            "/get-backfill-contact-job-status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactGetBackfillJobStatusResponse,
        )

    async def get_by_phone(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactResponse:
        """Retrieve a contact by phone number.

        At most one contact exists per phone number
        in an organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template("/get-contact-by-phone/{phone_number}", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContactResponse,
        )

    async def list_conversations(
        self,
        contact_id: str,
        *,
        limit: int | Omit = omit,
        pagination_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContactListConversationsResponse:
        """
        List a contact's conversations (inbound calls, outbound calls, and chats) merged
        into a single timeline, most recent first. Results are matched by the contact's
        phone number. Use the returned `pagination_key` to fetch the next page.

        Args:
          limit: Maximum number of items to return.

          pagination_key: Pagination key for fetching the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not contact_id:
            raise ValueError(f"Expected a non-empty value for `contact_id` but received {contact_id!r}")
        return await self._get(
            path_template("/list-contact-conversations/{contact_id}", contact_id=contact_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "pagination_key": pagination_key,
                    },
                    contact_list_conversations_params.ContactListConversationsParams,
                ),
            ),
            cast_to=ContactListConversationsResponse,
        )


class ContactResourceWithRawResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

        self.create = to_raw_response_wrapper(
            contact.create,
        )
        self.update = to_raw_response_wrapper(
            contact.update,
        )
        self.list = to_raw_response_wrapper(
            contact.list,
        )
        self.delete = to_raw_response_wrapper(
            contact.delete,
        )
        self.backfill_analysis_data = to_raw_response_wrapper(
            contact.backfill_analysis_data,
        )
        self.get = to_raw_response_wrapper(
            contact.get,
        )
        self.get_backfill_job_status = to_raw_response_wrapper(
            contact.get_backfill_job_status,
        )
        self.get_by_phone = to_raw_response_wrapper(
            contact.get_by_phone,
        )
        self.list_conversations = to_raw_response_wrapper(
            contact.list_conversations,
        )


class AsyncContactResourceWithRawResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

        self.create = async_to_raw_response_wrapper(
            contact.create,
        )
        self.update = async_to_raw_response_wrapper(
            contact.update,
        )
        self.list = async_to_raw_response_wrapper(
            contact.list,
        )
        self.delete = async_to_raw_response_wrapper(
            contact.delete,
        )
        self.backfill_analysis_data = async_to_raw_response_wrapper(
            contact.backfill_analysis_data,
        )
        self.get = async_to_raw_response_wrapper(
            contact.get,
        )
        self.get_backfill_job_status = async_to_raw_response_wrapper(
            contact.get_backfill_job_status,
        )
        self.get_by_phone = async_to_raw_response_wrapper(
            contact.get_by_phone,
        )
        self.list_conversations = async_to_raw_response_wrapper(
            contact.list_conversations,
        )


class ContactResourceWithStreamingResponse:
    def __init__(self, contact: ContactResource) -> None:
        self._contact = contact

        self.create = to_streamed_response_wrapper(
            contact.create,
        )
        self.update = to_streamed_response_wrapper(
            contact.update,
        )
        self.list = to_streamed_response_wrapper(
            contact.list,
        )
        self.delete = to_streamed_response_wrapper(
            contact.delete,
        )
        self.backfill_analysis_data = to_streamed_response_wrapper(
            contact.backfill_analysis_data,
        )
        self.get = to_streamed_response_wrapper(
            contact.get,
        )
        self.get_backfill_job_status = to_streamed_response_wrapper(
            contact.get_backfill_job_status,
        )
        self.get_by_phone = to_streamed_response_wrapper(
            contact.get_by_phone,
        )
        self.list_conversations = to_streamed_response_wrapper(
            contact.list_conversations,
        )


class AsyncContactResourceWithStreamingResponse:
    def __init__(self, contact: AsyncContactResource) -> None:
        self._contact = contact

        self.create = async_to_streamed_response_wrapper(
            contact.create,
        )
        self.update = async_to_streamed_response_wrapper(
            contact.update,
        )
        self.list = async_to_streamed_response_wrapper(
            contact.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            contact.delete,
        )
        self.backfill_analysis_data = async_to_streamed_response_wrapper(
            contact.backfill_analysis_data,
        )
        self.get = async_to_streamed_response_wrapper(
            contact.get,
        )
        self.get_backfill_job_status = async_to_streamed_response_wrapper(
            contact.get_backfill_job_status,
        )
        self.get_by_phone = async_to_streamed_response_wrapper(
            contact.get_by_phone,
        )
        self.list_conversations = async_to_streamed_response_wrapper(
            contact.list_conversations,
        )
