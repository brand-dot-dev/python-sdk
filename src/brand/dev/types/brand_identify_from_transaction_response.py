# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "BrandIdentifyFromTransactionResponse",
    "Brand",
    "BrandAddress",
    "BrandBackdrop",
    "BrandBackdropColor",
    "BrandBackdropResolution",
    "BrandColor",
    "BrandLogo",
    "BrandLogoColor",
    "BrandLogoResolution",
    "BrandSocial",
    "BrandStock",
]


class BrandAddress(BaseModel):
    city: Optional[str] = None
    """City name"""

    country: Optional[str] = None
    """Country name"""

    country_code: Optional[str] = None
    """Country code"""

    postal_code: Optional[str] = None
    """Postal or ZIP code"""

    state_code: Optional[str] = None
    """State or province code"""

    state_province: Optional[str] = None
    """State or province name"""

    street: Optional[str] = None
    """Street address"""


class BrandBackdropColor(BaseModel):
    hex: Optional[str] = None
    """Color in hexadecimal format"""

    name: Optional[str] = None
    """Name of the color"""


class BrandBackdropResolution(BaseModel):
    height: Optional[int] = None
    """Height of the image in pixels"""

    width: Optional[int] = None
    """Width of the image in pixels"""


class BrandBackdrop(BaseModel):
    colors: Optional[List[BrandBackdropColor]] = None
    """Array of colors in the backdrop image"""

    resolution: Optional[BrandBackdropResolution] = None
    """Resolution of the backdrop image"""

    url: Optional[str] = None
    """URL of the backdrop image"""


class BrandColor(BaseModel):
    hex: Optional[str] = None
    """Color in hexadecimal format"""

    name: Optional[str] = None
    """Name of the color"""


class BrandLogoColor(BaseModel):
    hex: Optional[str] = None
    """Color in hexadecimal format"""

    name: Optional[str] = None
    """Name of the color"""


class BrandLogoResolution(BaseModel):
    height: Optional[int] = None
    """Height of the image in pixels"""

    width: Optional[int] = None
    """Width of the image in pixels"""


class BrandLogo(BaseModel):
    colors: Optional[List[BrandLogoColor]] = None
    """Array of colors in the logo"""

    group: Optional[int] = None
    """Group identifier for logos"""

    mode: Optional[str] = None
    """Mode of the logo, e.g., 'dark', 'light'"""

    resolution: Optional[BrandLogoResolution] = None
    """Resolution of the logo image"""

    url: Optional[str] = None
    """URL of the logo image"""


class BrandSocial(BaseModel):
    type: Optional[str] = None
    """Type of social media, e.g., 'facebook', 'twitter'"""

    url: Optional[str] = None
    """URL of the social media page"""


class BrandStock(BaseModel):
    exchange: Optional[str] = None
    """Stock exchange name"""

    ticker: Optional[str] = None
    """Stock ticker symbol"""


class Brand(BaseModel):
    address: Optional[BrandAddress] = None
    """Physical address of the brand"""

    backdrops: Optional[List[BrandBackdrop]] = None
    """An array of backdrop images for the brand"""

    colors: Optional[List[BrandColor]] = None
    """An array of brand colors"""

    description: Optional[str] = None
    """A brief description of the brand"""

    domain: Optional[str] = None
    """The domain name of the brand"""

    logos: Optional[List[BrandLogo]] = None
    """An array of logos associated with the brand"""

    slogan: Optional[str] = None
    """The brand's slogan"""

    socials: Optional[List[BrandSocial]] = None
    """An array of social media links for the brand"""

    stock: Optional[BrandStock] = None
    """
    Stock market information for this brand (will be null if not a publicly traded
    company)
    """

    title: Optional[str] = None
    """The title or name of the brand"""


class BrandIdentifyFromTransactionResponse(BaseModel):
    brand: Optional[Brand] = None
    """Detailed brand information"""

    code: Optional[int] = None
    """HTTP status code"""

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""
