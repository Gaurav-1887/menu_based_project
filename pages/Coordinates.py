import streamlit as st
import requests

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown')
        state = data.get('region', 'Unknown')
        return lat, long, city, state
    except Exception as e:
        st.error("Internet Not available or unable to fetch location.")
        return None


st.title("GPS Using Python")

# Button to fetch location coordinates
if st.button("Get Location Coordinates"):
    result = locationCoordinates()
    if result:
        lat, long, city, state = result
        st.write(f'The coordinates and location are: {lat}, {long}, {city}, {state}')
    else:
        st.write("Could not fetch location coordinates.")

