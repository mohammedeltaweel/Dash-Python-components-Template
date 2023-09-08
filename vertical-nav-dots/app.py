import dash
from dash import html, callback, Output, Input, dcc, ClientsideFunction
import dash_bootstrap_components as dbc
from dash_extensions import DeferScript

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

app.layout = html.Div([

    # first section
    dcc.Location(id="url"),
    html.Div("Home", className="section", id="home", **{"data-label": "Home"}),
    html.Div("About Us", className="section", id="about", **{"data-label": "About Us"}),
    html.Div("Get In Touch", className="section", id="contact", **{"data-label": "Get In Touch"}),
    html.Div("Fourth", className="section", id="section4", **{"data-label": "Fourth Section"}),
    html.Div("Fifth", className="section", id="section5", **{"data-label": "Fifth Section"}),
    html.Div("Sixth", className="section", id="section6", **{"data-label": "Fifth Section"}),
    html.Div("Seventh", className="section", id="section7", **{"data-label": "Fifth Section"}),
    html.Div("Eighth", className="section", id="section8", **{"data-label": "Fifth Section"}),
#############################################################
    html.Nav(id='my-navigation',
        className="nav",
        children=[
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#home", className="nav-dot", id="link1"),
                    html.Span("Home", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#about", className="nav-dot", id="link2"),
                    html.Span("About Us", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#contact", className="nav-dot", id="link3"),
                    html.Span("Get In Touch", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#section4", className="nav-dot", id="link4"),
                    html.Span("Get In Touch", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#section5", className="nav-dot", id="link5"),
                    html.Span("Get In Touch", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#section6", className="nav-dot", id="link6"),
                    html.Span("Get In Touch", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#section7", className="nav-dot", id="link7"),
                    html.Span("Get In Touch", className="nav-label")
                ]
            ),
            html.Div(
                className="nav-item",
                children=[
                    html.A(href="#section8", className="nav-dot", id="link8"),
                    html.Span("Get In Touch", className="nav-label")
                ]
            )
        ]
    ),
    DeferScript(src='/assets/custom-script.js')

    ], className="page-container")

app.clientside_callback(
"""function (id) {
    activateNavigation();
    return window.dash_clientside.no_update
}""", 
Output('my-navigation', 'children'), Input('my-navigation', 'children'))

if __name__ == '__main__':
    app.run_server(debug=True, port=8070)
