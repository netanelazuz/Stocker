import requests, os
import yfinance as yf


def get_current_price(ticker):
    tick = yf.Ticker(ticker).info
    


print(get_current_price("AAPL"))


