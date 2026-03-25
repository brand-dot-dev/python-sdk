# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebWebScrapeMdParams"]


class WebWebScrapeMdParams(TypedDict, total=False):
    url: Required[str]
    """
    Full URL to scrape and convert to markdown (must include http:// or https://
    protocol)
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""
