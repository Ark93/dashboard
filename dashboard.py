import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import influxdb_client
import pandas as pd

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

idx = 0
gap = 1000

client = influxdb_client.connect_database()

df = influxdb_client.query_to_dataframe(client)
# Choose a css stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Instanciating web app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Instanciating data
time = df.set_index('time')['2020-07-27'][idx: gap + idx] #this query should be done by client

# Create plot
fig = px.line(time)

# Create html structure
app.layout = html.Div(children=[
    # Create html H1 tag
    html.H1(children='Personal Dashboard'),
    
    # Create table
    html.Div(children ='''
        Table
    '''),
    
    generate_table(
        time[-10:]
    ),
    
    # Create html Div tag
    html.Div(children='''
        Monitoring IPC.
    '''),
    
    # create html image element
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# run app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
    
    
