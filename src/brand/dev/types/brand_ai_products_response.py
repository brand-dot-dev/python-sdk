# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BrandAIProductsResponse", "Product"]


class Product(BaseModel):
    description: str
    """Description of the product"""

    features: List[str]
    """List of product features"""

    images: List[str]
    """URLs to product images on the page (up to 7)"""

    name: str
    """Name of the product"""

    sku: Optional[str] = None
    """Stock Keeping Unit (product identifier).

    Extracted from structured data (JSON-LD Product.sku), microdata, meta tags,
    platform-specific identifiers (e.g. Amazon ASIN, Etsy listing ID), or visible
    SKU/Model/Item # text. Null if no identifier is found.
    """

    tags: List[str]
    """Tags associated with the product"""

    target_audience: List[str]
    """Target audience for the product (array of strings)"""

    billing_frequency: Optional[Literal["monthly", "yearly", "one_time", "usage_based"]] = None
    """Billing frequency for the product"""

    category: Optional[str] = None
    """Category of the product"""

    currency: Optional[str] = None
    """Currency code for the price (e.g., USD, EUR)"""

    image_url: Optional[str] = None
    """URL to the product image"""

    price: Optional[float] = None
    """Price of the product"""

    pricing_model: Optional[Literal["per_seat", "flat", "tiered", "freemium", "custom"]] = None
    """Pricing model for the product"""

    url: Optional[str] = None
    """URL to the product page"""


class BrandAIProductsResponse(BaseModel):
    products: Optional[List[Product]] = None
    """Array of products extracted from the website"""
