#%%
import pandas as pd
BASE_PATH = "/home/vladimir/Documents/Estudos/pydata-book/data/"

#%%
# Lendo csv com cabeçalho
df = pd.read_csv(BASE_PATH + "ex1.csv")
df

#%%
# Lendo csv sem cabeçalho
df2 = pd.read_csv(BASE_PATH + "ex2.csv",
                  names=["a", "b", "c", "d", "message"])
df2

#%%
# Lendo csv formando um índice hierárquico
parsed = pd.read_csv(BASE_PATH + "csv_mindex.csv",
                     index_col=["key1", "key2"])
parsed

#%%
# Lendo csv com dados separados por espaços em branco
result = pd.read_csv(BASE_PATH + "ex3.txt",
                     sep="\s+")
result

#%%
# Lendo csv pulando linhas
result2 = pd.read_csv(BASE_PATH + "ex4.csv",
                      skiprows=[0, 2, 3])
result2

#%%
