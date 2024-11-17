#%%
import pandas as pd

#%%
price = pd.read_pickle('/home/vladimir/Documents/Estudos/pydata-book/ch05/03-correlacao-e-covariancia/data/yahoo_price.pkl')
price.head()

#%%
volume = pd.read_pickle('/home/vladimir/Documents/Estudos/pydata-book/ch05/03-correlacao-e-covariancia/data/yahoo_volume.pkl')
volume.head()

#%%
# Alterações percentuais nos preços
# Para cada linha, ele calcula a mudança percentual em relação à linha anterior:
# Variação Percentual = (valor atual - valor anterior) / valor anterior
returns = price.pct_change()
returns.tail()

#%%
# Correlação entre a variação percentual
# Calcula o coeficiente de correlação de Pearson entre as duas séries.
# Esse coeficiente mede a relação linear entre duas variáveis e varia entre -1 e 1:
# Magnitudes de Correlação:
# 0 a 0.3: Fraca.
# 0.3 a 0.7: Moderada.
# 0.7 a 1: Forte.
returns['MSFT'].corr(returns['IBM'])

#%%
# Covariância:
# A covariância mede como duas variáveis se movem em relação uma à outra.
# Se for positiva, significa que as variáveis tendem a se mover na mesma direção (quando uma aumenta, a outra tende a aumentar também).
# Se for negativa, significa que as variáveis tendem a se mover em direções opostas (quando uma aumenta, a outra tende a diminuir).
returns['MSFT'].cov(returns['IBM'])

#%%
# Calcula o grau de relação linear (correlação) entre os retornos percentuais dos ativos
returns.corr()
#%%
# Calcula a matriz de covariância, que mede como os retornos percentuais dos ativos variam juntos
returns.cov()


#%%
# O mét.odo returns.corrwith(returns['IBM']) calcula a correlação de Pearson entre cada coluna do DataFrame
# returns e a série returns['IBM'].
returns.corrwith(returns['IBM'])

#%%
# calcula a correlação de Pearson entre as colunas do DataFrame returns (retornos percentuais) e as
# colunas do DataFrame volume (volumes de negociação de cada ativo).
returns.corrwith(volume)
