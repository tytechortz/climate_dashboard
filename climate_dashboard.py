import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./data/Stapleton.csv')


app = dash.Dash()

year_options = []
for year in df['YEAR'].unique():
    year_options.append({'lable':str(year),'value':year})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker', options=year_options)
                value=df['YEAR'].min())
])

@app.callback(Output('graph', 'figure'),
            [Input('year-picker', 'value')])
def update_figure(selected_year):
    return #something

    filtered_df = df[df['YEAR']== selected_year]

    traces 

if __name__ == '__main__':
    ap.run.server()