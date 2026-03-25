# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    UtilityPrefetchResponse,
    UtilityPrefetchByEmailResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUtility:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_prefetch(self, client: ContextDev) -> None:
        utility = client.utility.prefetch(
            domain="domain",
        )
        assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_prefetch_with_all_params(self, client: ContextDev) -> None:
        utility = client.utility.prefetch(
            domain="domain",
            timeout_ms=1000,
        )
        assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_prefetch(self, client: ContextDev) -> None:
        response = client.utility.with_raw_response.prefetch(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        utility = response.parse()
        assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_prefetch(self, client: ContextDev) -> None:
        with client.utility.with_streaming_response.prefetch(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            utility = response.parse()
            assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_prefetch_by_email(self, client: ContextDev) -> None:
        utility = client.utility.prefetch_by_email(
            email="dev@stainless.com",
        )
        assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_prefetch_by_email_with_all_params(self, client: ContextDev) -> None:
        utility = client.utility.prefetch_by_email(
            email="dev@stainless.com",
            timeout_ms=1000,
        )
        assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_prefetch_by_email(self, client: ContextDev) -> None:
        response = client.utility.with_raw_response.prefetch_by_email(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        utility = response.parse()
        assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_prefetch_by_email(self, client: ContextDev) -> None:
        with client.utility.with_streaming_response.prefetch_by_email(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            utility = response.parse()
            assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUtility:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_prefetch(self, async_client: AsyncContextDev) -> None:
        utility = await async_client.utility.prefetch(
            domain="domain",
        )
        assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_prefetch_with_all_params(self, async_client: AsyncContextDev) -> None:
        utility = await async_client.utility.prefetch(
            domain="domain",
            timeout_ms=1000,
        )
        assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_prefetch(self, async_client: AsyncContextDev) -> None:
        response = await async_client.utility.with_raw_response.prefetch(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        utility = await response.parse()
        assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_prefetch(self, async_client: AsyncContextDev) -> None:
        async with async_client.utility.with_streaming_response.prefetch(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            utility = await response.parse()
            assert_matches_type(UtilityPrefetchResponse, utility, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_prefetch_by_email(self, async_client: AsyncContextDev) -> None:
        utility = await async_client.utility.prefetch_by_email(
            email="dev@stainless.com",
        )
        assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_prefetch_by_email_with_all_params(self, async_client: AsyncContextDev) -> None:
        utility = await async_client.utility.prefetch_by_email(
            email="dev@stainless.com",
            timeout_ms=1000,
        )
        assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_prefetch_by_email(self, async_client: AsyncContextDev) -> None:
        response = await async_client.utility.with_raw_response.prefetch_by_email(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        utility = await response.parse()
        assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_prefetch_by_email(self, async_client: AsyncContextDev) -> None:
        async with async_client.utility.with_streaming_response.prefetch_by_email(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            utility = await response.parse()
            assert_matches_type(UtilityPrefetchByEmailResponse, utility, path=["response"])

        assert cast(Any, response.is_closed) is True
