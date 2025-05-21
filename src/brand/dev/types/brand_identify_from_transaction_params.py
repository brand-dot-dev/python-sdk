# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrandIdentifyFromTransactionParams"]


class BrandIdentifyFromTransactionParams(TypedDict, total=False):
    transaction_info: Required[str]
    """Transaction information to identify the brand"""
