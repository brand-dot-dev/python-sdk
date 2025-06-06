# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    brand_search_params,
    brand_ai_query_params,
    brand_prefetch_params,
    brand_retrieve_params,
    brand_retrieve_naics_params,
    brand_retrieve_by_ticker_params,
    brand_identify_from_transaction_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ..types.brand_search_response import BrandSearchResponse
from ..types.brand_ai_query_response import BrandAIQueryResponse
from ..types.brand_prefetch_response import BrandPrefetchResponse
from ..types.brand_retrieve_response import BrandRetrieveResponse
from ..types.brand_retrieve_naics_response import BrandRetrieveNaicsResponse
from ..types.brand_retrieve_by_ticker_response import BrandRetrieveByTickerResponse
from ..types.brand_identify_from_transaction_response import BrandIdentifyFromTransactionResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brand-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brand-dot-dev/python-sdk#with_streaming_response
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
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | NotGiven = NOT_GIVEN,
        max_speed: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveResponse:
        """
        Retrieve brand data by domain

        Args:
          domain: Domain name to retrieve brand data for

          force_language: Optional parameter to force the language of the retrieved brand data

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

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
                    },
                    brand_retrieve_params.BrandRetrieveParams,
                ),
            ),
            cast_to=BrandRetrieveResponse,
        )

    def ai_query(
        self,
        *,
        data_to_extract: Iterable[brand_ai_query_params.DataToExtract],
        domain: str,
        specific_pages: brand_ai_query_params.SpecificPages | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandAIQueryResponse:
        """Beta feature: Use AI to extract specific data points from a brand's website.

        The
        AI will crawl the website and extract the requested information based on the
        provided data points.

        Args:
          data_to_extract: Array of data points to extract from the website

          domain: The domain name to analyze

          specific_pages: Optional object specifying which pages to analyze

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
                },
                brand_ai_query_params.BrandAIQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIQueryResponse,
        )

    def identify_from_transaction(
        self,
        *,
        transaction_info: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandIdentifyFromTransactionResponse:
        """
        Endpoint specially designed for platforms that want to identify transaction data
        by the transaction title.

        Args:
          transaction_info: Transaction information to identify the brand

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
                    {"transaction_info": transaction_info},
                    brand_identify_from_transaction_params.BrandIdentifyFromTransactionParams,
                ),
            ),
            cast_to=BrandIdentifyFromTransactionResponse,
        )

    def prefetch(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandPrefetchResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint does not charge credits and is available for paid
        customers to optimize future requests. [You must be on a paid plan to use this
        endpoint]

        Args:
          domain: Domain name to prefetch brand data for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/prefetch",
            body=maybe_transform({"domain": domain}, brand_prefetch_params.BrandPrefetchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchResponse,
        )

    def retrieve_by_ticker(
        self,
        *,
        ticker: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveByTickerResponse:
        """Retrieve brand data by stock ticker (e.g.

        AAPL, TSLA, etc.)

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g. AAPL, TSLA, etc.)

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
                query=maybe_transform({"ticker": ticker}, brand_retrieve_by_ticker_params.BrandRetrieveByTickerParams),
            ),
            cast_to=BrandRetrieveByTickerResponse,
        )

    def retrieve_naics(
        self,
        *,
        input: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveNaicsResponse:
        """
        Endpoint to classify any brand into a 2022 NAICS code.

        Args:
          input: Brand domain or title to retrieve NAICS code for. If a valid domain is provided
              in `input`, it will be used for classification, otherwise, we will search for
              the brand using the provided title.

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
                query=maybe_transform({"input": input}, brand_retrieve_naics_params.BrandRetrieveNaicsParams),
            ),
            cast_to=BrandRetrieveNaicsResponse,
        )

    def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandSearchResponse:
        """
        Search brands by query

        Args:
          query: Query string to search brands

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, brand_search_params.BrandSearchParams),
            ),
            cast_to=BrandSearchResponse,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/brand-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/brand-dot-dev/python-sdk#with_streaming_response
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
            "turkish",
            "ukrainian",
            "urdu",
            "uzbek",
            "vietnamese",
            "welsh",
        ]
        | NotGiven = NOT_GIVEN,
        max_speed: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveResponse:
        """
        Retrieve brand data by domain

        Args:
          domain: Domain name to retrieve brand data for

          force_language: Optional parameter to force the language of the retrieved brand data

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

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
                    },
                    brand_retrieve_params.BrandRetrieveParams,
                ),
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def ai_query(
        self,
        *,
        data_to_extract: Iterable[brand_ai_query_params.DataToExtract],
        domain: str,
        specific_pages: brand_ai_query_params.SpecificPages | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandAIQueryResponse:
        """Beta feature: Use AI to extract specific data points from a brand's website.

        The
        AI will crawl the website and extract the requested information based on the
        provided data points.

        Args:
          data_to_extract: Array of data points to extract from the website

          domain: The domain name to analyze

          specific_pages: Optional object specifying which pages to analyze

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
                },
                brand_ai_query_params.BrandAIQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandAIQueryResponse,
        )

    async def identify_from_transaction(
        self,
        *,
        transaction_info: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandIdentifyFromTransactionResponse:
        """
        Endpoint specially designed for platforms that want to identify transaction data
        by the transaction title.

        Args:
          transaction_info: Transaction information to identify the brand

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
                    {"transaction_info": transaction_info},
                    brand_identify_from_transaction_params.BrandIdentifyFromTransactionParams,
                ),
            ),
            cast_to=BrandIdentifyFromTransactionResponse,
        )

    async def prefetch(
        self,
        *,
        domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandPrefetchResponse:
        """
        Signal that you may fetch brand data for a particular domain soon to improve
        latency. This endpoint does not charge credits and is available for paid
        customers to optimize future requests. [You must be on a paid plan to use this
        endpoint]

        Args:
          domain: Domain name to prefetch brand data for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/prefetch",
            body=await async_maybe_transform({"domain": domain}, brand_prefetch_params.BrandPrefetchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandPrefetchResponse,
        )

    async def retrieve_by_ticker(
        self,
        *,
        ticker: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveByTickerResponse:
        """Retrieve brand data by stock ticker (e.g.

        AAPL, TSLA, etc.)

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g. AAPL, TSLA, etc.)

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
                    {"ticker": ticker}, brand_retrieve_by_ticker_params.BrandRetrieveByTickerParams
                ),
            ),
            cast_to=BrandRetrieveByTickerResponse,
        )

    async def retrieve_naics(
        self,
        *,
        input: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandRetrieveNaicsResponse:
        """
        Endpoint to classify any brand into a 2022 NAICS code.

        Args:
          input: Brand domain or title to retrieve NAICS code for. If a valid domain is provided
              in `input`, it will be used for classification, otherwise, we will search for
              the brand using the provided title.

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
                    {"input": input}, brand_retrieve_naics_params.BrandRetrieveNaicsParams
                ),
            ),
            cast_to=BrandRetrieveNaicsResponse,
        )

    async def search(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BrandSearchResponse:
        """
        Search brands by query

        Args:
          query: Query string to search brands

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, brand_search_params.BrandSearchParams),
            ),
            cast_to=BrandSearchResponse,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_raw_response_wrapper(
            brand.retrieve,
        )
        self.ai_query = to_raw_response_wrapper(
            brand.ai_query,
        )
        self.identify_from_transaction = to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = to_raw_response_wrapper(
            brand.prefetch,
        )
        self.retrieve_by_ticker = to_raw_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = to_raw_response_wrapper(
            brand.retrieve_naics,
        )
        self.search = to_raw_response_wrapper(
            brand.search,
        )


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_raw_response_wrapper(
            brand.retrieve,
        )
        self.ai_query = async_to_raw_response_wrapper(
            brand.ai_query,
        )
        self.identify_from_transaction = async_to_raw_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = async_to_raw_response_wrapper(
            brand.prefetch,
        )
        self.retrieve_by_ticker = async_to_raw_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = async_to_raw_response_wrapper(
            brand.retrieve_naics,
        )
        self.search = async_to_raw_response_wrapper(
            brand.search,
        )


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.ai_query = to_streamed_response_wrapper(
            brand.ai_query,
        )
        self.identify_from_transaction = to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = to_streamed_response_wrapper(
            brand.prefetch,
        )
        self.retrieve_by_ticker = to_streamed_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = to_streamed_response_wrapper(
            brand.retrieve_naics,
        )
        self.search = to_streamed_response_wrapper(
            brand.search,
        )


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.ai_query = async_to_streamed_response_wrapper(
            brand.ai_query,
        )
        self.identify_from_transaction = async_to_streamed_response_wrapper(
            brand.identify_from_transaction,
        )
        self.prefetch = async_to_streamed_response_wrapper(
            brand.prefetch,
        )
        self.retrieve_by_ticker = async_to_streamed_response_wrapper(
            brand.retrieve_by_ticker,
        )
        self.retrieve_naics = async_to_streamed_response_wrapper(
            brand.retrieve_naics,
        )
        self.search = async_to_streamed_response_wrapper(
            brand.search,
        )
