# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandAIProductsParams", "ByDomain", "ByDirectURL"]


class ByDomain(TypedDict, total=False):
    domain: Required[str]
    """The domain name to analyze."""

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

    max_products: Annotated[int, PropertyInfo(alias="maxProducts")]
    """Maximum number of products to extract."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    Maximum allowed value is 300000ms (5 minutes).
    """


BrandAIProductsParams: TypeAlias = Union[ByDomain, ByDirectURL]
