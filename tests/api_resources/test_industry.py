# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import IndustryRetrieveNaicsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndustry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_naics(self, client: ContextDev) -> None:
        industry = client.industry.retrieve_naics(
            input="input",
        )
        assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_naics_with_all_params(self, client: ContextDev) -> None:
        industry = client.industry.retrieve_naics(
            input="input",
            max_results=1,
            min_results=1,
            timeout_ms=1000,
        )
        assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_naics(self, client: ContextDev) -> None:
        response = client.industry.with_raw_response.retrieve_naics(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        industry = response.parse()
        assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_naics(self, client: ContextDev) -> None:
        with client.industry.with_streaming_response.retrieve_naics(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            industry = response.parse()
            assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIndustry:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_naics(self, async_client: AsyncContextDev) -> None:
        industry = await async_client.industry.retrieve_naics(
            input="input",
        )
        assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_naics_with_all_params(self, async_client: AsyncContextDev) -> None:
        industry = await async_client.industry.retrieve_naics(
            input="input",
            max_results=1,
            min_results=1,
            timeout_ms=1000,
        )
        assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_naics(self, async_client: AsyncContextDev) -> None:
        response = await async_client.industry.with_raw_response.retrieve_naics(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        industry = await response.parse()
        assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_naics(self, async_client: AsyncContextDev) -> None:
        async with async_client.industry.with_streaming_response.retrieve_naics(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            industry = await response.parse()
            assert_matches_type(IndustryRetrieveNaicsResponse, industry, path=["response"])

        assert cast(Any, response.is_closed) is True
