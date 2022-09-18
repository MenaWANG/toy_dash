# -*- coding: utf-8 -*-
from dash import Dash, dcc, html, Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# in this app, the list of cities will be filtered by the list of countries
# in order to do that, create a dictionary with countries as keys
all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    html.H4('select a country: '),
    dcc.RadioItems(
        list(all_options.keys()), # select keys in the dictionary
        'America',
        id='countries-radio',
    ),

    html.Hr(),
    html.H4('select a city: '),
    dcc.RadioItems(id='cities-radio'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@app.callback( # filter city options by countries
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


# @app.callback( # select the first available city as default choice
#     Output('cities-radio', 'value'),
#     Input('cities-radio', 'options'))
# def set_cities_value(available_options):
#     return available_options[0]['value']


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return u'{} is a city in {}'.format(
        selected_city, selected_country,
    )


if __name__ == '__main__':
    app.run_server(debug=True)
