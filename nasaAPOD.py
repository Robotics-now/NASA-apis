import requests
import streamlit as st
from datetime import date, timedelta

st.set_page_config(page_title="Astronomy Picture of the Day", page_icon="🔭")

api_key = st.secrets["nasa"]["api_key"]
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={yesterday}'
yesterday = (date.today() - timedelta(days=1)).isoformat()

request = rq.get(api_url)
data = request.json()


if "button" not in st.session_state:
    st.session_state.button = False

if st.session_state.button == False:
    # regular APOD or today's picture

    st.title('Astronomy picture of the day')
    st.subheader(data[1]['title'])
    st.image(data[1]['hdurl'])
    st.write("")
    st.write(data[1]['explanation'])
    st.button("⇽ Yesterday's picture", on_click=lambda: st.session_state.update(button=True), key='button-y')

if st.session_state.button == True:
    # yesterday's picture

    st.title('Astronomy picture of the day')
    st.subheader(data[0]['title'])
    st.image(data[0]['hdurl'])
    st.write("")
    st.write(data[0]['explanation'])
    st.button("⇾ Today's picture", on_click=lambda: st.session_state.update(button=False), key='button-t')

