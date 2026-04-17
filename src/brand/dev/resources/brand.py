# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..types import (
    brand_fonts_params,
    brand_ai_query_params,
    brand_prefetch_params,
    brand_retrieve_params,
    brand_ai_product_params,
    brand_screenshot_params,
    brand_styleguide_params,
    brand_ai_products_params,
    brand_web_scrape_md_params,
    brand_retrieve_naics_params,
    brand_web_scrape_html_params,
    brand_retrieve_by_isin_params,
    brand_retrieve_by_name_params,
    brand_prefetch_by_email_params,
    brand_retrieve_by_email_params,
    brand_web_scrape_images_params,
    brand_retrieve_by_ticker_params,
    brand_web_scrape_sitemap_params,
    brand_retrieve_simplified_params,
    brand_identify_from_transaction_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.brand_fonts_response import BrandFontsResponse
from ..types.brand_ai_query_response import BrandAIQueryResponse
from ..types.brand_prefetch_response import BrandPrefetchResponse
from ..types.brand_retrieve_response import BrandRetrieveResponse
from ..types.brand_ai_product_response import BrandAIProductResponse
from ..types.brand_screenshot_response import BrandScreenshotResponse
from ..types.brand_styleguide_response import BrandStyleguideResponse
from ..types.brand_ai_products_response import BrandAIProductsResponse
from ..types.brand_web_scrape_md_response import BrandWebScrapeMdResponse
from ..types.brand_retrieve_naics_response import BrandRetrieveNaicsResponse
from ..types.brand_web_scrape_html_response import BrandWebScrapeHTMLResponse
from ..types.brand_retrieve_by_isin_response import BrandRetrieveByIsinResponse
from ..types.brand_retrieve_by_name_response import BrandRetrieveByNameResponse
from ..types.brand_prefetch_by_email_response import BrandPrefetchByEmailResponse
from ..types.brand_retrieve_by_email_response import BrandRetrieveByEmailResponse
from ..types.brand_web_scrape_images_response import BrandWebScrapeImagesResponse
from ..types.brand_retrieve_by_ticker_response import BrandRetrieveByTickerResponse
from ..types.brand_web_scrape_sitemap_response import BrandWebScrapeSitemapResponse
from ..types.brand_retrieve_simplified_response import BrandRetrieveSimplifiedResponse
from ..types.brand_identify_from_transaction_response import BrandIdentifyFromTransactionResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#with_streaming_response
        """
        return BrandResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        domain: str,
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

          force_language: Optional parameter to force the language of the retrieved brand data.

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

    def ai_product(
        self,
        *,
        url: str,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductResponse:
        """
        Beta feature: Given a single URL, determines if it is a product detail page,
        classifies the platform/product type, and extracts the product information.
        Supports Amazon, TikTok Shop, Etsy, and generic ecommerce sites.

        Args:
          url: The product page URL to extract product data from.

          timeout_ms: Optional timeout in milliseconds for the request. Maximum allowed value is
              300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/ai/product",
            body=maybe_transform(
                {
                    "url": url,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_product_params.BrandAIProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductResponse,
        )

    @overload
    def ai_products(
        self,
        *,
        domain: str,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Beta feature: Extract product information from a brand's website.

        We will
        analyze the website and return a list of products with details such as name,
        description, image, pricing, features, and more.

        Args:
          domain: The domain name to analyze.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. Maximum allowed value is
              300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def ai_products(
        self,
        *,
        direct_url: str,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Beta feature: Extract product information from a brand's website.

        We will
        analyze the website and return a list of products with details such as name,
        description, image, pricing, features, and more.

        Args:
          direct_url: A specific URL to use directly as the starting point for extraction without
              domain resolution.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. Maximum allowed value is
              300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["domain"], ["direct_url"])
    def ai_products(
        self,
        *,
        domain: str | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        direct_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        return self._post(
            "/brand/ai/products",
            body=maybe_transform(
                {
                    "domain": domain,
                    "max_products": max_products,
                    "timeout_ms": timeout_ms,
                    "direct_url": direct_url,
                },
                brand_ai_products_params.BrandAIProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductsResponse,
        )

    def ai_query(
        self,
        *,
        data_to_extract: Iterable[brand_ai_query_params.DataToExtract],
        domain: str,
        specific_pages: brand_ai_query_params.SpecificPages | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIQueryResponse:
        """Use AI to extract specific data points from a brand's website.

        The AI will crawl
        the website and extract the requested information based on the provided data
        points.

        Args:
          data_to_extract: Array of data points to extract from the website

          domain: The domain name to analyze

          specific_pages: Optional object specifying which pages to analyze

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/ai/query",
            body=maybe_transform(
                {
                    "data_to_extract": data_to_extract,
                    "domain": domain,
                    "specific_pages": specific_pages,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_query_params.BrandAIQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIQueryResponse,
        )

    def fonts(
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
    ) -> BrandFontsResponse:
        """
        Extract font information from a brand's website including font families, usage
        statistics, fallbacks, and element/word counts.

        Args:
          domain: Domain name to extract fonts from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/fonts",
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
                    brand_fonts_params.BrandFontsParams,
                ),
            ),
            cast_to=BrandFontsResponse,
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

    def prefetch(
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
    ) -> BrandPrefetchResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint does not charge credits and is available for paid
        customers to optimize future requests. [You must be on a paid plan to use this
        endpoint]

        Args:
          domain: Domain name to prefetch brand data for

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/prefetch",
            body=maybe_transform(
                {
                    "domain": domain,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_params.BrandPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchResponse,
        )

    def prefetch_by_email(
        self,
        *,
        email: str,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandPrefetchByEmailResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint accepts an email address, extracts the domain from it,
        validates that it's not a disposable or free email provider, and queues the
        domain for prefetching. This endpoint does not charge credits and is available
        for paid customers to optimize future requests. [You must be on a paid plan to
        use this endpoint]

        Args:
          email: Email address to prefetch brand data for. The domain will be extracted from the
              email. Free email providers (gmail.com, yahoo.com, etc.) and disposable email
              addresses are not allowed.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/prefetch-by-email",
            body=maybe_transform(
                {
                    "email": email,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_by_email_params.BrandPrefetchByEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchByEmailResponse,
        )

    def retrieve_by_email(
        self,
        *,
        email: str,
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

    def retrieve_naics(
        self,
        *,
        input: str,
        max_results: int | Omit = omit,
        min_results: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveNaicsResponse:
        """
        Endpoint to classify any brand into a 2022 NAICS code.

        Args:
          input: Brand domain or title to retrieve NAICS code for. If a valid domain is provided
              in `input`, it will be used for classification, otherwise, we will search for
              the brand using the provided title.

          max_results: Maximum number of NAICS codes to return. Must be between 1 and 10. Defaults
              to 5.

          min_results: Minimum number of NAICS codes to return. Must be at least 1. Defaults to 1.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/naics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "input": input,
                        "max_results": max_results,
                        "min_results": min_results,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_naics_params.BrandRetrieveNaicsParams,
                ),
            ),
            cast_to=BrandRetrieveNaicsResponse,
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

    def screenshot(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandScreenshotResponse:
        """Capture a screenshot of a website.

        Supports both viewport (standard browser
        view) and full-page screenshots. Can also screenshot specific page types (login,
        pricing, etc.) by using heuristics to find the appropriate URL. Either 'domain'
        or 'directUrl' must be provided as a query parameter, but not both. Returns a
        URL to the uploaded screenshot image hosted on our CDN.

        Args:
          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          prioritize: Optional parameter to prioritize screenshot capture. If 'speed', optimizes for
              faster capture with basic quality. If 'quality', optimizes for higher quality
              with longer wait times. Defaults to 'quality' if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "page": page,
                        "prioritize": prioritize,
                    },
                    brand_screenshot_params.BrandScreenshotParams,
                ),
            ),
            cast_to=BrandScreenshotResponse,
        )

    def styleguide(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandStyleguideResponse:
        """
        Automatically extract comprehensive design system information from a brand's
        website including colors, typography, spacing, shadows, and UI components.
        Either 'domain' or 'directUrl' must be provided as a query parameter, but not
        both.

        Args:
          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system').

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/styleguide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    brand_styleguide_params.BrandStyleguideParams,
                ),
            ),
            cast_to=BrandStyleguideResponse,
        )

    def web_scrape_html(
        self,
        *,
        url: str,
        max_age_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeHTMLResponse:
        """
        Scrapes the given URL and returns the raw HTML content of the page.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Set to 0 to always scrape fresh.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "max_age_ms": max_age_ms,
                    },
                    brand_web_scrape_html_params.BrandWebScrapeHTMLParams,
                ),
            ),
            cast_to=BrandWebScrapeHTMLResponse,
        )

    def web_scrape_images(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeImagesResponse:
        """Scrapes all images from the given URL.

        Extracts images from img, svg,
        picture/source, link, and video elements including inline SVGs, base64 data
        URIs, and standard URLs.

        Args:
          url: Full URL to scrape images from (must include http:// or https:// protocol)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, brand_web_scrape_images_params.BrandWebScrapeImagesParams),
            ),
            cast_to=BrandWebScrapeImagesResponse,
        )

    def web_scrape_md(
        self,
        *,
        url: str,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeMdResponse:
        """
        Scrapes the given URL, converts the HTML content to Markdown, and returns the
        result.

        Args:
          url: Full URL to scrape and convert to markdown (must include http:// or https://
              protocol)

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Set to 0 to always scrape fresh.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "include_images": include_images,
                        "include_links": include_links,
                        "max_age_ms": max_age_ms,
                        "shorten_base64_images": shorten_base64_images,
                        "use_main_content_only": use_main_content_only,
                    },
                    brand_web_scrape_md_params.BrandWebScrapeMdParams,
                ),
            ),
            cast_to=BrandWebScrapeMdResponse,
        )

    def web_scrape_sitemap(
        self,
        *,
        domain: str,
        max_links: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeSitemapResponse:
        """
        Crawls the sitemap of the given domain and returns all discovered page URLs.
        Supports sitemap index files (recursive), parallel fetching with concurrency
        control, deduplication, and filters out non-page resources (images, PDFs, etc.).

        Args:
          domain: Domain name to crawl sitemaps for (e.g., 'example.com'). The domain will be
              automatically normalized and validated.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "max_links": max_links,
                    },
                    brand_web_scrape_sitemap_params.BrandWebScrapeSitemapParams,
                ),
            ),
            cast_to=BrandWebScrapeSitemapResponse,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/deprecated-brand-python-sdk#with_streaming_response
        """
        return AsyncBrandResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        domain: str,
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

          force_language: Optional parameter to force the language of the retrieved brand data.

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

    async def ai_product(
        self,
        *,
        url: str,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductResponse:
        """
        Beta feature: Given a single URL, determines if it is a product detail page,
        classifies the platform/product type, and extracts the product information.
        Supports Amazon, TikTok Shop, Etsy, and generic ecommerce sites.

        Args:
          url: The product page URL to extract product data from.

          timeout_ms: Optional timeout in milliseconds for the request. Maximum allowed value is
              300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/ai/product",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_product_params.BrandAIProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductResponse,
        )

    @overload
    async def ai_products(
        self,
        *,
        domain: str,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Beta feature: Extract product information from a brand's website.

        We will
        analyze the website and return a list of products with details such as name,
        description, image, pricing, features, and more.

        Args:
          domain: The domain name to analyze.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. Maximum allowed value is
              300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def ai_products(
        self,
        *,
        direct_url: str,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        """Beta feature: Extract product information from a brand's website.

        We will
        analyze the website and return a list of products with details such as name,
        description, image, pricing, features, and more.

        Args:
          direct_url: A specific URL to use directly as the starting point for extraction without
              domain resolution.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. Maximum allowed value is
              300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["domain"], ["direct_url"])
    async def ai_products(
        self,
        *,
        domain: str | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        direct_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIProductsResponse:
        return await self._post(
            "/brand/ai/products",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "max_products": max_products,
                    "timeout_ms": timeout_ms,
                    "direct_url": direct_url,
                },
                brand_ai_products_params.BrandAIProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIProductsResponse,
        )

    async def ai_query(
        self,
        *,
        data_to_extract: Iterable[brand_ai_query_params.DataToExtract],
        domain: str,
        specific_pages: brand_ai_query_params.SpecificPages | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandAIQueryResponse:
        """Use AI to extract specific data points from a brand's website.

        The AI will crawl
        the website and extract the requested information based on the provided data
        points.

        Args:
          data_to_extract: Array of data points to extract from the website

          domain: The domain name to analyze

          specific_pages: Optional object specifying which pages to analyze

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/ai/query",
            body=await async_maybe_transform(
                {
                    "data_to_extract": data_to_extract,
                    "domain": domain,
                    "specific_pages": specific_pages,
                    "timeout_ms": timeout_ms,
                },
                brand_ai_query_params.BrandAIQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIQueryResponse,
        )

    async def fonts(
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
    ) -> BrandFontsResponse:
        """
        Extract font information from a brand's website including font families, usage
        statistics, fallbacks, and element/word counts.

        Args:
          domain: Domain name to extract fonts from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/fonts",
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
                    brand_fonts_params.BrandFontsParams,
                ),
            ),
            cast_to=BrandFontsResponse,
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

    async def prefetch(
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
    ) -> BrandPrefetchResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint does not charge credits and is available for paid
        customers to optimize future requests. [You must be on a paid plan to use this
        endpoint]

        Args:
          domain: Domain name to prefetch brand data for

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/prefetch",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_params.BrandPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchResponse,
        )

    async def prefetch_by_email(
        self,
        *,
        email: str,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandPrefetchByEmailResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint accepts an email address, extracts the domain from it,
        validates that it's not a disposable or free email provider, and queues the
        domain for prefetching. This endpoint does not charge credits and is available
        for paid customers to optimize future requests. [You must be on a paid plan to
        use this endpoint]

        Args:
          email: Email address to prefetch brand data for. The domain will be extracted from the
              email. Free email providers (gmail.com, yahoo.com, etc.) and disposable email
              addresses are not allowed.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/prefetch-by-email",
            body=await async_maybe_transform(
                {
                    "email": email,
                    "timeout_ms": timeout_ms,
                },
                brand_prefetch_by_email_params.BrandPrefetchByEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchByEmailResponse,
        )

    async def retrieve_by_email(
        self,
        *,
        email: str,
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

    async def retrieve_naics(
        self,
        *,
        input: str,
        max_results: int | Omit = omit,
        min_results: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveNaicsResponse:
        """
        Endpoint to classify any brand into a 2022 NAICS code.

        Args:
          input: Brand domain or title to retrieve NAICS code for. If a valid domain is provided
              in `input`, it will be used for classification, otherwise, we will search for
              the brand using the provided title.

          max_results: Maximum number of NAICS codes to return. Must be between 1 and 10. Defaults
              to 5.

          min_results: Minimum number of NAICS codes to return. Must be at least 1. Defaults to 1.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/naics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "input": input,
                        "max_results": max_results,
                        "min_results": min_results,
                        "timeout_ms": timeout_ms,
                    },
                    brand_retrieve_naics_params.BrandRetrieveNaicsParams,
                ),
            ),
            cast_to=BrandRetrieveNaicsResponse,
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

    async def screenshot(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandScreenshotResponse:
        """Capture a screenshot of a website.

        Supports both viewport (standard browser
        view) and full-page screenshots. Can also screenshot specific page types (login,
        pricing, etc.) by using heuristics to find the appropriate URL. Either 'domain'
        or 'directUrl' must be provided as a query parameter, but not both. Returns a
        URL to the uploaded screenshot image hosted on our CDN.

        Args:
          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          prioritize: Optional parameter to prioritize screenshot capture. If 'speed', optimizes for
              faster capture with basic quality. If 'quality', optimizes for higher quality
              with longer wait times. Defaults to 'quality' if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "page": page,
                        "prioritize": prioritize,
                    },
                    brand_screenshot_params.BrandScreenshotParams,
                ),
            ),
            cast_to=BrandScreenshotResponse,
        )

    async def styleguide(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandStyleguideResponse:
        """
        Automatically extract comprehensive design system information from a brand's
        website including colors, typography, spacing, shadows, and UI components.
        Either 'domain' or 'directUrl' must be provided as a query parameter, but not
        both.

        Args:
          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system').

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/styleguide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    brand_styleguide_params.BrandStyleguideParams,
                ),
            ),
            cast_to=BrandStyleguideResponse,
        )

    async def web_scrape_html(
        self,
        *,
        url: str,
        max_age_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeHTMLResponse:
        """
        Scrapes the given URL and returns the raw HTML content of the page.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Set to 0 to always scrape fresh.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "max_age_ms": max_age_ms,
                    },
                    brand_web_scrape_html_params.BrandWebScrapeHTMLParams,
                ),
            ),
            cast_to=BrandWebScrapeHTMLResponse,
        )

    async def web_scrape_images(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeImagesResponse:
        """Scrapes all images from the given URL.

        Extracts images from img, svg,
        picture/source, link, and video elements including inline SVGs, base64 data
        URIs, and standard URLs.

        Args:
          url: Full URL to scrape images from (must include http:// or https:// protocol)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"url": url}, brand_web_scrape_images_params.BrandWebScrapeImagesParams
                ),
            ),
            cast_to=BrandWebScrapeImagesResponse,
        )

    async def web_scrape_md(
        self,
        *,
        url: str,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeMdResponse:
        """
        Scrapes the given URL, converts the HTML content to Markdown, and returns the
        result.

        Args:
          url: Full URL to scrape and convert to markdown (must include http:// or https://
              protocol)

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Set to 0 to always scrape fresh.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "include_images": include_images,
                        "include_links": include_links,
                        "max_age_ms": max_age_ms,
                        "shorten_base64_images": shorten_base64_images,
                        "use_main_content_only": use_main_content_only,
                    },
                    brand_web_scrape_md_params.BrandWebScrapeMdParams,
                ),
            ),
            cast_to=BrandWebScrapeMdResponse,
        )

    async def web_scrape_sitemap(
        self,
        *,
        domain: str,
        max_links: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandWebScrapeSitemapResponse:
        """
        Crawls the sitemap of the given domain and returns all discovered page URLs.
        Supports sitemap index files (recursive), parallel fetching with concurrency
        control, deduplication, and filters out non-page resources (images, PDFs, etc.).

        Args:
          domain: Domain name to crawl sitemaps for (e.g., 'example.com'). The domain will be
              automatically normalized and validated.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "max_links": max_links,
                    },
                    brand_web_scrape_sitemap_params.BrandWebScrapeSitemapParams,
                ),
            ),
            cast_to=BrandWebScrapeSitemapResponse,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_raw_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = to_raw_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = to_raw_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = to_raw_response_wrapper(
            brand.ai_query,
        )
        self.fonts = to_raw_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = to_raw_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = to_raw_response_wrapper(
            brand.prefetch_by_email,
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
        self.retrieve_naics = to_raw_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = to_raw_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = to_raw_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = to_raw_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = to_raw_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = to_raw_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = to_raw_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = to_raw_response_wrapper(
            brand.web_scrape_sitemap,
        )


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_raw_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = async_to_raw_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = async_to_raw_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = async_to_raw_response_wrapper(
            brand.ai_query,
        )
        self.fonts = async_to_raw_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = async_to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = async_to_raw_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = async_to_raw_response_wrapper(
            brand.prefetch_by_email,
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
        self.retrieve_naics = async_to_raw_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = async_to_raw_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = async_to_raw_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = async_to_raw_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = async_to_raw_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = async_to_raw_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = async_to_raw_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_raw_response_wrapper(
            brand.web_scrape_sitemap,
        )


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = to_streamed_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = to_streamed_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = to_streamed_response_wrapper(
            brand.ai_query,
        )
        self.fonts = to_streamed_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = to_streamed_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = to_streamed_response_wrapper(
            brand.prefetch_by_email,
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
        self.retrieve_naics = to_streamed_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = to_streamed_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = to_streamed_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = to_streamed_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = to_streamed_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = to_streamed_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = to_streamed_response_wrapper(
            brand.web_scrape_sitemap,
        )


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.ai_product = async_to_streamed_response_wrapper(
            brand.ai_product,
        )
        self.ai_products = async_to_streamed_response_wrapper(
            brand.ai_products,
        )
        self.ai_query = async_to_streamed_response_wrapper(
            brand.ai_query,
        )
        self.fonts = async_to_streamed_response_wrapper(
            brand.fonts,
        )
        self.identify_from_transaction = async_to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = async_to_streamed_response_wrapper(
            brand.prefetch,
        )
        self.prefetch_by_email = async_to_streamed_response_wrapper(
            brand.prefetch_by_email,
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
        self.retrieve_naics = async_to_streamed_response_wrapper(
            brand.retrieve_naics,
        )
        self.retrieve_simplified = async_to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
        self.screenshot = async_to_streamed_response_wrapper(
            brand.screenshot,
        )
        self.styleguide = async_to_streamed_response_wrapper(
            brand.styleguide,
        )
        self.web_scrape_html = async_to_streamed_response_wrapper(
            brand.web_scrape_html,
        )
        self.web_scrape_images = async_to_streamed_response_wrapper(
            brand.web_scrape_images,
        )
        self.web_scrape_md = async_to_streamed_response_wrapper(
            brand.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_streamed_response_wrapper(
            brand.web_scrape_sitemap,
        )
