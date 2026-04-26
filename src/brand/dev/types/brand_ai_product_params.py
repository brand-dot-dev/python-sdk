# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandAIProductParams"]


class BrandAIProductParams(TypedDict, total=False):
    url: Required[str]
    """The product page URL to extract product data from."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    Maximum allowed value is 300000ms (5 minutes).
    """
