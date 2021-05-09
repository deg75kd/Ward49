#!/usr/bin/env python
# coding: utf-8

# Import pandas library using an alias
import pandas as pd
# library to handle data in a vectorized manner
import numpy as np

# Converts JSON data to list of dictionaries
from sodapy import Socrata

# Find if a point is within a geographic polygon
from shapely.geometry import shape, Point

# To read json data
import json

# Define boundaries of Ward 49
# https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Wards-2015-/sp34-6z76
f = open('Boundaries - Wards (2015-).geojson')
data = json.load(f)

for feature in data['features']:
    if feature['properties']['ward'] == "49":
        ward49_poly = shape(feature['geometry'])

# Import Library Data
client = Socrata("data.cityofchicago.org", None)
results = client.get("x8fc-8rcq", limit=2000)
library_df = pd.DataFrame.from_records(results)

# Drop unwanted columns
column_drop_list = [':@computed_region_rpca_8um6',
                    ':@computed_region_vrxf_vc4k',
                    ':@computed_region_6mkv_f3dw',
                    ':@computed_region_bdys_3d7i',
                    ':@computed_region_43wa_7qmu']
library_df.drop(column_drop_list, axis=1, inplace=True)

# Fill missing data
library_df['hours_of_operation'].replace(np.nan, "Not listed", inplace=True)

# Separate longitude and latitude
library_df['latitude'] = pd.to_numeric(library_df['location'].apply(lambda x: x['latitude']))
library_df['longitude'] = pd.to_numeric(library_df['location'].apply(lambda x: x['longitude']))
library_df.drop('location', axis=1, inplace=True)

# Separate URL
library_df['url'] = library_df['website'].apply(lambda x: x['url'])
library_df.drop('website', axis=1, inplace=True)

# Fix column name
library_df.rename(columns={'name_':'name'}, inplace=True)

# Add location type columns
library_df['loc_type_pri'] = "Library"
library_df['loc_type_sec'] = "Library"

# Import School Data
#https://data.cityofchicago.org/resource/p83k-txqt.json
results = client.get("p83k-txqt", limit=2000)
schools_df = pd.DataFrame.from_records(results)

# Drop unwanted columns
column_drop_list = ['the_geom','school_id',
                    ':@computed_region_rpca_8um6',
                    ':@computed_region_vrxf_vc4k',
                    ':@computed_region_6mkv_f3dw',
                    ':@computed_region_bdys_3d7i',
                    ':@computed_region_43wa_7qmu']
schools_df.drop(column_drop_list, axis=1, inplace=True)

# Convert longitude/latitude to numbers
schools_df['lat'] = pd.to_numeric(schools_df['lat'])
schools_df['long'] = pd.to_numeric(schools_df['long'])

# Function to convert school types
def convert_schools_type(col):
    if col == 'ES':
        return 'Elementary School'
    elif col == 'HS':
        return 'High School'
    else:
        return 'School'

# Apply function
schools_df['loc_type_sec'] = schools_df.apply(lambda x: convert_schools_type(x['grade_cat']), axis=1)
schools_df.drop('grade_cat', axis=1, inplace=True)

# change names to match first dataset
schools_df.rename(columns={'short_name': 'name',
                           'lat': 'latitude',
                           'long': 'longitude'},
                  inplace=True)

# Add location type
schools_df['loc_type_pri'] = "School"

# Fix capitalization
schools_df['name'] = schools_df['name'].str.title()
schools_df['address'] = schools_df['address'].str.title()

# Import police stations
#https://data.cityofchicago.org/resource/z8bn-74gv.json
results = client.get("z8bn-74gv", limit=2000)
police_df = pd.DataFrame.from_records(results)

# Drop unwanted columns
column_drop_list = ['district',
                    'x_coordinate',
                    'y_coordinate',
                    'location',
                    'fax',
                    'tty',
                    ':@computed_region_rpca_8um6',
                    ':@computed_region_vrxf_vc4k',
                    ':@computed_region_6mkv_f3dw',
                    ':@computed_region_bdys_3d7i',
                    ':@computed_region_43wa_7qmu',
                    ':@computed_region_awaf_s7ux']
police_df.drop(column_drop_list, axis=1, inplace=True)

# Extract URL
police_df['url'] = police_df['website'].apply(lambda x: x['url'])
police_df.drop(['website'], axis=1, inplace=True)

# Rename columns
police_df.rename(columns={'district_name':'name'}, inplace=True)

