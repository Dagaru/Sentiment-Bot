import yfinance as yf

def GetTicker(string):
    company_name = string
    try:
        ticker = yf.Ticker(company_name).info["symbol"]
        tickerPriceAndDividend(ticker)
    except:
        print("error")


def get_ticker_info(ticker_symbol):
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_df = ticker_data.history(period='1d', start='2023-04-01', end='2023-04-25')
    with open('ticker_data.txt', 'w') as f:
        f.write(ticker_df.to_string())
        
def get_ticker_stats(ticker_symbol):
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_info = ticker_data.info
    with open('ticker_stats.txt', 'w') as f:
        for key, value in ticker_info.items():
            f.write(f'{key}: {value}\n')
            
def tickerPriceAndDividend(ticker_symbol):
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_info = ticker_data.info
    # creates a custom dictionary for the specific information wanted
    selectedInfo = {
        'previousClose': ticker_info['regularMarketPreviousClose'],
        'open': ticker_info['regularMarketOpen'],
        'dayLow': ticker_info['regularMarketDayLow'],
        'dayHigh': ticker_info['regularMarketDayHigh'],
        #'dividendRate': ticker_info['dividendRate'],
        #'dividendYield': ticker_info['dividendYield'],
        #'trailingAnnualDividendRate': ticker_info['trailingAnnualDividendRate'],
        #'trailingAnnualDividendYield': ticker_info['trailingAnnualDividendYield'],
        #'exDividendDate': ticker_info['exDividendDate'],
        #'payoutRatio': ticker_info['payoutRatio'],
        #'fiveYearAvgDividendYield': ticker_info['fiveYearAvgDividendYield'],
        'volume': ticker_info['regularMarketVolume']
    }
    
    with open('tickerPriceAndDividend.txt', 'w') as f:
        for key, value in selectedInfo.items():
            f.write(f'{key}: {value}\n')
    return selectedInfo
    