import requests as rq
import streamlit as st
from datetime import date, timedelta
from urllib.parse import urlparse
import os

st.set_page_config(page_title="Today's APOD', page_icon='https://github.com/Robotics-now/robotics-now/blob/main/assets/Logo_new.png")
st.logo("https://github.com/Robotics-now/robotics-now/blob/main/assets/Logo_new.png?raw=true", size='large')

api_key = st.secrets["nasa"]["api_key"]
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}'

request = rq.get(api_url)
data = request.json()

print('API data has been retrived.')

# -- Makes sure the 'hdurl' key exists, if not is gets the 'url' key from the api --
try:
    if 'error' in data.keys():
        st.error('The api ran into a error.')
    else:
        url = data['hdurl']
        print(f'Image/video url -> {url}')
        explanation = data['explanation']
        print(f'Explanation -> {explanation}')
        image_type = data['media_type']
        print(image_type)
except KeyError:
    print(data.keys())
    image_type = data['media_type']
    url = data['url']
    explanation = data['explanation']

# -- Extention bridge --    
st.markdown(f'<div id="nasa-url-bridge" style="display:none">{url}</div>', unsafe_allow_html=True)

img_data = rq.get(url).content

# -- Gets the file extension of the url --
parsed_url = urlparse(url)
path = parsed_url.path 
file_base, file_extension = os.path.splitext(path)


# -- If the media is a image --
if image_type == 'image':
    st.title('Astronomy picture of the day')
    st.subheader(data['title'])
    st.image(url)
    st.write('')
    st.write(explanation)
    with st.container(border=True):
        col1, col2,  = st.columns(2)
        
        with col1:
            st.write('')
            st.page_link('pages/Previous APODs.py', label='⇽Previous APODs')
        with col2:
            st.download_button(
            label="Download Image",
            data=img_data,  # This sends the actual image bytes
            file_name=f"{data['date']}{file_extension}",
            mime="image/jpeg"
    )

# -- If the media is a video --
elif image_type == 'video':
    st.title('Astronomy picture of the day')
    st.subheader(data['title'])
    st.video(url)
    st.write("")
    st.write(explanation)
    with st.container(border=True):
        col1, col2,  = st.columns(2)
        
        with col1:
            st.write('')
            st.page_link('pages/Previous APODs.py', label='⇽Previous APODs')
        with col2:
            st.download_button(
            label="Download Video",
            data=img_data,  # This sends the actual image bytes
            file_name=f"{data['date']}{file_extension}",
            mime="image/jpeg"
    )

