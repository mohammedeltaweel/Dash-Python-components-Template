# This is insipred by the following resources:
# https://codepen.io/dsr/pen/rNLxBxw
# https://www.smashingmagazine.com/2021/12/create-custom-range-input-consistent-browsers/

from dash import Dash, dcc, html, Input, Output, clientside_callback, callback

app = Dash(__name__)
year_values = [2017, 2018, 2019, 2020]
app.layout = html.Div(className="range-input", children=[
        dcc.Input(
            id="my-slider",
            type="range",
            min=min(year_values),
            max=max(year_values),
            value=year_values[0],
            step=year_values[2] - year_values[1],
            autoFocus=True
        ),
        html.Div(className="value", children=html.Div(id="output-div-js")),
        html.Div(id="dummy"),
        # If you want to show the values using dash callback instead of JS uncomment the following div and 
        # html.Div(id="slider-value-dash")
])

clientside_callback(
"""function (id) {
    sliderValShow();
    return window.dash_clientside.no_update
}""", 
Output('output-div-js', 'children'), Input('my-slider', 'value'))



# Uncomment to use the slider-value-dash div to show slider value instead of clientside callback
# @callback(
#     Output("slider-value-dash", "children"),
#     Input("my-slider", "value")
# )
# def update_slider(value_of):
#     return value_of

if __name__ == "__main__":
    app.run(debug=True)
