# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["BrandSearchResponse", "BrandSearchResponseItem"]


class BrandSearchResponseItem(BaseModel):
    domain: Optional[str] = None
    """Domain name of the brand"""

    logo: Optional[str] = None
    """URL of the brand's logo"""

    title: Optional[str] = None
    """Title or name of the brand"""


BrandSearchResponse: TypeAlias = List[BrandSearchResponseItem]
