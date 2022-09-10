from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

def serve_layout():
    return html.Div(children=[
    html.H6("see callback in action")
    ,html.Div([
        "Input: "
        ,dcc.Input(
            id = 'my-input'
            ,value = 'initial value'
            ,type = 'text'
        )
    ])
    ,html.Br()
    ,html.Div(id = 'my-output')
])

app.layout = serve_layout

@app.callback(
    Output('my-output','children')
    ,Input('my-input','value')
)
def update_output_value(input_value):
    return f'Output : {input_value}'

if __name__ == '__main__':
    app.run_server(
        debug = True
        ,host = '0.0.0.0'
        ,port = 5000
    )
