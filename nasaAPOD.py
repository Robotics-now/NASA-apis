import requests
import streamlit as st
from dotenv import load_dotenv
from os import getenv

# Make sure to create a .env file.
load_dotenv()

api_key = getenv('NASA_APOD_API_KEY')
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

request = requests.get(api_url)
data = request.json()

st.title('Astronomy picture of the day')
st.subheader(data['title'])
st.image(data['hdurl'])
st.write(data['explanation'])
