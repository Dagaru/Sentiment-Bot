import yfinance as yf

msft = yf.Ticker('msft')
print("day high: " + str(msft.fast_info.day_high))
print("day low: " + str(msft.fast_info.day_low))
print("day open: " + str(msft.fast_info.open))
print("fifty Day Average: " + str(msft.fast_info.fifty_day_average))
