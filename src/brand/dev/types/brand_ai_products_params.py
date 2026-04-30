# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandAIProductsParams", "ByDomain", "ByDirectURL"]


class ByDomain(TypedDict, total=False):
    domain: Required[str]
    """The domain name to analyze."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    max_products: Annotated[int, PropertyInfo(alias="maxProducts")]
    """Maximum number of products to extract."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    Maximum allowed value is 300000ms (5 minutes).
    """


class ByDirectURL(TypedDict, total=False):
    direct_url: Required[Annotated[str, PropertyInfo(alias="directUrl")]]
    """
    A specific URL to use directly as the starting point for extraction without
    domain resolution.
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    max_products: Annotated[int, PropertyInfo(alias="maxProducts")]
    """Maximum number of products to extract."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    Maximum allowed value is 300000ms (5 minutes).
    """


BrandAIProductsParams: TypeAlias = Union[ByDomain, ByDirectURL]
