import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
import pandas as pd

df1 = pd.read_csv('./data/Stapleton.csv')

np.random.seed(56)
x_values = df1['TOT_DAY']
y_values = df1['TMAX']

# Create traces
# trace0 = go.Scatter(
#     x = x_values,
#     y = y_values+5,
#     mode = 'markers',
#     name = 'markers'
# )
trace1 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'lines',
    name = 'lines'
)
# trace2 = go.Scatter(
#     x = x_values,
#     y = y_values-5,
#     mode = 'lines',
#     name = 'lines'
# )
data = [trace1]  # assign traces to data
layout = go.Layout(
    title = 'Denver Temperature '
)
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='line1.html')

if __name__ == '__main__':
    app.run_server()