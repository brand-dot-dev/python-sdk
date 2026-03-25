# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebWebScrapeHTMLResponse"]


class WebWebScrapeHTMLResponse(BaseModel):
    html: str
    """Raw HTML content of the page"""

    success: Literal[True]
    """Indicates success"""

    url: str
    """The URL that was scraped"""
