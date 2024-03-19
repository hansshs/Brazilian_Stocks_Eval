import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import ssl

import smtplib
from email.mime.text import MIMEText

#%% Weekly Wallet
ativos      = ['CSMG3.SA', 'EQTL3.SA', 'RAIL3.SA', 'VALE3.SA']
target_gain = [22.20, 36.52, 24.27, 65.67]
target_loss = [18.16, 29.88, 19.85, 53.73]
prices      = []
sell        = []
maintain    = []

#%% Functions
def actions ():
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

def new_test():
    subject     = "Vender Ações Semanais"
    body        = f"As ações {sell} atingiram o preço desejado. VENDER é sugerido!" #add desired message
    sender      = "abcd@gmail.com"  #add desired email
    recipients  = ["abcd@gmail.com"] #add desired email
    password    = "1234 5678 1234 5678" #add Google 16 digit app code

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    
    print("Message sent!")

#%%Main
actions()
if sell:
    new_test()

sell = []