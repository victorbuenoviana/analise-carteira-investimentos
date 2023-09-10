
#pip install pandas
import pandas as pd
#pip install numpy
import numpy as np
# pip install statistics
import statistics  as sts


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

if __name__ == '__main__':
    pass