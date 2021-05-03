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
python Ward49_import.py
'''

## Results


## Built With


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)
