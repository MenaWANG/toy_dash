from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd 


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app =  Dash(__name__)

def serve_layout():
    return html.Div([
        dcc.Graph(id = 'graph-with-slider'),
        dcc.Slider(
            df['year'].min(),
            df['year'].max(),
            step = None,
            value = df['year'].min(),
            marks={str(year): str(year) for year in df['year'].unique()},
            id = 'year-slider',
        ),
    ])

app.layout = serve_layout

@app.callback(
    Output('graph-with-slider','figure') #component type should be figure
    ,Input('year-slider','value')
)
def update_graph_with_slider(selected_year):
    filtered_df = df[df['year']==selected_year]
    fig = px.scatter(
        filtered_df,
        x="gdpPercap", y="lifeExp",
        size="pop", color="continent",
        hover_name="country",
    )
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(
        debug = True
        ,host = '0.0.0.0'
        ,port = 5000
    )

