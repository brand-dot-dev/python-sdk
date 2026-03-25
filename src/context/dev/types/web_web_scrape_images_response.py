# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebWebScrapeImagesResponse", "Image"]


class Image(BaseModel):
    alt: Optional[str] = None
    """Alt text of the image, or null if not present"""

    element: Literal["img", "svg", "link", "source", "video"]
    """The HTML element the image was found in"""

    src: str
    """The image source - can be a URL, inline HTML (for SVGs), or a base64 data URI"""

    type: Literal["url", "html", "base64"]
    """The type/format of the src value"""


class WebWebScrapeImagesResponse(BaseModel):
    images: List[Image]
    """Array of scraped images"""

    success: Literal[True]
    """Indicates success"""

    url: str
    """The URL that was scraped"""
