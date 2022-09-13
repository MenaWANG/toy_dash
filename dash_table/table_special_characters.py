# -*- coding: utf-8 -*-

from dash import Dash, dash_table
import pandas as pd
from collections import OrderedDict

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

df['Rating'] = df['Humidity'].apply(lambda x:
    '⭐⭐⭐' if x > 30 else (
    '⭐⭐' if x > 20 else (
    '⭐' if x > 10 else ''
)))
df['Growth'] = df['Temperature'].apply(lambda x: '↗️' if x > 0 else '↘️')
df['Status'] = df['Temperature'].apply(lambda x: '🔥' if x > 0 else '🚒')

app = Dash(__name__)

app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    columns=[
        {"name": i, "id": i} for i in df.columns
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
