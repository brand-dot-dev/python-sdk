# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    StyleExtractFontsResponse,
    StyleExtractStyleguideResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStyle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_fonts(self, client: ContextDev) -> None:
        style = client.style.extract_fonts(
            domain="domain",
        )
        assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_fonts_with_all_params(self, client: ContextDev) -> None:
        style = client.style.extract_fonts(
            domain="domain",
            timeout_ms=1000,
        )
        assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_fonts(self, client: ContextDev) -> None:
        response = client.style.with_raw_response.extract_fonts(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = response.parse()
        assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_fonts(self, client: ContextDev) -> None:
        with client.style.with_streaming_response.extract_fonts(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = response.parse()
            assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_styleguide(self, client: ContextDev) -> None:
        style = client.style.extract_styleguide()
        assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_styleguide_with_all_params(self, client: ContextDev) -> None:
        style = client.style.extract_styleguide(
            direct_url="https://example.com",
            domain="domain",
            prioritize="speed",
            timeout_ms=1000,
        )
        assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_styleguide(self, client: ContextDev) -> None:
        response = client.style.with_raw_response.extract_styleguide()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = response.parse()
        assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_styleguide(self, client: ContextDev) -> None:
        with client.style.with_streaming_response.extract_styleguide() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = response.parse()
            assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStyle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_fonts(self, async_client: AsyncContextDev) -> None:
        style = await async_client.style.extract_fonts(
            domain="domain",
        )
        assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_fonts_with_all_params(self, async_client: AsyncContextDev) -> None:
        style = await async_client.style.extract_fonts(
            domain="domain",
            timeout_ms=1000,
        )
        assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_fonts(self, async_client: AsyncContextDev) -> None:
        response = await async_client.style.with_raw_response.extract_fonts(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = await response.parse()
        assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_fonts(self, async_client: AsyncContextDev) -> None:
        async with async_client.style.with_streaming_response.extract_fonts(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = await response.parse()
            assert_matches_type(StyleExtractFontsResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_styleguide(self, async_client: AsyncContextDev) -> None:
        style = await async_client.style.extract_styleguide()
        assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_styleguide_with_all_params(self, async_client: AsyncContextDev) -> None:
        style = await async_client.style.extract_styleguide(
            direct_url="https://example.com",
            domain="domain",
            prioritize="speed",
            timeout_ms=1000,
        )
        assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_styleguide(self, async_client: AsyncContextDev) -> None:
        response = await async_client.style.with_raw_response.extract_styleguide()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        style = await response.parse()
        assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_styleguide(self, async_client: AsyncContextDev) -> None:
        async with async_client.style.with_streaming_response.extract_styleguide() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            style = await response.parse()
            assert_matches_type(StyleExtractStyleguideResponse, style, path=["response"])

        assert cast(Any, response.is_closed) is True
