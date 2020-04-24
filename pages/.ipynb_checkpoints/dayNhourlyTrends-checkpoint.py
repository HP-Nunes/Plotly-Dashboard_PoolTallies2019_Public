# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_StatisticalSummaryofHourlyPatronageofBakarIndoorPoolfor2019 = pd.read_csv(DATA_PATH.joinpath("StatisticalSummaryofHourlyPatronageofBakarIndoorPoolfor2019.csv"))
df_StatSummaryDailyTrends = pd.read_csv(DATA_PATH.joinpath("StatSummaryDailyTrends.csv"))
df_StatSummaryHourlyTrends = pd.read_csv(DATA_PATH.joinpath("StatSummaryHourlyTrends.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 4
            html.Div(
                [
                    # Copied
                 html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Summary, Daily Trends"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_StatSummaryDailyTrends)),
                                ],
#                                 className="six columns",
                            ),
#                             html.Div(
#                                 [
#                                     html.H6(
#                                         ["Observations"], className="subtitle padded"
#                                     ),
#                                     html.P(
#                                         "\
#                                         TEXT.",
#                                     ),
#                                     html.P(
#                                         "\
#                                         TEXT."
#                                     ),
#                                 ],
#                                 className="six columns",
#                                 style={"color": "#696969"},
#                             ),
                        ],
                        className="row",
                        style={"margin-bottom": "10px"},
                    ),
                    #
                    html.Div(
                        [
                         html.H6(
                                  "2019 Total Daily Patronage, Hourly",
                                    className="subtitle padded",
                                ),
                                html.Iframe(src = "//plotly.com/~HP-Nunes/276.embed",width="100%", height="400"),
                        ]),
                    # Plot Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                html.H6(
                                        "2019 Lap Swim Daily Patronage, Hourly",
                                        className="subtitle padded",
                                    ),
                                    html.Iframe(src = "//plotly.com/~HP-Nunes/260.embed",width="350", height="500"
                                                ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                html.H6(
                                        "2019 Family Swim Daily Patronage, Hourly",
                                        className="subtitle padded",
                                    ),
                                    html.Iframe(src = "//plotly.com/~HP-Nunes/262.embed",width="350", height="500"
                                                ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "10px"},
                    ),
                    # Plot Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                html.H6(
                                        "2019 Aquatic Programs Daily Patronage, Hourly",
                                        className="subtitle padded",
                                    ),
                                    html.Iframe(src = "//plotly.com/~HP-Nunes/267.embed",width="350", height="500"
                                                ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                html.H6(
                                        "2019 Water Exercise Daily Patronage, Hourly",
                                        className="subtitle padded",
                                    ),
                                    html.Iframe(src = "//plotly.com/~HP-Nunes/265.embed",width="350", height="500"
                                                ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "10px"},
                    ),
#                     html.Br([]),
                    # Row 1
                    # Copied 2
                    html.Br([]),
                     html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Summary, Hourly Trends"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_StatSummaryHourlyTrends)),
                                ],
#                                 className="six columns",
                            ),
#                             html.Div(
#                                 [
#                                     html.H6(
#                                         ["Observations"], className="subtitle padded"
#                                     ),
#                                     html.P(
#                                         "\
#                                         TEXT.",
#                                     ),
#                                     html.P(
#                                         "\
#                                         TEXT."
#                                     ),
#                                 ],
#                                 className="six columns",
#                                 style={"color": "#696969"},
#                             ),
                        ],
                        className="row",
                        style={"margin-bottom": "10px"},
                    ), 
                    # Row X
#                     html.Br([]),
                    html.Div(
                        [
                         html.H6(
                                  "Hourly Patronage Timeseries",
                                    className="subtitle padded",
                                ),
                                html.Iframe(src = "//plotly.com/~HP-Nunes/254.embed",width="100%", height="500"),
                        ]),
                         html.Div(
                                                [
                                                    html.Br([]),
                                                    html.H6("Descriptive Statistics of Average Hourly Patronage", className="subtitle padded"),
                                                    html.Table(
                                                        make_dash_table(df_StatisticalSummaryofHourlyPatronageofBakarIndoorPoolfor2019),
                                                        className="tiny-header",
                                                                )
                                                ],
                                                style={"overflow-x": "auto"},
                                                    ),
                    # Row 3
