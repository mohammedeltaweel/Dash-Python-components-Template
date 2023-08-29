import dash
from dash import Input, Output, dcc, html, clientside_callback, Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Nav(
        className="main-navigation",
        children=[
        html.Div(className="menu-icon", children=[
            html.Span(className="fas fa-bars")
        ]),
        html.Div(className="main-logo", children="My Logo"),
        html.Ul(className="main-nav-items underline-indicators flex", children=[
            html.Li(html.A("Home", href="/")),
            html.Li(html.A("Page1", href="/page1")),
            html.Li(html.A("Page2", href="/page2")),
            html.Li(html.A("Page3", href="/page3")),
        ]),
        html.Div(className="search-icon", children=[
            html.Span(className="fas fa-search")
        ]),
        html.Div(className="cancel-icon", children=[
            html.Span(className="fas fa-times")
        ]),
        html.Form(action="#", children=[
            dcc.Input(type="search", className="search-data", placeholder="Search", required=True),
            html.Button(type="submit", className="fas fa-search")
        ]),
    ]),

    html.Div(id="nav-dummy")
    ])

clientside_callback(
"""function (id) {
    setupNavbarFunctionality();
    return window.dash_clientside.no_update
}""", 
Output('nav-dummy', 'children'), Input('nav-dummy', 'children'))



if __name__ == "__main__":
    app.run_server(debug=True)
