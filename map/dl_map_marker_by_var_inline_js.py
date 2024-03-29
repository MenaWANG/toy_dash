import dash_leaflet as dl
import dash_leaflet.express as dlx
from dash import Dash, html
from dash_extensions.javascript import assign


# Assign map icons/markers by value of a variable
# Credit to Emil, the plotly pro: http://dash-leaflet.herokuapp.com/
# When the app runs, this approach will automatically create a .js file in the assets folder (dashExtensions_default_inline_js.js)
# Compare with the javascript variable approach (see dl_map_marker_by_var_js_vars.py)

# A few countries.
countries = [dict(name="Denmark", iso2="dk", lat=56.26392, lon=9.501785),
             dict(name="Sweden", iso2="se", lat=59.334591, lon=18.063240),
             dict(name="Norway", iso2="no", lat=59.911491, lon=9.501785)]
# Generate geojson with a marker for each country and name as tooltip.
geojson = dlx.dicts_to_geojson([{**c, **dict(tooltip=c['name'])} for c in countries])
# print(geojson) # see below for how dlx turn dict to geojson
# {'type': 'FeatureCollection', 
#  'features': [{'type': 'Feature', 
#                'geometry': {'type': 'Point', 'coordinates': [9.501785, 56.26392]}, 
#                'properties': {'name': 'Denmark', 'iso2': 'dk', 'tooltip': 'Denmark'}}, 
#               {'type': 'Feature', 
#                'geometry': {'type': 'Point', 'coordinates': [18.06324, 59.334591]}, 
#                'properties': {'name': 'Sweden', 'iso2': 'se', 'tooltip': 'Sweden'}}, 
#               {'type': 'Feature', 
#                'geometry': {'type': 'Point', 'coordinates': [9.501785, 59.911491]}, 
#                'properties': {'name': 'Norway', 'iso2': 'no', 'tooltip': 'Norway'}}]}


# Create javascript function that draws a marker with a custom icon, in this case a flag hosted by flagcdn.
# Alternatively, the icons can be saved in the assets folder 
draw_flag = assign("""function(feature, latlng){
const flag = L.icon({iconUrl: `https://flagcdn.com/64x48/${feature.properties.iso2}.png`, iconSize: [64, 48]});
return L.marker(latlng, {icon: flag});
}""")

# Create the app
app = Dash()
app.layout = html.Div([
    dl.Map( children=[
                    dl.TileLayer(), 
                    dl.GeoJSON(data=geojson, options=dict(pointToLayer=draw_flag), zoomToBounds=True)
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