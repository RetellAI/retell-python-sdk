# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from retell import Retell, AsyncRetell
from tests.utils import assert_matches_type
from retell.types import McpToolGetMcpToolsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcpTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_mcp_tools(self, client: Retell) -> None:
        mcp_tool = client.mcp_tool.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
        )
        assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

    @parametrize
    def test_method_get_mcp_tools_with_all_params(self, client: Retell) -> None:
        mcp_tool = client.mcp_tool.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
            version=1,
        )
        assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

    @parametrize
    def test_raw_response_get_mcp_tools(self, client: Retell) -> None:
        response = client.mcp_tool.with_raw_response.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_tool = response.parse()
        assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

    @parametrize
    def test_streaming_response_get_mcp_tools(self, client: Retell) -> None:
        with client.mcp_tool.with_streaming_response.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_tool = response.parse()
            assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_mcp_tools(self, client: Retell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.mcp_tool.with_raw_response.get_mcp_tools(
                agent_id="",
                mcp_id="mcp-server-1",
            )


class TestAsyncMcpTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_mcp_tools(self, async_client: AsyncRetell) -> None:
        mcp_tool = await async_client.mcp_tool.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
        )
        assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

    @parametrize
    async def test_method_get_mcp_tools_with_all_params(self, async_client: AsyncRetell) -> None:
        mcp_tool = await async_client.mcp_tool.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
            version=1,
        )
        assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

    @parametrize
    async def test_raw_response_get_mcp_tools(self, async_client: AsyncRetell) -> None:
        response = await async_client.mcp_tool.with_raw_response.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp_tool = await response.parse()
        assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

    @parametrize
    async def test_streaming_response_get_mcp_tools(self, async_client: AsyncRetell) -> None:
        async with async_client.mcp_tool.with_streaming_response.get_mcp_tools(
            agent_id="oBeDLoLOeuAbiuaMFXRtDOLriTJ5tSxD",
            mcp_id="mcp-server-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp_tool = await response.parse()
            assert_matches_type(McpToolGetMcpToolsResponse, mcp_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_mcp_tools(self, async_client: AsyncRetell) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.mcp_tool.with_raw_response.get_mcp_tools(
                agent_id="",
                mcp_id="mcp-server-1",
            )
