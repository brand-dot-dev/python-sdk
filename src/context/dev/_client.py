# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, ContextDevError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import ai, web, brand, style, utility, industry
    from .resources.ai import AIResource, AsyncAIResource
    from .resources.web import WebResource, AsyncWebResource
    from .resources.brand import BrandResource, AsyncBrandResource
    from .resources.style import StyleResource, AsyncStyleResource
    from .resources.utility import UtilityResource, AsyncUtilityResource
    from .resources.industry import IndustryResource, AsyncIndustryResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ContextDev",
    "AsyncContextDev",
    "Client",
    "AsyncClient",
]


class ContextDev(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ContextDev client instance.

        This automatically infers the `api_key` argument from the `CONTEXT_DEV_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CONTEXT_DEV_API_KEY")
        if api_key is None:
            raise ContextDevError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CONTEXT_DEV_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CONTEXT_DEV_BASE_URL")
        if base_url is None:
            base_url = f"https://api.context.dev/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def web(self) -> WebResource:
        from .resources.web import WebResource

        return WebResource(self)

    @cached_property
    def ai(self) -> AIResource:
        from .resources.ai import AIResource

        return AIResource(self)

    @cached_property
    def style(self) -> StyleResource:
        from .resources.style import StyleResource

        return StyleResource(self)

    @cached_property
    def brand(self) -> BrandResource:
        from .resources.brand import BrandResource

        return BrandResource(self)

    @cached_property
    def industry(self) -> IndustryResource:
        from .resources.industry import IndustryResource

        return IndustryResource(self)

    @cached_property
    def utility(self) -> UtilityResource:
        from .resources.utility import UtilityResource

        return UtilityResource(self)

    @cached_property
    def with_raw_response(self) -> ContextDevWithRawResponse:
        return ContextDevWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContextDevWithStreamedResponse:
        return ContextDevWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncContextDev(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncContextDev client instance.

        This automatically infers the `api_key` argument from the `CONTEXT_DEV_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("CONTEXT_DEV_API_KEY")
        if api_key is None:
            raise ContextDevError(
                "The api_key client option must be set either by passing api_key to the client or by setting the CONTEXT_DEV_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("CONTEXT_DEV_BASE_URL")
        if base_url is None:
            base_url = f"https://api.context.dev/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def web(self) -> AsyncWebResource:
        from .resources.web import AsyncWebResource

        return AsyncWebResource(self)

    @cached_property
    def ai(self) -> AsyncAIResource:
        from .resources.ai import AsyncAIResource

        return AsyncAIResource(self)

    @cached_property
    def style(self) -> AsyncStyleResource:
        from .resources.style import AsyncStyleResource

        return AsyncStyleResource(self)

    @cached_property
    def brand(self) -> AsyncBrandResource:
        from .resources.brand import AsyncBrandResource

        return AsyncBrandResource(self)

    @cached_property
    def industry(self) -> AsyncIndustryResource:
        from .resources.industry import AsyncIndustryResource

        return AsyncIndustryResource(self)

    @cached_property
    def utility(self) -> AsyncUtilityResource:
        from .resources.utility import AsyncUtilityResource

        return AsyncUtilityResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncContextDevWithRawResponse:
        return AsyncContextDevWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContextDevWithStreamedResponse:
        return AsyncContextDevWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ContextDevWithRawResponse:
    _client: ContextDev

    def __init__(self, client: ContextDev) -> None:
        self._client = client

    @cached_property
    def web(self) -> web.WebResourceWithRawResponse:
        from .resources.web import WebResourceWithRawResponse

        return WebResourceWithRawResponse(self._client.web)

    @cached_property
    def ai(self) -> ai.AIResourceWithRawResponse:
        from .resources.ai import AIResourceWithRawResponse

        return AIResourceWithRawResponse(self._client.ai)

    @cached_property
    def style(self) -> style.StyleResourceWithRawResponse:
        from .resources.style import StyleResourceWithRawResponse

        return StyleResourceWithRawResponse(self._client.style)

    @cached_property
    def brand(self) -> brand.BrandResourceWithRawResponse:
        from .resources.brand import BrandResourceWithRawResponse

        return BrandResourceWithRawResponse(self._client.brand)

    @cached_property
    def industry(self) -> industry.IndustryResourceWithRawResponse:
        from .resources.industry import IndustryResourceWithRawResponse

        return IndustryResourceWithRawResponse(self._client.industry)

    @cached_property
    def utility(self) -> utility.UtilityResourceWithRawResponse:
        from .resources.utility import UtilityResourceWithRawResponse

        return UtilityResourceWithRawResponse(self._client.utility)


class AsyncContextDevWithRawResponse:
    _client: AsyncContextDev

    def __init__(self, client: AsyncContextDev) -> None:
        self._client = client

    @cached_property
    def web(self) -> web.AsyncWebResourceWithRawResponse:
        from .resources.web import AsyncWebResourceWithRawResponse

        return AsyncWebResourceWithRawResponse(self._client.web)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithRawResponse:
        from .resources.ai import AsyncAIResourceWithRawResponse

        return AsyncAIResourceWithRawResponse(self._client.ai)

    @cached_property
    def style(self) -> style.AsyncStyleResourceWithRawResponse:
        from .resources.style import AsyncStyleResourceWithRawResponse

        return AsyncStyleResourceWithRawResponse(self._client.style)

    @cached_property
    def brand(self) -> brand.AsyncBrandResourceWithRawResponse:
        from .resources.brand import AsyncBrandResourceWithRawResponse

        return AsyncBrandResourceWithRawResponse(self._client.brand)

    @cached_property
    def industry(self) -> industry.AsyncIndustryResourceWithRawResponse:
        from .resources.industry import AsyncIndustryResourceWithRawResponse

        return AsyncIndustryResourceWithRawResponse(self._client.industry)

    @cached_property
    def utility(self) -> utility.AsyncUtilityResourceWithRawResponse:
        from .resources.utility import AsyncUtilityResourceWithRawResponse

        return AsyncUtilityResourceWithRawResponse(self._client.utility)


class ContextDevWithStreamedResponse:
    _client: ContextDev

    def __init__(self, client: ContextDev) -> None:
        self._client = client

    @cached_property
    def web(self) -> web.WebResourceWithStreamingResponse:
        from .resources.web import WebResourceWithStreamingResponse

        return WebResourceWithStreamingResponse(self._client.web)

    @cached_property
    def ai(self) -> ai.AIResourceWithStreamingResponse:
        from .resources.ai import AIResourceWithStreamingResponse

        return AIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def style(self) -> style.StyleResourceWithStreamingResponse:
        from .resources.style import StyleResourceWithStreamingResponse

        return StyleResourceWithStreamingResponse(self._client.style)

    @cached_property
    def brand(self) -> brand.BrandResourceWithStreamingResponse:
        from .resources.brand import BrandResourceWithStreamingResponse

        return BrandResourceWithStreamingResponse(self._client.brand)

    @cached_property
    def industry(self) -> industry.IndustryResourceWithStreamingResponse:
        from .resources.industry import IndustryResourceWithStreamingResponse

        return IndustryResourceWithStreamingResponse(self._client.industry)

    @cached_property
    def utility(self) -> utility.UtilityResourceWithStreamingResponse:
        from .resources.utility import UtilityResourceWithStreamingResponse

        return UtilityResourceWithStreamingResponse(self._client.utility)


class AsyncContextDevWithStreamedResponse:
    _client: AsyncContextDev

    def __init__(self, client: AsyncContextDev) -> None:
        self._client = client

    @cached_property
    def web(self) -> web.AsyncWebResourceWithStreamingResponse:
        from .resources.web import AsyncWebResourceWithStreamingResponse

        return AsyncWebResourceWithStreamingResponse(self._client.web)

    @cached_property
    def ai(self) -> ai.AsyncAIResourceWithStreamingResponse:
        from .resources.ai import AsyncAIResourceWithStreamingResponse

        return AsyncAIResourceWithStreamingResponse(self._client.ai)

    @cached_property
    def style(self) -> style.AsyncStyleResourceWithStreamingResponse:
        from .resources.style import AsyncStyleResourceWithStreamingResponse

        return AsyncStyleResourceWithStreamingResponse(self._client.style)

    @cached_property
    def brand(self) -> brand.AsyncBrandResourceWithStreamingResponse:
        from .resources.brand import AsyncBrandResourceWithStreamingResponse

        return AsyncBrandResourceWithStreamingResponse(self._client.brand)

    @cached_property
    def industry(self) -> industry.AsyncIndustryResourceWithStreamingResponse:
        from .resources.industry import AsyncIndustryResourceWithStreamingResponse

        return AsyncIndustryResourceWithStreamingResponse(self._client.industry)

    @cached_property
    def utility(self) -> utility.AsyncUtilityResourceWithStreamingResponse:
        from .resources.utility import AsyncUtilityResourceWithStreamingResponse

        return AsyncUtilityResourceWithStreamingResponse(self._client.utility)


Client = ContextDev

AsyncClient = AsyncContextDev
