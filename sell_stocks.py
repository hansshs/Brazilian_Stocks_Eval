import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import ssl

import smtplib
from email.mime.text import MIMEText
import config

#%% Weekly Wallet
ativos      = ['CSMG3.SA', 'EQTL3.SA', 'RAIL3.SA', 'VALE3.SA']
target_gain = [22.20, 36.52, 24.27, 65.67]
target_loss = [18.16, 29.88, 19.85, 53.73]

prices      = []
sell        = []
maintain    = []

#%% Functions
def sell_check ():
    for i in ativos:
        tick = yf.Ticker(i).info
        instant_price = tick['currentPrice']
        prices.append(instant_price)

    for i in range(len(ativos)):
        if (prices[i] <= target_loss[i]):
            print(f"You should LOSS sell {ativos[i]} at R$ {prices[i]}")
            sell.append(ativos[i])

        elif (prices[i]>=target_gain[i]):
            print(f"You should GAIN sell {ativos[i]} at R$ {prices[i]}")
            sell.append(ativos[i])
            
        else:
            print(f"{ativos[i]}: R$ {prices[i]}\n    No action required\n")
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

#%%Main
sell_check()
send_mail(sell)
#Checks if there is a Stock within the SELL range. If yes, send warning email.
if (sell):
    send_mail(sell)

#Makes sure, the variable is ready for another iteration
sell = []