from dash import Dash, dcc, html, Input, Output, clientside_callback, callback
button_dict = {"btn-title":"air-land",
               "values":["air", "land"],
               "value-description":["Air Tourism", "Land Tourism"],
               "toggle-title": "Please select a display method"}
app = Dash(__name__)
app.layout = html.Div([
   html.Div(className="toggle-select {}".format(button_dict["btn-title"]),
            children=[
               html.Div(className="toggle-select-container {}-toggle".format(button_dict["btn-title"]),
                        children=[
                           html.Div(className="toggle-title", children="{}".format(button_dict["toggle-title"])),
                           html.Ul(className="toggle-select-outer", children=[
                                  html.Li(
                                    className="toggle-select-button {} {}".format(i, "active" if idx == 0 else ""),
                                    **{"data-value": i}, 
                                    children=button_dict["value-description"][idx])
                                  for idx, i in enumerate(button_dict["values"])
                           ])
                        ])
            ])
])

if __name__ == "__main__":
    app.run(debug=True)

