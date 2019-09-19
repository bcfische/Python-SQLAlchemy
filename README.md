Surfs Up!

Here, we use SQLAlchemy ORM queries, Pandas, and Matplotlib to do basic climate analysis and data exploration of a Hawaii climate
database (Steps 1-3). Then, we design an application using Flask API to display the data and results (Step 4).

Step 1 - Precipitation Analysis
~Design a query to retrieve the last 12 months of precipitation data.
~Select only the date and prcp values.
~Load the query results into a Pandas DataFrame and set the index to the date column.
~Sort the DataFrame values by date.
~Plot the results using the DataFrame plot method.
~Use Pandas to print the summary statistics for the precipitation data.

Step 2 - Station Analysis
~Design a query to calculate the total number of stations.
~Design a query to find the most active stations.
~List the stations and observation counts in descending order.
~Which station has the highest number of observations?
~Design a query to retrieve the last 12 months of temperature observation data (tobs).
~Filter by the station with the highest number of observations.
~Plot the results as a histogram with bins=12.

Step 3 - Temperature Analysis
~Use the calc_temps function to calculate the min, avg, and max temperatures using the matching dates from the previous year,
and plot as bar chart.

Step 4 - Climate App Queries/Routes
~Home page to list all available routes (/)
~JSON dictionary of dates and precipitation values (/api/v1.0/precipitation)
~JSON list of stations (/api/v1.0/stations)
~JSON list of temperature observations for the previous year (/api/v1.0/tobs)
~JSON list of the min, avg, and max temperatures for the given date range (/api/v1.0/<start> and /api/v1.0/<start>/<end>)
