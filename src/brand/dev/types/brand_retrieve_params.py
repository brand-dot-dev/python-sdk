# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandRetrieveParams"]


class BrandRetrieveParams(TypedDict, total=False):
    domain: Required[str]
    """Domain name to retrieve brand data for (e.g., 'example.com', 'google.com').

    Cannot be used with name or ticker parameters.
    """

    force_language: Literal[
        "afrikaans",
        "albanian",
        "amharic",
        "arabic",
        "armenian",
        "assamese",
        "aymara",
        "azeri",
        "basque",
        "belarusian",
        "bengali",
        "bosnian",
        "bulgarian",
        "burmese",
        "cantonese",
        "catalan",
        "cebuano",
        "chinese",
        "corsican",
        "croatian",
        "czech",
        "danish",
        "dutch",
        "english",
        "esperanto",
        "estonian",
        "farsi",
        "fijian",
        "finnish",
        "french",
        "galician",
        "georgian",
        "german",
        "greek",
        "guarani",
        "gujarati",
        "haitian-creole",
        "hausa",
        "hawaiian",
        "hebrew",
        "hindi",
        "hmong",
        "hungarian",
        "icelandic",
        "igbo",
        "indonesian",
        "irish",
        "italian",
        "japanese",
        "javanese",
        "kannada",
        "kazakh",
        "khmer",
        "kinyarwanda",
        "korean",
        "kurdish",
        "kyrgyz",
        "lao",
        "latin",
        "latvian",
        "lingala",
        "lithuanian",
        "luxembourgish",
        "macedonian",
        "malagasy",
        "malay",
        "malayalam",
        "maltese",
        "maori",
        "marathi",
        "mongolian",
        "nepali",
        "norwegian",
        "odia",
        "oromo",
        "pashto",
        "pidgin",
        "polish",
        "portuguese",
        "punjabi",
        "quechua",
        "romanian",
        "russian",
        "samoan",
        "scottish-gaelic",
        "serbian",
        "sesotho",
        "shona",
        "sindhi",
        "sinhala",
        "slovak",
        "slovene",
        "somali",
        "spanish",
        "sundanese",
        "swahili",
        "swedish",
        "tagalog",
        "tajik",
        "tamil",
        "tatar",
        "telugu",
        "thai",
        "tibetan",
        "tigrinya",
        "tongan",
        "tswana",
        "turkish",
        "turkmen",
        "ukrainian",
        "urdu",
        "uyghur",
        "uzbek",
        "vietnamese",
        "welsh",
        "wolof",
        "xhosa",
        "yiddish",
        "yoruba",
        "zulu",
    ]
    """Optional parameter to force the language of the retrieved brand data."""

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Optional parameter to optimize the API call for maximum speed.

    When set to true, the API will skip time-consuming operations for faster
    response at the cost of less comprehensive data. Works with all three lookup
    methods.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
