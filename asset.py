print("Hello")
import pandas as pd
import numpy as np
df=pd.read_csv('C:\\Users\\GG_Mosuru\\Desktop\\hack_illinois_part1.csv')
df.head()
df1=pd.read_csv('C:\\Users\\GG_Mosuru\\Desktop\\hack_illinois_part2.csv')
df1.head()
dfmerged=pd.merge(left=df, right=df1, how='outer', left_on='AssetID', right_on='AssetID')