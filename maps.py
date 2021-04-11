from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool
from bokeh.plotting import gmap
import pandas as pd

# LOAD THE DATA
data = pd.read_csv("testdata.csv")
# coordinates = data[['GPS Lattitude', 'GPS Longitude']]
psource = ColumnDataSource(data)
# print(psource)

# SORTING/CLASSIFICATION FUNCTION





# SET TOOLTIPS
hover = HoverTool(
    tooltips=[
        ('Asset', '@AssetID'),
        ('Asset Type', '@{Asset type}'),
        ('Date', '@Date'),

    ])

# LOAD GOOGLE MAPS AND CUSTOMIZE IT
map_options = GMapOptions(lat=37.501627, lng=-79.868284, map_type="hybrid", zoom=16)
p = gmap("", map_options, title="Fleet Tracker", tools='pan,wheel_zoom,reset', toolbar_location="right")
p.add_tools(hover)



p.circle(y="GPS Lattitude", x="GPS Longitude", size=13, fill_color="red", fill_alpha=0.8, source=psource)
# p.multi_line('GPS Longitude','GPS Lattitude', source=psource, color='red', line_width=3)


output_file(filename="./templates/maps.html", title="Static HTML file")

# show the results
show(p)
