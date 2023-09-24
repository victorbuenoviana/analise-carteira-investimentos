
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
        df[coluna] = df[coluna].ffill()


carteria = web.get_data_yahoo(tickers, period="5y")["Adj Close"]
carteria["saldo"] = carteria.sum(axis=1)
carteria_normalizada = ((carteria / carteria.iloc[0])*100)
carteria_normalizada.reset_index(inplace=True)
tratar_dados(carteria_normalizada)