# Add location types
police_df['loc_type_pri'] = "Police"
police_df['loc_type_sec'] = "Police"

# Convert longitude/latitude to numbers
police_df['latitude'] = pd.to_numeric(police_df['latitude'])
police_df['longitude'] = pd.to_numeric(police_df['longitude'])

# Import public health clinics
#https://data.cityofchicago.org/resource/kcki-hnch.json
results = client.get("kcki-hnch", limit=2000)
clinic_df = pd.DataFrame.from_records(results)
# Nothing in Ward 49

# Import park facilities
#https://data.cityofchicago.org/resource/eix4-gf83.json
results = client.get("eix4-gf83", limit=4500)
parks_df = pd.DataFrame.from_records(results)

# Rename columns
parks_df.rename(columns={'park':'name',
                         'facility_n':'loc_type_sec',
                         'x_coord':'longitude',
                         'y_coord':'latitude'},
                inplace=True)

# Drop unwanted columns
column_drop_list = ['objectid','park_no','the_geom','facility_t','gisobjid']
parks_df.drop(column_drop_list, axis=1, inplace=True)

# Drop duplicates
parks_df.drop_duplicates(subset=['name','loc_type_sec'],
                         keep='first',
                         inplace=True)

# Convert longitude/latitude to numbers
parks_df['longitude'] = pd.to_numeric(parks_df['longitude'])
parks_df['latitude'] = pd.to_numeric(parks_df['latitude'])

# Add location type
parks_df['loc_type_pri'] = 'Park'

# Fix capitalization
parks_df['name'] = parks_df['name'].str.title()
parks_df['loc_type_sec'] = parks_df['loc_type_sec'].str.title()

# Import fire stations
#https://data.cityofchicago.org/resource/28km-gtjn.json
results = client.get("28km-gtjn", limit=2000)
fire_df = pd.DataFrame.from_records(results)

# Drop unwanted columns
column_drop_list = ['engine',
                    ':@computed_region_rpca_8um6',
                    ':@computed_region_vrxf_vc4k',
                    ':@computed_region_6mkv_f3dw',
                    ':@computed_region_bdys_3d7i',
                    ':@computed_region_43wa_7qmu',
                    ':@computed_region_awaf_s7ux']
fire_df.drop(column_drop_list, axis=1, inplace=True)

# Extract longitude/latitude
fire_df['longitude'] = pd.to_numeric(fire_df['location'].apply(lambda x: x['longitude']))
fire_df['latitude'] = pd.to_numeric(fire_df['location'].apply(lambda x: x['latitude']))
fire_df.drop(['location'], axis=1, inplace=True)

# Add location types
fire_df['loc_type_pri'] = 'Fire Station'
fire_df['loc_type_sec'] = 'Fire Station'

# Fix capitalization
fire_df['address'] = fire_df['address'].str.title()
fire_df['city'] = fire_df['city'].str.title()

# Merge datasets
poi_df = pd.concat([library_df, schools_df, police_df, parks_df, fire_df], ignore_index=True)

# Create Empty Dataset for Ward Locations
df_column_list = poi_df.columns.to_list()
ward49_df = pd.DataFrame(columns=df_column_list)

# Change data type for longitude/latitude to numbers
ward49_df['latitude'] = ward49_df['latitude'].astype(float)
ward49_df['longitude'] = ward49_df['longitude'].astype(float)

# Save Ward 49 Locations to New Dataset
entries = {}
for index, row in poi_df.iterrows():
    point = Point(row['longitude'], row['latitude'])
    if ward49_poly.contains(point):
        ward49_df = ward49_df.append(poi_df.loc[index])

# Drop duplicate information
ward49_df.drop(ward49_df[ward49_df['loc_type_sec'] == 'Basketball Backboard'].index, inplace=True)

# A fitness course is not a location
ward49_df.drop(ward49_df[ward49_df['loc_type_sec'] == 'Fitness Course'].index, inplace=True)

# Rename "playground park" to "playground"
ward49_df.loc[ward49_df['loc_type_sec'] == 'Playground Park', 'loc_type_sec'] = "Playground"

# Remove "Beach" from name
ward49_df['name'] = ward49_df['name'].apply(lambda x: x.replace('Beach',''))

# remove NaN
ward49_df.fillna(value='', inplace=True)

# Save data as file
ward49_df.to_excel(excel_writer='Ward49.xlsx',
                    sheet_name='Sheet1',
                    columns=df_column_list, 
                    header=True, 
                    index=False, 
                    verbose=True)
