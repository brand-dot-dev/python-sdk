# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandWebScrapeSitemapParams"]


class BrandWebScrapeSitemapParams(TypedDict, total=False):
    domain: Required[str]
    """Domain name to crawl sitemaps for (e.g., 'example.com').

    The domain will be automatically normalized and validated.
    """

    max_links: Annotated[int, PropertyInfo(alias="maxLinks")]
    """Maximum number of links to return from the sitemap crawl.

    Defaults to 10,000. Minimum is 1, maximum is 100,000.
    """
