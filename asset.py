import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

df=pd.read_csv('C:\\Users\\GG_Mosuru\\Desktop\\hack_illinois_part1.csv')
df.head()
df1=pd.read_csv('C:\\Users\\GG_Mosuru\\Desktop\\hack_illinois_part2.csv')
print(df.head())
print(df1.tail())
dfmerged=pd.concat([df, df1], ignore_index=True)
print(dfmerged.head())
print(dfmerged.tail())
dfsort = (dfmerged.groupby(['AssetID', 'Asset type']).mean().reset_index())
print(dfsort.head())
print(dfsort.tail())
dfsort['Efficiency (liters per hour)'] = dfsort.apply(lambda x: x['Total Fuel (Liters)'] / x['Total Hours'], axis=1)
print(dfsort.head())
print(dfsort.tail())
print(dfsort.info())
print(dfsort.loc[dfsort["Efficiency (liters per hour)"].idxmax()])
print(dfsort.loc[dfsort["Efficiency (liters per hour)"].idxmin()])


sample = dfsort.sample(50)
source = ColumnDataSource(sample)


output_file("gg.html")

p = figure()
p.circle(x='Total Fuel (Liters)', y='Total Hours',
         source=source,
         size=10, color='green')

p.title.text = 'Assets and their fuel consumption'
p.xaxis.axis_label = 'Average fuel consumed over a year in Liters'
p.yaxis.axis_label = 'Average time used over a year in hours'

hover = HoverTool()
hover.tooltips=[
    ('Asset ID', '@AssetID'),
    ('Asset Type', '@{Asset type}'),
    ('Average fuel level', '@{Fuel Level (%)}')
]

p.add_tools(hover)

show(p)