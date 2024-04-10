import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

import smtplib
from   email.mime.text import MIMEText
import config

import schedule
import time

#%% Weekly Projection Menu
ativos      = ['ABEV3.SA', 'EQTL3.SA', 'VIVT3.SA', 'VALE3.SA']
target_gain = [13.45, 35.04, 56.62, 65.68]
target_loss = [11.01, 28.67, 46.32, 53.74]
weights     = [0.25, 0.25, 0.25, 0.25]
paid        = [12.19, 32.24, 51.58, 62.56]
my_wallet   = 267.31
mkt_close   = "17:00"


prices      = []  #This variables are for the email only.
sell        = []
maintain    = []

#%% Functions

def print_start_time():
    start_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print("\n\nIteration running at:", start_time)
    return start_time

def sell_check ():
    for i in ativos:
        tick = yf.Ticker(i).info
        instant_price = tick['currentPrice']
        prices.append(instant_price)

    for i in range(len(ativos)):
        if (prices[i] <= target_loss[i]):
            print(f"You should LOSS sell {ativos[i]} at R$ {prices[i]}\n")
            sell.append(ativos[i]) #se condiçao verdadeira, adiciona ativo na lista

        elif (prices[i]>=target_gain[i]):
            print(f"You should GAIN sell {ativos[i]} at R$ {prices[i]}\n")
            sell.append(ativos[i]) #se condiçao verdadeira, adiciona ativo na lista
            
        else:
            ratio = ((prices[i] - paid[i])/paid[i])*100
            print(f"{ativos[i]}: R$ {prices[i]}\n    No action required\n    Current ratio: {ratio:.3f}%")
            maintain.append(ativos[i])

def send_mail(status):
    subject     = "Vender Ações Semanais"
    actions_str = '\n '.join(status)
    body        = f"As seguintes ações atingiram o preço desejado:\n {actions_str}\nVENDER é sugerido!" #add desired message
    sender      = config.SENDER     #add desired email
    recipients  = config.RECIPIENTS #add desired email
    password    = config.PASSWORD   #add Google 16 digit app code

    msg             = MIMEText(body)
    msg['Subject']  = subject
    msg['From']     = sender
    msg['To']       = ', '.join(recipients)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    
    print("Message sent!")

def calculate_shares(total_balance, percentages, stock_prices):
    # Calculate the total amount of money available for each stock
    total_allocation = [total_balance * percentage for percentage in percentages]
    
    # Calculate the number of shares you can buy for each stock
    shares_to_buy = [int(allocation / price) for allocation, price in zip(total_allocation, stock_prices)]
    
    total_spent = sum([shares * price for shares, price in zip(shares_to_buy, stock_prices)])
    remaining_balance = total_balance - total_spent

    print("Number of individual shares:\n")
    for i in range(len(ativos)):
        print(f"{ativos[i]}: {shares_to_buy[i]} share(s)")
    print(f"\nRemaining balance: R$ {remaining_balance:.2f}")
    return shares_to_buy
#%% ###################### Main #################################

def execution():
    print("Main loop started...\n")
    print_start_time()
    #Check selling position
    sell_check()

    #Indicates how many shares can be bought with weekly balance
    calculate_shares(my_wallet, weights, prices)

    #Checks if there is a Stock within the SELL range. If yes, send warning email.
    if (sell): #checa se sell é vazio
        send_mail(sell) 

    #Makes sure, the variable is ready for another iteration
    sell.clear()