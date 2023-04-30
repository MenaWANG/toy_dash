import dash
import dash_leaflet as dl
from dash import html

app = dash.Dash(__name__)

# Set up the initial map view
center = [-37.7749, 144.085] # San Francisco
zoom = 10

# Define the map layout
app.layout =  html.Div([
    dl.Map(
        center=center,
        zoom=zoom,
        children = [dl.TileLayer()] + 
                   [dl.Marker(position=[-37.7749, 144.085])] + 
                   [dl.CircleMarker(center=[-37.68, 144.1])]
        ,style={'width': '100%', 'height': '100vh',
               'margin': "auto", "display": "block", "position": "relative"})
])

if __name__ == '__main__':
    app.run_server(debug=True)
