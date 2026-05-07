# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandWebScrapeSitemapParams"]


class BrandWebScrapeSitemapParams(TypedDict, total=False):
    domain: Required[str]
    """Domain to build a sitemap for"""

    max_links: Annotated[int, PropertyInfo(alias="maxLinks")]
    """Maximum number of links to return from the sitemap crawl.

    Defaults to 10,000. Minimum is 1, maximum is 100,000.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Optional RE2-compatible regex pattern.

    Only URLs matching this pattern are returned and counted against maxLinks.
    """
