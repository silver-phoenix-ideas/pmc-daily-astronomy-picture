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

img_url = content["url"]
img_title = content["title"]
img_description = content["explanation"]
img_copyright = content["copyright"] if "copyright" in content else ""

# Web App
st.set_page_config(img_title + " | " + api_title)

st.title(api_title)
st.image(img_url)

if img_copyright:
    st.caption("Copyright: " + img_copyright)

st.header(img_title)
st.text(img_description)
