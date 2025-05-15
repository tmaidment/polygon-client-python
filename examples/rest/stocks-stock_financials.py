from polygon import RESTClient

# docs
# https://polygon.theedman.com:8000/docs/stocks/get_vx_reference_financials
# https://polygon-api-client.readthedocs.io/en/latest/vX.html#list-stock-financials

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

financials = []
for f in client.vx.list_stock_financials("AAPL", filing_date="2024-11-01"):
    financials.append(f)

    # get diluted_earnings_per_share
    # print(f.financials.income_statement.diluted_earnings_per_share)

    # get net_income_loss
    # print(f.financials.income_statement.net_income_loss)

print(financials)
