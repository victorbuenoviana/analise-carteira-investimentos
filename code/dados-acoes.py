
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import statistics  as sts
from tratar_dados import tratar_dados
import yfinance as yf


yf.pdr_override()

tickers = ["VALE3.SA", 
           "ITSA4.SA",  
           "WEGE3.SA",
           "PETR4.SA",
           "BBAS3.SA"]

carteria = web.get_data_yahoo(tickers, period="5y")["Adj Close"]
tratar_dados(carteria)
carteria["saldo"] = carteria.sum(axis=1)
carteria_normalizada = ((carteria / carteria.iloc[0])*100)
carteria_normalizada.reset_index(inplace=True)
