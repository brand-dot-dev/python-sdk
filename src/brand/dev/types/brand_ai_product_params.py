# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandAIProductParams"]


class BrandAIProductParams(TypedDict, total=False):
    url: Required[str]
    """The product page URL to extract product data from."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    Maximum allowed value is 300000ms (5 minutes).
    """
