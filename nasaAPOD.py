import requests
import streamlit as st

st.set_page_config(page_title="Astronomy Picture of the Day", page_icon="🔭")

api_key = st.secrets["nasa"]["api_key"]
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

request = requests.get(api_url)
data = request.json()

st.title('Astronomy picture of the day')
st.subheader(data.get('title', 'No title available'))
st.image(data.get('hdurl', None))
st.write(data.get('explanation', 'No explanation available'))
