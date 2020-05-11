import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dashboard import dashboard_api
from dash.dependencies import Input, Output

#https://towardsdatascience.com/build-your-own-data-dashboard-93e4848a0dcf
#https://towardsdatascience.com/how-to-build-a-complex-reporting-dashboard-using-dash-and-plotl-4f4257c18a7f
#https://medium.com/swlh/dashboards-in-python-using-dash-creating-a-data-table-using-data-from-reddit-1d6c0cecb4bd

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    html.Div([
        html.H1('DASHBOARD'),
    ])
    ,dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in dashboard_api.get_main_table().columns],
        fixed_rows={'headers': True, 'data': 0},
        data=dashboard_api.get_main_table().to_dict('records'),
        style_cell_conditional=[
            {'if': {'column_id': 'title'},
             'width': '200px'},
            {'if': {'column_id': 'post'},
             'width': '670px'
             ,'height':'auto'}
        ],
        style_data_conditional=[
            {
                'if': {
                    'column_id': 'LABEL',
                    'filter_query': '{LABEL} = "RENEWED"'
                },
                'color': 'green'
            },
            {
                'if': {
                    'column_id': 'LABEL',
                    'filter_query': '{LABEL} = "NOT_RENEWED"'
                },
                'color': 'red'
            }
        ]
        ,style_cell={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': '50px'
        },
        style_table={
            'maxHeight': '300px'
            ,'overflowY': 'scroll'
        }
    )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)


