import streamlit as st
import requests

# Query an external API for the public IP
try:
    server_public_ip = requests.get('https://api.ipify.org').text
except Exception as e:
    server_public_ip = "Could not resolve IP"

st.write(f"Server's Public IP Address: {server_public_ip}")
