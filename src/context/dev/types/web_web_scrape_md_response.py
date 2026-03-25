# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebWebScrapeMdResponse"]


class WebWebScrapeMdResponse(BaseModel):
    markdown: str
    """Page content converted to GitHub Flavored Markdown"""

    success: Literal[True]
    """Indicates success"""

    url: str
    """The URL that was scraped"""
