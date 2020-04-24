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


SampleSizeoftheFiltered30minIncrementalDataset = pd.read_csv(DATA_PATH.joinpath("SampleSizeoftheFiltered30minIncrementalDataset.csv"))
StatisticalSummaryofDailyPatronageofBakarIndoorPoolfor2019 = pd.read_csv(DATA_PATH.joinpath("StatisticalSummaryofDailyPatronageofBakarIndoorPoolfor2019.csv"))


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Data Cleaning and Manipulation", className="subtitle padded"),
#                                     html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "I filtered the original dataset based on the following criteria:"
                                            ),
                                            html.Li(
                                                "I only retained tallies for 2019 (January 1st - December 31st);"
                                            ),
                                            html.Li(
                                                "I excluded days with noted pool closures on: January, Thursday 17th \
                                                (from 5:45 am to 8:15 am); February, Sunday 10th to Thursday 14th (door-breaking incident), \
                                                and May, Sunday 26th at 10:45 am; "
                                            ),
                                            html.Li(
                                                "I dropped rows if no tallies were taken for any Aquatic Activity \
                                                (i.e. Family Swim, Lap Swim, Water Excercise, and Aquatic Programs), i.e. if \
                                                the row only had NULL for any tally. You can think of those as missing tallies;"
                                            ),
                                            html.Li(
                                                "IMPORTANT: The tally sheets for the period spanning October 21st to November 24th \
                                                were missing, which are equivalent to four weeks worth of tallies. Thus there is a \
                                                significant gap in the dataset for the Fall period. "
                                            ),
                                            html.P(
                                                "As a result, approximately 45 % of all rows were retained from the original raw \
                                                dataset, with a count breakdown per Aquatic Activity summarized in the table below:"
                                            ),
                                        html.Div(
                                                [
                                            html.Div(
                                                [
                                                    html.Table(
                                                        make_dash_table(SampleSizeoftheFiltered30minIncrementalDataset),
                                                        className="tiny-header",
                                                                )
                                                ],
                                                style={"overflow-x": "auto"},
                                                    ),
                                                ],
                                                className="twelve columns",
                                                ),
                                        html.Div(
                                                [
                                            html.Div([
                                                html.P(
                                                "The filtered dataset represents a total of 167,430 minutes, or approximately \
                                                over 116 days, for which tallies were recorded. There were 241 recorded instances \
                                                of 0 swimmers, equivalent to 7,230 minutes or approximately 5 days. \
                                                Do note however that, once the dataset is grouped by the day, these 167,430 minutes \
                                                of collected tallies are spread over 314 days, roughly equivalent of 9 hours worth of \
                                                collected tallies per day on average. For added context, if we assume on most weekdays \
                                                that the pool is operational from 5:30 am to 9:30 pm, and closed from 12:00 pm to 4 pm, \
                                                usual operational hours at the Indoor Pool should be amounting close to 12 hours. \
                                                Holidays were defined by the Fitness Facility’s Holiday Schedules, transposed for 2019."
                                                    ),
                                                    ],),
                                                ],
                                                ),
                                            
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                        html.Div(
                        [
                            html.Br([]),
                            html.H6(
                                "Data Table: Patronage per Day",
                                className="subtitle padded",
                            ),
                            html.Iframe(src = "//plotly.com/~HP-Nunes/241.embed",width="100%", height="400")
                            ]),
                        html.Div(
                                [
                                html.Br([]),
                                html.H6(
                                  "Daily Patronage Timeseries",
                                    className="subtitle padded",
                                        ),
                                html.Iframe(src = "//plotly.com/~HP-Nunes/250.embed",width="100%", height="600"),
                                ]),
                        ],
                        className="row ",
                    ),
                    # Row 2
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Br([]),
                                    html.H6("Descriptive Statistics of Daily Patronage", className="subtitle padded"),
#                                     html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "I dropped rows where the number of tallies grouped by the day where below \
                                                two standard deviation from the mean. In other words, from a maximum of 32 tallies \
                                                that can be taken per day, I dropped those which had fewer than 7 entries (given the \
                                                average was close to 18 tallies/days)."
                                            ),
                                            html.P(
                                                "I ended-up removing about 10 entries (or days) down to a total of 314 days. I deemed \
                                                this to be a necessary step in order to remove tallies with–for the most part–deflated \
                                                values, thereby filtering out outlier values from the dataset."
                                            ),
                                            html.Br([]),
                                            html.P(
                                                "Statistical Summary of Daily Patronage for 2019:"
                                            ),
                                        html.Div(
                                                [
                                            html.Div(
                                                [
                                                    html.Table(
                                                        make_dash_table(StatisticalSummaryofDailyPatronageofBakarIndoorPoolfor2019),
                                                        className="tiny-header",
                                                                )
                                                ],
                                                style={"overflow-x": "auto"},
                                                    ),
                                                ],
                                                className="twelve columns",
                                                ),
                                        html.Div(
                                                [
                                            html.Div([
                                                html.P("The two plots below shows the Histogram & Boxplot of patronage for \
                                                all Aquatic Activities per day for the entire dataset in 2019:"),
                                                html.Img(
                                                src=app.get_asset_url("hist1.png"),
                                                className="plot",
                                                        ),
                                                html.P("The distribution of total daily patronage follows a normal distribution \
                                                skewing to the right, with a daily average of 136 patrons. The right-skewing in \
                                                the histogram can be explained by a many handful of outliers where attendance was \
                                                very high (with a recorded maximum of 679 daily patrons)."),
                                                html.Img(
                                                src=app.get_asset_url("boxplot1.png"),
                                                className="plot",
                                                        ),
                                                html.P("From the boxplot above, note that the median is equal to 106 daily patrons, a useful comparative statistic to the mean (shown as the green triangle), as the median is less suceptible to outlier values. That being said, since the distribution is approximately Gaussian (bell-curved), the mean should be approximate to the “real mean” of the population; i.e. the average daily patronage if we had 100% of all tallies recorded."),
                                                    ],),
                                                ],
                                                ),
                                            
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
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
