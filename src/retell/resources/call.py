# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, cast
from typing_extensions import Literal

import httpx

from ..types import (
    call_list_params,
    call_update_params,
    call_create_web_call_params,
    call_create_phone_call_params,
    call_register_phone_call_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.call_response import CallResponse
from ..types.web_call_response import WebCallResponse
from ..types.call_list_response import CallListResponse
from ..types.phone_call_response import PhoneCallResponse

__all__ = ["CallResource", "AsyncCallResource"]


class CallResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return CallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return CallResourceWithStreamingResponse(self)

    def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallResponse:
        """
        Retrieve details of a specific call

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return cast(
            CallResponse,
            self._get(
                f"/v2/get-call/{call_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CallResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update(
        self,
        call_id: str,
        *,
        metadata: object | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallResponse:
        """
        Update metadata and sensitive data storage settings for an existing call.

        Args:
          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object. Size limited to 50kB max.

          opt_out_sensitive_data_storage: Whether this call opts out of sensitive data storage like transcript, recording,
              logging. Can only be changed from false to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return cast(
            CallResponse,
            self._patch(
                f"/v2/update-call/{call_id}",
                body=maybe_transform(
                    {
                        "metadata": metadata,
                        "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    },
                    call_update_params.CallUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CallResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        filter_criteria: call_list_params.FilterCriteria | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        pagination_key: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallListResponse:
        """
        Retrieve call details

        Args:
          filter_criteria: Filter criteria for the calls to retrieve.

          limit: Limit the number of calls returned. Default 50, Max 1000. To retrieve more than
              1000, use pagination_key to continue fetching the next page.

          pagination_key: The pagination key to continue fetching the next page of calls. Pagination key
              is represented by a call id here, and it's exclusive (not included in the
              fetched calls). The last call id from the list calls is usually used as
              pagination key here. If not set, will start from the beginning.

          sort_order: The calls will be sorted by `start_timestamp`, whether to return the calls in
              ascending or descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/list-calls",
            body=maybe_transform(
                {
                    "filter_criteria": filter_criteria,
                    "limit": limit,
                    "pagination_key": pagination_key,
                    "sort_order": sort_order,
                },
                call_list_params.CallListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallListResponse,
        )

    def delete(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific call and its associated data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v2/delete-call/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_phone_call(
        self,
        *,
        from_number: str,
        to_number: str,
        custom_sip_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        override_agent_id: str | NotGiven = NOT_GIVEN,
        override_agent_version: int | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneCallResponse:
        """
        Create a new outbound phone call

        Args:
          from_number: The number you own in E.164 format. Must be a number purchased from Retell or
              imported to Retell.

          to_number: The number you want to call, in E.164 format. If using a number purchased from
              Retell, only US numbers are supported as destination.

          custom_sip_headers: Add optional custom SIP headers to the call.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object.

          override_agent_id: For this particular call, override the agent used with this agent id. This does
              not bind the agent to this number, this is for one time override.

          override_agent_version: For this particular call, override the agent version used with this version.
              This does not bind the agent version to this number, this is for one time
              override.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/create-phone-call",
            body=maybe_transform(
                {
                    "from_number": from_number,
                    "to_number": to_number,
                    "custom_sip_headers": custom_sip_headers,
                    "metadata": metadata,
                    "override_agent_id": override_agent_id,
                    "override_agent_version": override_agent_version,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                call_create_phone_call_params.CallCreatePhoneCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCallResponse,
        )

    def create_web_call(
        self,
        *,
        agent_id: str,
        agent_version: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebCallResponse:
        """Create a new web call

        Args:
          agent_id: Unique id of agent used for the call.

        Your agent would contain the LLM Websocket
              url used for this call.

          agent_version: The version of the agent to use for the call.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/create-web-call",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_version": agent_version,
                    "metadata": metadata,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                call_create_web_call_params.CallCreateWebCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebCallResponse,
        )

    def register_phone_call(
        self,
        *,
        agent_id: str,
        agent_version: int | NotGiven = NOT_GIVEN,
        direction: Literal["inbound", "outbound"] | NotGiven = NOT_GIVEN,
        from_number: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        to_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneCallResponse:
        """
        Register a new phone call for custom telephony

        Args:
          agent_id: The agent to use for the call.

          agent_version: The version of the agent to use for the call.

          direction: Direction of the phone call. Stored for tracking purpose.

          from_number: The number you own in E.164 format. Stored for tracking purpose.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          to_number: The number you want to call, in E.164 format. Stored for tracking purpose.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/register-phone-call",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_version": agent_version,
                    "direction": direction,
                    "from_number": from_number,
                    "metadata": metadata,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                    "to_number": to_number,
                },
                call_register_phone_call_params.CallRegisterPhoneCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCallResponse,
        )


class AsyncCallResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCallResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCallResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/RetellAI/retell-python-sdk#with_streaming_response
        """
        return AsyncCallResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallResponse:
        """
        Retrieve details of a specific call

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return cast(
            CallResponse,
            await self._get(
                f"/v2/get-call/{call_id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CallResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update(
        self,
        call_id: str,
        *,
        metadata: object | NotGiven = NOT_GIVEN,
        opt_out_sensitive_data_storage: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallResponse:
        """
        Update metadata and sensitive data storage settings for an existing call.

        Args:
          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object. Size limited to 50kB max.

          opt_out_sensitive_data_storage: Whether this call opts out of sensitive data storage like transcript, recording,
              logging. Can only be changed from false to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        return cast(
            CallResponse,
            await self._patch(
                f"/v2/update-call/{call_id}",
                body=await async_maybe_transform(
                    {
                        "metadata": metadata,
                        "opt_out_sensitive_data_storage": opt_out_sensitive_data_storage,
                    },
                    call_update_params.CallUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, CallResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        filter_criteria: call_list_params.FilterCriteria | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        pagination_key: str | NotGiven = NOT_GIVEN,
        sort_order: Literal["ascending", "descending"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CallListResponse:
        """
        Retrieve call details

        Args:
          filter_criteria: Filter criteria for the calls to retrieve.

          limit: Limit the number of calls returned. Default 50, Max 1000. To retrieve more than
              1000, use pagination_key to continue fetching the next page.

          pagination_key: The pagination key to continue fetching the next page of calls. Pagination key
              is represented by a call id here, and it's exclusive (not included in the
              fetched calls). The last call id from the list calls is usually used as
              pagination key here. If not set, will start from the beginning.

          sort_order: The calls will be sorted by `start_timestamp`, whether to return the calls in
              ascending or descending order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/list-calls",
            body=await async_maybe_transform(
                {
                    "filter_criteria": filter_criteria,
                    "limit": limit,
                    "pagination_key": pagination_key,
                    "sort_order": sort_order,
                },
                call_list_params.CallListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallListResponse,
        )

    async def delete(
        self,
        call_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a specific call and its associated data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not call_id:
            raise ValueError(f"Expected a non-empty value for `call_id` but received {call_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v2/delete-call/{call_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_phone_call(
        self,
        *,
        from_number: str,
        to_number: str,
        custom_sip_headers: Dict[str, str] | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        override_agent_id: str | NotGiven = NOT_GIVEN,
        override_agent_version: int | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneCallResponse:
        """
        Create a new outbound phone call

        Args:
          from_number: The number you own in E.164 format. Must be a number purchased from Retell or
              imported to Retell.

          to_number: The number you want to call, in E.164 format. If using a number purchased from
              Retell, only US numbers are supported as destination.

          custom_sip_headers: Add optional custom SIP headers to the call.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object.

          override_agent_id: For this particular call, override the agent used with this agent id. This does
              not bind the agent to this number, this is for one time override.

          override_agent_version: For this particular call, override the agent version used with this version.
              This does not bind the agent version to this number, this is for one time
              override.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/create-phone-call",
            body=await async_maybe_transform(
                {
                    "from_number": from_number,
                    "to_number": to_number,
                    "custom_sip_headers": custom_sip_headers,
                    "metadata": metadata,
                    "override_agent_id": override_agent_id,
                    "override_agent_version": override_agent_version,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                call_create_phone_call_params.CallCreatePhoneCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCallResponse,
        )

    async def create_web_call(
        self,
        *,
        agent_id: str,
        agent_version: int | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WebCallResponse:
        """Create a new web call

        Args:
          agent_id: Unique id of agent used for the call.

        Your agent would contain the LLM Websocket
              url used for this call.

          agent_version: The version of the agent to use for the call.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/create-web-call",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_version": agent_version,
                    "metadata": metadata,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                },
                call_create_web_call_params.CallCreateWebCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebCallResponse,
        )

    async def register_phone_call(
        self,
        *,
        agent_id: str,
        agent_version: int | NotGiven = NOT_GIVEN,
        direction: Literal["inbound", "outbound"] | NotGiven = NOT_GIVEN,
        from_number: str | NotGiven = NOT_GIVEN,
        metadata: object | NotGiven = NOT_GIVEN,
        retell_llm_dynamic_variables: Dict[str, object] | NotGiven = NOT_GIVEN,
        to_number: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PhoneCallResponse:
        """
        Register a new phone call for custom telephony

        Args:
          agent_id: The agent to use for the call.

          agent_version: The version of the agent to use for the call.

          direction: Direction of the phone call. Stored for tracking purpose.

          from_number: The number you own in E.164 format. Stored for tracking purpose.

          metadata: An arbitrary object for storage purpose only. You can put anything here like
              your internal customer id associated with the call. Not used for processing. You
              can later get this field from the call object.

          retell_llm_dynamic_variables: Add optional dynamic variables in key value pairs of string that injects into
              your Response Engine prompt and tool description. Only applicable for Response
              Engine.

          to_number: The number you want to call, in E.164 format. Stored for tracking purpose.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/register-phone-call",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "agent_version": agent_version,
                    "direction": direction,
                    "from_number": from_number,
                    "metadata": metadata,
                    "retell_llm_dynamic_variables": retell_llm_dynamic_variables,
                    "to_number": to_number,
                },
                call_register_phone_call_params.CallRegisterPhoneCallParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneCallResponse,
        )


class CallResourceWithRawResponse:
    def __init__(self, call: CallResource) -> None:
        self._call = call

        self.retrieve = to_raw_response_wrapper(
            call.retrieve,
        )
        self.update = to_raw_response_wrapper(
            call.update,
        )
        self.list = to_raw_response_wrapper(
            call.list,
        )
        self.delete = to_raw_response_wrapper(
            call.delete,
        )
        self.create_phone_call = to_raw_response_wrapper(
            call.create_phone_call,
        )
        self.create_web_call = to_raw_response_wrapper(
            call.create_web_call,
        )
        self.register_phone_call = to_raw_response_wrapper(
            call.register_phone_call,
        )


class AsyncCallResourceWithRawResponse:
    def __init__(self, call: AsyncCallResource) -> None:
        self._call = call

        self.retrieve = async_to_raw_response_wrapper(
            call.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            call.update,
        )
        self.list = async_to_raw_response_wrapper(
            call.list,
        )
        self.delete = async_to_raw_response_wrapper(
            call.delete,
        )
        self.create_phone_call = async_to_raw_response_wrapper(
            call.create_phone_call,
        )
        self.create_web_call = async_to_raw_response_wrapper(
            call.create_web_call,
        )
        self.register_phone_call = async_to_raw_response_wrapper(
            call.register_phone_call,
        )


class CallResourceWithStreamingResponse:
    def __init__(self, call: CallResource) -> None:
        self._call = call

        self.retrieve = to_streamed_response_wrapper(
            call.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            call.update,
        )
        self.list = to_streamed_response_wrapper(
            call.list,
        )
        self.delete = to_streamed_response_wrapper(
            call.delete,
        )
        self.create_phone_call = to_streamed_response_wrapper(
            call.create_phone_call,
        )
        self.create_web_call = to_streamed_response_wrapper(
            call.create_web_call,
        )
        self.register_phone_call = to_streamed_response_wrapper(
            call.register_phone_call,
        )


class AsyncCallResourceWithStreamingResponse:
    def __init__(self, call: AsyncCallResource) -> None:
        self._call = call

        self.retrieve = async_to_streamed_response_wrapper(
            call.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            call.update,
        )
        self.list = async_to_streamed_response_wrapper(
            call.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            call.delete,
        )
        self.create_phone_call = async_to_streamed_response_wrapper(
            call.create_phone_call,
        )
        self.create_web_call = async_to_streamed_response_wrapper(
            call.create_web_call,
        )
        self.register_phone_call = async_to_streamed_response_wrapper(
            call.register_phone_call,
        )
