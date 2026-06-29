import streamlit as st
import requests

@st.cache_data
def get_server_location():
    try:
        # Fetch public IP and location of the server
        response = requests.get("https://ipinfo.io")
        data = response.json()
        return data.get("country"), data.get("city"), data.get("region")
    except Exception as e:
        return "Unknown", "Unknown", "Unknown"

country, city, region = get_server_location()
st.write(f"Server Location: {city}, {region}, {country}")
