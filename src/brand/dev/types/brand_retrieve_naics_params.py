# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BrandRetrieveNaicsParams"]


class BrandRetrieveNaicsParams(TypedDict, total=False):
    input: Required[str]
    """Brand domain or title to retrieve NAICS code for.

    If a valid domain is provided in `input`, it will be used for classification,
    otherwise, we will search for the brand using the provided title.
    """
