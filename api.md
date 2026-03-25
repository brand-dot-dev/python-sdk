# Web

Types:

```python
from context.dev.types import (
    WebScreenshotResponse,
    WebWebScrapeHTMLResponse,
    WebWebScrapeImagesResponse,
    WebWebScrapeMdResponse,
    WebWebScrapeSitemapResponse,
)
```

Methods:

- <code title="get /brand/screenshot">client.web.<a href="./src/context/dev/resources/web.py">screenshot</a>(\*\*<a href="src/context/dev/types/web_screenshot_params.py">params</a>) -> <a href="./src/context/dev/types/web_screenshot_response.py">WebScreenshotResponse</a></code>
- <code title="get /web/scrape/html">client.web.<a href="./src/context/dev/resources/web.py">web_scrape_html</a>(\*\*<a href="src/context/dev/types/web_web_scrape_html_params.py">params</a>) -> <a href="./src/context/dev/types/web_web_scrape_html_response.py">WebWebScrapeHTMLResponse</a></code>
- <code title="get /web/scrape/images">client.web.<a href="./src/context/dev/resources/web.py">web_scrape_images</a>(\*\*<a href="src/context/dev/types/web_web_scrape_images_params.py">params</a>) -> <a href="./src/context/dev/types/web_web_scrape_images_response.py">WebWebScrapeImagesResponse</a></code>
- <code title="get /web/scrape/markdown">client.web.<a href="./src/context/dev/resources/web.py">web_scrape_md</a>(\*\*<a href="src/context/dev/types/web_web_scrape_md_params.py">params</a>) -> <a href="./src/context/dev/types/web_web_scrape_md_response.py">WebWebScrapeMdResponse</a></code>
- <code title="get /web/scrape/sitemap">client.web.<a href="./src/context/dev/resources/web.py">web_scrape_sitemap</a>(\*\*<a href="src/context/dev/types/web_web_scrape_sitemap_params.py">params</a>) -> <a href="./src/context/dev/types/web_web_scrape_sitemap_response.py">WebWebScrapeSitemapResponse</a></code>

# AI

Types:

```python
from context.dev.types import AIAIQueryResponse, AIExtractProductResponse, AIExtractProductsResponse
```

Methods:

- <code title="post /brand/ai/query">client.ai.<a href="./src/context/dev/resources/ai.py">ai_query</a>(\*\*<a href="src/context/dev/types/ai_ai_query_params.py">params</a>) -> <a href="./src/context/dev/types/ai_ai_query_response.py">AIAIQueryResponse</a></code>
- <code title="post /brand/ai/product">client.ai.<a href="./src/context/dev/resources/ai.py">extract_product</a>(\*\*<a href="src/context/dev/types/ai_extract_product_params.py">params</a>) -> <a href="./src/context/dev/types/ai_extract_product_response.py">AIExtractProductResponse</a></code>
- <code title="post /brand/ai/products">client.ai.<a href="./src/context/dev/resources/ai.py">extract_products</a>(\*\*<a href="src/context/dev/types/ai_extract_products_params.py">params</a>) -> <a href="./src/context/dev/types/ai_extract_products_response.py">AIExtractProductsResponse</a></code>

# Style

Types:

```python
from context.dev.types import StyleExtractFontsResponse, StyleExtractStyleguideResponse
```

Methods:

- <code title="get /brand/fonts">client.style.<a href="./src/context/dev/resources/style.py">extract_fonts</a>(\*\*<a href="src/context/dev/types/style_extract_fonts_params.py">params</a>) -> <a href="./src/context/dev/types/style_extract_fonts_response.py">StyleExtractFontsResponse</a></code>
- <code title="get /brand/styleguide">client.style.<a href="./src/context/dev/resources/style.py">extract_styleguide</a>(\*\*<a href="src/context/dev/types/style_extract_styleguide_params.py">params</a>) -> <a href="./src/context/dev/types/style_extract_styleguide_response.py">StyleExtractStyleguideResponse</a></code>

# Brand

Types:

```python
from context.dev.types import (
    BrandRetrieveResponse,
    BrandIdentifyFromTransactionResponse,
    BrandRetrieveByEmailResponse,
    BrandRetrieveByIsinResponse,
    BrandRetrieveByNameResponse,
    BrandRetrieveByTickerResponse,
    BrandRetrieveSimplifiedResponse,
)
```

Methods:

- <code title="get /brand/retrieve">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve</a>(\*\*<a href="src/context/dev/types/brand_retrieve_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_response.py">BrandRetrieveResponse</a></code>
- <code title="get /brand/transaction_identifier">client.brand.<a href="./src/context/dev/resources/brand.py">identify_from_transaction</a>(\*\*<a href="src/context/dev/types/brand_identify_from_transaction_params.py">params</a>) -> <a href="./src/context/dev/types/brand_identify_from_transaction_response.py">BrandIdentifyFromTransactionResponse</a></code>
- <code title="get /brand/retrieve-by-email">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve_by_email</a>(\*\*<a href="src/context/dev/types/brand_retrieve_by_email_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_by_email_response.py">BrandRetrieveByEmailResponse</a></code>
- <code title="get /brand/retrieve-by-isin">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve_by_isin</a>(\*\*<a href="src/context/dev/types/brand_retrieve_by_isin_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_by_isin_response.py">BrandRetrieveByIsinResponse</a></code>
- <code title="get /brand/retrieve-by-name">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve_by_name</a>(\*\*<a href="src/context/dev/types/brand_retrieve_by_name_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_by_name_response.py">BrandRetrieveByNameResponse</a></code>
- <code title="get /brand/retrieve-by-ticker">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve_by_ticker</a>(\*\*<a href="src/context/dev/types/brand_retrieve_by_ticker_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_by_ticker_response.py">BrandRetrieveByTickerResponse</a></code>
- <code title="get /brand/retrieve-simplified">client.brand.<a href="./src/context/dev/resources/brand.py">retrieve_simplified</a>(\*\*<a href="src/context/dev/types/brand_retrieve_simplified_params.py">params</a>) -> <a href="./src/context/dev/types/brand_retrieve_simplified_response.py">BrandRetrieveSimplifiedResponse</a></code>

# Industry

Types:

```python
from context.dev.types import IndustryRetrieveNaicsResponse
```

Methods:

- <code title="get /brand/naics">client.industry.<a href="./src/context/dev/resources/industry.py">retrieve_naics</a>(\*\*<a href="src/context/dev/types/industry_retrieve_naics_params.py">params</a>) -> <a href="./src/context/dev/types/industry_retrieve_naics_response.py">IndustryRetrieveNaicsResponse</a></code>

# Utility

Types:

```python
from context.dev.types import UtilityPrefetchResponse, UtilityPrefetchByEmailResponse
```

Methods:

- <code title="post /brand/prefetch">client.utility.<a href="./src/context/dev/resources/utility.py">prefetch</a>(\*\*<a href="src/context/dev/types/utility_prefetch_params.py">params</a>) -> <a href="./src/context/dev/types/utility_prefetch_response.py">UtilityPrefetchResponse</a></code>
- <code title="post /brand/prefetch-by-email">client.utility.<a href="./src/context/dev/resources/utility.py">prefetch_by_email</a>(\*\*<a href="src/context/dev/types/utility_prefetch_by_email_params.py">params</a>) -> <a href="./src/context/dev/types/utility_prefetch_by_email_response.py">UtilityPrefetchByEmailResponse</a></code>
