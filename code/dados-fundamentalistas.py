
import fundamentus
import pandas as pd
import matplotlib.pyplot as plt


tickers = ["VALE3", 
           "ITSA4",  
           "WEGE3",
           "PETR4",
           "BBAS3"]

indicadores_fundamentalistas = fundamentus.get_resultado()

indicadores_carteira = pd.DataFrame(columns=['cotacao', 'pl', 'pvp', 'psr', 'dy', 'pa', 'pcg', 'pebit', 'pacl',
       'evebit', 'evebitda', 'mrgebit', 'mrgliq', 'roic', 'roe', 'liqc',
       'liq2m', 'patrliq', 'divbpatr', 'c5y'])

for ticker in tickers:
    indicadores_carteira.loc[ticker] = indicadores_fundamentalistas.loc[ticker]

indicadores_carteira.reset_index(inplace=True)
indicadores_carteira.rename(columns={'index': 'ticker'}, inplace=True)
indicadores_carteira
