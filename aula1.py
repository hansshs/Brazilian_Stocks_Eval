#%%Libraries
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sn
#%%Opening .xlsx
model = pd.read_excel("modelo_df.xlsx")
#%% Creating DataFrames for each tick
abev3 = model[(model.Ativo == 'ABEV3.SA') & (model.Parametro == 'Adj Close')]
prio3 =  model[(model.Ativo == 'PRIO3.SA') & (model.Parametro == 'Adj Close')]
#%%Plotting Desired Info
plt.plot(abev3.Data, abev3.Valor, color = 'b')
plt.plot(prio3.Data, prio3.Valor, color = 'orange')
plt.title('Valores de Ações')
plt.xlabel('Data')
plt.ylabel('Valor [R$]')
plt.legend(['ABEV3', 'PRIO3'])
plt.show()
#%% Calculating and Plotting Daily Change of the Prices
abev3['Retornos'] = abev3.Valor.pct_change()
prio3['Retornos'] = prio3.Valor.pct_change()

plt.plot(abev3.Data, abev3.Retornos)
plt.plot(prio3.Data, prio3.Retornos)
plt.title('Retornos de Ações')
plt.xlabel('Data')
plt.ylabel('Retorno [%]')
plt.legend(['ABEV3', 'PRIO3'])
plt.show()