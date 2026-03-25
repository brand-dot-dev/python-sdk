# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebWebScrapeSitemapParams"]


class WebWebScrapeSitemapParams(TypedDict, total=False):
    domain: Required[str]
    """Domain name to crawl sitemaps for (e.g., 'example.com').

    The domain will be automatically normalized and validated.
    """
