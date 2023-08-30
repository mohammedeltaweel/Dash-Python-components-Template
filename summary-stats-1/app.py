from dash import Dash, dash, html, dcc

layout = html.Div(
    className="summary-column",
    children=html.Div(
        className="stats-summary",
        children=html.Div(className="report-summary",
                          children=html.Div(
                              className="summary-highlights",
                              children= [
                                  # loop begin
                                  html.Div(className="summary-highlight",
                                           children=[
                                               html.Div(className="summary-highlight-header",
                                                        children=[
                                                            html.Span("#{}".format(i), className="summary-index"),
                                                            html.Span("Bilion R.S", className="summary-name")
                                                        ]),
                                                html.Div(className="summary-highlight-description",
                                                         children=[
                                                             html.Div(className="summary-highlight-description-value",
                                                                      children=[
                                                                          html.P(className="value",
                                                                                 children=[
                                                                                     html.Span("1.3", className="value-number"),
                                                                                     html.Span("Bilion R.S", className="value-suffix"),
                                                                                 ]),
                                                                            html.Div(className="description", children=[html.Span("Imports Value")])
                                                                      ]),
                                                            html.Div(className="summary-highlight-description-percentage",
                                                                     children=[
                                                                         html.P(className="value",
                                                                                children=[
                                                                                    html.Span("22.1", className="value-number"),
                                                                                    html.Span("%", className="value-suffix")
                                                                                ]),
                                                                        html.Div(className="description",
                                                                                 children=[
                                                                                     html.Span("Percentage")
                                                                                 ])
                                                                     ])
                                                         ])
                                           ]
                                           ) for i in range(0, 4)
                              ]
                          ))
    )
)
app = Dash(__name__)

app.layout = layout

if __name__ == "__main__":
    app.run(debug=True)
