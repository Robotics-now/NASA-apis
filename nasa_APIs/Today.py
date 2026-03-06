import requests as rq
import streamlit as st
from datetime import date, timedelta


yesterday = (date.today() - timedelta(days=1)).isoformat()
today = date.today().isoformat()

api_key = st.secrets["nasa"]["api_key"]
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

request = rq.get(api_url)
data = request.json()

try:
    title = data['title']
    url = data['hdurl']
    explanation = data['explanation']
    image_type = data['media_type']
except KeyError:
    title = data['title']
    url = data['url']
    explanation = data['explanation']




if image_type == 'image':
    st.title('Astronomy picture of the day')
    st.subheader(title)
    st.image(url)
    st.write("")
    st.write(explanation)
    with st.container(border=True):
        col1, col2,  = st.columns(2)
        
        with col1:
            st.page_link('pages/Previous APODs.py', label='⇽Previous APODs')
        with col2:
            st.download_button(
            label="Download Image",
            data=img_data,  # This sends the actual image bytes
            file_name=f"{data['date']}.jpg",
            mime="image/jpeg"
    )

elif image_type == 'video':
    st.title('Astronomy picture of the day')
    st.subheader(title)
    st.video(url)
    st.write("")
    st.write(explanation)
    with st.container(border=True):
        col1, col2,  = st.columns(2)
        
        with col1:
            st.page_link('pages/Previous APODs.py', label='⇽Previous APODs')
        with col2:
            st.download_button(
            label="Download Image",
            data=img_data,  # This sends the actual image bytes
            file_name=f"{data['date']}.jpg",
            mime="image/jpeg"
    )

