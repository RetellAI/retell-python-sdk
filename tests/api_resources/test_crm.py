# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    CRMConfig,
    CRMGetSchemaResponse,
    CRMRunSyncJobResponse,
    CRMGetSyncJobStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCRM:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_config(self, client: Retell) -> None:
        crm = client.crm.get_config()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_config(self, client: Retell) -> None:
        response = client.crm.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = response.parse()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_config(self, client: Retell) -> None:
        with client.crm.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = response.parse()
            assert_matches_type(CRMConfig, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_schema(self, client: Retell) -> None:
        crm = client.crm.get_schema()
        assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_schema_with_all_params(self, client: Retell) -> None:
        crm = client.crm.get_schema(
            app_id="app_id",
        )
        assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_schema(self, client: Retell) -> None:
        response = client.crm.with_raw_response.get_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = response.parse()
        assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_schema(self, client: Retell) -> None:
        with client.crm.with_streaming_response.get_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = response.parse()
            assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_sync_job_status(self, client: Retell) -> None:
        crm = client.crm.get_sync_job_status()
        assert_matches_type(CRMGetSyncJobStatusResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_sync_job_status(self, client: Retell) -> None:
        response = client.crm.with_raw_response.get_sync_job_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = response.parse()
        assert_matches_type(CRMGetSyncJobStatusResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_sync_job_status(self, client: Retell) -> None:
        with client.crm.with_streaming_response.get_sync_job_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = response.parse()
            assert_matches_type(CRMGetSyncJobStatusResponse, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_run_sync_job(self, client: Retell) -> None:
        crm = client.crm.run_sync_job()
        assert_matches_type(CRMRunSyncJobResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_run_sync_job(self, client: Retell) -> None:
        response = client.crm.with_raw_response.run_sync_job()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = response.parse()
        assert_matches_type(CRMRunSyncJobResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_run_sync_job(self, client: Retell) -> None:
        with client.crm.with_streaming_response.run_sync_job() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = response.parse()
            assert_matches_type(CRMRunSyncJobResponse, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_config(self, client: Retell) -> None:
        crm = client.crm.update_config()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_config_with_all_params(self, client: Retell) -> None:
        crm = client.crm.update_config(
            app_id="app_id",
            contact_columns_order=["string"],
            crm_analysis_data_mappings=[
                {
                    "analysis_data_name": "analysis_data_name",
                    "field_name": "field_name",
                    "update_mode": "overwrite",
                }
            ],
            custom_fields=[
                {
                    "name": "name",
                    "type": "string",
                    "description": "description",
                    "label": "label",
                    "options": ["string"],
                }
            ],
        )
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_config(self, client: Retell) -> None:
        response = client.crm.with_raw_response.update_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = response.parse()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_config(self, client: Retell) -> None:
        with client.crm.with_streaming_response.update_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = response.parse()
            assert_matches_type(CRMConfig, crm, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCRM:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_config(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.get_config()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_config(self, async_client: AsyncRetell) -> None:
        response = await async_client.crm.with_raw_response.get_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = await response.parse()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_config(self, async_client: AsyncRetell) -> None:
        async with async_client.crm.with_streaming_response.get_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = await response.parse()
            assert_matches_type(CRMConfig, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_schema(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.get_schema()
        assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_schema_with_all_params(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.get_schema(
            app_id="app_id",
        )
        assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_schema(self, async_client: AsyncRetell) -> None:
        response = await async_client.crm.with_raw_response.get_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = await response.parse()
        assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_schema(self, async_client: AsyncRetell) -> None:
        async with async_client.crm.with_streaming_response.get_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = await response.parse()
            assert_matches_type(CRMGetSchemaResponse, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_sync_job_status(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.get_sync_job_status()
        assert_matches_type(CRMGetSyncJobStatusResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_sync_job_status(self, async_client: AsyncRetell) -> None:
        response = await async_client.crm.with_raw_response.get_sync_job_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = await response.parse()
        assert_matches_type(CRMGetSyncJobStatusResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_sync_job_status(self, async_client: AsyncRetell) -> None:
        async with async_client.crm.with_streaming_response.get_sync_job_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = await response.parse()
            assert_matches_type(CRMGetSyncJobStatusResponse, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_run_sync_job(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.run_sync_job()
        assert_matches_type(CRMRunSyncJobResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_run_sync_job(self, async_client: AsyncRetell) -> None:
        response = await async_client.crm.with_raw_response.run_sync_job()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = await response.parse()
        assert_matches_type(CRMRunSyncJobResponse, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_run_sync_job(self, async_client: AsyncRetell) -> None:
        async with async_client.crm.with_streaming_response.run_sync_job() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = await response.parse()
            assert_matches_type(CRMRunSyncJobResponse, crm, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_config(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.update_config()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_config_with_all_params(self, async_client: AsyncRetell) -> None:
        crm = await async_client.crm.update_config(
            app_id="app_id",
            contact_columns_order=["string"],
            crm_analysis_data_mappings=[
                {
                    "analysis_data_name": "analysis_data_name",
                    "field_name": "field_name",
                    "update_mode": "overwrite",
                }
            ],
            custom_fields=[
                {
                    "name": "name",
                    "type": "string",
                    "description": "description",
                    "label": "label",
                    "options": ["string"],
                }
            ],
        )
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_config(self, async_client: AsyncRetell) -> None:
        response = await async_client.crm.with_raw_response.update_config()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        crm = await response.parse()
        assert_matches_type(CRMConfig, crm, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_config(self, async_client: AsyncRetell) -> None:
        async with async_client.crm.with_streaming_response.update_config() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            crm = await response.parse()
            assert_matches_type(CRMConfig, crm, path=["response"])

        assert cast(Any, response.is_closed) is True
