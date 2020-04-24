import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_StatisticalSummaryofMonthlyPatronageofBakarIndoorPoolfor2019 = pd.read_csv(DATA_PATH.joinpath("StatisticalSummaryofMonthlyPatronageofBakarIndoorPoolfor2019.csv"))
df_seasonsalstats = pd.read_csv(DATA_PATH.joinpath("seasonsal_stats.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Summary"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_seasonsalstats)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Observations"], className="subtitle padded"
                                    ),
                                    html.P(
                                        "\
                                        Patronage peaks early in the year and steadily rises through \
                                        the Spring until April. The slowest period occurs from June to July, \
                                        before the second annual peak in September. We can make inferences about \
                                        the Fall due to missing data, but we can guess that the trend is generally \
                                        downward until the next anticipated January peak.",
                                    ),
                                    html.P(
                                        "\
                                        Lap Swim is the most popular activity throughout the year, \
                                        except in March where it is overtaken by Family Swim."
                                    ),
                                ],
                                className="six columns",
                                style={"color": "#696969"},
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "10px"},
                    ),
                    # Row 3
                    html.Div(
                        [
                            html.H6(
                                "Bar Chart of Total Monthly Patronage",
                                className="subtitle padded",
                            ),
                            html.Iframe(src = "//plotly.com/~HP-Nunes/239.embed",width="100%", height="400")
                            ]),
                    html.Div(
                                                [
                                                    html.Br([]),
                                                    html.H6("Descriptive Statistics of Monthly Patronage", className="subtitle padded"),
                                                    html.Table(
                                                        make_dash_table(df_StatisticalSummaryofMonthlyPatronageofBakarIndoorPoolfor2019),
                                                        className="tiny-header",
                                                                )
                                                ],
                                                style={"overflow-x": "auto"},
                                                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
