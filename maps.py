from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool, CheckboxButtonGroup, CustomJS, Select
from bokeh.plotting import gmap, curdoc
import pandas as pd

# LOAD THE DATA
data = pd.read_csv("testdata.csv")
# coordinates = data[['GPS Lattitude', 'GPS Longitude']]
psource = ColumnDataSource(data)
# print(psource)

bokeh_doc = curdoc()

# LABELS = ["Option 1", "Option 2", "Option 3"]
# checkbox_button_group = CheckboxButtonGroup(labels=LABELS, active=[0, 1])
# checkbox_button_group.js_on_click(CustomJS(code="""
#     console.log('checkbox_button_group: active=' + this.active, this.toString())
# """))

select = Select(title="Tracking Option:", value="Entire Fleet", options=["Entire Fleet", "Motor Graders", "Excavators", "Off Highway Truck"])
select.js_on_change("value", CustomJS(code="""
    console.log('select: value=' + this.value, this.toString())
"""))

# SORTING/CLASSIFICATION FUNCTION
def update(attr, old, new):
    if new == "Entire Fleet":
        dataset = data

    elif new == "Excavators":
        dataset = data[data['Asset type'] == 'Excavator']
        print(dataset)

    else:
        dataset = data[['GPS Lattitude', 'GPS Longitude']]


    psource.data = dataset

select.on_change("value", update)

# SET TOOLTIPS
hover = HoverTool(
    tooltips=[
        ('Asset', '@{Asset type}'),
        ('Asset ID', '@AssetID'),
        ('Date', '@Date'),

    ])

# LOAD GOOGLE MAPS AND CUSTOMIZE IT
map_options = GMapOptions(lat=37.501627, lng=-79.868284, map_type="hybrid", zoom=16)
p = gmap("", map_options, title="Fleet Tracker", tools='pan,wheel_zoom,reset', toolbar_location="right")
p.add_tools(hover)

p2 = gmap("", map_options, title="Fleet Tracker", tools='pan,wheel_zoom,reset', toolbar_location="right")
p2.add_tools(hover)

p.circle(y="GPS Lattitude", x="GPS Longitude", size=13, fill_color="red", fill_alpha=0.8, source=psource)
# p.multi_line('GPS Longitude','GPS Lattitude', source=psource, color='red', line_width=3)


output_file(filename="./templates/maps.html", title="Static HTML file")


# show the results
layout = column(select, p)
show(layout)
bokeh_doc.title = "Fleet Management System"
bokeh_doc.add_root(layout)
