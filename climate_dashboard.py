import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./data/USCRN_data.csv')


app = dash.Dash()

station_options = []
for station in df['station'].unique():
    station_options.append({'label':str(station), 'value':station})



app.layout = html.Div([

    html.Div([
        dcc.Graph(id='MAX_graph'),
        html.Label('Dropdown'),
        dcc.Dropdown(
            id='station-picker_max',
            options=station_options,value=df['station'],
            placeholder = "Select Station",
        ),
    ]),

    html.Div([
        dcc.Graph(id='MIN_graph'),
        html.Label('Dropdown'),
        dcc.Dropdown(
            id='station-picker_min',
            options=station_options,value=df['station'],
            placeholder = "Select Station",
        ),
    ])
])


@app.callback(Output('MAX_graph', 'figure'),
        [Input('station-picker_max', 'value')])
def update_figure(selected_station):
    filtered_df = df[df['station'] == selected_station]
    traces = []
    for station_name in filtered_df['station'].unique():
        df_by_station = filtered_df[filtered_df['station'] == station_name]
        traces.append(go.Scatter(
            x=df_by_station['RUN_MON'],
            y=df_by_station['T_MAX'],
            text=df_by_station['station'],
            mode='markers+lines',
            opacity=0.7,
            marker={'size': 5},
            name=station_name
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'Running Total Months'},
            yaxis={'title': 'Temp in Deg C'},
            hovermode='closest'
        )
    }


@app.callback(Output('MIN_graph', 'figure'),
        [Input('station-picker_min', 'value')])
def update_figure(selected_station):
    filtered_df = df[df['station'] == selected_station]
    traces = []
    for station_name in filtered_df['station'].unique():
        df_by_station = filtered_df[filtered_df['station'] == station_name]
        traces.append(go.Scatter(
            x=df_by_station['RUN_MON'],
            y=df_by_station['T_MIN'],
            text=df_by_station['station'],
            mode='markers+lines',
            opacity=0.7,
            marker={'size': 5},
            name=station_name
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'Running Total Months'},
            yaxis={'title': 'Temp in Deg C'},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()