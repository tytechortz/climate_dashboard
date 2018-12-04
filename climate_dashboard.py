import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./data/USCRN_data.csv')
df1 = pd.read_csv('./data/Stapleton.csv')


app = dash.Dash()

station_options = []
for station in df['station'].unique():
    station_options.append({'label':str(station), 'value':station})

year_options = []
for YEAR in df1['YEAR'].unique():
    year_options.append({'label':str(YEAR), 'value':YEAR})


app.layout = html.Div([

    html.Div([
        dcc.Graph(id='max_graph'),
        html.Label('Dropdown'),
        dcc.Dropdown(
            id='station-picker-max',
            options=station_options,value=df['station'],
            placeholder = "Select Station",
        ),
    ]),

    html.Div([
        dcc.Graph(id='min_graph'),
        html.Label('Dropdown'),
        dcc.Dropdown(
            id='station-picker-min',
            options=station_options,value=df['station'],
            placeholder = "Select Station",
        ),
    ]),

    html.Div([
        dcc.Graph(id='stapleton'),
        html.Label('denver'),
        dcc.Dropdown(
            id='denver-year-picker',
            options=year_options,value=df1['YEAR'],
        )
    ])

])


@app.callback(Output('max_graph', 'figure'),
        [Input('station-picker-max', 'value')])
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


@app.callback(Output('min_graph', 'figure'),
        [Input('station-picker-min', 'value')])
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

@app.callback(Output('stapleton', 'figure'),
        [Input('denver-year-picker', 'value')])
def update_figure(selected_station):
    filtered_df1 = df1[df1['YEAR'] == selected_station]
    traces = []
    for station_name in filtered_df1['YEAR'].unique():
        df1_by_station = filtered_df1[filtered_df1['YEAR'] == station_name]
        traces.append(go.Scatter(
            x=df_by_year['YEAR'],
            y=df_by_year['TMAX'],
            text=df_by_year['YEAR'],
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