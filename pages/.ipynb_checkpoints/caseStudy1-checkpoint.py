# -*- coding: utf-8 -*-
import dash_html_components as html
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()



def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 5
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.H6("The Ask:", className="subtitle padded"),
                            html.P(
                                                "Compare weekend patronage between periods with and without lessons, between the time of 8am to 1pm. Make note of holidays and if it had a noticeable effect on attendance."
                                            ),
                            html.P(
                                "Note: Periods in which no lessons occured were based-off handwritten annotation on the tally sheets. If there were no notes on the tally sheets indicating otherwise, it was then assumed that lessons did occur.\
                                    Noted periods indicating ‘no lessons’ occured from:"
                                            ),
                            html.Li(
                            "December 31st, 2018 to January 13th, 2019;"
                            ),
                            html.Li(
                            "March 25th to April 7th;"
                            ),
                            html.Li(
                            "June 10th to June 16th;"
                            ),
                            html.Li(
                            "July 8th to July 14th;"
                            ),
                            html.Li(
                            "August 26th to September 1st;"
                            ),
                            html.Li(
                            "September 23rd to September 28th;"
                            ),
                            html.Li(
                            "November 25th to December 7th;"
                            ),
                            html.Li(
                            "December 30th to January 5th, 2020."
                            ),
                            html.Br([]),
                            html.Div(
                        [
                            html.H6(
                                "Weekend Morning (8am-1pm) Patronage, between days With & Without Lessons",
                                className="subtitle padded",
                            ),
                            html.Iframe(src = "//plotly.com/~HP-Nunes/212.embed",width="100%", height="400")
                            ]),
                            html.Br([]),
                            html.H6("Key Observations", className="subtitle padded"),
                            html.Li(
                                                "There were 5,686 patrons over the course of 2019 on weekends with Lessons, compared to 1,056 on those with none. That’s a comparison of approximately 76 swimmers per day to 59 between weekends with and without lessons."
                                            ),
                            html.Li(
                                                "There were 484 tallies taken over the course of 75 days in 2019 on weekends with Lessons, compared to 147 tallies over 18 days on those with none. That’s approximately 6 tallies taken compared to approximately 8 between weekends with and without lessons (a maximum of 10 tallies can be taken between 8am - 1pm)."
                                            ),
                            html.Li(
                                                "Only one facility holiday fell on a Weekend for 2019: Cesar Chavez Day on Sunday March 31st."
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
