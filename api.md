# Brand

Types:

```python
from brand.dev.types import (
    BrandRetrieveResponse,
    BrandAIProductResponse,
    BrandAIProductsResponse,
    BrandAIQueryResponse,
    BrandIdentifyFromTransactionResponse,
    BrandPrefetchResponse,
    BrandPrefetchByEmailResponse,
    BrandRetrieveByEmailResponse,
    BrandRetrieveByIsinResponse,
    BrandRetrieveByNameResponse,
    BrandRetrieveByTickerResponse,
    BrandRetrieveNaicsResponse,
    BrandRetrieveSimplifiedResponse,
    BrandStyleguideResponse,
    BrandWebScrapeHTMLResponse,
    BrandWebScrapeImagesResponse,
    BrandWebScrapeMdResponse,
    BrandWebScrapeSitemapResponse,
)
```

Methods:

- <code title="get /brand/retrieve">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_response.py">BrandRetrieveResponse</a></code>
- <code title="post /brand/ai/product">client.brand.<a href="./src/brand/dev/resources/brand.py">ai_product</a>(\*\*<a href="src/brand/dev/types/brand_ai_product_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_ai_product_response.py">BrandAIProductResponse</a></code>
- <code title="post /brand/ai/products">client.brand.<a href="./src/brand/dev/resources/brand.py">ai_products</a>(\*\*<a href="src/brand/dev/types/brand_ai_products_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_ai_products_response.py">BrandAIProductsResponse</a></code>
- <code title="post /brand/ai/query">client.brand.<a href="./src/brand/dev/resources/brand.py">ai_query</a>(\*\*<a href="src/brand/dev/types/brand_ai_query_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_ai_query_response.py">BrandAIQueryResponse</a></code>
- <code title="get /brand/transaction_identifier">client.brand.<a href="./src/brand/dev/resources/brand.py">identify_from_transaction</a>(\*\*<a href="src/brand/dev/types/brand_identify_from_transaction_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_identify_from_transaction_response.py">BrandIdentifyFromTransactionResponse</a></code>
- <code title="post /brand/prefetch">client.brand.<a href="./src/brand/dev/resources/brand.py">prefetch</a>(\*\*<a href="src/brand/dev/types/brand_prefetch_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_prefetch_response.py">BrandPrefetchResponse</a></code>
- <code title="post /brand/prefetch-by-email">client.brand.<a href="./src/brand/dev/resources/brand.py">prefetch_by_email</a>(\*\*<a href="src/brand/dev/types/brand_prefetch_by_email_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_prefetch_by_email_response.py">BrandPrefetchByEmailResponse</a></code>
- <code title="get /brand/retrieve-by-email">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_by_email</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_by_email_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_by_email_response.py">BrandRetrieveByEmailResponse</a></code>
- <code title="get /brand/retrieve-by-isin">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_by_isin</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_by_isin_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_by_isin_response.py">BrandRetrieveByIsinResponse</a></code>
- <code title="get /brand/retrieve-by-name">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_by_name</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_by_name_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_by_name_response.py">BrandRetrieveByNameResponse</a></code>
- <code title="get /brand/retrieve-by-ticker">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_by_ticker</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_by_ticker_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_by_ticker_response.py">BrandRetrieveByTickerResponse</a></code>
- <code title="get /brand/naics">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_naics</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_naics_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_naics_response.py">BrandRetrieveNaicsResponse</a></code>
- <code title="get /brand/retrieve-simplified">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_simplified</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_simplified_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_simplified_response.py">BrandRetrieveSimplifiedResponse</a></code>
- <code title="get /brand/styleguide">client.brand.<a href="./src/brand/dev/resources/brand.py">styleguide</a>(\*\*<a href="src/brand/dev/types/brand_styleguide_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_styleguide_response.py">BrandStyleguideResponse</a></code>
- <code title="get /web/scrape/html">client.brand.<a href="./src/brand/dev/resources/brand.py">web_scrape_html</a>(\*\*<a href="src/brand/dev/types/brand_web_scrape_html_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_web_scrape_html_response.py">BrandWebScrapeHTMLResponse</a></code>
- <code title="get /web/scrape/images">client.brand.<a href="./src/brand/dev/resources/brand.py">web_scrape_images</a>(\*\*<a href="src/brand/dev/types/brand_web_scrape_images_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_web_scrape_images_response.py">BrandWebScrapeImagesResponse</a></code>
- <code title="get /web/scrape/markdown">client.brand.<a href="./src/brand/dev/resources/brand.py">web_scrape_md</a>(\*\*<a href="src/brand/dev/types/brand_web_scrape_md_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_web_scrape_md_response.py">BrandWebScrapeMdResponse</a></code>
- <code title="get /web/scrape/sitemap">client.brand.<a href="./src/brand/dev/resources/brand.py">web_scrape_sitemap</a>(\*\*<a href="src/brand/dev/types/brand_web_scrape_sitemap_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_web_scrape_sitemap_response.py">BrandWebScrapeSitemapResponse</a></code>
