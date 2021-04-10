from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

map_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=11)

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
p = gmap("", map_options, title="Austin")

source = ColumnDataSource(
    data=dict(lat=[ 30.29,  30.20,  30.29],
              lon=[-97.70, -97.74, -97.78])
)

#p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)

output_file(filename="./templates/maps.html", title="Static HTML file")

# show the results
show(p)