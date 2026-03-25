# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import utility_prefetch_params, utility_prefetch_by_email_params
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
from ..types.utility_prefetch_response import UtilityPrefetchResponse
from ..types.utility_prefetch_by_email_response import UtilityPrefetchByEmailResponse

__all__ = ["UtilityResource", "AsyncUtilityResource"]


class UtilityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UtilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return UtilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UtilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return UtilityResourceWithStreamingResponse(self)

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
    ) -> UtilityPrefetchResponse:
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
                utility_prefetch_params.UtilityPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchResponse,
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
    ) -> UtilityPrefetchByEmailResponse:
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
                utility_prefetch_by_email_params.UtilityPrefetchByEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchByEmailResponse,
        )


class AsyncUtilityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUtilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUtilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUtilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/python-sdk#with_streaming_response
        """
        return AsyncUtilityResourceWithStreamingResponse(self)

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
    ) -> UtilityPrefetchResponse:
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
                utility_prefetch_params.UtilityPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchResponse,
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
    ) -> UtilityPrefetchByEmailResponse:
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
                utility_prefetch_by_email_params.UtilityPrefetchByEmailParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchByEmailResponse,
        )


class UtilityResourceWithRawResponse:
    def __init__(self, utility: UtilityResource) -> None:
        self._utility = utility

        self.prefetch = to_raw_response_wrapper(
            utility.prefetch,
        )
        self.prefetch_by_email = to_raw_response_wrapper(
            utility.prefetch_by_email,
        )


class AsyncUtilityResourceWithRawResponse:
    def __init__(self, utility: AsyncUtilityResource) -> None:
        self._utility = utility

        self.prefetch = async_to_raw_response_wrapper(
            utility.prefetch,
        )
        self.prefetch_by_email = async_to_raw_response_wrapper(
            utility.prefetch_by_email,
        )


class UtilityResourceWithStreamingResponse:
    def __init__(self, utility: UtilityResource) -> None:
        self._utility = utility

        self.prefetch = to_streamed_response_wrapper(
            utility.prefetch,
        )
        self.prefetch_by_email = to_streamed_response_wrapper(
            utility.prefetch_by_email,
        )


class AsyncUtilityResourceWithStreamingResponse:
    def __init__(self, utility: AsyncUtilityResource) -> None:
        self._utility = utility

        self.prefetch = async_to_streamed_response_wrapper(
            utility.prefetch,
        )
        self.prefetch_by_email = async_to_streamed_response_wrapper(
            utility.prefetch_by_email,
        )
