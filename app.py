# -*- coding: utf-8 -*-
import dash
import base64
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(id="error-message"),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    html.Div(
        id="upload",
        children=[
            dcc.Upload(
                id="upload-image",
                className="upload",
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                children=html.Div(
                    children=[
                        "Drag and Drop or ",
                        html.A("Select Files"),
                    ]
                ),
            ),
            html.Div(id="output-image-upload")
        ]
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
])


@app.callback(
    Output("output-image-upload", "children"),
    [Input("upload-image", "contents")],
)
def upload_image(contents):
    if contents:
        return html.Div([html.Img(src=contents)])
    return html.Div(["No image content available."])


if __name__ == '__main__':
    app.run_server(debug=True)
