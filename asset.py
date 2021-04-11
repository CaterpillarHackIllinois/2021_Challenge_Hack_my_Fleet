import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.models.widgets import Div
from bokeh.layouts import widgetbox
from bokeh.transform import factor_cmap
from bokeh.layouts import column

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

print(dfsort["Asset type"].unique())

sample = dfsort.sample(1000)
source = ColumnDataSource(sample)
index_cmap = factor_cmap('Asset type', palette=['red', 'blue', 'green', 'navy', 'yellow', 'olive'],
                         factors=sorted(dfsort['Asset type'].unique()))

output_file("gg.html")

p = figure()
p.circle(x='Total Fuel (Liters)', y='Total Hours',
         source=dfsort,
         size=5, fill_color=index_cmap, legend='Asset type')

p.title.text = 'Assets and their fuel consumption'
p.xaxis.axis_label = 'Average fuel consumed over a year in Liters'
p.yaxis.axis_label = 'Average time used over a year in hours'

hover = HoverTool()
hover.tooltips=[
    ('Asset ID', '@AssetID'),
    ('Asset Type', '@{Asset type}'),
    ('Average fuel level', '@{Fuel Level (%)}'),
    ('Efficiency', '@{Efficiency (liters per hour)}')
]

p.add_tools(hover)
p.legend.location = "top_left"

div_exp00 = Div(
            text=""" <b>FUEL EFFICIENCY GRAPH</b>
            """,
            width=300, style={'font-size': '100%'})
div_exp01 = Div(
            text=""" Mileage is a key factor when it comes to analysing the performance of motor vehicles, for 
            heavy duty vehicles the fuel consumed over time plays a similar role.
            The graph shows the average fuel consumption for each asset in the fleet in a year. 
            Each sphere represents an unique asset and the slope of the graph gives the average fuel consumption
            per hour. This data allows the fleet manager to identify the most efficient assets in the fleet. The asset
            can be closely inspected by zooming in and hovering over the spheres.""",
            width=300)

show(column(div_exp00,div_exp01,p))
