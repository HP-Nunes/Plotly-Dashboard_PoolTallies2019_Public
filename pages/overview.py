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


df_tally2019_facts = pd.read_csv(DATA_PATH.joinpath("df_tally2019_facts.csv"))


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Executive Summary"),
                                    html.Br([]),
                                    html.P(
                                     "\
                                    Over the course of 2019, the Bakar Fitness Center's Indoor Pool was patronized at least 43,067 times over \
                                    324 days; on average, the pool was patronized 133 times per day. \
                                    Lifeguards, who are tasked with tallying pool attendance every 30 minutes on the \
                                    15-minute mark, recorded collectively 5,581 tallies, totaling 167,430 minutes worth \
                                    of data, or an average of 9 operational pool hours per day (out of an estimated maximum of \
                                    12 hours on most days). While Lap Swim is the pool activity which saw the most cumulative \
                                    annual patronage (accounting for nearly a third of all patrons), the busiest days occured during Family Swim \
                                    programming on weekends. The busiest months were January and September respectively, a trend that can \
                                    be reasonably correlated to the start of the University's academic calendar for the Fall & \
                                    Winter Quarters. Included in this report are two analytical case studies: 1) a comparison of \
                                    attendance between weekends with scheduled lessons and those with none, and 2) change in patronage \
                                    during early morning Lap Swim programming on weekdays.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                    html.Hr([]),
                                    html.P(
                                    "\
                                    Throughout the report, the term “patronage“ refers to \
                                    the usage of the facility by undefined individuals. That is, we cannot assess whether these \
                                    are unique or reoccuring patrons for any given time.",
                                    ),
                                    html.P(
                                    "\
                                    Water Exercise includes tallies for Water Walking and Aqua Fit.",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Fast Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_tally2019_facts)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                html.H6(
                                        "2019 Total Patronage per Activities",
                                        className="subtitle padded",
                                    ),
                                    html.Iframe(src = "//plotly.com/~HP-Nunes/243.embed",width="350", height="500"
                                                ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "10px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.H5("Recommendations"),
                                    html.Br([]),
                                    html.P(
                                     "\
                                    The following are a set of recommendations in order to ensure \
                                    that future tallying records improve in accuracy, fidelity, \
                                    and completedness, with the intent to generate greater patronage insights:",
                                        style={"color": "black"},
                                        className="row",
                                    ),
                                    html.Li("\
                                    A Well-Defined and Consistent Data-Entry Protocol: Consistently digitizing \
                                    the records on a regular basis (weekly preferrably) would allow to identify \
                                    tallying errors or incoherences between programming and attendance. It would \
                                    also decrease the risk of data-entry errors, or data loss (as shown with the \
                                    four weeks' worth of missing tallies in the Fall).",
                                    ),
                                    html.Li("\
                                    Tally Annotations: Perhaps adding a section on the Tally Sheets to make note of \
                                    'irregularities' either in scheduling or activity would allow for higher accuracy \
                                     during data-entry.",
                                     ),
                                     html.Li("\
                                     Tallying Accountability: Although tallying is not the most important or \
                                     pressing of tasks, lifeguards are nonetheless liable to tally and should be able \
                                     to do so consistently. Thus, a tally completedness score per scheduling \
                                     cycles would permit to evaluate overall staff performance on the matter, but also ensure that \
                                     enough tallies are collected on a daily basis so that meaningful inferences about \
                                     long-term trends can be made.",
                                     ),
                                     html.Li("\
                                     Normalizing Patronage to Unique Patrons: either through the use of selective sampling \
                                     or a survey, normalize patronage down to unique patrons. This would allow to derive \
                                     a supplementary and meaningful metric for analysis.",
                                    ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
