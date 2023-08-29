import dash
from dash import Input, Output, dcc, html, clientside_callback, Dash
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME],suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Nav(
        className="main-navigation",id="main-nav",
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

    html.Div(id="nav-dummy"),
    html.Span("""
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam, rerum reprehenderit! Culpa error veritatis beatae officiis dolores nulla animi nobis quo quam sint excepturi, dignissimos fugiat nisi quibusdam voluptas ea!
              
              """)
    ], className="main-content")

clientside_callback(
"""function (id) {
    setupNavbarFunctionality();
    return window.dash_clientside.no_update
}""", 
Output('nav-dummy', 'children'), Input('nav-dummy', 'children'))

clientside_callback(
    """
    function(id) {
    changeNavStyle();
    return window.dash_clientside.no_update
    }
""",
Output("main-nav", "children"), Input("main-nav", "children")
)


if __name__ == "__main__":
    app.run_server(debug=True)
