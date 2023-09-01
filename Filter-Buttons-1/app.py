
from dash import Dash, dash, html
app = Dash(__name__)

app.layout = html.Div(className="section Line-chart", children=[
    html.Div(className="Line-chart-comments"),
    html.Div(className="Line-chart-main"),
    html.Div(className="side-menu", children=[
        html.Aside(className="filters", children=[
            html.Span("Transportation type"),
            html.Div(className="filter-selection", children=[
                html.Ul(children=[
                    html.Li(children=[
                        html.Span(className="filter-dot"),
                        html.Span("Cars and Buses"),
                    ]),
                    html.Li(children=[
                        html.Span(className="filter-dot"),
                        html.Span("Car"),
                    ]),
                    html.Li(children=[
                        html.Span(className="filter-dot"),
                        html.Span("Car"),
                    ]),
                ])
            ]),
            html.Div(className="arrow-left"),
        ]),
        html.Div(className="download-option", children=[
            html.Button("Download Report", className="download-button")
        ])
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
