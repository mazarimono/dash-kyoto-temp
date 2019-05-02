import dash  
import dash_core_components as dcc  
import dash_html_components as html 
import pandas as pd  
import plotly.graph_objs as go 

df = pd.read_csv('kyoto-temp-winter.csv', index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(['1880年からの京都の12月〜3月の気温(Graph by Plotly)'], style={'textAlign': 'center'}),
    html.Div([
        dcc.Graph(
            id = 'kyoto-winter-line-chart',
            figure = {
                'data': [go.Scatter(
                    x = df[df['year'] == select_year]['month'],
                    y = df[df['year'] == select_year]['temp'],
                    name = str(select_year),
                    line = {'color': 'red' if select_year == 2018 else 'grey', 
                            'width': 6 if select_year == 2018 else 1},
                ) for select_year in df['year'].unique()],
                'layout': go.Layout(
                        height = 900,
                        hovermode = 'closest',
                        title = {'text': '線グラフ（2018年）', 'font':{'size':25}},
                        yaxis = {'title': '平均気温（度）'},
                        xaxis= {'title': '月'}
                    )
            }
        )
    ], style ={'display': 'inline-block', 'width': '40%'}),
    html.Div([
        dcc.Graph(
            id='kyoto-winter-boxplot',
            figure = {
                'data': [go.Box(
                    y = df[df['year'] == select_year]['temp'],
                    name = str(select_year),
                    showlegend = False
                ) for select_year in df['year'].unique()],
                'layout': go.Layout(
                    height = 550,
                    title = {'text': 'ボックスプロット', 'font': {'size':25}},
                    yaxis = {'title': '平均気温（度）'},
                    xaxis = {'title': '年度'},
                )
            }
        ),
        dcc.Graph(
            id = 'kyoto-winter-heatmap',
            figure = {
                'data':[
                    go.Heatmap(
                        x = df['month'],
                        y = df['year'],
                        z = df['temp'],
                    )
                ],
                'layout': go.Layout(
                    height = 350,
                    title = {'text': 'ヒートマップ', 'font': {'size':25}},
                    yaxis = {'title': '年度'},
                    xaxis = {'title': '月'},
                    hovermode = 'closest'
                )
            }
        )
    ], style = {'display': 'inline-block', 'width':'60%'})
])

if __name__=='__main__':
    app.run_server(debug=True)