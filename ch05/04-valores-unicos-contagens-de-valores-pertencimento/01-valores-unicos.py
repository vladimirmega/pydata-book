#%%
import pandas as pd

#%%
obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])

#%%
# Retorna os valores únicos ordenados
uniques = sorted(obj.unique())
uniques

#%%
# Contagem (por padrão ordem desc)
obj.value_counts()

#%%
# Filtro baseado em lista com retorno booleano
mask = obj.isin( ["b", "c"])
obj[mask]
