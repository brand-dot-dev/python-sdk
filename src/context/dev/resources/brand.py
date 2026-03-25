# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    brand_retrieve_params,
    brand_retrieve_by_isin_params,
    brand_retrieve_by_name_params,
    brand_retrieve_by_email_params,
    brand_retrieve_by_ticker_params,
    brand_retrieve_simplified_params,
    brand_identify_from_transaction_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.brand_retrieve_response import BrandRetrieveResponse
from ..types.brand_retrieve_by_isin_response import BrandRetrieveByIsinResponse
from ..types.brand_retrieve_by_name_response import BrandRetrieveByNameResponse
from ..types.brand_retrieve_by_email_response import BrandRetrieveByEmailResponse
from ..types.brand_retrieve_by_ticker_response import BrandRetrieveByTickerResponse
from ..types.brand_retrieve_simplified_response import BrandRetrieveSimplifiedResponse
from ..types.brand_identify_from_transaction_response import BrandIdentifyFromTransactionResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return BrandResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        domain: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Retrieve logos, backdrops, colors, industry, description, and more from any
        domain

        Args:
          domain: Domain name to retrieve brand data for (e.g., 'example.com', 'google.com').
              Cannot be used with name or ticker parameters.

          force_language: Optional parameter to force the language of the retrieved brand data. Works with
              all three lookup methods.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data. Works with all three lookup methods.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_params.BrandRetrieveParams,
                ),
            ),
            cast_to=BrandRetrieveResponse,
        )

    def identify_from_transaction(
        self,
        *,
        transaction_info: str,
        city: str | Omit = omit,
        country_gl: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "an",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "st",
            "sv",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        high_confidence_only: bool | Omit = omit,
        max_speed: bool | Omit = omit,
        mcc: str | Omit = omit,
        phone: float | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandIdentifyFromTransactionResponse:
        """
        Endpoint specially designed for platforms that want to identify transaction data
        by the transaction title.

        Args:
          transaction_info: Transaction information to identify the brand

          city: Optional city name to prioritize when searching for the brand.

          country_gl: Optional country code (GL parameter) to specify the country. This affects the
              geographic location used for search queries.

          force_language: Optional parameter to force the language of the retrieved brand data.

          high_confidence_only: When set to true, the API will perform an additional verification steps to
              ensure the identified brand matches the transaction with high confidence.
              Defaults to false.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          mcc: Optional Merchant Category Code (MCC) to help identify the business
              category/industry.

          phone: Optional phone number from the transaction to help verify brand match.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/transaction_identifier",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "transaction_info": transaction_info,
                        "city": city,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "high_confidence_only": high_confidence_only,
                        "max_speed": max_speed,
                        "mcc": mcc,
                        "phone": phone,
                        "timeout_ms": timeout_ms,
                    },
                    brand_identify_from_transaction_params.BrandIdentifyFromTransactionParams,
                ),
            ),
            cast_to=BrandIdentifyFromTransactionResponse,
        )

    def retrieve_by_email(
        self,
        *,
        email: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByEmailResponse:
        """
        Retrieve brand information using an email address while detecting disposable and
        free email addresses. This endpoint extracts the domain from the email address
        and returns brand data for that domain. Disposable and free email addresses
        (like gmail.com, yahoo.com) will throw a 422 error.

        Args:
          email: Email address to retrieve brand data for (e.g., 'contact@example.com'). The
              domain will be extracted from the email. Free email providers (gmail.com,
              yahoo.com, etc.) and disposable email addresses are not allowed.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "email": email,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_email_params.BrandRetrieveByEmailParams,
                ),
            ),
            cast_to=BrandRetrieveByEmailResponse,
        )

    def retrieve_by_isin(
        self,
        *,
        isin: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByIsinResponse:
        """
        Retrieve brand information using an ISIN (International Securities
        Identification Number). This endpoint looks up the company associated with the
        ISIN and returns its brand data.

        Args:
          isin: ISIN (International Securities Identification Number) to retrieve brand data for
              (e.g., 'AU000000IMD5', 'US0378331005'). Must be exactly 12 characters: 2 letters
              followed by 9 alphanumeric characters and ending with a digit.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-isin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "isin": isin,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_isin_params.BrandRetrieveByIsinParams,
                ),
            ),
            cast_to=BrandRetrieveByIsinResponse,
        )

    def retrieve_by_name(
        self,
        *,
        name: str,
        country_gl: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "an",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "st",
            "sv",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByNameResponse:
        """Retrieve brand information using a company name.

        This endpoint searches for the
        company by name and returns its brand data.

        Args:
          name: Company name to retrieve brand data for (e.g., 'Apple Inc', 'Microsoft
              Corporation'). Must be 3-30 characters.

          country_gl: Optional country code (GL parameter) to specify the country. This affects the
              geographic location used for search queries.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-name",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_name_params.BrandRetrieveByNameParams,
                ),
            ),
            cast_to=BrandRetrieveByNameResponse,
        )

    def retrieve_by_ticker(
        self,
        *,
        ticker: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        ticker_exchange: Literal[
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "BVC",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUB",
            "DUS",
            "DXE",
            "EGX",
            "FSX",
            "HAM",
            "HEL",
            "HKSE",
            "HOSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LIS",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NSE",
            "NYSE",
            "NZE",
            "OSL",
            "OTC",
            "PAR",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TAL",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "WSE",
            "XETRA",
        ]
        | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByTickerResponse:
        """Retrieve brand information using a stock ticker symbol.

        This endpoint looks up
        the company associated with the ticker and returns its brand data.

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL', 'GOOGL', 'BRK.A').
              Must be 1-15 characters, letters/numbers/dots only.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          ticker_exchange: Optional stock exchange for the ticker. Defaults to NASDAQ if not specified.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-by-ticker",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ticker": ticker,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "ticker_exchange": ticker_exchange,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_ticker_params.BrandRetrieveByTickerParams,
                ),
            ),
            cast_to=BrandRetrieveByTickerResponse,
        )

    def retrieve_simplified(
        self,
        *,
        domain: str,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveSimplifiedResponse:
        """
        Returns a simplified version of brand data containing only essential
        information: domain, title, colors, logos, and backdrops. This endpoint is
        optimized for faster responses and reduced data transfer.

        Args:
          domain: Domain name to retrieve simplified brand data for

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-simplified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_simplified_params.BrandRetrieveSimplifiedParams,
                ),
            ),
            cast_to=BrandRetrieveSimplifiedResponse,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return AsyncBrandResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        domain: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """
        Retrieve logos, backdrops, colors, industry, description, and more from any
        domain

        Args:
          domain: Domain name to retrieve brand data for (e.g., 'example.com', 'google.com').
              Cannot be used with name or ticker parameters.

          force_language: Optional parameter to force the language of the retrieved brand data. Works with
              all three lookup methods.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data. Works with all three lookup methods.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_params.BrandRetrieveParams,
                ),
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def identify_from_transaction(
        self,
        *,
        transaction_info: str,
        city: str | Omit = omit,
        country_gl: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "an",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "st",
            "sv",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        high_confidence_only: bool | Omit = omit,
        max_speed: bool | Omit = omit,
        mcc: str | Omit = omit,
        phone: float | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandIdentifyFromTransactionResponse:
        """
        Endpoint specially designed for platforms that want to identify transaction data
        by the transaction title.

        Args:
          transaction_info: Transaction information to identify the brand

          city: Optional city name to prioritize when searching for the brand.

          country_gl: Optional country code (GL parameter) to specify the country. This affects the
              geographic location used for search queries.

          force_language: Optional parameter to force the language of the retrieved brand data.

          high_confidence_only: When set to true, the API will perform an additional verification steps to
              ensure the identified brand matches the transaction with high confidence.
              Defaults to false.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          mcc: Optional Merchant Category Code (MCC) to help identify the business
              category/industry.

          phone: Optional phone number from the transaction to help verify brand match.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/transaction_identifier",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "transaction_info": transaction_info,
                        "city": city,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "high_confidence_only": high_confidence_only,
                        "max_speed": max_speed,
                        "mcc": mcc,
                        "phone": phone,
                        "timeout_ms": timeout_ms,
                    },
                    brand_identify_from_transaction_params.BrandIdentifyFromTransactionParams,
                ),
            ),
            cast_to=BrandIdentifyFromTransactionResponse,
        )

    async def retrieve_by_email(
        self,
        *,
        email: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByEmailResponse:
        """
        Retrieve brand information using an email address while detecting disposable and
        free email addresses. This endpoint extracts the domain from the email address
        and returns brand data for that domain. Disposable and free email addresses
        (like gmail.com, yahoo.com) will throw a 422 error.

        Args:
          email: Email address to retrieve brand data for (e.g., 'contact@example.com'). The
              domain will be extracted from the email. Free email providers (gmail.com,
              yahoo.com, etc.) and disposable email addresses are not allowed.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-email",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "email": email,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_email_params.BrandRetrieveByEmailParams,
                ),
            ),
            cast_to=BrandRetrieveByEmailResponse,
        )

    async def retrieve_by_isin(
        self,
        *,
        isin: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByIsinResponse:
        """
        Retrieve brand information using an ISIN (International Securities
        Identification Number). This endpoint looks up the company associated with the
        ISIN and returns its brand data.

        Args:
          isin: ISIN (International Securities Identification Number) to retrieve brand data for
              (e.g., 'AU000000IMD5', 'US0378331005'). Must be exactly 12 characters: 2 letters
              followed by 9 alphanumeric characters and ending with a digit.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-isin",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "isin": isin,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_isin_params.BrandRetrieveByIsinParams,
                ),
            ),
            cast_to=BrandRetrieveByIsinResponse,
        )

    async def retrieve_by_name(
        self,
        *,
        name: str,
        country_gl: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "an",
            "ao",
            "aq",
            "ar",
            "as",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "br",
            "bs",
            "bt",
            "bv",
            "bw",
            "by",
            "bz",
            "ca",
            "cc",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "ck",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cu",
            "cv",
            "cx",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "eh",
            "er",
            "es",
            "et",
            "fi",
            "fj",
            "fk",
            "fm",
            "fo",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gh",
            "gi",
            "gl",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gs",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hm",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "in",
            "io",
            "iq",
            "ir",
            "is",
            "it",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "ki",
            "km",
            "kn",
            "kp",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "li",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "mg",
            "mh",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mp",
            "mq",
            "mr",
            "ms",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "nf",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nr",
            "nu",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pm",
            "pn",
            "pr",
            "ps",
            "pt",
            "pw",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sb",
            "sc",
            "sd",
            "se",
            "sg",
            "sh",
            "si",
            "sj",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "st",
            "sv",
            "sy",
            "sz",
            "tc",
            "td",
            "tf",
            "tg",
            "th",
            "tj",
            "tk",
            "tl",
            "tm",
            "tn",
            "to",
            "tr",
            "tt",
            "tv",
            "tw",
            "tz",
            "ua",
            "ug",
            "um",
            "us",
            "uy",
            "uz",
            "va",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "vu",
            "wf",
            "ws",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByNameResponse:
        """Retrieve brand information using a company name.

        This endpoint searches for the
        company by name and returns its brand data.

        Args:
          name: Company name to retrieve brand data for (e.g., 'Apple Inc', 'Microsoft
              Corporation'). Must be 3-30 characters.

          country_gl: Optional country code (GL parameter) to specify the country. This affects the
              geographic location used for search queries.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-name",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "country_gl": country_gl,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_name_params.BrandRetrieveByNameParams,
                ),
            ),
            cast_to=BrandRetrieveByNameResponse,
        )

    async def retrieve_by_ticker(
        self,
        *,
        ticker: str,
        force_language: Literal[
            "albanian",
            "arabic",
            "azeri",
            "bengali",
            "bulgarian",
            "cantonese",
            "cebuano",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "estonian",
            "farsi",
            "finnish",
            "french",
            "german",
            "hausa",
            "hawaiian",
            "hindi",
            "hungarian",
            "icelandic",
            "indonesian",
            "italian",
            "kazakh",
            "korean",
            "kyrgyz",
            "latin",
            "latvian",
            "lithuanian",
            "macedonian",
            "mongolian",
            "nepali",
            "norwegian",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "romanian",
            "russian",
            "serbian",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "swahili",
            "swedish",
            "tagalog",
            "thai",
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | Omit = omit,
        max_speed: bool | Omit = omit,
        ticker_exchange: Literal[
            "AMEX",
            "AMS",
            "AQS",
            "ASX",
            "ATH",
            "BER",
            "BME",
            "BRU",
            "BSE",
            "BUD",
            "BUE",
            "BVC",
            "CBOE",
            "CNQ",
            "CPH",
            "DFM",
            "DOH",
            "DUB",
            "DUS",
            "DXE",
            "EGX",
            "FSX",
            "HAM",
            "HEL",
            "HKSE",
            "HOSE",
            "ICE",
            "IOB",
            "IST",
            "JKT",
            "JNB",
            "JPX",
            "KLS",
            "KOE",
            "KSC",
            "KUW",
            "LIS",
            "LSE",
            "MCX",
            "MEX",
            "MIL",
            "MUN",
            "NASDAQ",
            "NEO",
            "NSE",
            "NYSE",
            "NZE",
            "OSL",
            "OTC",
            "PAR",
            "PNK",
            "PRA",
            "RIS",
            "SAO",
            "SAU",
            "SES",
            "SET",
            "SGO",
            "SHH",
            "SHZ",
            "SIX",
            "STO",
            "STU",
            "TAI",
            "TAL",
            "TLV",
            "TSX",
            "TSXV",
            "TWO",
            "VIE",
            "WSE",
            "XETRA",
        ]
        | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveByTickerResponse:
        """Retrieve brand information using a stock ticker symbol.

        This endpoint looks up
        the company associated with the ticker and returns its brand data.

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL', 'GOOGL', 'BRK.A').
              Must be 1-15 characters, letters/numbers/dots only.

          force_language: Optional parameter to force the language of the retrieved brand data.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          ticker_exchange: Optional stock exchange for the ticker. Defaults to NASDAQ if not specified.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-by-ticker",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ticker": ticker,
                        "force_language": force_language,
                        "max_speed": max_speed,
                        "ticker_exchange": ticker_exchange,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_by_ticker_params.BrandRetrieveByTickerParams,
                ),
            ),
            cast_to=BrandRetrieveByTickerResponse,
        )

    async def retrieve_simplified(
        self,
        *,
        domain: str,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveSimplifiedResponse:
        """
        Returns a simplified version of brand data containing only essential
        information: domain, title, colors, logos, and backdrops. This endpoint is
        optimized for faster responses and reduced data transfer.

        Args:
          domain: Domain name to retrieve simplified brand data for

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-simplified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_simplified_params.BrandRetrieveSimplifiedParams,
                ),
            ),
            cast_to=BrandRetrieveSimplifiedResponse,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_raw_response_wrapper(
            brand.retrieve,
        )
        self.identify_from_transaction = to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.retrieve_by_email = to_raw_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = to_raw_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = to_raw_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = to_raw_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_simplified = to_raw_response_wrapper(
            brand.retrieve_simplified,
        )


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_raw_response_wrapper(
            brand.retrieve,
        )
        self.identify_from_transaction = async_to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.retrieve_by_email = async_to_raw_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = async_to_raw_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = async_to_raw_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = async_to_raw_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_simplified = async_to_raw_response_wrapper(
            brand.retrieve_simplified,
        )


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.identify_from_transaction = to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.retrieve_by_email = to_streamed_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = to_streamed_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = to_streamed_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = to_streamed_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_simplified = to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.identify_from_transaction = async_to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.retrieve_by_email = async_to_streamed_response_wrapper(
            brand.retrieve_by_email,
        )
        self.retrieve_by_isin = async_to_streamed_response_wrapper(
            brand.retrieve_by_isin,
        )
        self.retrieve_by_name = async_to_streamed_response_wrapper(
            brand.retrieve_by_name,
        )
        self.retrieve_by_ticker = async_to_streamed_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_simplified = async_to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