#                     html.Div(
#                         [
#                             html.Div(
#                                 [
#                                     html.H6(["Fees"], className="subtitle"),
#                                     html.Br([]),
#                                     html.Div(
#                                         [
#                                             html.Div(
#                                                 [
#                                                     html.Div(
#                                                         [
#                                                             html.Strong(
#                                                                 ["Purchase fee"],
#                                                                 style={
#                                                                     "color": "#515151"
#                                                                 },
#                                                             )
#                                                         ],
#                                                         className="three columns right-aligned",
#                                                     ),
#                                                     html.Div(
#                                                         [
#                                                             html.P(
#                                                                 ["None"],
#                                                                 style={
#                                                                     "color": "#7a7a7a"
#                                                                 },
#                                                             )
#                                                         ],
#                                                         className="nine columns",
#                                                     ),
#                                                 ],
#                                                 className="row",
#                                                 style={
#                                                     "background-color": "#f9f9f9",
#                                                     "padding-top": "20px",
#                                                 },
#                                             ),
#                                             html.Div(
#                                                 [
#                                                     html.Div(
#                                                         [
#                                                             html.Strong(
#                                                                 ["Redemption fee"],
#                                                                 style={
#                                                                     "color": "#515151"
#                                                                 },
#                                                             )
#                                                         ],
#                                                         className="three columns right-aligned",
#                                                     ),
#                                                     html.Div(
#                                                         [
#                                                             html.P(
#                                                                 ["None"],
#                                                                 style={
#                                                                     "color": "#7a7a7a"
#                                                                 },
#                                                             )
#                                                         ],
#                                                         className="nine columns",
#                                                     ),
#                                                 ],
#                                                 className="row",
#                                                 style={"background-color": "#f9f9f9"},
#                                             ),
#                                             html.Div(
#                                                 [
#                                                     html.Div(
#                                                         [
#                                                             html.Strong(
#                                                                 ["12b-1 fee"],
#                                                                 style={
#                                                                     "color": "#515151"
#                                                                 },
#                                                             )
#                                                         ],
#                                                         className="three columns right-aligned",
#                                                     ),
#                                                     html.Div(
#                                                         [
#                                                             html.P(
#                                                                 ["None"],
#                                                                 style={
#                                                                     "color": "#7a7a7a"
#                                                                 },
#                                                             )
#                                                         ],
#                                                         className="nine columns",
#                                                     ),
#                                                 ],
#                                                 className="row",
#                                                 style={"background-color": "#f9f9f9"},
#                                             ),
#                                         ],
#                                         className="fees",
#                                     ),
#                                     html.Div(
#                                         [
#                                             html.Div(
#                                                 [
#                                                     html.Strong(
#                                                         ["Account service fee"],
#                                                         style={"color": "#515151"},
#                                                     )
#                                                 ],
#                                                 className="three columns right-aligned",
#                                             ),
#                                             html.Div(
#                                                 [
#                                                     html.Strong(
#                                                         [
#                                                             "Nonretirement accounts, traditional IRAs, Roth IRAs, UGMAs/UTMAs, SEP-IRAs, and education savings accounts (ESAs)"
#                                                         ],
#                                                         style={"color": "#515151"},
#                                                     ),
#                                                     html.P(
#                                                         [
#                                                             "We charge a $20 annual account service fee for each Brokerage Account, as well as each individual mutual fund holding with a balance of less than $10,000 in an account. This fee does not apply if you sign up for account and choose electronic delivery of statements, confirmations, and fund reports and prospectuses. This fee also does not apply to members of Flagship Select™, Flagship®, Voyager Select®, and Voyager® Services."
#                                                         ],
#                                                         style={"color": "#7a7a7a"},
#                                                     ),
#                                                     html.Br([]),
#                                                     html.Strong(
#                                                         ["SIMPLE IRAs"],
#                                                         style={"color": "#515151"},
#                                                     ),
#                                                     html.P(
#                                                         [
#                                                             "We charge participants a $25 annual account service fee for each fund they hold in their SIMPLE IRA. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."
#                                                         ],
#                                                         style={"color": "#7a7a7a"},
#                                                     ),
#                                                     html.Br([]),
#                                                     html.Strong(
#                                                         ["403(b)(7) plans"],
#                                                         style={"color": "#515151"},
#                                                     ),
#                                                     html.P(
#                                                         [
#                                                             "We charge participants a $15 annual account service fee for each fund they hold in their 403(b)(7) account. This fee does not apply to members of Flagship Select, Flagship, Voyager Select, and Voyager Services."
#                                                         ],
#                                                         style={"color": "#7a7a7a"},
#                                                     ),
#                                                     html.Br([]),
#                                                     html.Strong(
#                                                         ["Individual 401(k) plans"],
#                                                         style={"color": "#515151"},
#                                                     ),
#                                                     html.P(
#                                                         [
#                                                             "We charge participants a $20 annual account service fee for each fund they hold in their Individual 401(k) account. This fee will be waived for all participants in the plan if at least 1 participant qualifies for Flagship Select, Flagship, Voyager Select, and Voyager Services"
#                                                         ],
#                                                         style={"color": "#7a7a7a"},
#                                                     ),
#                                                     html.Br([]),
#                                                 ],
#                                                 className="nine columns",
#                                             ),
#                                         ],
#                                         className="row",
#                                         style={
#                                             "background-color": "#f9f9f9",
#                                             "padding-bottom": "30px",
#                                         },
#                                     ),
#                                 ],
#                                 className="twelve columns",
#                             )
#                         ],
#                         className="row",
#                     ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
