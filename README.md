# Chicago Ward 49 Information

## Table of Contents

* [Summary](#summary)
* [File Descriptions](#file-descriptions)
* [Prerequisites](#prerequisites)
* [Running the Code](#running-the-code)
* [Results](#results)
* [Built With](#built-with)
* [License](#license)

## Summary

As a resident of Chicago', I have sometimes wondered what city facilities are near me. Chicago is famously a city of neighborhoods, and my neighborhood maps very closely to the 49th Ward. In this project I set out to map the facilities with the ward. First, I browsed Chicago's public data store for data sets containing the locations of places that might be of interest to many residents - schools, libraries, park facilities, etc. Initially I used Jupyter Notebooks to pull the data using the API to confirm there are locations within the ward. Then I cleaned and consolidated the data sets.

After having a working data set, I used a few other Jupyter Notebooks to try out creating maps. First, I used Folium. Then I tried Plotly but didn't like it as much. I also looked at incorporating data from Foursquare's API. I decided to limit the scope of the project and abandoned those efforts.

The final step was to prepare the map for deployment as a web page. At first I tried to mimic previous projects where I displayed Plotly graphs using Bootstrap. That was no working out, but I found a way to display the map in a more direct manner.

## File Descriptions

* Boundaries - Wards (2015-).geojson - Geographic boundaries of Chicago's wards
* Ward49-boundaries.ipynb - Initial test for working with geospatial data
* Ward49_import.ipynb - Import data using the City of Chicago API
* Ward49_import.py - Standalone script to import and format data
* Ward49_map.ipynb - Create a map of points of interest in Chicago
* Ward49_map.py - Create map as part of web site
* Ward49_plotly.ipynb - Testing maps made with Plotly
* Ward49_foursquare.ipynb - Testing pulling restaurants from Foursquare
* Ward49.xlsx - Locations within ward 49 as identified by import script

## Prerequisites

numpy 1.18.1\
pandas 0.25.3\
python 3.6\
geos 3.9.1\
sodapy 2.1.0\
shapely 1.7.1\
geopy 2.1.0\
folium 0.12.1\
waitress 2.0.0\
flask 1.1.2\
json5 0.9.5

## Running the Code

Import and format the data and save to an Excel file

'''
cd scripts
python Ward49_import.py
'''

Running the web page from a Windows computer

'''
python myapp.py win
'''

The page is accessible at http://127.0.0.1:8080/


## Results


## Built With


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
