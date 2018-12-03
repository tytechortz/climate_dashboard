import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./data/Boulder_USCRN.csv')


app = dash.Dash()

month_options = []
for month in df['month'].unique():
    month_options.append({'label':str(month), 'value':month})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='month-picker',options=month_options,value=df['month'].min())
])



if __name__ == '__main__':
    app.run_server()