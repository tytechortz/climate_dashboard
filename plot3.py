import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('./data/Stapleton.csv')

app = dash.Dash()


# https://dash.plot.ly/dash-core-components/dropdown
# We need to construct a dictionary of dropdown values for the years
year_options = []
for year in df['YEAR'].unique():
    year_options.append({'label':str(year),'value':year})

app.layout = html.Div([
    html.H3('Denver Max Daily Temp'),
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='year-picker',options=year_options,value=df['YEAR'].min())
])

@app.callback(Output('graph', 'figure'),
              [Input('year-picker', 'value')])
def update_figure(selected_year):
    filtered_df = df[df['YEAR'] == selected_year]
    traces = []
    for month_num in filtered_df['MONTH'].unique():
        df_by_month = filtered_df[filtered_df['MONTH'] == month_num]
        traces.append(go.Scatter(
            x=df_by_month['DAY'],
            y=df_by_month['TMAX'],
            text=df_by_month['NAME'],
            mode='markers + lines',
            opacity=0.7,
            marker={'size': 5},
            name=month_num
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'title': 'TIME'},
            yaxis={'title': 'TMAX'},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server()