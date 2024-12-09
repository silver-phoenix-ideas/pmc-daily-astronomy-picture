# Imports
import requests
import streamlit as st

# Configurations
api_title = "Astronomy Picture of the Day"
endpoint = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": st.secrets["API_KEY"],
    "thumbs": True
}

# Request
response = requests.get(endpoint, params)
content = response.json()

print(content)
