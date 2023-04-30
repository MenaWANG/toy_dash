# -*- coding: utf-8 -*-
from dash import Dash, dcc, html, Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# in this app, the list of cities will be filtered by the list of countries
# in order to do that, create a dictionary with countries as keys
# If I were to use placeholder, the chained dropdown list will have KeyError
### Solution A: Have a default option
### Solution B (a workaround if we definately don't want a default value) 
        # treat 'Please select a country' as an legitimate option 
        # Create placeholder pair in the all_options dictionary


all_options = {
    #'Please select a country':['Please select a city'], #B
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.Dropdown(
        list(all_options.keys()), # select keys in the dictionary
        #value = 'Please select a country', #B
        value = 'America',
        id='countries-dropdown',
    ),

    html.Hr(),
    dcc.Dropdown(id='cities-dropdown',
                placeholder = 'Please select a city'),

    html.Hr(),

    html.Div(id='display-selected-values')
])


@app.callback( # filter city options by countries
    Output('cities-dropdown', 'options'),
    Input('countries-dropdown', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


if __name__ == '__main__':
    app.run_server(debug=True)
