import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('sample_data/by_month_cluster_200.csv')

fig = px.scatter_mapbox(df, lat="GPS Lattitude_y", lon="GPS Longitude_y", hover_name="cluster_label",
                  hover_data=["AssetID"],color_discrete_sequence=["fuchsia"], zoom=3, height=300)

fig.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        },
      ])
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig = px.bar(df, x="cluster_label", y="Fuel Used Per Hour", color="AssetID", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='MyCaterPillars'),

    html.Div(children='''
        A dashboard for fleet management!
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.head(10).to_dict('records'),
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)