# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    WebScreenshotResponse,
    WebWebScrapeMdResponse,
    WebWebScrapeHTMLResponse,
    WebWebScrapeImagesResponse,
    WebWebScrapeSitemapResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_screenshot(self, client: ContextDev) -> None:
        web = client.web.screenshot(
            domain="domain",
        )
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_screenshot_with_all_params(self, client: ContextDev) -> None:
        web = client.web.screenshot(
            domain="domain",
            full_screenshot="true",
            page="login",
            prioritize="speed",
        )
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_screenshot(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.screenshot(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_screenshot(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.screenshot(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebScreenshotResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_html(self, client: ContextDev) -> None:
        web = client.web.web_scrape_html(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_html(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_html(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_html(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_html(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_images(self, client: ContextDev) -> None:
        web = client.web.web_scrape_images(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_images(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_images(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_images(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_images(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_md(self, client: ContextDev) -> None:
        web = client.web.web_scrape_md(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_md_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_md(
            url="https://example.com",
            include_images=True,
            include_links=True,
            shorten_base64_images=True,
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_md(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_md(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_md(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_md(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_sitemap(self, client: ContextDev) -> None:
        web = client.web.web_scrape_sitemap(
            domain="domain",
        )
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_sitemap(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_sitemap(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_sitemap(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_sitemap(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWeb:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_screenshot(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.screenshot(
            domain="domain",
        )
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_screenshot_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.screenshot(
            domain="domain",
            full_screenshot="true",
            page="login",
            prioritize="speed",
        )
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_screenshot(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.screenshot(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_screenshot(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.screenshot(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebScreenshotResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_html(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_html(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_html(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_html(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_html(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_html(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_images(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_images(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_images(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_images(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_images(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_images(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_md(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_md(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_md_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_md(
            url="https://example.com",
            include_images=True,
            include_links=True,
            shorten_base64_images=True,
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_md(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_md(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_md(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_md(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_sitemap(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_sitemap(
            domain="domain",
        )
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_sitemap(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_sitemap(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_sitemap(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_sitemap(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True
