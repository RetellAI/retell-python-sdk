# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    ContactResponse,
    ContactListResponse,
    ContactListConversationsResponse,
    ContactBackfillAnalysisDataResponse,
    ContactGetBackfillJobStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Retell) -> None:
        contact = client.contact.create(
            phone_number="phone_number",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        contact = client.contact.create(
            phone_number="phone_number",
            custom_fields={},
            do_not_call=True,
            first_name="first_name",
            last_name="last_name",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.contact.with_raw_response.create(
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.contact.with_streaming_response.create(
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Retell) -> None:
        contact = client.contact.update(
            contact_id="contact_id",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        contact = client.contact.update(
            contact_id="contact_id",
            custom_fields={},
            do_not_call=True,
            first_name="first_name",
            last_name="last_name",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.contact.with_raw_response.update(
            contact_id="contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.contact.with_streaming_response.update(
            contact_id="contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contact.with_raw_response.update(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        contact = client.contact.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        contact = client.contact.list(
            filter_criteria={
                "contact_id": {
                    "op": "eq",
                    "type": "string",
                    "value": "value",
                },
                "custom_fields": [
                    {
                        "op": "eq",
                        "type": "string",
                        "value": "value",
                        "key": "key",
                    }
                ],
                "do_not_call": {
                    "op": "eq",
                    "type": "boolean",
                    "value": True,
                },
                "external_id": {
                    "op": "eq",
                    "type": "string",
                    "value": "value",
                },
                "last_conversation_timestamp": {
                    "op": "eq",
                    "type": "number",
                    "value": 0,
                },
                "phone_number": {
                    "op": "eq",
                    "type": "string",
                    "value": "value",
                },
            },
            limit=1,
            pagination_key="pagination_key",
            search_query="search_query",
            skip=0,
            sort_order="asc",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.contact.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.contact.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        contact = client.contact.delete(
            "contact_id",
        )
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.contact.with_raw_response.delete(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.contact.with_streaming_response.delete(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contact.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_backfill_analysis_data(self, client: Retell) -> None:
        contact = client.contact.backfill_analysis_data(
            backfill_attributes=["string"],
        )
        assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_backfill_analysis_data_with_all_params(self, client: Retell) -> None:
        contact = client.contact.backfill_analysis_data(
            backfill_attributes=["string"],
            backfill_call_filter={
                "agent": [
                    {
                        "agent_id": "x",
                        "version": [0],
                    }
                ],
                "start_timestamp": {
                    "op": "eq",
                    "type": "number",
                    "value": 0,
                },
            },
        )
        assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_backfill_analysis_data(self, client: Retell) -> None:
        response = client.contact.with_raw_response.backfill_analysis_data(
            backfill_attributes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_backfill_analysis_data(self, client: Retell) -> None:
        with client.contact.with_streaming_response.backfill_analysis_data(
            backfill_attributes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Retell) -> None:
        contact = client.contact.get(
            "contact_id",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Retell) -> None:
        response = client.contact.with_raw_response.get(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Retell) -> None:
        with client.contact.with_streaming_response.get(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contact.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_backfill_job_status(self, client: Retell) -> None:
        contact = client.contact.get_backfill_job_status()
        assert_matches_type(ContactGetBackfillJobStatusResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_backfill_job_status(self, client: Retell) -> None:
        response = client.contact.with_raw_response.get_backfill_job_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactGetBackfillJobStatusResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_backfill_job_status(self, client: Retell) -> None:
        with client.contact.with_streaming_response.get_backfill_job_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactGetBackfillJobStatusResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_by_phone(self, client: Retell) -> None:
        contact = client.contact.get_by_phone(
            "phone_number",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_by_phone(self, client: Retell) -> None:
        response = client.contact.with_raw_response.get_by_phone(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_by_phone(self, client: Retell) -> None:
        with client.contact.with_streaming_response.get_by_phone(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_by_phone(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.contact.with_raw_response.get_by_phone(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_conversations(self, client: Retell) -> None:
        contact = client.contact.list_conversations(
            contact_id="contact_id",
        )
        assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_conversations_with_all_params(self, client: Retell) -> None:
        contact = client.contact.list_conversations(
            contact_id="contact_id",
            limit=1000,
            pagination_key="pagination_key",
        )
        assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_conversations(self, client: Retell) -> None:
        response = client.contact.with_raw_response.list_conversations(
            contact_id="contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = response.parse()
        assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_conversations(self, client: Retell) -> None:
        with client.contact.with_streaming_response.list_conversations(
            contact_id="contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = response.parse()
            assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_conversations(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            client.contact.with_raw_response.list_conversations(
                contact_id="",
            )


class TestAsyncContact:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.create(
            phone_number="phone_number",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.create(
            phone_number="phone_number",
            custom_fields={},
            do_not_call=True,
            first_name="first_name",
            last_name="last_name",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.create(
            phone_number="phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.create(
            phone_number="phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.update(
            contact_id="contact_id",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.update(
            contact_id="contact_id",
            custom_fields={},
            do_not_call=True,
            first_name="first_name",
            last_name="last_name",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.update(
            contact_id="contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.update(
            contact_id="contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contact.with_raw_response.update(
                contact_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.list()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.list(
            filter_criteria={
                "contact_id": {
                    "op": "eq",
                    "type": "string",
                    "value": "value",
                },
                "custom_fields": [
                    {
                        "op": "eq",
                        "type": "string",
                        "value": "value",
                        "key": "key",
                    }
                ],
                "do_not_call": {
                    "op": "eq",
                    "type": "boolean",
                    "value": True,
                },
                "external_id": {
                    "op": "eq",
                    "type": "string",
                    "value": "value",
                },
                "last_conversation_timestamp": {
                    "op": "eq",
                    "type": "number",
                    "value": 0,
                },
                "phone_number": {
                    "op": "eq",
                    "type": "string",
                    "value": "value",
                },
            },
            limit=1,
            pagination_key="pagination_key",
            search_query="search_query",
            skip=0,
            sort_order="asc",
        )
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.delete(
            "contact_id",
        )
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.delete(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert contact is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.delete(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert contact is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contact.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_backfill_analysis_data(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.backfill_analysis_data(
            backfill_attributes=["string"],
        )
        assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_backfill_analysis_data_with_all_params(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.backfill_analysis_data(
            backfill_attributes=["string"],
            backfill_call_filter={
                "agent": [
                    {
                        "agent_id": "x",
                        "version": [0],
                    }
                ],
                "start_timestamp": {
                    "op": "eq",
                    "type": "number",
                    "value": 0,
                },
            },
        )
        assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_backfill_analysis_data(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.backfill_analysis_data(
            backfill_attributes=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_backfill_analysis_data(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.backfill_analysis_data(
            backfill_attributes=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactBackfillAnalysisDataResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.get(
            "contact_id",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.get(
            "contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.get(
            "contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contact.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_backfill_job_status(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.get_backfill_job_status()
        assert_matches_type(ContactGetBackfillJobStatusResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_backfill_job_status(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.get_backfill_job_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactGetBackfillJobStatusResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_backfill_job_status(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.get_backfill_job_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactGetBackfillJobStatusResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_by_phone(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.get_by_phone(
            "phone_number",
        )
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_by_phone(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.get_by_phone(
            "phone_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_phone(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.get_by_phone(
            "phone_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_by_phone(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.contact.with_raw_response.get_by_phone(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_conversations(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.list_conversations(
            contact_id="contact_id",
        )
        assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_conversations_with_all_params(self, async_client: AsyncRetell) -> None:
        contact = await async_client.contact.list_conversations(
            contact_id="contact_id",
            limit=1000,
            pagination_key="pagination_key",
        )
        assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_conversations(self, async_client: AsyncRetell) -> None:
        response = await async_client.contact.with_raw_response.list_conversations(
            contact_id="contact_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contact = await response.parse()
        assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_conversations(self, async_client: AsyncRetell) -> None:
        async with async_client.contact.with_streaming_response.list_conversations(
            contact_id="contact_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contact = await response.parse()
            assert_matches_type(ContactListConversationsResponse, contact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_conversations(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contact_id` but received ''"):
            await async_client.contact.with_raw_response.list_conversations(
                contact_id="",
            )
