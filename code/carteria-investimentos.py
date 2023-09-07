
import pandas as pd
import numpy as np
import pandas_datareader.data as web
import statistics  as sts

import yfinance as yf
yf.pdr_override()


def tratar_dados(df: pd.DataFrame) -> None:
    """
    Esta função realiza o pré-processamento dos dados no DataFrame fornecido.

    Args:
        df (pd.DataFrame): O DataFrame a ser processado.

    Returns:
        None
    """
    # Remove duplicatas do DataFrame
    df.drop_duplicates(inplace=True)
    
    # Preenche valores ausentes em cada coluna com a mediana
    for coluna in df.columns:
        df[coluna] = df[coluna].fillna(df[coluna].median())


tickers = ["VALE3.SA", "ITSA4.SA", "WEGE3.SA", "PETR4.SA", "BBAS3.SA"]

carteria = web.get_data_yahoo(tickers, period="5y")["Adj Close"]
carteria

ibov = web.get_data_yahoo("^BVSP", period="5y")["Adj Close"]
ibov = pd.DataFrame(ibov)

tratar_dados(carteria)
tratar_dados(ibov)

carteria_normalizada = (carteria / carteria.iloc[0])*(100/(carteria.columns.size))
carteria_normalizada["saldo"] =  carteria_normalizada.sum(axis=1)
carteria_normalizada.reset_index(inplace=True)

ibov_normalizado = (ibov / ibov.iloc[0])*100
ibov_normalizado.reset_index(inplace=True)
