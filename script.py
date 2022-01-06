import folium
import pandas as pd

data = pd.read_csv('https://data.ny.gov/api/views/i9wp-a4ja/rows.csv?accessType=DOWNLOAD&sorting=true')
for i in data.columns:
  if(i != 'Station Longitude' and i != 'Station Latitude'):
    data = data.drop(columns=i)

data = data.drop_duplicates()

m = folium.Map(location=[40.7128, -74.0060], tiles='Stamen Toner', zoom_start=12)
for index, station in data.iterrows():
  folium.Circle(location=[station['Station Latitude'],station['Station Longitude']], radius=804.672, fill_color='blue', color=None, fill_opacity=1.0).add_to(m)

folium.Choropleth('https://raw.githubusercontent.com/dwillis/nyc-maps/master/boroughs.geojson', name="geojson", fill_color='transparent', line_weight=3, line_color='red').add_to(m)
m.save('file.html')
m
