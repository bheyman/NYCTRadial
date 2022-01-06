# NYCTRadial

This is a simple project that I made when I was wondering how much of the City of New York is within walking distance to a subway stop.
Because the subway system is fully connected, this map becomes a view of the city if you are only willing to walk some fixed distance to and from a subway stop.
It also nicely highlights areas where subway service could/should be expanded, moreso that simply looking at the subway map.

The project works by first reading in Subway station data from New York's open data portal.
The data is read in CSV format and stored into a pandas dataframe.
Any columns that are not the station's latitude or longitude are dropped.
Next, any identical rows are dropped for the dataframe.
There will be identical rows because the dataset lists every subway entrance/exit.
We only want a single datapoint for each subway station.

Folium is used to generate a map centered on New York.
I used the 'Stamen Toner' tiles because it is the easiest to distinguish between land and water.
For every station in the system, I draw a blue circle on the map with a radius of 0.5 miles.
I chose 0.5 miles because this is roughly how far I would be willing to walk to a subway stop.
At an average human walking speed of 3 miles per hour, this equates to a ten minute walk.

Lastly, I used the borough boundary map provided by https://github.com/dwillis/nyc-maps to draw a red line around the boroughs.
Upon running the script, the map is produced in the directory.

## Future Work

1. Cut off any blue that exceeds the boundary of the city.
2. Add a slider that allows the user to change the radius of the circles.
3. Provide stats on how much of each borough is covered.
4. Allow the user to add in their own stops and display how much additional land is covered and what percent of the circle covered new land.
