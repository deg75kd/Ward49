from myapp import app
import os
import numpy as np
import pandas as pd
import json
from flask import render_template, request
from geopy.geocoders import Nominatim
import folium

# print("Defining pages")

@app.route('/')
@app.route('/index')
def index():
    """Render the main portfolio page

    Args:
        None

    Returns:
        index.html page
    """
    # Load data
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/Ward49.xlsx')
    ward49_df = pd.read_excel(filename)

    # replace NaN values
    ward49_df.fillna('', inplace=True)

    # get list of location types
    location_type_list = ward49_df['loc_type_sec'].drop_duplicates().sort_values().to_list()

    # Get approximate coordinates for Ward 49
    address = 'Rogers Park, Chicago, IL'
    geolocator = Nominatim(user_agent='chi_explorer')
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    # Create map
    chicago_map = folium.Map(location=[latitude, longitude],
                             width='100%',
                             height='100%',
                             zoom_start=14)

    fgroup = []
    for i in range(len(location_type_list)):
        fgroup.append(folium.FeatureGroup(name=location_type_list[i],
                                          overlay=True,
                                          show=False).add_to(chicago_map))
        for row in ward49_df[ward49_df['loc_type_sec'] == location_type_list[i]].itertuples():
            if row.loc_type_pri == "Park":
                cir_color = "green"
            elif row.loc_type_pri == "Police":
                cir_color = "blue"
            elif row.loc_type_pri == "Fire Station":
                cir_color = "red"
            elif row.loc_type_pri == "School":
                cir_color = "orange"
            elif row.loc_type_pri == "Library":
                cir_color = "yellow"
            else:
                cir_color = "grey"
                
            tooltip_label = row.name + " " + row.loc_type_sec
            # popup_label = "{} {} {}".format(row.name, row.loc_type_sec, row.address)
            if not row.address:
                popup_label = "{} {}".format(row.name, row.loc_type_sec)
            else:
                popup_label = "{} {} {}".format(row.name, row.loc_type_sec, row.address)
                
            label = folium.Popup(html=popup_label, parse_html=True)
            fgroup[i].add_child(folium.CircleMarker(
                [row.latitude, row.longitude],
                radius=5,
                popup=label,
                tooltip=tooltip_label,
                color=cir_color,
                fill=True,
                fill_opacity=0.7).add_to(chicago_map)
            )
        
    folium.LayerControl().add_to(chicago_map)

    return chicago_map._repr_html_()