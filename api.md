# Brand

Types:

```python
from brand.dev.types import (
    BrandRetrieveResponse,
    BrandAIQueryResponse,
    BrandIdentifyFromTransactionResponse,
    BrandPrefetchResponse,
    BrandRetrieveByTickerResponse,
    BrandRetrieveNaicsResponse,
    BrandSearchResponse,
)
```

Methods:

- <code title="get /brand/retrieve">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_response.py">BrandRetrieveResponse</a></code>
- <code title="post /brand/ai/query">client.brand.<a href="./src/brand/dev/resources/brand.py">ai_query</a>(\*\*<a href="src/brand/dev/types/brand_ai_query_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_ai_query_response.py">BrandAIQueryResponse</a></code>
- <code title="get /brand/transaction_identifier">client.brand.<a href="./src/brand/dev/resources/brand.py">identify_from_transaction</a>(\*\*<a href="src/brand/dev/types/brand_identify_from_transaction_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_identify_from_transaction_response.py">BrandIdentifyFromTransactionResponse</a></code>
- <code title="post /brand/prefetch">client.brand.<a href="./src/brand/dev/resources/brand.py">prefetch</a>(\*\*<a href="src/brand/dev/types/brand_prefetch_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_prefetch_response.py">BrandPrefetchResponse</a></code>
- <code title="get /brand/retrieve-by-ticker">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_by_ticker</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_by_ticker_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_by_ticker_response.py">BrandRetrieveByTickerResponse</a></code>
- <code title="get /brand/naics">client.brand.<a href="./src/brand/dev/resources/brand.py">retrieve_naics</a>(\*\*<a href="src/brand/dev/types/brand_retrieve_naics_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_retrieve_naics_response.py">BrandRetrieveNaicsResponse</a></code>
- <code title="get /brand/search">client.brand.<a href="./src/brand/dev/resources/brand.py">search</a>(\*\*<a href="src/brand/dev/types/brand_search_params.py">params</a>) -> <a href="./src/brand/dev/types/brand_search_response.py">BrandSearchResponse</a></code>
