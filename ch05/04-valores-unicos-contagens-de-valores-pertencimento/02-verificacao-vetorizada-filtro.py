#%%
import pandas as pd

#%%
obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])

#%%
# Filtro baseado em lista com retorno booleano
mask = obj.isin( ["b", "c"])
obj[mask]
