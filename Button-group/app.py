from dash import Dash, dcc, html, Input, Output, clientside_callback, callback

app = Dash(__name__)
app.layout = html.Div([
])

if __name__ == "__main__":
    app.run(debug=True)
