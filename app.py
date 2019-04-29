import dash  
import dash_core_components as dcc  
import dash_html_components as html 
import pandas as pd  
import plotly.graph_objs as go 
import os 

df = pd.read_csv('kyoto-temp-winter.csv', index_col=0)

app = dash.Dash(__name__)

server = app.server 

app.layout = html.Div([
    html.H2(['1880年からの京都の12−3月の気温'], style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id = 'kyoto-winter-line-chart',
            figure = {
                'data': [
                    {
                        'x': df[df['year'] == y]['month'],
                        'y': df[df['year'] == y]['temp'],
                        'type': 'lines',
                        'line': {'color': 'blue' if y == 2018 else 'grey',
                                'width': 6 if y == 2018 else 1},
                        'name': y,
                    } for y in df['year'].unique()
                ],
                'layout': {
                    'height': 900,
                    'color': 'grey',
                    'hovermode': 'closest',
                    'yaxis':{'title': '気温'},
                    'xaxis':{'title': '月'}
                }
            }
        )
    ], style={'display': 'inline-block', 'width': '47%', 'height': 900}),

    html.Div([
        dcc.Graph(id='kyoto-winter-heatmap',
        figure = {
            'data': [{
                'x': df['month'],
                'y': df['year'],
                'z': df['temp'],
                'type': 'heatmap',
            }
            ],
            'layout':{
                'height': 900,
                'hovermode': 'closest',
                'yaxis': {'title': '年'},
                'xaxis':{'title': '月'}
            }
        }
        )
    ], style={'display': 'inline-block', 'width': '47%', 'height': 900}),
])

if __name__=='__main__':
    app.run_server(debug=True)