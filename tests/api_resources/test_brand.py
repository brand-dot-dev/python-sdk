# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    BrandRetrieveResponse,
    BrandRetrieveByIsinResponse,
    BrandRetrieveByNameResponse,
    BrandRetrieveByEmailResponse,
    BrandRetrieveByTickerResponse,
    BrandRetrieveSimplifiedResponse,
    BrandIdentifyFromTransactionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            domain="domain",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_identify_from_transaction(self, client: ContextDev) -> None:
        brand = client.brand.identify_from_transaction(
            transaction_info="transaction_info",
        )
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_identify_from_transaction_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.identify_from_transaction(
            transaction_info="transaction_info",
            city="city",
            country_gl="ad",
            force_language="albanian",
            high_confidence_only=True,
            max_speed=True,
            mcc="mcc",
            phone=0,
            timeout_ms=1000,
        )
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_identify_from_transaction(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.identify_from_transaction(
            transaction_info="transaction_info",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_identify_from_transaction(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.identify_from_transaction(
            transaction_info="transaction_info",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_email(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_email(
            email="dev@stainless.com",
        )
        assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_email_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_email(
            email="dev@stainless.com",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_email(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve_by_email(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_email(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve_by_email(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_isin(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_isin(
            isin="SE60513A9993",
        )
        assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_isin_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_isin(
            isin="SE60513A9993",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_isin(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve_by_isin(
            isin="SE60513A9993",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_isin(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve_by_isin(
            isin="SE60513A9993",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_name(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_name(
            name="xxx",
        )
        assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_name_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_name(
            name="xxx",
            country_gl="ad",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_name(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve_by_name(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_name(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve_by_name(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_ticker(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_ticker(
            ticker="ticker",
        )
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_by_ticker_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_by_ticker(
            ticker="ticker",
            force_language="albanian",
            max_speed=True,
            ticker_exchange="AMEX",
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_by_ticker(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve_by_ticker(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_by_ticker(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve_by_ticker(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_simplified(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_simplified(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_simplified_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_simplified(
            domain="domain",
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_simplified(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve_simplified(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_simplified(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve_simplified(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBrand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            domain="domain",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_identify_from_transaction(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.identify_from_transaction(
            transaction_info="transaction_info",
        )
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_identify_from_transaction_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.identify_from_transaction(
            transaction_info="transaction_info",
            city="city",
            country_gl="ad",
            force_language="albanian",
            high_confidence_only=True,
            max_speed=True,
            mcc="mcc",
            phone=0,
            timeout_ms=1000,
        )
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_identify_from_transaction(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.identify_from_transaction(
            transaction_info="transaction_info",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_identify_from_transaction(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.identify_from_transaction(
            transaction_info="transaction_info",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_email(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_email(
            email="dev@stainless.com",
        )
        assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_email_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_email(
            email="dev@stainless.com",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_email(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_by_email(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_email(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_by_email(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveByEmailResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_isin(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_isin(
            isin="SE60513A9993",
        )
        assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_isin_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_isin(
            isin="SE60513A9993",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_isin(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_by_isin(
            isin="SE60513A9993",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_isin(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_by_isin(
            isin="SE60513A9993",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveByIsinResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_name(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_name(
            name="xxx",
        )
        assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_name_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_name(
            name="xxx",
            country_gl="ad",
            force_language="albanian",
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_name(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_by_name(
            name="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_name(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_by_name(
            name="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveByNameResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_ticker(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_ticker(
            ticker="ticker",
        )
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_by_ticker_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_by_ticker(
            ticker="ticker",
            force_language="albanian",
            max_speed=True,
            ticker_exchange="AMEX",
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_by_ticker(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_by_ticker(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_by_ticker(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_by_ticker(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_simplified(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_simplified(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_simplified_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_simplified(
            domain="domain",
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_simplified(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_simplified(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_simplified(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_simplified(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True
