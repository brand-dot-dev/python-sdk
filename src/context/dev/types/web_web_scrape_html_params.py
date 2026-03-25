# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WebWebScrapeHTMLParams"]


class WebWebScrapeHTMLParams(TypedDict, total=False):
    url: Required[str]
    """Full URL to scrape (must include http:// or https:// protocol)"""
