from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
import pandas as pd

data = pd.read_csv("testdata.csv")
coordinates = data[['GPS Lattitude', 'GPS Longitude']]
psource = ColumnDataSource(coordinates)

map_options = GMapOptions(lat=37.501627, lng=-79.868284, map_type="hybrid", zoom=16)
p = gmap("", map_options, title="Fleet Tracker")

#print(coordinates.head()

#print(psource)

p.circle(y = "GPS Lattitude", x = "GPS Longitude", size=13, fill_color="red", fill_alpha=0.8, source=psource)


output_file(filename="./templates/maps.html", title="Static HTML file")

# show the results
show(p)

