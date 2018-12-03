import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./data/Boulder_USCRN.csv')


app = dash.Dash()

station_options = []
for station in df['station'].unique():
    station_options.append({'label':str(station), 'value':station})


month_options = []
for month in df['month'].unique():
    month_options.append({'label':str(month), 'value':month})

app.layout = html.Div([
    dcc.Dropdown(id='station-picker',options=station_options,value=df['station']),
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='month-picker',options=month_options,value=df['month'].min())
])

@app.callback(Output('graph', 'figure'),
        [Input('month-picker', 'value')])
def update_figure(selected_month):
    filtered_df = df[df['month'] == selected_month]
        traces = []
        for station_name in filtered_df['station'] == station_name]
        traces.append(go.Scatter(
            x=df_by_continent[''],
            y=df_by_continent[''],
            text=df_by_continent[''],
            mode='markers',
            opacity=0.7,
        ))


if __name__ == '__main__':
    app.run_server()