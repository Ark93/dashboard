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

#---------------------------------------------------------------
client = influxdb_client.connect_database()

df = influxdb_client.query_to_dataframe(client)

# Instanciating data
time = df.set_index('time')['2020-07-27'][idx: gap + idx] #this query should be done by client


#---------------------------------------------------------------------

# Instanciating web app
app = dash.Dash(__name__)

# Create html structure
app.layout = html.Div(
    children=[
        html.Div(
            className='row',
            children = [
                html.Div(
                    className='four columns div-user-controls',
                    children = [
                        html.H2('Dash - STOCK PRICES'),
                        html.P('''Visualising time series with Plotly - Dash'''),
                        html.P('''Pick one or more stocks from the dropdown below.''')
                    ]
                ),
                html.Div(
                    className='eight columns div-charts bg-grey',
                    children = [
                        dcc.Graph(id='timeseries',
                                  config={'displayModeBar': False},
                                  animate = True,
                                  figure = px.line(time,
                                                   template='plotly_dark'
                                                  ).update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                                                                   'paper_bgcolor': 'rgba(0, 0, 0, 0)'
                                                                  }
                                                                 )
                                 )
                    ]
                )
            ]
        )
    ]
)

# run app
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
    
    
