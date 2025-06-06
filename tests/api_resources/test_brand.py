# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from brand.dev import BrandDev, AsyncBrandDev
from tests.utils import assert_matches_type
from brand.dev.types import (
    BrandSearchResponse,
    BrandAIQueryResponse,
    BrandPrefetchResponse,
    BrandRetrieveResponse,
    BrandRetrieveNaicsResponse,
    BrandRetrieveByTickerResponse,
    BrandIdentifyFromTransactionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: BrandDev) -> None:
        brand = client.brand.retrieve(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: BrandDev) -> None:
        brand = client.brand.retrieve(
            domain="domain",
            force_language="albanian",
            max_speed=True,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_ai_query(self, client: BrandDev) -> None:
        brand = client.brand.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
        )
        assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ai_query_with_all_params(self, client: BrandDev) -> None:
        brand = client.brand.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
            specific_pages={
                "about_us": True,
                "blog": True,
                "careers": True,
                "contact_us": True,
                "faq": True,
                "home_page": True,
                "privacy_policy": True,
                "terms_and_conditions": True,
            },
        )
        assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ai_query(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ai_query(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_identify_from_transaction(self, client: BrandDev) -> None:
        brand = client.brand.identify_from_transaction(
            transaction_info="transaction_info",
        )
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_identify_from_transaction(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.identify_from_transaction(
            transaction_info="transaction_info",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_identify_from_transaction(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.identify_from_transaction(
            transaction_info="transaction_info",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_prefetch(self, client: BrandDev) -> None:
        brand = client.brand.prefetch(
            domain="domain",
        )
        assert_matches_type(BrandPrefetchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_prefetch(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.prefetch(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandPrefetchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_prefetch(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.prefetch(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandPrefetchResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_by_ticker(self, client: BrandDev) -> None:
        brand = client.brand.retrieve_by_ticker(
            ticker="ticker",
        )
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_by_ticker(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.retrieve_by_ticker(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_by_ticker(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.retrieve_by_ticker(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_naics(self, client: BrandDev) -> None:
        brand = client.brand.retrieve_naics(
            input="input",
        )
        assert_matches_type(BrandRetrieveNaicsResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_naics(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.retrieve_naics(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveNaicsResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_naics(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.retrieve_naics(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveNaicsResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: BrandDev) -> None:
        brand = client.brand.search(
            query="query",
        )
        assert_matches_type(BrandSearchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: BrandDev) -> None:
        response = client.brand.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandSearchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: BrandDev) -> None:
        with client.brand.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandSearchResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBrand:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.retrieve(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.retrieve(
            domain="domain",
            force_language="albanian",
            max_speed=True,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_ai_query(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
        )
        assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ai_query_with_all_params(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
            specific_pages={
                "about_us": True,
                "blog": True,
                "careers": True,
                "contact_us": True,
                "faq": True,
                "home_page": True,
                "privacy_policy": True,
                "terms_and_conditions": True,
            },
        )
        assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ai_query(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ai_query(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                }
            ],
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandAIQueryResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_identify_from_transaction(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.identify_from_transaction(
            transaction_info="transaction_info",
        )
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_identify_from_transaction(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.identify_from_transaction(
            transaction_info="transaction_info",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_identify_from_transaction(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.identify_from_transaction(
            transaction_info="transaction_info",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandIdentifyFromTransactionResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_prefetch(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.prefetch(
            domain="domain",
        )
        assert_matches_type(BrandPrefetchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_prefetch(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.prefetch(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandPrefetchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_prefetch(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.prefetch(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandPrefetchResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_by_ticker(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.retrieve_by_ticker(
            ticker="ticker",
        )
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_by_ticker(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_by_ticker(
            ticker="ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_by_ticker(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_by_ticker(
            ticker="ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveByTickerResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_naics(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.retrieve_naics(
            input="input",
        )
        assert_matches_type(BrandRetrieveNaicsResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_naics(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_naics(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveNaicsResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_naics(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_naics(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveNaicsResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncBrandDev) -> None:
        brand = await async_client.brand.search(
            query="query",
        )
        assert_matches_type(BrandSearchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncBrandDev) -> None:
        response = await async_client.brand.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandSearchResponse, brand, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncBrandDev) -> None:
        async with async_client.brand.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandSearchResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True
