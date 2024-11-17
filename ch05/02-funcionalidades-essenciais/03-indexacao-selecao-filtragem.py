#%%
import pandas as pd
import numpy as np

#%%
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
obj

#%%
obj['b']

#%%
obj[1]

#%%
obj[['b', 'a', 'd']]

#%%
obj[[1, 3]]

#%%
obj[obj < 2]

#%%
# Selecionando usando loc (usado para rótulos)
obj.loc[['b', 'a', 'd']]

#%%
# Selecionando usando iloc (usado para inteiros)
obj.iloc[[1, 3]]

