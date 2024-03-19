import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

#%% Weekly Wallet
ativos      = ['CSMG3.SA', 'EQTL3.SA', 'RAIL3.SA', 'VALE3.SA']
target_gain = [22.20, 36.52, 24.27, 65.67]
target_loss = [18.16, 29.88, 19.85, 53.73]
prices=[]

#%% FUnctions
def actions (ativos, current_price, loss, gain):
    for i in range(len(ativos)):
        if (current_price[i] <= loss[i]):
            print(f"You should LOSS sell {ativos[i]} at R$ {current_price[i]}")
        elif (current_price[i]>=gain[i]):
            print(f"You should GAIN sell {ativos[i]} at R$ {current_price[i]}")
        else:
            print(f"{ativos[i]}: R$ {current_price[i]}\n    No action required\n")

#%% Create DF with assets info
for i in ativos:
    tick = yf.Ticker(i).info
    current_price = tick['currentPrice']
    prices.append(current_price)

actions(ativos, prices, target_loss, target_gain)