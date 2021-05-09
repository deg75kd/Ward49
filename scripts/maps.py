import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim
import folium

def return_maps():
    """Creates folium map

    Args:
        None

    Returns:
        list (dict): list containing the map visualization
    """
    # Load data
    ward49_df = pd.read_excel('Ward49.xlsx')

    # get list of location types
    location_type_list = ward49_df['loc_type_sec'].drop_duplicates().to_list()

    # Get approximate coordinates for Ward 49
    address = 'Rogers Park, Chicago, IL'
    geolocator = Nominatim(user_agent='chi_explorer')
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude

    # 
    map_one = []
    
    for genre in genre_list:
        length_list = lyrics_df[lyrics_df['genre'] == genre]['lyrics-length'].values.tolist()
        map_one.append(
            go.Box(
                y = length_list,
                name = genre
            )
        )
    layout_four = dict(title = 'Lyric Lengths by Genre')

    # append all charts to the maps list
    maps = []
    maps.append(dict(data=map_one, layout=layout_four))

    return maps