# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BrandAIQueryParams", "DataToExtract"]


class BrandAIQueryParams(TypedDict, total=False):
    data_to_extract: Required[Iterable[DataToExtract]]
    """Array of data points to extract from the website"""

    domain: Required[str]
    """The domain name to analyze"""

    specific_pages: List[str]
    """Optional array of specific pages to analyze"""


class DataToExtract(TypedDict, total=False):
    datapoint_description: Required[str]
    """Description of what to extract"""

    datapoint_example: Required[str]
    """Example of the expected value"""

    datapoint_name: Required[str]
    """Name of the data point to extract"""

    datapoint_type: Required[Literal["text", "number", "date", "boolean", "list", "url"]]
    """Type of the data point"""
