#%%
# 
import pandas as pd

p = "D:\\bianmu_changguang\\JL1.csv"

df = pd.read_csv(p)

print(df.info())
#%% 
df.cloud_percent.hist()
# %%
