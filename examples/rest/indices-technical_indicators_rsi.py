from polygon import RESTClient

# docs
# https://polygon.theedman.com:8000/docs/indices/get_v1_indicators_rsi__indicesticker
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

rsi = client.get_rsi(
    ticker="I:SPX",
    timespan="day",
    window=14,
    series_type="close",
)

print(rsi)
