# sqlalchemy-challenge
*SQL Alchemy Homework:* This assignment used a SQLite database to extract data on weather measurements at weather stations in Hawaii. The data was first explored to find any interesting insights, using SQLAlchemy to query the database. Then, an API app was created to query the database and return JSON results when a user selects certain endpoint routes. Two bonus parts were also completed to further analyze the data to discover any additional insights into the weather patterns.

***Resources Folder:***
- hawaii.sqlite
- hawaii_measurements.csv
- hawaii_stations.csv

***Images Folder:***
- PNG images of the graphs generated for the analysis

**climate_analysis.ipynb:**
- This file contains the initial climate analysis and exploration of the SQLite database provided and shows graphs that were generated to better understand trends in the data. The database was queried using SQLAlchemy ORM queries, Pandas, and Matplotlib.
- This file also contains an analysis and exploration of the weather stations in Hawaii, discovering which station is the most active with the highest number of observations over time.

**app.py:**
- This file contains code that runs an API app that returns JSON responses for different queries, depending on which endpoint the user selects.
- In this app, the user can also input their own start and/or end date to discover the minimum, maximum, and average temperature for that range of dates.

**temp_analysis_bonus_1.ipynb:**
- This file contains a bonus section of the assignment, which looks at the average temperatures in Hawaii in June and December. The objective is to look at the statisical significance of the difference between temperatures in Hawaii in these two months.

**temp_analysis_bonus_2.ipynb:**
- This file contains a second bonus section of the assignment, which finds the historical temperature highs, lows, and averages for a specified date range, over all of the years contained in the database.
- The daily rainfall averages and daily temperature normals are also provided, to give the user the most relevant data concerning their upcoming trip to Hawaii.

