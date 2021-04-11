import dash
import dash_core_components as dcc
import dash_table
import dash_html_components as html
import pandas as pd
from graphlib import map_graph
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# deployment heroku
server = app.server

print(os.listdir())
df = pd.read_csv('ceramic/sample_data/by_month_cluster_200.csv')


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
        html.H1(children='MyCaterPillars'),
        html.Div(children='''
        A dashboard for fleet fuel management and optimization!
        '''),
    ]),

    html.Div([
        html.Div(["Gender: ", dcc.Dropdown(id='gender',
                                           options=[{'label': k, 'value': v} for k, v in genders.items()],
                                           value=1)]),
        html.Br(),
        html.Div(["Highest Education: ", dcc.Dropdown(id='education',
                                                      options=[{'label': k, 'value': v} for k, v in educations.items()],
                                                      value=2, )]),
        html.Br(),
        html.Div(["Age: ", dcc.Dropdown(id='age',
                                        options=[{'label': k, 'value': v} for k, v in ages.items()],
                                        value=0, )]),
        html.Br(),
        html.Div(["Socio-Economic-Range: ", dcc.Dropdown(id='soecon',
                                                         options=[{'label': k, 'value': v} for k, v in socio.items()],
                                                         value=55.0, )]),
        html.Br(),
        html.Div(
            ["Num of Prev Attempts (for course you'll be taking): ", dcc.Input(id='attempt', value=0, type='number')]),
        html.Br(),
        html.Div(["Credits (30-300): ", dcc.Input(id='credit', value='30', type='number')]),
        html.Br(),
        html.Div(["Disability: ", dcc.Dropdown(id='disability',
                                               options=[{'label': k, 'value': v} for k, v in disability.items()],
                                               value=0)]),
        html.Br(),
        html.Div(["How Productive are you?: ", dcc.Dropdown(id='productivity',
                                                            options=[{'label': k, 'value': v} for k, v in
                                                                     productivity.items()],
                                                            value=170)]),
        html.Br(),
        html.H6(children=[html.Div(id='my-output', )])

    ], id='control_panel'),

    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=map_graph(df)
        ),
        dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.head(10).to_dict('records'),
        )
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
