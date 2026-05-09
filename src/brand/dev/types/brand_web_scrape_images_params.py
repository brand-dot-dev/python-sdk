# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandWebScrapeImagesParams", "Enrichment"]


class BrandWebScrapeImagesParams(TypedDict, total=False):
    url: Required[str]
    """Page URL to inspect. Must include http:// or https://."""

    enrichment: Enrichment
    """
    Optional per-image processing, sent as deep-object query params such as
    enrichment[resolution]=true.
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Reuse a cached result this many milliseconds old or newer.

    Default: 86400000 (1 day). Set to 0 to bypass cache. Maximum: 2592000000 (30
    days).
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before
    collecting images. Min: 0. Max: 30000 (30 seconds).
    """


class Enrichment(TypedDict, total=False):
    """
    Optional per-image processing, sent as deep-object query params such as enrichment[resolution]=true.
    """

    classification: bool
    """Classify each image by visual asset type."""

    hosted_url: Annotated[bool, PropertyInfo(alias="hostedUrl")]
    """
    Host materializable images on the Brand.dev CDN and return their URL and MIME
    type.
    """

    max_time_per_ms: Annotated[int, PropertyInfo(alias="maxTimePerMs")]
    """Per-image enrichment timeout in milliseconds. Default: 30000. Maximum: 60000."""

    resolution: bool
    """Measure image width and height when possible."""
