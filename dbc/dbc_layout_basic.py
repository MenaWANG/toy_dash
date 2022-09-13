from dash import Dash, html
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.FLATLY])

app.layout = dbc.Container([
    html.P("This is above the alert"),
    dbc.Alert("Hello Bootstrap!", color="success")],
    # className cheatsheet: https://dashcheatsheet.pythonanywhere.com/
    className="p-3 bg-danger bg-opacity-50 text-white",
)

if __name__ == "__main__":
    app.run_server(debug = True,
                    host = '0.0.0.0',
                    port = 5000)