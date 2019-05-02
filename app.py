import dash  
import dash_core_components as dcc  
import dash_html_components as html 
import pandas as pd  

df = pd.read_csv('kyoto-temp-winter.csv', index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H2(['1880年からの京都の12−3月の気温'], style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(id = 'kyoto-winter-line-chart',
            figure = {
                'data': [
                    {
                        'x': df[df['year'] == select_year]['month'],
                        'y': df[df['year'] == select_year]['temp'],
                        'type': 'lines',
                        'line': {'color': 'red' if select_year == 2018 else 'grey',
                                'width': 6 if select_year == 2018 else 1},
                        'name': select_year,    
                    } for select_year in df['year'].unique()
                ],
                'layout': {
                    'height': 900,
                    'hovermode': 'closest',
                    'title': {'text': '線グラフ（2018年（赤色））', 'font':{'size': 25}},
                    'yaxis':{'title': '平均気温（度）'},
                    'xaxis':{'title': '月'}
                }
            }
        )
    ], style={'display': 'inline-block', 'width': '40%'}),

    html.Div([
        dcc.Graph(id='kyoto-winter-boxplot',
        figure = {
            'data':[
                {
                    'y':df[df['year'] == select_year]['temp'],
                    'name': select_year,
                    'type': 'box',
                    'showlegend':False,
                } for select_year in df['year'].unique()
            ],
            'layout':{
                'height': 550,
                'title':{'text': 'ボックスプロット','font':{'size': 25}},
                'yaxis':{'title': '平均気温（度）'},
                'xaxis':{'title': '年度'}
            }
        }
        ),
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
                'height': 350,
                'hovermode': 'closest',
                'yaxis': {'title': '年度'},
                'xaxis':{'title': '月'},
                'title': {'text': 'ヒートマップ', 'font':{'size': 25}}
            }
        }
        ),
    ], style={'display': 'inline-block', 'width': '60%'}),
])

if __name__=='__main__':
    app.run_server(debug=True)