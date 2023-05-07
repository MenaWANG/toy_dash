import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html
from dash_extensions.javascript import Namespace

# Credit to Emil, the plotly pro: http://dash-leaflet.herokuapp.com/
# Different from the inline javascript approach (see dl_map_marker_by_var_inline_js.py)
# This approach needs us to mannually create a js file (dashExtensions_default.js) then refer to it through `Namespace`

# A few countries.
countries = [dict(name="Denmark", iso2="dk", lat=56.26392, lon=9.501785),
             dict(name="Sweden", iso2="se", lat=59.334591, lon=18.063240),
             dict(name="Norway", iso2="no", lat=59.911491, lon=9.501785)]
# Generate geojson with a marker for each country and name as tooltip.
geojson = dlx.dicts_to_geojson([{**c, **dict(tooltip=c['name'])} for c in countries])
ns = Namespace("country", "assign_marker")

# Create the app
app = Dash()
app.layout = html.Div([
    dl.Map( children=[
                    dl.TileLayer(), 
                    dl.GeoJSON(data=geojson, 
                               options=dict(pointToLayer=ns("pointToLayer")),
                               zoomToBounds=True)
                    ], 
            style={'width': '100%', 'height': '70vh', 
            'margin': "auto", "display": "block"}, 
            id="map"
        ),
])

if __name__ == '__main__':
    app.run_server(
        debug = True
        ,host = '0.0.0.0'
        ,port = 5002
    )