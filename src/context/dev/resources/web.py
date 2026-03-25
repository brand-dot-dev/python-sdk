# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    web_screenshot_params,
    web_web_scrape_md_params,
    web_web_scrape_html_params,
    web_web_scrape_images_params,
    web_web_scrape_sitemap_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.web_screenshot_response import WebScreenshotResponse
from ..types.web_web_scrape_md_response import WebWebScrapeMdResponse
from ..types.web_web_scrape_html_response import WebWebScrapeHTMLResponse
from ..types.web_web_scrape_images_response import WebWebScrapeImagesResponse
from ..types.web_web_scrape_sitemap_response import WebWebScrapeSitemapResponse

__all__ = ["WebResource", "AsyncWebResource"]


class WebResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return WebResourceWithStreamingResponse(self)

    def screenshot(
        self,
        *,
        domain: str,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """Capture a screenshot of a website.

        Supports both viewport (standard browser
        view) and full-page screenshots. Can also screenshot specific page types (login,
        pricing, etc.) by using heuristics to find the appropriate URL. Returns a URL to
        the uploaded screenshot image hosted on our CDN.

        Args:
          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page.

          prioritize: Optional parameter to prioritize screenshot capture. If 'speed', optimizes for
              faster capture with basic quality. If 'quality', optimizes for higher quality
              with longer wait times. Defaults to 'quality' if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "page": page,
                        "prioritize": prioritize,
                    },
                    web_screenshot_params.WebScreenshotParams,
                ),
            ),
            cast_to=WebScreenshotResponse,
        )

    def web_scrape_html(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeHTMLResponse:
        """Scrapes the given URL and returns the raw HTML content of the page.

        Uses
        automatic proxy escalation to handle blocked sites.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, web_web_scrape_html_params.WebWebScrapeHTMLParams),
            ),
            cast_to=WebWebScrapeHTMLResponse,
        )

    def web_scrape_images(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeImagesResponse:
        """Scrapes all images from the given URL.

        Extracts images from img, svg,
        picture/source, link, and video elements including inline SVGs, base64 data
        URIs, and standard URLs.

        Args:
          url: Full URL to scrape images from (must include http:// or https:// protocol)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, web_web_scrape_images_params.WebWebScrapeImagesParams),
            ),
            cast_to=WebWebScrapeImagesResponse,
        )

    def web_scrape_md(
        self,
        *,
        url: str,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """
        Scrapes the given URL, converts the HTML content to GitHub Flavored Markdown
        (GFM), and returns the result. Uses automatic proxy escalation to handle blocked
        sites.

        Args:
          url: Full URL to scrape and convert to markdown (must include http:// or https://
              protocol)

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "include_images": include_images,
                        "include_links": include_links,
                        "shorten_base64_images": shorten_base64_images,
                    },
                    web_web_scrape_md_params.WebWebScrapeMdParams,
                ),
            ),
            cast_to=WebWebScrapeMdResponse,
        )

    def web_scrape_sitemap(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """
        Crawls the sitemap of the given domain and returns all discovered page URLs.
        Supports sitemap index files (recursive), parallel fetching with concurrency
        control, deduplication, and filters out non-page resources (images, PDFs, etc.).

        Args:
          domain: Domain name to crawl sitemaps for (e.g., 'example.com'). The domain will be
              automatically normalized and validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"domain": domain}, web_web_scrape_sitemap_params.WebWebScrapeSitemapParams),
            ),
            cast_to=WebWebScrapeSitemapResponse,
        )


class AsyncWebResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return AsyncWebResourceWithStreamingResponse(self)

    async def screenshot(
        self,
        *,
        domain: str,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """Capture a screenshot of a website.

        Supports both viewport (standard browser
        view) and full-page screenshots. Can also screenshot specific page types (login,
        pricing, etc.) by using heuristics to find the appropriate URL. Returns a URL to
        the uploaded screenshot image hosted on our CDN.

        Args:
          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page.

          prioritize: Optional parameter to prioritize screenshot capture. If 'speed', optimizes for
              faster capture with basic quality. If 'quality', optimizes for higher quality
              with longer wait times. Defaults to 'quality' if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "page": page,
                        "prioritize": prioritize,
                    },
                    web_screenshot_params.WebScreenshotParams,
                ),
            ),
            cast_to=WebScreenshotResponse,
        )

    async def web_scrape_html(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeHTMLResponse:
        """Scrapes the given URL and returns the raw HTML content of the page.

        Uses
        automatic proxy escalation to handle blocked sites.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, web_web_scrape_html_params.WebWebScrapeHTMLParams),
            ),
            cast_to=WebWebScrapeHTMLResponse,
        )

    async def web_scrape_images(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeImagesResponse:
        """Scrapes all images from the given URL.

        Extracts images from img, svg,
        picture/source, link, and video elements including inline SVGs, base64 data
        URIs, and standard URLs.

        Args:
          url: Full URL to scrape images from (must include http:// or https:// protocol)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, web_web_scrape_images_params.WebWebScrapeImagesParams),
            ),
            cast_to=WebWebScrapeImagesResponse,
        )

    async def web_scrape_md(
        self,
        *,
        url: str,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """
        Scrapes the given URL, converts the HTML content to GitHub Flavored Markdown
        (GFM), and returns the result. Uses automatic proxy escalation to handle blocked
        sites.

        Args:
          url: Full URL to scrape and convert to markdown (must include http:// or https://
              protocol)

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "include_images": include_images,
                        "include_links": include_links,
                        "shorten_base64_images": shorten_base64_images,
                    },
                    web_web_scrape_md_params.WebWebScrapeMdParams,
                ),
            ),
            cast_to=WebWebScrapeMdResponse,
        )

    async def web_scrape_sitemap(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """
        Crawls the sitemap of the given domain and returns all discovered page URLs.
        Supports sitemap index files (recursive), parallel fetching with concurrency
        control, deduplication, and filters out non-page resources (images, PDFs, etc.).

        Args:
          domain: Domain name to crawl sitemaps for (e.g., 'example.com'). The domain will be
              automatically normalized and validated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"domain": domain}, web_web_scrape_sitemap_params.WebWebScrapeSitemapParams
                ),
            ),
            cast_to=WebWebScrapeSitemapResponse,
        )


class WebResourceWithRawResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.screenshot = to_raw_response_wrapper(
            web.screenshot,
        )
        self.web_scrape_html = to_raw_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = to_raw_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = to_raw_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = to_raw_response_wrapper(
            web.web_scrape_sitemap,
        )


class AsyncWebResourceWithRawResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.screenshot = async_to_raw_response_wrapper(
            web.screenshot,
        )
        self.web_scrape_html = async_to_raw_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = async_to_raw_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = async_to_raw_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_raw_response_wrapper(
            web.web_scrape_sitemap,
        )


class WebResourceWithStreamingResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.screenshot = to_streamed_response_wrapper(
            web.screenshot,
        )
        self.web_scrape_html = to_streamed_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = to_streamed_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = to_streamed_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = to_streamed_response_wrapper(
            web.web_scrape_sitemap,
        )


class AsyncWebResourceWithStreamingResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.screenshot = async_to_streamed_response_wrapper(
            web.screenshot,
        )
        self.web_scrape_html = async_to_streamed_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = async_to_streamed_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = async_to_streamed_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_streamed_response_wrapper(
            web.web_scrape_sitemap,
        )
