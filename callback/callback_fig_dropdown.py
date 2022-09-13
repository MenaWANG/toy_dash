from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd 


df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

app =  Dash(__name__)

# slider should be the better choice, just playing with dropdown here
def serve_layout():
    return html.Div([
        # top section
        html.Div([
            # 40% width on the left? 
            html.Div([
            dcc.Dropdown(
            df['year'].unique(), #list
            df['year'].min(), #default choice
            id = 'year-dropdown'
            )],
            style = {'width' : '40%'})
        ]),
        # bottom section
        dcc.Graph(id = 'graph-with-dropdown'),
    ])

app.layout = serve_layout

@app.callback(
    Output('graph-with-dropdown','figure') #component type should be figure
    ,Input('year-dropdown','value')
)
def update_graph_with_slider(selected_year):
    dff = df[df['year']==selected_year]
    fig = px.scatter(
        dff,
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

