import yfinance as yf

def download_prices(tickers, start='2015-01-01'):

    data = yf.download(
        tickers,
        start=start
    )

    prices = data["Close"]

    return prices