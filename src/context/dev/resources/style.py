# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import style_extract_fonts_params, style_extract_styleguide_params
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
from ..types.style_extract_fonts_response import StyleExtractFontsResponse
from ..types.style_extract_styleguide_response import StyleExtractStyleguideResponse

__all__ = ["StyleResource", "AsyncStyleResource"]


class StyleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StyleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return StyleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StyleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return StyleResourceWithStreamingResponse(self)

    def extract_fonts(
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
    ) -> StyleExtractFontsResponse:
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
                    style_extract_fonts_params.StyleExtractFontsParams,
                ),
            ),
            cast_to=StyleExtractFontsResponse,
        )

    def extract_styleguide(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleExtractStyleguideResponse:
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

          prioritize: Optional parameter to prioritize screenshot capture for styleguide extraction.
              If 'speed', optimizes for faster capture with basic quality. If 'quality',
              optimizes for higher quality with longer wait times. Defaults to 'quality' if
              not provided.

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
                        "prioritize": prioritize,
                        "timeout_ms": timeout_ms,
                    },
                    style_extract_styleguide_params.StyleExtractStyleguideParams,
                ),
            ),
            cast_to=StyleExtractStyleguideResponse,
        )


class AsyncStyleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStyleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStyleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStyleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return AsyncStyleResourceWithStreamingResponse(self)

    async def extract_fonts(
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
    ) -> StyleExtractFontsResponse:
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
                    style_extract_fonts_params.StyleExtractFontsParams,
                ),
            ),
            cast_to=StyleExtractFontsResponse,
        )

    async def extract_styleguide(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StyleExtractStyleguideResponse:
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

          prioritize: Optional parameter to prioritize screenshot capture for styleguide extraction.
              If 'speed', optimizes for faster capture with basic quality. If 'quality',
              optimizes for higher quality with longer wait times. Defaults to 'quality' if
              not provided.

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
                        "prioritize": prioritize,
                        "timeout_ms": timeout_ms,
                    },
                    style_extract_styleguide_params.StyleExtractStyleguideParams,
                ),
            ),
            cast_to=StyleExtractStyleguideResponse,
        )


class StyleResourceWithRawResponse:
    def __init__(self, style: StyleResource) -> None:
        self._style = style

        self.extract_fonts = to_raw_response_wrapper(
            style.extract_fonts,
        )
        self.extract_styleguide = to_raw_response_wrapper(
            style.extract_styleguide,
        )


class AsyncStyleResourceWithRawResponse:
    def __init__(self, style: AsyncStyleResource) -> None:
        self._style = style

        self.extract_fonts = async_to_raw_response_wrapper(
            style.extract_fonts,
        )
        self.extract_styleguide = async_to_raw_response_wrapper(
            style.extract_styleguide,
        )


class StyleResourceWithStreamingResponse:
    def __init__(self, style: StyleResource) -> None:
        self._style = style

        self.extract_fonts = to_streamed_response_wrapper(
            style.extract_fonts,
        )
        self.extract_styleguide = to_streamed_response_wrapper(
            style.extract_styleguide,
        )


class AsyncStyleResourceWithStreamingResponse:
    def __init__(self, style: AsyncStyleResource) -> None:
        self._style = style

        self.extract_fonts = async_to_streamed_response_wrapper(
            style.extract_fonts,
        )
        self.extract_styleguide = async_to_streamed_response_wrapper(
            style.extract_styleguide,
        )
