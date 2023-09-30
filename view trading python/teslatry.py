from tradingview_ta import TA_Handler, Interval, Exchange

tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY
)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}

# {'RECOMMENDATION': 'SELL', 'BUY': 3, 'SELL': 14, 'NEUTRAL': 9} 
# {'RECOMMENDATION': 'SELL', 'BUY': 3, 'SELL': 14, 'NEUTRAL': 9}