# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import phone_number_create_params, phone_number_import_params, phone_number_update_params
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
from .._base_client import make_request_options
from ..types.phone_number_response import PhoneNumberResponse
from ..types.phone_number_list_response import PhoneNumberListResponse

__all__ = ["PhoneNumberResource", "AsyncPhoneNumberResource"]


class PhoneNumberResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return PhoneNumberResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        area_code: int | NotGiven = NOT_GIVEN,
        inbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        nickname: str | NotGiven = NOT_GIVEN,
        outbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Buy a new phone number & Bind agents

        Args:
          area_code: Area code of the number to obtain. Format is a 3 digit integer. Currently only
              supports US area code.

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If null, this number would not accept
              inbound call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/create-phone-number",
            body=maybe_transform(
                {
                    "area_code": area_code,
                    "inbound_agent_id": inbound_agent_id,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
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
        inbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        outbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Update agent bound to a purchased phone number

        Args:
          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If set to null, this number would not accept
              inbound call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If set to null, this number would not be
              able to initiate outbound call without agent id override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._patch(
            f"/update-phone-number/{phone_number}",
            body=maybe_transform(
                {
                    "inbound_agent_id": inbound_agent_id,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
            ),
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

    def import_(
        self,
        *,
        phone_number: str,
        termination_uri: str,
        inbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        nickname: str | NotGiven = NOT_GIVEN,
        outbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        sip_trunk_auth_password: str | NotGiven = NOT_GIVEN,
        sip_trunk_auth_username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Import a phone number from custom telephony & Bind agents

        Args:
          phone_number: The number you are trying to import in E.164 format of the number (+country
              code, then number with no space, no special characters), used as the unique
              identifier for phone number APIs.

          termination_uri: The termination uri to uniquely identify your elastic SIP trunk. This is used
              for outbound calls. For Twilio elastic SIP trunks it always end with
              ".pstn.twilio.com".

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If null, this number would not accept
              inbound call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          sip_trunk_auth_password: The password used for authentication for the SIP trunk.

          sip_trunk_auth_username: The username used for authentication for the SIP trunk.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/import-phone-number",
            body=maybe_transform(
                {
                    "phone_number": phone_number,
                    "termination_uri": termination_uri,
                    "inbound_agent_id": inbound_agent_id,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                    "sip_trunk_auth_password": sip_trunk_auth_password,
                    "sip_trunk_auth_username": sip_trunk_auth_username,
                },
                phone_number_import_params.PhoneNumberImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )


class AsyncPhoneNumberResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncPhoneNumberResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        area_code: int | NotGiven = NOT_GIVEN,
        inbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        nickname: str | NotGiven = NOT_GIVEN,
        outbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Buy a new phone number & Bind agents

        Args:
          area_code: Area code of the number to obtain. Format is a 3 digit integer. Currently only
              supports US area code.

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If null, this number would not accept
              inbound call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/create-phone-number",
            body=await async_maybe_transform(
                {
                    "area_code": area_code,
                    "inbound_agent_id": inbound_agent_id,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
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
        inbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        nickname: Optional[str] | NotGiven = NOT_GIVEN,
        outbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Update agent bound to a purchased phone number

        Args:
          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If set to null, this number would not accept
              inbound call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If set to null, this number would not be
              able to initiate outbound call without agent id override.

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
                {
                    "inbound_agent_id": inbound_agent_id,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                },
                phone_number_update_params.PhoneNumberUpdateParams,
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

    async def import_(
        self,
        *,
        phone_number: str,
        termination_uri: str,
        inbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        nickname: str | NotGiven = NOT_GIVEN,
        outbound_agent_id: Optional[str] | NotGiven = NOT_GIVEN,
        sip_trunk_auth_password: str | NotGiven = NOT_GIVEN,
        sip_trunk_auth_username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneNumberResponse:
        """
        Import a phone number from custom telephony & Bind agents

        Args:
          phone_number: The number you are trying to import in E.164 format of the number (+country
              code, then number with no space, no special characters), used as the unique
              identifier for phone number APIs.

          termination_uri: The termination uri to uniquely identify your elastic SIP trunk. This is used
              for outbound calls. For Twilio elastic SIP trunks it always end with
              ".pstn.twilio.com".

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If null, this number would not accept
              inbound call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          sip_trunk_auth_password: The password used for authentication for the SIP trunk.

          sip_trunk_auth_username: The username used for authentication for the SIP trunk.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/import-phone-number",
            body=await async_maybe_transform(
                {
                    "phone_number": phone_number,
                    "termination_uri": termination_uri,
                    "inbound_agent_id": inbound_agent_id,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                    "sip_trunk_auth_password": sip_trunk_auth_password,
                    "sip_trunk_auth_username": sip_trunk_auth_username,
                },
                phone_number_import_params.PhoneNumberImportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberResponse,
        )


class PhoneNumberResourceWithRawResponse:
    def __init__(self, phone_number: PhoneNumberResource) -> None:
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
        self.import_ = to_raw_response_wrapper(
            phone_number.import_,
        )


class AsyncPhoneNumberResourceWithRawResponse:
    def __init__(self, phone_number: AsyncPhoneNumberResource) -> None:
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
        self.import_ = async_to_raw_response_wrapper(
            phone_number.import_,
        )


class PhoneNumberResourceWithStreamingResponse:
    def __init__(self, phone_number: PhoneNumberResource) -> None:
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
        self.import_ = to_streamed_response_wrapper(
            phone_number.import_,
        )


class AsyncPhoneNumberResourceWithStreamingResponse:
    def __init__(self, phone_number: AsyncPhoneNumberResource) -> None:
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
        self.import_ = async_to_streamed_response_wrapper(
            phone_number.import_,
        )
