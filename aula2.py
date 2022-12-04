import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
#%% Define Assets and time interval
ativos  = ['CIEL3.SA', 'COGN3.SA', 'EGIE3.SA', 'GFSA3.SA', 'GRND3.SA', 'ITSA4.SA', 'TAEE11.SA', 'WEGE3.SA']
inicio  = '2021-01-01'
fim     = '2022-11-29'

df      = pd.DataFrame()
#%% Create DF with assets info
for i in ativos:
    df[i] = yf.download(i, start=inicio, end=fim)['Adj Close']

#%% DF Plot
df.plot()

#%% Normal
normal = df/df.iloc[0]
normal.plot(title = 'Normal Returns Comparison').set_ylabel('Normalized Return')

#%% Daily Return
daily_ret = df.pct_change()
daily_ret.dropna(inplace=True)
daily_ret.plot(grid= 'True', title = "Daily Returns").set_ylabel("Returns")