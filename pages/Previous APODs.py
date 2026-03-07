import requests as rq
import streamlit as st

from datetime import date, timedelta

yesterday = (date.today() - timedelta(days=1))


if "date" not in st.session_state:
    st.session_state["date"] = yesterday
    st.rerun()

def update_date():
    st.session_state["date"] = st.session_state.date_picker

api_key = st.secrets["nasa"]["api_key"]
formatted_date = st.session_state["date"].isoformat()
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={formatted_date}'


request = rq.get(api_url)
data = request.json()

try:
    url = data['hdurl']
except KeyError:
    url = data['url']
img_data = rq.get(url).content


if data['media_type'] == 'image':
    title = st.empty()
    title = (st.title(f'Astronomy picture of {data["date"]}') ,st.subheader(data['title']))
    st.image(url)
    st.divider()
    st.write(data['explanation'])
    st.write('')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.session_state["date"] = st.date_input("Select previous date", max_value=yesterday, key="date_picker", on_change=update_date)
    with col2:
        st.write('')
        st.write('')

        st.page_link('Today.py', label='⇾Today\'s APOD')
    # Get the raw bytes directly from the URL

    with col3:  
        st.write("")
        st.write('')
        st.download_button(
            label="Download Image",
            data=img_data,  # This sends the actual image bytes
            file_name=f"{data['date']}.jpg",
            mime="image/jpeg"
)

if data['media_type'] == 'video':
    title = st.empty()
    title = (st.title(f'Astronomy picture of {data["date"]}') ,st.subheader(data['title']))
    st.video(url)
    st.divider()
    st.write(data['explanation'])
    st.write('')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.session_state["date"] = st.date_input("Select previous date", max_value=yesterday, key="date_picker", on_change=update_date)
    with col2:
        st.write('')
        st.write('')

        st.page_link('Today.py', label='⇾Today\'s APOD')
    # Get the raw bytes directly from the URL

    with col3:  
        st.write('')
        st.write('')
        st.download_button(
            label="Download Image",
            data=img_data,  # This sends the actual image bytes
            file_name=f"{data['date']}.jpg",
            mime="image/jpeg"
    )
