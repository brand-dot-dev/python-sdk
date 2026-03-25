# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import industry_retrieve_naics_params
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
from ..types.industry_retrieve_naics_response import IndustryRetrieveNaicsResponse

__all__ = ["IndustryResource", "AsyncIndustryResource"]


class IndustryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndustryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return IndustryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndustryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return IndustryResourceWithStreamingResponse(self)

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
    ) -> IndustryRetrieveNaicsResponse:
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
                    industry_retrieve_naics_params.IndustryRetrieveNaicsParams,
                ),
            ),
            cast_to=IndustryRetrieveNaicsResponse,
        )


class AsyncIndustryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndustryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIndustryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndustryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return AsyncIndustryResourceWithStreamingResponse(self)

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
    ) -> IndustryRetrieveNaicsResponse:
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
                    industry_retrieve_naics_params.IndustryRetrieveNaicsParams,
                ),
            ),
            cast_to=IndustryRetrieveNaicsResponse,
        )


class IndustryResourceWithRawResponse:
    def __init__(self, industry: IndustryResource) -> None:
        self._industry = industry

        self.retrieve_naics = to_raw_response_wrapper(
            industry.retrieve_naics,
        )


class AsyncIndustryResourceWithRawResponse:
    def __init__(self, industry: AsyncIndustryResource) -> None:
        self._industry = industry

        self.retrieve_naics = async_to_raw_response_wrapper(
            industry.retrieve_naics,
        )


class IndustryResourceWithStreamingResponse:
    def __init__(self, industry: IndustryResource) -> None:
        self._industry = industry

        self.retrieve_naics = to_streamed_response_wrapper(
            industry.retrieve_naics,
        )


class AsyncIndustryResourceWithStreamingResponse:
    def __init__(self, industry: AsyncIndustryResource) -> None:
        self._industry = industry

        self.retrieve_naics = async_to_streamed_response_wrapper(
            industry.retrieve_naics,
        )
