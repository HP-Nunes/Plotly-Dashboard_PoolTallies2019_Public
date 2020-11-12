# Plotly Dashboard: 2019 Analysis of Pool Tallies

<img src= assets/pool-underwater.jpg width=100% height="100">
***
## Description

This dashboard summarizes patronage attendance over time and by aquatic programming activities. Analog records were digitized, and the subsequent dataset was wrangled with Python Pandas in Jupyter Notebook.

I was tasked with: observing and describing seasonal and annual patronage trends over the course of 2019, and consider two specific case studies which would help facility staff with future scheduling and planning.

## Summary

In 2019, a pool was patronized at least 43,067 times over the course of 324 days; an average patronage of 133 times per day. Lifeguards, who are tasked with tallying pool attendance every 30 minutes on the 15-minute mark, recorded collectively 5,581 tallies, totaling 167,430 minutes worth of data, or an average of 9 operational pool hours per day (out of an estimated maximum of 12 hours on most days). Although Lap Swim was the pool activity which saw the most cumulative annual patronage (nearly a third of all patrons), the busiest days occurred during Family Swim programming on weekends. 

Included in this report are two case studies: 1) a comparison of patronage between weekends with scheduled lessons and those with none, and 2) attendance trends in early morning Lap Swim weekday patronage.

Throughout the report, “patronage“ refers to the usage of the facility by undefined individuals. That is, we cannot assess whether these were unique or reoccuring patrons for any given time. The tallying dataset would require to be appropriately normalized to derive such a metric.

The Water Exercise category included tallies for both Water Walking and Aqua Fit.

## Recommendations

The following are a set of recommendations moving forward in order to ensure that future tallying records improve in accuracy, fidelity, and completedness, with the intent to generate greater patronage insights:
* A Well-Defined and Consistent Data-Entry Protocol: Consistently digitizing the records on a regular basis (weekly preferrably) would allow to identify tallying errors or incoherences between programming and attendance. It would also decrease the risk of data-entry errors, or data loss (as shown with the four weeks' worth of missing tallies in the Fall).
* Tally Annotations: Perhaps adding a section on the Tally Sheets to make note of 'irregularities' either in scheduling or activity would allow for higher accuracy during data-entry.
* Tallying Accountability: Although tallying is not the most important or pressing of tasks, lifeguards are nonetheless liable to tally and should be able to do so consistently. Thus, a tally completedness score per scheduling cycles would permit to evaluate overall staff performance on the matter, but also ensure that enough tallies are collected on a daily basis so that meaningful inferences about long-term trends can be made.
* Normalizing Patronage to Unique Patrons: either through the use of selective sampling or a survey, normalize patronage down to unique patrons. This would allow to derive a supplementary and meaningful metric for analysis.

***
## TechStack 

* Python Pandas
* Numpy
* Seaborn
* Plotly
* Gunicorn
* Dash

Deployed via Heroku.
