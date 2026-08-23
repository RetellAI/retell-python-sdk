# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    AppResponse,
    AppListResponse,
    AppTestAuthResponse,
    AppListUsagesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Retell) -> None:
        app = client.app.create(
            provider="provider",
            type="crm",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Retell) -> None:
        app = client.app.create(
            provider="provider",
            type="crm",
            auth_config={
                "client_id": "x",
                "client_secret": "x",
                "type": "oauth2",
            },
            crm_config={
                "inbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "outbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "sync_conversation_activity": True,
                "sync_new_contacts": True,
            },
            name="name",
            tenant_id="tenant_id",
            tenant_url="tenant_url",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Retell) -> None:
        response = client.app.with_raw_response.create(
            provider="provider",
            type="crm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Retell) -> None:
        with client.app.with_streaming_response.create(
            provider="provider",
            type="crm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Retell) -> None:
        app = client.app.update(
            app_id="app_id",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Retell) -> None:
        app = client.app.update(
            app_id="app_id",
            auth_config={
                "client_id": "x",
                "client_secret": "x",
                "type": "oauth2",
            },
            crm_config={
                "inbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "outbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "sync_conversation_activity": True,
                "sync_new_contacts": True,
            },
            name="name",
            tenant_id="tenant_id",
            tenant_url="tenant_url",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Retell) -> None:
        response = client.app.with_raw_response.update(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Retell) -> None:
        with client.app.with_streaming_response.update(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.app.with_raw_response.update(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Retell) -> None:
        app = client.app.list()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Retell) -> None:
        app = client.app.list(
            limit=1000,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Retell) -> None:
        response = client.app.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Retell) -> None:
        with client.app.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppListResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Retell) -> None:
        app = client.app.delete(
            app_id="app_id",
        )
        assert app is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Retell) -> None:
        app = client.app.delete(
            app_id="app_id",
            force_delete=True,
        )
        assert app is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Retell) -> None:
        response = client.app.with_raw_response.delete(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert app is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Retell) -> None:
        with client.app.with_streaming_response.delete(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert app is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.app.with_raw_response.delete(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: Retell) -> None:
        app = client.app.get(
            "app_id",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: Retell) -> None:
        response = client.app.with_raw_response.get(
            "app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: Retell) -> None:
        with client.app.with_streaming_response.get(
            "app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.app.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_usages(self, client: Retell) -> None:
        app = client.app.list_usages(
            app_id="app_id",
        )
        assert_matches_type(AppListUsagesResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_usages_with_all_params(self, client: Retell) -> None:
        app = client.app.list_usages(
            app_id="app_id",
            limit=1000,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(AppListUsagesResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_usages(self, client: Retell) -> None:
        response = client.app.with_raw_response.list_usages(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppListUsagesResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_usages(self, client: Retell) -> None:
        with client.app.with_streaming_response.list_usages(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppListUsagesResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_usages(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.app.with_raw_response.list_usages(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_test_auth(self, client: Retell) -> None:
        app = client.app.test_auth(
            "app_id",
        )
        assert_matches_type(AppTestAuthResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_test_auth(self, client: Retell) -> None:
        response = client.app.with_raw_response.test_auth(
            "app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppTestAuthResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_test_auth(self, client: Retell) -> None:
        with client.app.with_streaming_response.test_auth(
            "app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppTestAuthResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_test_auth(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.app.with_raw_response.test_auth(
                "",
            )


class TestAsyncApp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.create(
            provider="provider",
            type="crm",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.create(
            provider="provider",
            type="crm",
            auth_config={
                "client_id": "x",
                "client_secret": "x",
                "type": "oauth2",
            },
            crm_config={
                "inbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "outbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "sync_conversation_activity": True,
                "sync_new_contacts": True,
            },
            name="name",
            tenant_id="tenant_id",
            tenant_url="tenant_url",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.create(
            provider="provider",
            type="crm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.create(
            provider="provider",
            type="crm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.update(
            app_id="app_id",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.update(
            app_id="app_id",
            auth_config={
                "client_id": "x",
                "client_secret": "x",
                "type": "oauth2",
            },
            crm_config={
                "inbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "outbound_sync_mappings": [
                    {
                        "external_field_name": "external_field_name",
                        "field_name": "field_name",
                    }
                ],
                "sync_conversation_activity": True,
                "sync_new_contacts": True,
            },
            name="name",
            tenant_id="tenant_id",
            tenant_url="tenant_url",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.update(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.update(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.app.with_raw_response.update(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.list()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.list(
            limit=1000,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppListResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppListResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.delete(
            app_id="app_id",
        )
        assert app is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.delete(
            app_id="app_id",
            force_delete=True,
        )
        assert app is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.delete(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert app is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.delete(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert app is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.app.with_raw_response.delete(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.get(
            "app_id",
        )
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.get(
            "app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.get(
            "app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.app.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_usages(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.list_usages(
            app_id="app_id",
        )
        assert_matches_type(AppListUsagesResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_usages_with_all_params(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.list_usages(
            app_id="app_id",
            limit=1000,
            pagination_key="pagination_key",
            sort_order="ascending",
        )
        assert_matches_type(AppListUsagesResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_usages(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.list_usages(
            app_id="app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppListUsagesResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_usages(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.list_usages(
            app_id="app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppListUsagesResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_usages(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.app.with_raw_response.list_usages(
                app_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_test_auth(self, async_client: AsyncRetell) -> None:
        app = await async_client.app.test_auth(
            "app_id",
        )
        assert_matches_type(AppTestAuthResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_test_auth(self, async_client: AsyncRetell) -> None:
        response = await async_client.app.with_raw_response.test_auth(
            "app_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppTestAuthResponse, app, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_test_auth(self, async_client: AsyncRetell) -> None:
        async with async_client.app.with_streaming_response.test_auth(
            "app_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppTestAuthResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_test_auth(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.app.with_raw_response.test_auth(
                "",
            )
