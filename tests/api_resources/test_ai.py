# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    AIAIQueryResponse,
    AIExtractProductResponse,
    AIExtractProductsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAI:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ai_query(self, client: ContextDev) -> None:
        ai = client.ai.ai_query(
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
        assert_matches_type(AIAIQueryResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ai_query_with_all_params(self, client: ContextDev) -> None:
        ai = client.ai.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                    "datapoint_list_type": "string",
                    "datapoint_object_schema": {
                        "testimonial_text": "string",
                        "testimonial_author": "string",
                    },
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
                "pricing": True,
                "privacy_policy": True,
                "terms_and_conditions": True,
            },
            timeout_ms=1000,
        )
        assert_matches_type(AIAIQueryResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ai_query(self, client: ContextDev) -> None:
        response = client.ai.with_raw_response.ai_query(
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
        ai = response.parse()
        assert_matches_type(AIAIQueryResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ai_query(self, client: ContextDev) -> None:
        with client.ai.with_streaming_response.ai_query(
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

            ai = response.parse()
            assert_matches_type(AIAIQueryResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_product(self, client: ContextDev) -> None:
        ai = client.ai.extract_product(
            url="https://example.com",
        )
        assert_matches_type(AIExtractProductResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_product_with_all_params(self, client: ContextDev) -> None:
        ai = client.ai.extract_product(
            url="https://example.com",
            timeout_ms=1000,
        )
        assert_matches_type(AIExtractProductResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_product(self, client: ContextDev) -> None:
        response = client.ai.with_raw_response.extract_product(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(AIExtractProductResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_product(self, client: ContextDev) -> None:
        with client.ai.with_streaming_response.extract_product(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(AIExtractProductResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_products_overload_1(self, client: ContextDev) -> None:
        ai = client.ai.extract_products(
            domain="domain",
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_products_with_all_params_overload_1(self, client: ContextDev) -> None:
        ai = client.ai.extract_products(
            domain="domain",
            max_products=1,
            timeout_ms=1000,
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_products_overload_1(self, client: ContextDev) -> None:
        response = client.ai.with_raw_response.extract_products(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_products_overload_1(self, client: ContextDev) -> None:
        with client.ai.with_streaming_response.extract_products(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_products_overload_2(self, client: ContextDev) -> None:
        ai = client.ai.extract_products(
            direct_url="https://example.com",
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_products_with_all_params_overload_2(self, client: ContextDev) -> None:
        ai = client.ai.extract_products(
            direct_url="https://example.com",
            max_products=1,
            timeout_ms=1000,
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_products_overload_2(self, client: ContextDev) -> None:
        response = client.ai.with_raw_response.extract_products(
            direct_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = response.parse()
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_products_overload_2(self, client: ContextDev) -> None:
        with client.ai.with_streaming_response.extract_products(
            direct_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = response.parse()
            assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAI:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ai_query(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.ai_query(
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
        assert_matches_type(AIAIQueryResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ai_query_with_all_params(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.ai_query(
            data_to_extract=[
                {
                    "datapoint_description": "datapoint_description",
                    "datapoint_example": "datapoint_example",
                    "datapoint_name": "datapoint_name",
                    "datapoint_type": "text",
                    "datapoint_list_type": "string",
                    "datapoint_object_schema": {
                        "testimonial_text": "string",
                        "testimonial_author": "string",
                    },
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
                "pricing": True,
                "privacy_policy": True,
                "terms_and_conditions": True,
            },
            timeout_ms=1000,
        )
        assert_matches_type(AIAIQueryResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ai_query(self, async_client: AsyncContextDev) -> None:
        response = await async_client.ai.with_raw_response.ai_query(
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
        ai = await response.parse()
        assert_matches_type(AIAIQueryResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ai_query(self, async_client: AsyncContextDev) -> None:
        async with async_client.ai.with_streaming_response.ai_query(
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

            ai = await response.parse()
            assert_matches_type(AIAIQueryResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_product(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.extract_product(
            url="https://example.com",
        )
        assert_matches_type(AIExtractProductResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_product_with_all_params(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.extract_product(
            url="https://example.com",
            timeout_ms=1000,
        )
        assert_matches_type(AIExtractProductResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_product(self, async_client: AsyncContextDev) -> None:
        response = await async_client.ai.with_raw_response.extract_product(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(AIExtractProductResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_product(self, async_client: AsyncContextDev) -> None:
        async with async_client.ai.with_streaming_response.extract_product(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(AIExtractProductResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_products_overload_1(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.extract_products(
            domain="domain",
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_products_with_all_params_overload_1(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.extract_products(
            domain="domain",
            max_products=1,
            timeout_ms=1000,
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_products_overload_1(self, async_client: AsyncContextDev) -> None:
        response = await async_client.ai.with_raw_response.extract_products(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_products_overload_1(self, async_client: AsyncContextDev) -> None:
        async with async_client.ai.with_streaming_response.extract_products(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_products_overload_2(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.extract_products(
            direct_url="https://example.com",
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_products_with_all_params_overload_2(self, async_client: AsyncContextDev) -> None:
        ai = await async_client.ai.extract_products(
            direct_url="https://example.com",
            max_products=1,
            timeout_ms=1000,
        )
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_products_overload_2(self, async_client: AsyncContextDev) -> None:
        response = await async_client.ai.with_raw_response.extract_products(
            direct_url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ai = await response.parse()
        assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_products_overload_2(self, async_client: AsyncContextDev) -> None:
        async with async_client.ai.with_streaming_response.extract_products(
            direct_url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ai = await response.parse()
            assert_matches_type(AIExtractProductsResponse, ai, path=["response"])

        assert cast(Any, response.is_closed) is True
