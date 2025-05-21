# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrandRetrieveByTickerParams"]


class BrandRetrieveByTickerParams(TypedDict, total=False):
    ticker: Required[str]
    """Stock ticker symbol to retrieve brand data for (e.g. AAPL, TSLA, etc.)"""
