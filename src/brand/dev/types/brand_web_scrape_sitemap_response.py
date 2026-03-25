# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BrandWebScrapeSitemapResponse", "Meta"]


class Meta(BaseModel):
    """Metadata about the sitemap crawl operation"""

    errors: int
    """Number of errors encountered during crawling"""

    sitemaps_discovered: int = FieldInfo(alias="sitemapsDiscovered")
    """Total number of sitemap files discovered"""

    sitemaps_fetched: int = FieldInfo(alias="sitemapsFetched")
    """Number of sitemap files successfully fetched and parsed"""

    sitemaps_skipped: int = FieldInfo(alias="sitemapsSkipped")
    """Number of sitemap files skipped (due to errors, timeouts, or limits)"""


class BrandWebScrapeSitemapResponse(BaseModel):
    domain: str
    """The normalized domain that was crawled"""

    meta: Meta
    """Metadata about the sitemap crawl operation"""

    success: Literal[True]
    """Indicates success"""

    urls: List[str]
    """Array of discovered page URLs from the sitemap (max 500)"""
