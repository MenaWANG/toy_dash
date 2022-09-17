import json
from dash import Dash, html, Input, Output, ctx

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.P('Click the three buttons to check out how callback context works')
    ])
    ,html.Div([
        html.A('check out the three buttons',style = {'backgroundColor':'blue'})
        ,html.Button('Button 1', id='btn-1')
        ,html.Button('Button 2', id='btn-2')
        ,html.Button('Button 3', id='btn-3')

    ])
    ,html.Div([
        html.P('Followed please see the various properties of "ctx"')
    ])
    ,html.Div(id='container')
])


@app.callback(Output('container', 'children'),
              Input('btn-1', 'n_clicks'),
              Input('btn-2', 'n_clicks'),
              Input('btn-3', 'n_clicks'))

def display(btn1, btn2, btn3):
    button_id = ctx.triggered_id if not None else 'No clicks yet'

    ctx_msg = json.dumps({
        'ctx.states': ctx.states
        ,'ctx.triggered': ctx.triggered
        ,'ctx.inputs': ctx.inputs
    }, indent=2)

    return html.Div([
        html.Table([
            html.Tr([html.Th('Btn-1.n_clicks')
                    ,html.Th('Btn-2.clicks')
                    ,html.Th('Btn-3.n_clicks')
                    ,html.Th('ctx.triggered_id')
                    ])
            ,html.Tr([html.Td(btn1 or 0) # when btn1==NULL shows 0
                    ,html.Td(btn2 or 0)
                    ,html.Td(btn3 or 0)
                    ,html.Td(button_id)
                    ])
        ])
        ,html.Pre(ctx_msg)
    ])


if __name__ == '__main__':
    app.run_server(debug=True
                    ,host = '0.0.0.0'
                    ,port = 5000)
