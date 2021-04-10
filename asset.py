import pandas as pd
import numpy as np
df=pd.read_csv('C:\\Users\\GG_Mosuru\\Desktop\\hack_illinois_part1.csv')
df.head()
df1=pd.read_csv('C:\\Users\\GG_Mosuru\\Desktop\\hack_illinois_part2.csv')
print(df.head())
print(df1.tail())
dfmerged=pd.concat([df, df1], ignore_index=True)
print(dfmerged.head())
print(dfmerged.tail())
dfsort = (dfmerged.groupby(['AssetID', 'Asset type']).mean())
print(dfsort.head())
dfsort['Efficiency (liters per hour)'] = dfsort.apply(lambda x: x['Total Fuel (Liters)'] / x['Total Hours'], axis=1)
print(dfsort.head())