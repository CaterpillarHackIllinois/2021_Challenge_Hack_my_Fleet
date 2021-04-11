import plotly.express as px

def map_graph(df):

    fig = px.scatter_mapbox(df, lat="GPS Lattitude_y", lon="GPS Longitude_y", hover_name="cluster_label",
                            hover_data=["AssetID"], color="cluster_label", color_continuous_scale=px.colors.sequential.Blues, zoom=3, height=300)

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
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig