import yfinance as yf
import os
import pandas as pd
import math
from pycoingecko import CoinGeckoAPI

TICKERS = 'PYPL MSFT AMZN AAPL TSLA GOOG'

stock_name = {"tesla": "TSLA",
              "microsoft": "MSFT",
              "paypal": "PYPL",
              "apple": "AAPL",
              "amazon": "AMZN",
              "google": "GOOG"}

# stock price api
def fetch_data(timeframe="1mo", tickers=TICKERS):
    path = os.getcwd()
    data = yf.download(tickers, period=timeframe, group_by='ticker', auto_adjust=True)
    return data

def get_close(dataframe):
    #extracts the closing price from larger set of fetched data
    close = pd.DataFrame()
    for ticker in dataframe.stack().columns.values:
        close[ticker] = dataframe[ticker]['Close']
    return close[~close.index.duplicated(keep='first')] #removes duplicate indexes

def get_today(d):
	res = get_close(fetch_data())
	return res.loc[d]

def get_tickers():
	return TICKERS


# coin price api
cg = CoinGeckoAPI()

def get_crypto_price(targets):
    '''
    id: the name of the coin
    symbol: short name of the coin
    name: official name of the coin
    '''

    # get current price
    price = cg.get_price(ids=targets, vs_currencies="usd")
    return price