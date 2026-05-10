# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandWebScrapeMdParams", "Pdf"]


class BrandWebScrapeMdParams(TypedDict, total=False):
    url: Required[str]
    """
    Full URL to scrape into LLM usable Markdown (must include http:// or https://
    protocol)
    """

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """When true, the contents of iframes are rendered to Markdown."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: Pdf
    """PDF parsing controls.

    Use start/end to limit text extraction and OCR to an inclusive 1-based page
    range.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content of the page, excluding headers, footers, sidebars,
    and navigation
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before
    converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).
    """


class Pdf(TypedDict, total=False):
    """PDF parsing controls.

    Use start/end to limit text extraction and OCR to an inclusive 1-based page range.
    """

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 WEBSITE_ACCESS_ERROR is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
