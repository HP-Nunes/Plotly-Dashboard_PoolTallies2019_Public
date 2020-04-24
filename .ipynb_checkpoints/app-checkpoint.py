# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    overview,
    technicalSummary,
    seasonalTrends,
    dayNhourlyTrends,
    caseStudy1,
    caseStudy2
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/technical-summary":
        return technicalSummary.create_layout(app)
    elif pathname == "/seasonal-trends":
        return seasonalTrends.create_layout(app)
    elif pathname == "/day-n-hourly-trends":
        return dayNhourlyTrends.create_layout(app)
    elif pathname == "/case-study-1":
        return caseStudy1.create_layout(app)
    elif pathname == "/case-study-2":
        return caseStudy2.create_layout(app)
    elif pathname == "/full-view":
        return (
            overview.create_layout(app),
            technicalSummary.create_layout(app),
            seasonalTrends.create_layout(app),
            dayNhourlyTrends.create_layout(app),
            caseStudy1.create_layout(app),
            caseStudy2.create_layout(app),
        )
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
