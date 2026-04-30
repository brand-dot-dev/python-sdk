# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandWebScrapeMdParams"]


class BrandWebScrapeMdParams(TypedDict, total=False):
    url: Required[str]
    """
    Full URL to scrape into LLM usable Markdown (must include http:// or https://
    protocol)
    """

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

    parse_pdf: Annotated[bool, PropertyInfo(alias="parsePDF")]
    """
    When true (default), PDF URLs are fetched and their text layer is extracted and
    converted to Markdown. When false, PDF URLs are skipped and a 400
    WEBSITE_ACCESS_ERROR is returned.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content of the page, excluding headers, footers, sidebars,
    and navigation
    """
