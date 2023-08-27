# This is insipred by the following resources:
# https://codepen.io/dsr/pen/rNLxBxw
# https://www.smashingmagazine.com/2021/12/create-custom-range-input-consistent-browsers/

from dash import Dash, dcc, html, Input, Output, clientside_callback, callback

app = Dash(__name__)
year_values = [2017, 2018, 2019, 2020]
app.layout = html.Div(className="range-input", children=[
        html.Div("Select Year", className="year-chooser-title"),
        dcc.Input(
            id="my-slider",
            type="range",
            min=min(year_values),
            max=max(year_values),
            value=year_values[len(year_values)-1],
            step=year_values[2] - year_values[1]
            ),
        html.Div(className="value", children=html.Div(id="output-div-js")),
        html.Ul(
            className="range-labels",
            children= [
                html.Li(
                    id="year-{}".format(i),
                    className="range-labels-item item-{} {}".format(year_values[i], "always-show start" if i == 0 else "always-show end active" if i == len(year_values) - 1 else ""),
                    **{"data-index": i},
                    children=year_values[i]
                )
                for i in range(0, len(year_values))
            ]
            ),
        html.Div(id="dummy"),

])

clientside_callback(
"""function (id) {
    sliderValShow();
    return window.dash_clientside.no_update
}""", 
Output('output-div-js', 'children'), Input('my-slider', 'value'))


if __name__ == "__main__":
    app.run(debug=True)
