# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import phone_number_create_params, phone_number_import_params, phone_number_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.phone_number_response import PhoneNumberResponse
from ..types.phone_number_list_response import PhoneNumberListResponse

__all__ = ["PhoneNumberResource", "AsyncPhoneNumberResource"]


class PhoneNumberResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhoneNumberResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        area_code: int | Omit = omit,
        country_code: Literal["US", "CA"] | Omit = omit,
        inbound_agent_id: Optional[str] | Omit = omit,
        inbound_agent_version: Optional[int] | Omit = omit,
        inbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        inbound_webhook_url: Optional[str] | Omit = omit,
        nickname: str | Omit = omit,
        number_provider: Literal["twilio", "telnyx"] | Omit = omit,
        outbound_agent_id: Optional[str] | Omit = omit,
        outbound_agent_version: Optional[int] | Omit = omit,
        outbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        phone_number: str | Omit = omit,
        toll_free: bool | Omit = omit,
        transport: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Buy a new phone number & Bind agents

        Args:
          area_code: Area code of the number to obtain. Format is a 3 digit integer. Currently only
              supports US area code.

          country_code: The ISO 3166-1 alpha-2 country code of the number you are trying to purchase. If
              left empty, will default to "US".

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If null, this number would not accept
              inbound call.

          inbound_agent_version: Version of the inbound agent to bind to the number. If not provided, will
              default to latest version.

          inbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.
              If not set or empty, calls from all countries are allowed.

          inbound_webhook_url: If set, will send a webhook for inbound calls, where you can to override agent
              id, set dynamic variables and other fields specific to that call.

          nickname: Nickname of the number. This is for your reference only.

          number_provider: The provider to purchase the phone number from. Default to twilio.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          outbound_agent_version: Version of the outbound agent to bind to the number. If not provided, will
              default to latest version.

          outbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed. If
              not set or empty, calls to all countries are allowed.

          phone_number: The number you are trying to purchase in E.164 format of the number (+country
              code then number with no space and no special characters).

          toll_free: Whether to purchase a toll-free number. Toll-free numbers incur higher costs.

          transport: Outbound transport protocol to use for the phone number. Valid values are "TLS",
              "TCP" and "UDP". Default is "TCP".

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
                    "country_code": country_code,
                    "inbound_agent_id": inbound_agent_id,
                    "inbound_agent_version": inbound_agent_version,
                    "inbound_allowed_countries": inbound_allowed_countries,
                    "inbound_webhook_url": inbound_webhook_url,
                    "nickname": nickname,
                    "number_provider": number_provider,
                    "outbound_agent_id": outbound_agent_id,
                    "outbound_agent_version": outbound_agent_version,
                    "outbound_allowed_countries": outbound_allowed_countries,
                    "phone_number": phone_number,
                    "toll_free": toll_free,
                    "transport": transport,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        auth_password: str | Omit = omit,
        auth_username: str | Omit = omit,
        inbound_agent_id: Optional[str] | Omit = omit,
        inbound_agent_version: Optional[int] | Omit = omit,
        inbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        inbound_webhook_url: Optional[str] | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        outbound_agent_id: Optional[str] | Omit = omit,
        outbound_agent_version: Optional[int] | Omit = omit,
        outbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        termination_uri: str | Omit = omit,
        transport: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Update agent bound to a purchased phone number

        Args:
          auth_password: The password used for authentication for the SIP trunk to update for the phone
              number.

          auth_username: The username used for authentication for the SIP trunk to update for the phone
              number.

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If set to null, this number would not accept
              inbound call.

          inbound_agent_version: Version of the inbound agent to bind to the number. If not provided, will
              default to latest version.

          inbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.
              If not set or empty, calls from all countries are allowed.

          inbound_webhook_url: If set, will send a webhook for inbound calls, where you can to override agent
              id, set dynamic variables and other fields specific to that call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If set to null, this number would not be
              able to initiate outbound call without agent id override.

          outbound_agent_version: Version of the outbound agent to bind to the number. If not provided, will
              default to latest version.

          outbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed. If
              not set or empty, calls to all countries are allowed.

          termination_uri: The termination uri to update for the phone number. This is used for outbound
              calls.

          transport: Outbound transport protocol to update for the phone number. Valid values are
              "TLS", "TCP" and "UDP". Default is "TCP".

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
                    "auth_password": auth_password,
                    "auth_username": auth_username,
                    "inbound_agent_id": inbound_agent_id,
                    "inbound_agent_version": inbound_agent_version,
                    "inbound_allowed_countries": inbound_allowed_countries,
                    "inbound_webhook_url": inbound_webhook_url,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                    "outbound_agent_version": outbound_agent_version,
                    "outbound_allowed_countries": outbound_allowed_countries,
                    "termination_uri": termination_uri,
                    "transport": transport,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        inbound_agent_id: Optional[str] | Omit = omit,
        inbound_agent_version: Optional[int] | Omit = omit,
        inbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        inbound_webhook_url: Optional[str] | Omit = omit,
        nickname: str | Omit = omit,
        outbound_agent_id: Optional[str] | Omit = omit,
        outbound_agent_version: Optional[int] | Omit = omit,
        outbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        sip_trunk_auth_password: str | Omit = omit,
        sip_trunk_auth_username: str | Omit = omit,
        transport: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          inbound_agent_version: Version of the inbound agent to bind to the number. If not provided, will
              default to latest version.

          inbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.
              If not set or empty, calls from all countries are allowed.

          inbound_webhook_url: If set, will send a webhook for inbound calls, where you can to override agent
              id, set dynamic variables and other fields specific to that call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          outbound_agent_version: Version of the outbound agent to bind to the number. If not provided, will
              default to latest version.

          outbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed. If
              not set or empty, calls to all countries are allowed.

          sip_trunk_auth_password: The password used for authentication for the SIP trunk.

          sip_trunk_auth_username: The username used for authentication for the SIP trunk.

          transport: Outbound transport protocol to update for the phone number. Valid values are
              "TLS", "TCP" and "UDP". Default is "TCP".

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
                    "inbound_agent_version": inbound_agent_version,
                    "inbound_allowed_countries": inbound_allowed_countries,
                    "inbound_webhook_url": inbound_webhook_url,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                    "outbound_agent_version": outbound_agent_version,
                    "outbound_allowed_countries": outbound_allowed_countries,
                    "sip_trunk_auth_password": sip_trunk_auth_password,
                    "sip_trunk_auth_username": sip_trunk_auth_username,
                    "transport": transport,
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
        This property can be used as a prefix for any HTTP method call to return
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
        area_code: int | Omit = omit,
        country_code: Literal["US", "CA"] | Omit = omit,
        inbound_agent_id: Optional[str] | Omit = omit,
        inbound_agent_version: Optional[int] | Omit = omit,
        inbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        inbound_webhook_url: Optional[str] | Omit = omit,
        nickname: str | Omit = omit,
        number_provider: Literal["twilio", "telnyx"] | Omit = omit,
        outbound_agent_id: Optional[str] | Omit = omit,
        outbound_agent_version: Optional[int] | Omit = omit,
        outbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        phone_number: str | Omit = omit,
        toll_free: bool | Omit = omit,
        transport: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Buy a new phone number & Bind agents

        Args:
          area_code: Area code of the number to obtain. Format is a 3 digit integer. Currently only
              supports US area code.

          country_code: The ISO 3166-1 alpha-2 country code of the number you are trying to purchase. If
              left empty, will default to "US".

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If null, this number would not accept
              inbound call.

          inbound_agent_version: Version of the inbound agent to bind to the number. If not provided, will
              default to latest version.

          inbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.
              If not set or empty, calls from all countries are allowed.

          inbound_webhook_url: If set, will send a webhook for inbound calls, where you can to override agent
              id, set dynamic variables and other fields specific to that call.

          nickname: Nickname of the number. This is for your reference only.

          number_provider: The provider to purchase the phone number from. Default to twilio.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          outbound_agent_version: Version of the outbound agent to bind to the number. If not provided, will
              default to latest version.

          outbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed. If
              not set or empty, calls to all countries are allowed.

          phone_number: The number you are trying to purchase in E.164 format of the number (+country
              code then number with no space and no special characters).

          toll_free: Whether to purchase a toll-free number. Toll-free numbers incur higher costs.

          transport: Outbound transport protocol to use for the phone number. Valid values are "TLS",
              "TCP" and "UDP". Default is "TCP".

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
                    "country_code": country_code,
                    "inbound_agent_id": inbound_agent_id,
                    "inbound_agent_version": inbound_agent_version,
                    "inbound_allowed_countries": inbound_allowed_countries,
                    "inbound_webhook_url": inbound_webhook_url,
                    "nickname": nickname,
                    "number_provider": number_provider,
                    "outbound_agent_id": outbound_agent_id,
                    "outbound_agent_version": outbound_agent_version,
                    "outbound_allowed_countries": outbound_allowed_countries,
                    "phone_number": phone_number,
                    "toll_free": toll_free,
                    "transport": transport,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        auth_password: str | Omit = omit,
        auth_username: str | Omit = omit,
        inbound_agent_id: Optional[str] | Omit = omit,
        inbound_agent_version: Optional[int] | Omit = omit,
        inbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        inbound_webhook_url: Optional[str] | Omit = omit,
        nickname: Optional[str] | Omit = omit,
        outbound_agent_id: Optional[str] | Omit = omit,
        outbound_agent_version: Optional[int] | Omit = omit,
        outbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        termination_uri: str | Omit = omit,
        transport: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberResponse:
        """
        Update agent bound to a purchased phone number

        Args:
          auth_password: The password used for authentication for the SIP trunk to update for the phone
              number.

          auth_username: The username used for authentication for the SIP trunk to update for the phone
              number.

          inbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when receiving inbound calls. If set to null, this number would not accept
              inbound call.

          inbound_agent_version: Version of the inbound agent to bind to the number. If not provided, will
              default to latest version.

          inbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.
              If not set or empty, calls from all countries are allowed.

          inbound_webhook_url: If set, will send a webhook for inbound calls, where you can to override agent
              id, set dynamic variables and other fields specific to that call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If set to null, this number would not be
              able to initiate outbound call without agent id override.

          outbound_agent_version: Version of the outbound agent to bind to the number. If not provided, will
              default to latest version.

          outbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed. If
              not set or empty, calls to all countries are allowed.

          termination_uri: The termination uri to update for the phone number. This is used for outbound
              calls.

          transport: Outbound transport protocol to update for the phone number. Valid values are
              "TLS", "TCP" and "UDP". Default is "TCP".

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
                    "auth_password": auth_password,
                    "auth_username": auth_username,
                    "inbound_agent_id": inbound_agent_id,
                    "inbound_agent_version": inbound_agent_version,
                    "inbound_allowed_countries": inbound_allowed_countries,
                    "inbound_webhook_url": inbound_webhook_url,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                    "outbound_agent_version": outbound_agent_version,
                    "outbound_allowed_countries": outbound_allowed_countries,
                    "termination_uri": termination_uri,
                    "transport": transport,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        inbound_agent_id: Optional[str] | Omit = omit,
        inbound_agent_version: Optional[int] | Omit = omit,
        inbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        inbound_webhook_url: Optional[str] | Omit = omit,
        nickname: str | Omit = omit,
        outbound_agent_id: Optional[str] | Omit = omit,
        outbound_agent_version: Optional[int] | Omit = omit,
        outbound_allowed_countries: Optional[SequenceNotStr[str]] | Omit = omit,
        sip_trunk_auth_password: str | Omit = omit,
        sip_trunk_auth_username: str | Omit = omit,
        transport: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

          inbound_agent_version: Version of the inbound agent to bind to the number. If not provided, will
              default to latest version.

          inbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes from which inbound calls are allowed.
              If not set or empty, calls from all countries are allowed.

          inbound_webhook_url: If set, will send a webhook for inbound calls, where you can to override agent
              id, set dynamic variables and other fields specific to that call.

          nickname: Nickname of the number. This is for your reference only.

          outbound_agent_id: Unique id of agent to bind to the number. The number will automatically use the
              agent when conducting outbound calls. If null, this number would not be able to
              initiate outbound call without agent id override.

          outbound_agent_version: Version of the outbound agent to bind to the number. If not provided, will
              default to latest version.

          outbound_allowed_countries: List of ISO 3166-1 alpha-2 country codes to which outbound calls are allowed. If
              not set or empty, calls to all countries are allowed.

          sip_trunk_auth_password: The password used for authentication for the SIP trunk.

          sip_trunk_auth_username: The username used for authentication for the SIP trunk.

          transport: Outbound transport protocol to update for the phone number. Valid values are
              "TLS", "TCP" and "UDP". Default is "TCP".

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
                    "inbound_agent_version": inbound_agent_version,
                    "inbound_allowed_countries": inbound_allowed_countries,
                    "inbound_webhook_url": inbound_webhook_url,
                    "nickname": nickname,
                    "outbound_agent_id": outbound_agent_id,
                    "outbound_agent_version": outbound_agent_version,
                    "outbound_allowed_countries": outbound_allowed_countries,
                    "sip_trunk_auth_password": sip_trunk_auth_password,
                    "sip_trunk_auth_username": sip_trunk_auth_username,
                    "transport": transport,
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
