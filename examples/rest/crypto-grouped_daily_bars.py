from polygon import RESTClient
import pprint

# docs
# https://polygon.theedman.com:8000/docs/crypto/get_v2_aggs_grouped_locale_global_market_crypto__date
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-grouped-daily-aggs

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

grouped = client.get_grouped_daily_aggs(
    "2023-01-09", locale="global", market_type="crypto"
)

# print(grouped)

# pprint (short for "pretty-print") is a module that provides a more human-
# readable output format for data structures.
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(grouped)
