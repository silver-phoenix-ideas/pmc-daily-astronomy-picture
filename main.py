# Imports
import requests
import streamlit as st

# Configurations
api_title = "Astronomy Picture of the Day"
endpoint = "https://api.nasa.gov/planetary/apod"
params = {
    "api_key": st.secrets["API_KEY"]
}

# Request
response = requests.get(endpoint, params)
content = response.json()

media_url = content["url"]
media_type = content["media_type"]
media_copyright = content["copyright"] if "copyright" in content else ""

title = content["title"]
description = content["explanation"]

# Web App
st.set_page_config(title + " | " + api_title)

st.title(api_title)

match media_type:
    case "image":
        st.image(media_url)
    case "video":
        st.video(media_url)

if media_copyright:
    st.caption("Copyright: " + media_copyright)

st.header(title)
st.text(description)
