#%%
import pandas as pd

#%%
data = pd.DataFrame({"Qu1": [1, 3, 4, 3, 4],
                     "Qu2": [2, 3, 1, 2, 3],
                     "Qu3": [1, 5, 2, 4, 4]})
data

#%%
# Calcular contagem de valores para uma única coluna
data["Qu1"].value_counts().sort_index()

#%%
# Calculo para toads as colunas
result = data.apply(pd.value_counts).fillna(0)
result

