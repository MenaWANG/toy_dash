import dash_leaflet as dl
from dash_extensions.enrich import html
import dash

# use LayersControl to control the characterisitic and visibility of makers by group. 
# code revised based on source: https://dash-leaflet.herokuapp.com/

center = [-37.80, 145] # Melbourne
zoom = 10

# Two groups of markers
markers_A = [dl.Marker(position=[-37.70, 144.80]), dl.Marker(position=[-37.85, 145.10])]
markers_B = [dl.CircleMarker(center=[-37.60, 145.20]), dl.CircleMarker(center=[-37.78, 144.7])]

# Create app.
app = dash.Dash()
app.layout = html.Div(dl.Map([
    dl.LayersControl(
        [dl.BaseLayer(dl.TileLayer(), name="basemap", checked=True)] +
        [dl.Overlay(dl.LayerGroup(markers_A), name="drop", checked=True),
         dl.Overlay(dl.LayerGroup(markers_B), name="circle", checked=True)]
    )
], zoom=zoom, center=center, 
   style={'width': '100%', 'height': '100vh', 'margin': "auto", "display": "block"}))

if __name__ == '__main__':
    app.run_server()