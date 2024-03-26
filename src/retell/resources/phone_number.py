# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    PhoneNumberResponse,
    PhoneNumberListResponse,
    phone_number_create_params,
    phone_number_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["PhoneNumber", "AsyncPhoneNumber"]


class PhoneNumber(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberWithRawResponse:
        return PhoneNumberWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberWithStreamingResponse:
        return PhoneNumberWithStreamingResponse(self)

    def create(
        self,
        *,
        agent_id: str,
        area_code: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Buy a new phone number & Bind an agent

        Args:
          agent_id: Unique id of agent to bind to newly obtained number. The number will
              automatically use the agent when doing inbound / outbound calls.

          area_code: Area code of the number to obtain. Format is a 3 digit integer. Currently only
              supports US area code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-phone-number",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "area_code": area_code,
                },
                phone_number_create_params.PhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Retrieve details of a specific phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/get-phone-number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    def update(
        self,
        phone_number: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Update an existing Retell LLM

        Args:
          agent_id: Unique id of agent to bind to number. The number will automatically use the
              agent when doing inbound / outbound calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._patch(
            f"/update-phone-number/{phone_number}",
            body=maybe_transform({"agent_id": agent_id}, phone_number_update_params.PhoneNumberUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberListResponse:
        """List all phone numbers"""
        return self._get(
            "/list-phone-numbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberListResponse,
        )

    def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/delete-phone-number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncPhoneNumber(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberWithRawResponse:
        return AsyncPhoneNumberWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberWithStreamingResponse:
        return AsyncPhoneNumberWithStreamingResponse(self)

    async def create(
        self,
        *,
        agent_id: str,
        area_code: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Buy a new phone number & Bind an agent

        Args:
          agent_id: Unique id of agent to bind to newly obtained number. The number will
              automatically use the agent when doing inbound / outbound calls.

          area_code: Area code of the number to obtain. Format is a 3 digit integer. Currently only
              supports US area code.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-phone-number",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "area_code": area_code,
                },
                phone_number_create_params.PhoneNumberCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Retrieve details of a specific phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/get-phone-number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    async def update(
        self,
        phone_number: str,
        *,
        agent_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Update an existing Retell LLM

        Args:
          agent_id: Unique id of agent to bind to number. The number will automatically use the
              agent when doing inbound / outbound calls.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._patch(
            f"/update-phone-number/{phone_number}",
            body=await async_maybe_transform(
                {"agent_id": agent_id}, phone_number_update_params.PhoneNumberUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberListResponse:
        """List all phone numbers"""
        return await self._get(
            "/list-phone-numbers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberListResponse,
        )

    async def delete(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete an existing phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/delete-phone-number/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class PhoneNumberWithRawResponse:
    def __init__(self, phone_number: PhoneNumber) -> None:
        self._phone_number = phone_number

        self.create = to_raw_response_wrapper(
            phone_number.create,
        )
        self.retrieve = to_raw_response_wrapper(
            phone_number.retrieve,
        )
        self.update = to_raw_response_wrapper(
            phone_number.update,
        )
        self.list = to_raw_response_wrapper(
            phone_number.list,
        )
        self.delete = to_raw_response_wrapper(
            phone_number.delete,
        )


class AsyncPhoneNumberWithRawResponse:
    def __init__(self, phone_number: AsyncPhoneNumber) -> None:
        self._phone_number = phone_number

        self.create = async_to_raw_response_wrapper(
            phone_number.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            phone_number.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            phone_number.update,
        )
        self.list = async_to_raw_response_wrapper(
            phone_number.list,
        )
        self.delete = async_to_raw_response_wrapper(
            phone_number.delete,
        )


class PhoneNumberWithStreamingResponse:
    def __init__(self, phone_number: PhoneNumber) -> None:
        self._phone_number = phone_number

        self.create = to_streamed_response_wrapper(
            phone_number.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            phone_number.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            phone_number.update,
        )
        self.list = to_streamed_response_wrapper(
            phone_number.list,
        )
        self.delete = to_streamed_response_wrapper(
            phone_number.delete,
        )


class AsyncPhoneNumberWithStreamingResponse:
    def __init__(self, phone_number: AsyncPhoneNumber) -> None:
        self._phone_number = phone_number

        self.create = async_to_streamed_response_wrapper(
            phone_number.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            phone_number.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            phone_number.update,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_number.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            phone_number.delete,
        )
