
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statistics as sts
import yfinance as yf
from tratar_dados import tratar_dados
yf.pdr_override()
 
ibov = web.get_data_yahoo("^BVSP", period="5y")["Adj Close"]
ibov = pd.DataFrame(ibov)
tratar_dados(ibov)
ibov_normalizado = (ibov / ibov.iloc[0])*100
