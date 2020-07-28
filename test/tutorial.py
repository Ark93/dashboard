import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Choose a css stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Instanciating web app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Instanciating data
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Create plot
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Create html structure
app.layout = html.Div(children=[
    # Create html H1 tag
    html.H1(children='Hello Dash'),

    # Create html Div tag
    html.Div(children='''
        Dash: A web application framework for Python.
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
