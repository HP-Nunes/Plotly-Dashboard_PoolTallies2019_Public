# -*- coding: utf-8 -*-
import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("pool-underwater.jpg"),
                        className="logo",
                    ),
#                     html.A(
#                         html.Button("GitHub", id="learn-more-button"),
#                         href="https://github.com/HP-Nunes/dataAnalysis",
#                         target="_blank",
#                     ),
                    html.P("Prepared by Hadrien N. Picq • April 2020 • ",  id="attribution"
                    ),
                    html.A("Analysis source code available on GitHub", id ="attribution2", href="https://github.com/HP-Nunes/dataAnalysis",target="_blank"
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Pool Tallies")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/overview",
                className="tab first",
            ),
            dcc.Link(
                "Technical Summary", # Price Performance
                href="/technical-summary",
                className="tab",
            ),
            dcc.Link(
                "Seasonal Trends", # Portfolio & Management
                href="/seasonal-trends",
                className="tab",
            ),
            dcc.Link(
                "Daily & Hourly Trends", # Fees & Minimums
                href="/day-n-hourly-trends", 
                className="tab"
            ),
            dcc.Link(
                "Case Study 1", # Distributions
                href="/case-study-1",
                className="tab",
            ),
            dcc.Link(
                "Case Study 2", # News & Reviews
                href="/case-study-2",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
