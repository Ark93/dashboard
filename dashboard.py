from libs import influxdb_client
from libs import config
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import dash

def get_options():
    dict_list = []
    for i in config.stocks:
        dict_list.append({'label': i, 'value': i})
    return dict_list

idx = 0
gap = 1000

#---------------------------------------------------------------
client = influxdb_client.connect_database()

df = influxdb_client.query_to_dataframe(client)

# Instanciating data
time = df.set_index('time')['2020-07-27'][idx: gap + idx] #this query should be done by client
time = time.reset_index()


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
                        html.P('''Pick one or more stocks from the dropdown below.'''),
                        html.Div(className='div-for-dropdown',
                                 children=[
                                     dcc.Dropdown(id='stockselector',
                                                  options=get_options(),
                                                  style={'backgroundColor': '#1E1E1E'},
                                                  className='stockselector')
                                 ],
                                 style={'color': '#1E1E1E'})
                    ]
                ),
                html.Div(
                    className='eight columns div-charts bg-grey',
                    children = [
                        dcc.Graph(id='timeseries',
                                  config={'displayModeBar': False},
                                  animate = True,
                                  figure = px.line(time,
                                                   x='time',
                                                   y='value',
                                                   color='serie',
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
    
    
