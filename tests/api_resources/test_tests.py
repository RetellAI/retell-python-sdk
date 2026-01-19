# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import (
    BatchTestResponse,
    TestCaseJobResponse,
    TestListTestRunsResponse,
    TestCaseDefinitionResponse,
    TestListBatchTestsResponse,
    TestListTestCaseDefinitionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch_test(self, client: Retell) -> None:
        test = client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_batch_test_with_all_params(self, client: Retell) -> None:
        test = client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            test_case_definition_ids=["string"],
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_batch_test(self, client: Retell) -> None:
        response = client.tests.with_raw_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_batch_test(self, client: Retell) -> None:
        with client.tests.with_streaming_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(BatchTestResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_test_case_definition(self, client: Retell) -> None:
        test = client.tests.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            user_prompt="user_prompt",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_test_case_definition_with_all_params(self, client: Retell) -> None:
        test = client.tests.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            user_prompt="user_prompt",
            dynamic_variables={"foo": "string"},
            llm_model="gpt-4.1",
            tool_mocks=[
                {
                    "input_match_rule": {"type": "any"},
                    "output": "output",
                    "tool_name": "tool_name",
                    "result": True,
                }
            ],
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_test_case_definition(self, client: Retell) -> None:
        response = client.tests.with_raw_response.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            user_prompt="user_prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_test_case_definition(self, client: Retell) -> None:
        with client.tests.with_streaming_response.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            user_prompt="user_prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_test_case_definition(self, client: Retell) -> None:
        test = client.tests.delete_test_case_definition(
            "test_case_definition_id",
        )
        assert test is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_test_case_definition(self, client: Retell) -> None:
        response = client.tests.with_raw_response.delete_test_case_definition(
            "test_case_definition_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert test is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_test_case_definition(self, client: Retell) -> None:
        with client.tests.with_streaming_response.delete_test_case_definition(
            "test_case_definition_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert test is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete_test_case_definition(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_definition_id` but received ''"
        ):
            client.tests.with_raw_response.delete_test_case_definition(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_batch_test(self, client: Retell) -> None:
        test = client.tests.get_batch_test(
            "test_case_batch_job_id",
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_batch_test(self, client: Retell) -> None:
        response = client.tests.with_raw_response.get_batch_test(
            "test_case_batch_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_batch_test(self, client: Retell) -> None:
        with client.tests.with_streaming_response.get_batch_test(
            "test_case_batch_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(BatchTestResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_batch_test(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_batch_job_id` but received ''"
        ):
            client.tests.with_raw_response.get_batch_test(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_test_case_definition(self, client: Retell) -> None:
        test = client.tests.get_test_case_definition(
            "test_case_definition_id",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_test_case_definition(self, client: Retell) -> None:
        response = client.tests.with_raw_response.get_test_case_definition(
            "test_case_definition_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_test_case_definition(self, client: Retell) -> None:
        with client.tests.with_streaming_response.get_test_case_definition(
            "test_case_definition_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_test_case_definition(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_definition_id` but received ''"
        ):
            client.tests.with_raw_response.get_test_case_definition(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_test_run(self, client: Retell) -> None:
        test = client.tests.get_test_run(
            "test_case_job_id",
        )
        assert_matches_type(TestCaseJobResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_test_run(self, client: Retell) -> None:
        response = client.tests.with_raw_response.get_test_run(
            "test_case_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestCaseJobResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_test_run(self, client: Retell) -> None:
        with client.tests.with_streaming_response.get_test_run(
            "test_case_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestCaseJobResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_test_run(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_job_id` but received ''"):
            client.tests.with_raw_response.get_test_run(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_batch_tests(self, client: Retell) -> None:
        test = client.tests.list_batch_tests(
            type="retell-llm",
        )
        assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_batch_tests_with_all_params(self, client: Retell) -> None:
        test = client.tests.list_batch_tests(
            type="retell-llm",
            conversation_flow_id="conversation_flow_id",
            llm_id="llm_id",
            version=0,
        )
        assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_batch_tests(self, client: Retell) -> None:
        response = client.tests.with_raw_response.list_batch_tests(
            type="retell-llm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_batch_tests(self, client: Retell) -> None:
        with client.tests.with_streaming_response.list_batch_tests(
            type="retell-llm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_test_case_definitions(self, client: Retell) -> None:
        test = client.tests.list_test_case_definitions(
            type="retell-llm",
        )
        assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_test_case_definitions_with_all_params(self, client: Retell) -> None:
        test = client.tests.list_test_case_definitions(
            type="retell-llm",
            conversation_flow_id="conversation_flow_id",
            llm_id="llm_id",
            version=0,
        )
        assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_test_case_definitions(self, client: Retell) -> None:
        response = client.tests.with_raw_response.list_test_case_definitions(
            type="retell-llm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_test_case_definitions(self, client: Retell) -> None:
        with client.tests.with_streaming_response.list_test_case_definitions(
            type="retell-llm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_test_runs(self, client: Retell) -> None:
        test = client.tests.list_test_runs(
            "test_case_batch_job_id",
        )
        assert_matches_type(TestListTestRunsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_test_runs(self, client: Retell) -> None:
        response = client.tests.with_raw_response.list_test_runs(
            "test_case_batch_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestListTestRunsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_test_runs(self, client: Retell) -> None:
        with client.tests.with_streaming_response.list_test_runs(
            "test_case_batch_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestListTestRunsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_test_runs(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_batch_job_id` but received ''"
        ):
            client.tests.with_raw_response.list_test_runs(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_test_case_definition(self, client: Retell) -> None:
        test = client.tests.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_test_case_definition_with_all_params(self, client: Retell) -> None:
        test = client.tests.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
            dynamic_variables={"foo": "string"},
            llm_model="gpt-4.1",
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            tool_mocks=[
                {
                    "input_match_rule": {"type": "any"},
                    "output": "output",
                    "tool_name": "tool_name",
                    "result": True,
                }
            ],
            user_prompt="user_prompt",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_test_case_definition(self, client: Retell) -> None:
        response = client.tests.with_raw_response.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = response.parse()
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_test_case_definition(self, client: Retell) -> None:
        with client.tests.with_streaming_response.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = response.parse()
            assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_test_case_definition(self, client: Retell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_definition_id` but received ''"
        ):
            client.tests.with_raw_response.update_test_case_definition(
                test_case_definition_id="",
            )


class TestAsyncTests:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch_test(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_batch_test_with_all_params(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            test_case_definition_ids=["string"],
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_batch_test(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_batch_test(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.create_batch_test(
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            test_case_definition_ids=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(BatchTestResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_test_case_definition(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            user_prompt="user_prompt",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_test_case_definition_with_all_params(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            user_prompt="user_prompt",
            dynamic_variables={"foo": "string"},
            llm_model="gpt-4.1",
            tool_mocks=[
                {
                    "input_match_rule": {"type": "any"},
                    "output": "output",
                    "tool_name": "tool_name",
                    "result": True,
                }
            ],
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_test_case_definition(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            user_prompt="user_prompt",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_test_case_definition(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.create_test_case_definition(
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
            },
            user_prompt="user_prompt",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_test_case_definition(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.delete_test_case_definition(
            "test_case_definition_id",
        )
        assert test is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_test_case_definition(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.delete_test_case_definition(
            "test_case_definition_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert test is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_test_case_definition(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.delete_test_case_definition(
            "test_case_definition_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert test is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete_test_case_definition(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_definition_id` but received ''"
        ):
            await async_client.tests.with_raw_response.delete_test_case_definition(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_batch_test(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.get_batch_test(
            "test_case_batch_job_id",
        )
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_batch_test(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.get_batch_test(
            "test_case_batch_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(BatchTestResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_batch_test(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.get_batch_test(
            "test_case_batch_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(BatchTestResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_batch_test(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_batch_job_id` but received ''"
        ):
            await async_client.tests.with_raw_response.get_batch_test(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_test_case_definition(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.get_test_case_definition(
            "test_case_definition_id",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_test_case_definition(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.get_test_case_definition(
            "test_case_definition_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_test_case_definition(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.get_test_case_definition(
            "test_case_definition_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_test_case_definition(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_definition_id` but received ''"
        ):
            await async_client.tests.with_raw_response.get_test_case_definition(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_test_run(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.get_test_run(
            "test_case_job_id",
        )
        assert_matches_type(TestCaseJobResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_test_run(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.get_test_run(
            "test_case_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestCaseJobResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_test_run(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.get_test_run(
            "test_case_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestCaseJobResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_test_run(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `test_case_job_id` but received ''"):
            await async_client.tests.with_raw_response.get_test_run(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_batch_tests(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.list_batch_tests(
            type="retell-llm",
        )
        assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_batch_tests_with_all_params(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.list_batch_tests(
            type="retell-llm",
            conversation_flow_id="conversation_flow_id",
            llm_id="llm_id",
            version=0,
        )
        assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_batch_tests(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.list_batch_tests(
            type="retell-llm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_batch_tests(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.list_batch_tests(
            type="retell-llm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestListBatchTestsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_test_case_definitions(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.list_test_case_definitions(
            type="retell-llm",
        )
        assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_test_case_definitions_with_all_params(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.list_test_case_definitions(
            type="retell-llm",
            conversation_flow_id="conversation_flow_id",
            llm_id="llm_id",
            version=0,
        )
        assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_test_case_definitions(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.list_test_case_definitions(
            type="retell-llm",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_test_case_definitions(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.list_test_case_definitions(
            type="retell-llm",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestListTestCaseDefinitionsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_test_runs(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.list_test_runs(
            "test_case_batch_job_id",
        )
        assert_matches_type(TestListTestRunsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_test_runs(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.list_test_runs(
            "test_case_batch_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestListTestRunsResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_test_runs(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.list_test_runs(
            "test_case_batch_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestListTestRunsResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_test_runs(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_batch_job_id` but received ''"
        ):
            await async_client.tests.with_raw_response.list_test_runs(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_test_case_definition(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_test_case_definition_with_all_params(self, async_client: AsyncRetell) -> None:
        test = await async_client.tests.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
            dynamic_variables={"foo": "string"},
            llm_model="gpt-4.1",
            metrics=["string"],
            name="name",
            response_engine={
                "llm_id": "llm_id",
                "type": "retell-llm",
                "version": 0,
            },
            tool_mocks=[
                {
                    "input_match_rule": {"type": "any"},
                    "output": "output",
                    "tool_name": "tool_name",
                    "result": True,
                }
            ],
            user_prompt="user_prompt",
        )
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_test_case_definition(self, async_client: AsyncRetell) -> None:
        response = await async_client.tests.with_raw_response.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        test = await response.parse()
        assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_test_case_definition(self, async_client: AsyncRetell) -> None:
        async with async_client.tests.with_streaming_response.update_test_case_definition(
            test_case_definition_id="test_case_definition_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            test = await response.parse()
            assert_matches_type(TestCaseDefinitionResponse, test, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_test_case_definition(self, async_client: AsyncRetell) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `test_case_definition_id` but received ''"
        ):
            await async_client.tests.with_raw_response.update_test_case_definition(
                test_case_definition_id="",
            )
