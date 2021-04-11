import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html
import dash_daq as daq
import pandas as pd
from graphlib import map_graph
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# app = dash.Dash(__name__)

# deployment heroku
server = app.server

print(os.listdir())
df = pd.read_csv('https://hack-objectstore.nyc3.digitaloceanspaces.com/by_month_cluster_200.csv')

colors = {'yellow': '#FFCD05', 'dark-gray': '#231F20', 'white': '#FFFFFF', 'light-gray': '#d3d3d3'}

# Options for control panel, feel free to change around!!!!
genders = {"Female": 0, "Male": 1, }
educations = {"None": 0, "Lower than High School": 1, "High-School/GED": 2, "College/eqv": 3, "Graduate": 4}
ages = {"Under 35": 0, "35-55": 1, "Over 55": 2}
socio = {"Bottom 0-10%": 5, "Bottom 10-20%": 15, "Bottom 20-30%": 25, "Bottom 30-40%": 35, "Top 40-50%": 45,
           "Top 50-60%": 55, "Top 60-70%": 65, "Top 70-80%": 75,  "Top 80-90%": 85, "Top 90-100%": 95}
disability = {"No": 0, "Yes": 1}
productivity = {"I am Yoda": 250, "Work hard, play-hard": 170, "I take things easy": 155,
                "Cs get degrees, right?": 140, "I like to sleep": 100}

app.layout = html.Div([

    html.Div([
        html.Img(src = "assets/images/logo.png", id = "logo"),
        html.H1('FUEL ANALYTICS', className="app-header padding-l-20"),

        # html.Div(children='''
        # A dashboard for fleet fuel management and optimization!
        # '''),
        html.Div([
            # html.Div(["Gender: ", dcc.Dropdown(id='gender',
            #                                 options=[{'label': k, 'value': v} for k, v in genders.items()],
            #                                 value=1)]),
            # html.Br(),
            # html.Div(["Highest Education: ", dcc.Dropdown(id='education',
            #                                             options=[{'label': k, 'value': v} for k, v in educations.items()],
            #                                             value=2, )]),
            # html.Br(),
            # html.Div(["Age: ", dcc.Dropdown(id='age',
            #                                 options=[{'label': k, 'value': v} for k, v in ages.items()],
            #                                 value=0, )]),
            # html.Br(),
            # html.Div(["Socio-Economic-Range: ", dcc.Dropdown(id='soecon',
            #                                                 options=[{'label': k, 'value': v} for k, v in socio.items()],
            #                                                 value=55.0, )]),
            # html.Br(),
            daq.ToggleSwitch(
                id='toggle-1',
                className='toggle',
                value=False,
                labelPosition = "bottom",
                label = "Monthly | Average",
            ),
             daq.ToggleSwitch(
                id='toggle-2',
                className='toggle',
                value=False,
                labelPosition = "bottom",
                label = "Cluster Aggregation",
            ),
             daq.ToggleSwitch(
                id='toggle-3',
                className='toggle',
                value=False,
                labelPosition = "bottom",
                label = "Offender or general",
            ),
             daq.ToggleSwitch(
                id='toggle-4',
                className='toggle',
                value=False,
                labelPosition = "bottom",
                label = "Weather",
            ),
            html.Div(
                ["K clusters ", dcc.Input(id='k-cluster', value=0, type='number')], id='css-low-fuel'),
            html.Div(
                ["Low fuel threshold % ", dcc.Input(id='low-fuel', value=0, type='number')], style={'paddingTop': '20px'}),
            html.Br(),
            html.Div(["Fuel Price: ", dcc.Input(id='fuel-price', value='30', type='number')]),
            html.Br(),
        ], id='control-panel')
    ], id='side-bar'),

    

    html.Div([
        dcc.Graph(
            id='scatter-graph1',
            figure=map_graph(df)
        ),
        dash_table.DataTable(
            id='table1',
            style_cell={
                'padding': '5px',
                'backgroundColor': colors['dark-gray'],
                'color': colors['white'],
            },
            style_data={ 'border': '0px solid #d3d3d3' },
            style_header={
                'backgroundColor': colors['dark-gray'],
                'fontWeight': 'bold',
                'color': colors['white'],
                'border': '0px solid #d3d3d3'
            },
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.head(7).to_dict('records'),
            # style_as_list_view=True,
        )
    ], id='charts'),
], id='hero')

if __name__ == '__main__':
    app.run_server(debug=True)
