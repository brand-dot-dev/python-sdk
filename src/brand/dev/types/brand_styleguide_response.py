# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "BrandStyleguideResponse",
    "Styleguide",
    "StyleguideColors",
    "StyleguideComponents",
    "StyleguideComponentsButton",
    "StyleguideComponentsButtonLink",
    "StyleguideComponentsButtonPrimary",
    "StyleguideComponentsButtonSecondary",
    "StyleguideComponentsCard",
    "StyleguideElementSpacing",
    "StyleguideShadows",
    "StyleguideTypography",
    "StyleguideTypographyHeadings",
    "StyleguideTypographyHeadingsH1",
    "StyleguideTypographyHeadingsH2",
    "StyleguideTypographyHeadingsH3",
    "StyleguideTypographyHeadingsH4",
    "StyleguideTypographyP",
]


class StyleguideColors(BaseModel):
    """Primary colors used on the website"""

    accent: str
    """Accent color (hex format)"""

    background: str
    """Background color (hex format)"""

    text: str
    """Text color (hex format)"""


class StyleguideComponentsButtonLink(BaseModel):
    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """
    Border color as CSS hex (#RRGGBB or #RRGGBBAA when computed border-color has
    alpha)
    """

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")
    """Computed box-shadow (comma-separated layers when present)"""

    color: str

    css: str
    """Ready-to-use CSS declaration block for this component style"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    min_height: str = FieldInfo(alias="minHeight")
    """Sampled minimum height of the button box (typically px)"""

    min_width: str = FieldInfo(alias="minWidth")
    """Sampled minimum width of the button box (typically px)"""

    padding: str

    text_decoration: str = FieldInfo(alias="textDecoration")

    font_fallbacks: Optional[List[str]] = FieldInfo(alias="fontFallbacks", default=None)
    """Full ordered font list from computed font-family"""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Primary button typeface (first in fontFallbacks)"""

    text_decoration_color: Optional[str] = FieldInfo(alias="textDecorationColor", default=None)
    """Hex color of the underline when it differs from the text color"""


class StyleguideComponentsButtonPrimary(BaseModel):
    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """
    Border color as CSS hex (#RRGGBB or #RRGGBBAA when computed border-color has
    alpha)
    """

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")
    """Computed box-shadow (comma-separated layers when present)"""

    color: str

    css: str
    """Ready-to-use CSS declaration block for this component style"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    min_height: str = FieldInfo(alias="minHeight")
    """Sampled minimum height of the button box (typically px)"""

    min_width: str = FieldInfo(alias="minWidth")
    """Sampled minimum width of the button box (typically px)"""

    padding: str

    text_decoration: str = FieldInfo(alias="textDecoration")

    font_fallbacks: Optional[List[str]] = FieldInfo(alias="fontFallbacks", default=None)
    """Full ordered font list from computed font-family"""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Primary button typeface (first in fontFallbacks)"""

    text_decoration_color: Optional[str] = FieldInfo(alias="textDecorationColor", default=None)
    """Hex color of the underline when it differs from the text color"""


class StyleguideComponentsButtonSecondary(BaseModel):
    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """
    Border color as CSS hex (#RRGGBB or #RRGGBBAA when computed border-color has
    alpha)
    """

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")
    """Computed box-shadow (comma-separated layers when present)"""

    color: str

    css: str
    """Ready-to-use CSS declaration block for this component style"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    min_height: str = FieldInfo(alias="minHeight")
    """Sampled minimum height of the button box (typically px)"""

    min_width: str = FieldInfo(alias="minWidth")
    """Sampled minimum width of the button box (typically px)"""

    padding: str

    text_decoration: str = FieldInfo(alias="textDecoration")

    font_fallbacks: Optional[List[str]] = FieldInfo(alias="fontFallbacks", default=None)
    """Full ordered font list from computed font-family"""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Primary button typeface (first in fontFallbacks)"""

    text_decoration_color: Optional[str] = FieldInfo(alias="textDecorationColor", default=None)
    """Hex color of the underline when it differs from the text color"""


class StyleguideComponentsButton(BaseModel):
    """Button component styles"""

    link: Optional[StyleguideComponentsButtonLink] = None

    primary: Optional[StyleguideComponentsButtonPrimary] = None

    secondary: Optional[StyleguideComponentsButtonSecondary] = None


class StyleguideComponentsCard(BaseModel):
    """Card component style"""

    background_color: str = FieldInfo(alias="backgroundColor")

    border_color: str = FieldInfo(alias="borderColor")
    """
    Border color as CSS hex (#RRGGBB or #RRGGBBAA when computed border-color has
    alpha)
    """

    border_radius: str = FieldInfo(alias="borderRadius")

    border_style: str = FieldInfo(alias="borderStyle")

    border_width: str = FieldInfo(alias="borderWidth")

    box_shadow: str = FieldInfo(alias="boxShadow")

    css: str
    """Ready-to-use CSS declaration block for this component style"""

    padding: str

    text_color: str = FieldInfo(alias="textColor")


class StyleguideComponents(BaseModel):
    """UI component styles"""

    button: StyleguideComponentsButton
    """Button component styles"""

    card: Optional[StyleguideComponentsCard] = None
    """Card component style"""


class StyleguideElementSpacing(BaseModel):
    """Spacing system used on the website"""

    lg: str

    md: str

    sm: str

    xl: str

    xs: str


class StyleguideShadows(BaseModel):
    """Shadow styles used on the website"""

    inner: str

    lg: str

    md: str

    sm: str

    xl: str


class StyleguideTypographyHeadingsH1(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full ordered font list from resolved computed font-family"""

    font_family: str = FieldInfo(alias="fontFamily")
    """Primary face (first family in the computed stack)"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadingsH2(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full ordered font list from resolved computed font-family"""

    font_family: str = FieldInfo(alias="fontFamily")
    """Primary face (first family in the computed stack)"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadingsH3(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full ordered font list from resolved computed font-family"""

    font_family: str = FieldInfo(alias="fontFamily")
    """Primary face (first family in the computed stack)"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadingsH4(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full ordered font list from resolved computed font-family"""

    font_family: str = FieldInfo(alias="fontFamily")
    """Primary face (first family in the computed stack)"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypographyHeadings(BaseModel):
    """Heading styles"""

    h1: Optional[StyleguideTypographyHeadingsH1] = None

    h2: Optional[StyleguideTypographyHeadingsH2] = None

    h3: Optional[StyleguideTypographyHeadingsH3] = None

    h4: Optional[StyleguideTypographyHeadingsH4] = None


class StyleguideTypographyP(BaseModel):
    font_fallbacks: List[str] = FieldInfo(alias="fontFallbacks")
    """Full ordered font list from resolved computed font-family"""

    font_family: str = FieldInfo(alias="fontFamily")
    """Primary face (first family in the computed stack)"""

    font_size: str = FieldInfo(alias="fontSize")

    font_weight: float = FieldInfo(alias="fontWeight")

    letter_spacing: str = FieldInfo(alias="letterSpacing")

    line_height: str = FieldInfo(alias="lineHeight")


class StyleguideTypography(BaseModel):
    """Typography styles used on the website"""

    headings: StyleguideTypographyHeadings
    """Heading styles"""

    p: Optional[StyleguideTypographyP] = None


class Styleguide(BaseModel):
    """Comprehensive styleguide data extracted from the website"""

    colors: StyleguideColors
    """Primary colors used on the website"""

    components: StyleguideComponents
    """UI component styles"""

    element_spacing: StyleguideElementSpacing = FieldInfo(alias="elementSpacing")
    """Spacing system used on the website"""

    mode: Literal["light", "dark"]
    """The primary color mode of the website design"""

    shadows: StyleguideShadows
    """Shadow styles used on the website"""

    typography: StyleguideTypography
    """Typography styles used on the website"""


class BrandStyleguideResponse(BaseModel):
    code: Optional[int] = None
    """HTTP status code"""

    domain: Optional[str] = None
    """The normalized domain that was processed"""

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    styleguide: Optional[Styleguide] = None
    """Comprehensive styleguide data extracted from the website"""
