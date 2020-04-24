# -*- coding: utf-8 -*-
import dash_html_components as html
from utils import Header


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
                                    "Compare the rate of Patronage during Early Lap Swim from 5:30 to 8am, between\
                                    Monday-Wednesday-Friday."
                                            ),
                            html.Br([]),
                            html.Div(
                        [
                            html.H6(
                                "Hourly Average Patronage between 5:30-8am, early Lap Swim",
                                className="subtitle padded",
                            ),
                            html.Iframe(src = "//plotly.com/~HP-Nunes/247.embed",width="100%", height="400")
                            ]),
                            html.Br([]),
                            html.H6("Key Observations", className="subtitle padded"),
                            html.Li("There are on average approximately two patrons present when the first tally is taken at 5:45 am."
                                   ),
                            html.Li("Early morning Lap Swim is most busy on Wednesdays at 7:45am, with over three patrons on average."
                                   ),
                             html.Li("Patronage is below average on Friday mornings, whereas Wednesday sees above average patronage after 6:45am."
                                   ),
                             html.Li("Early Lap Swim tends to be the least busy of timeslots for Lap Swim, with some noted exceptions such as Fridays at 4pm."
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
