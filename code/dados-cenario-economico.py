
import pandas as pd
from datetime import datetime
from bcb import currency
from bcb import sgs


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


data_atual = str(datetime.now().strftime("%Y-%m-%d"))

dolar = currency.get(['USD'], start='1994-07-01', end=data_atual, side='both')
tratar_dados(dolar)
dolar.reset_index(inplace=True)

ipca = sgs.get({'ipca': 433}, start = '1994-07-01', end=data_atual)
tratar_dados(ipca)
ipca.reset_index(inplace=True)

igpm = sgs.get({'igp-m': 189}, start = '1994-07-01', end=data_atual)
tratar_dados(igpm)
igpm.reset_index(inplace=True)

selic = sgs.get({'selic':432}, start = '1994-07-01', end=data_atual)
tratar_dados(selic)
selic.reset_index(inplace=True)
