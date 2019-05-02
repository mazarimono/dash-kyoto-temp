import dash  
import dash_core_components as dcc 
import dash_html_components as html 
import pandas as pd  
import plotly.graph_objs as go 

df = pd.read_csv('kyoto-temp-winter.csv', index_col=0)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1(id='h1-title', style={'textAlign': 'center'}),
    html.Div([
    dcc.Dropdown(id = 'month-select',
                options = [{'label': i, 'value': i} for i in df['month'].unique()],
                value = '12月'
                ),
    ], style={'textAlign': 'center'}),
    html.Div([
    dcc.Graph(id = 'tempGraph')
    ])
])

@app.callback(
    dash.dependencies.Output('tempGraph', 'figure'),
    [dash.dependencies.Input('month-select', 'value')]
)

def make_monthly_temp_chart(month):
    dff = df[df['month'] == month]
    return {
        'data': [go.Scatter(
            x = dff['year'],
            y = dff['temp']
        )]
    }


if __name__ == '__main__':
    app.run_server(debug=True)