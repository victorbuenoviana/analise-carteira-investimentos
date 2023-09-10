
import pandas as pd
import numpy as np
import statistics  as sts
import matplotlib.pyplot as plt
from datetime import datetime
from datetime import timedelta
from bcb import currency
from bcb import sgs
from tratar_dados import tratar_dados


data_atual = str(datetime.now().strftime("%Y-%m-%d"))

dolar = currency.get(['USD'], start='1994-07-01', end=data_atual, side='both')
ipca = sgs.get({'ipca': 433}, start = '1994-07-01', end=data_atual)
igpm = sgs.get({'igp-m': 189}, start = '1994-07-01', end=data_atual)
selic = sgs.get({'selic':432}, start = '1994-07-01', end=data_atual)



