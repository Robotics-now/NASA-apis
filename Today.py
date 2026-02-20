import requests as rq
import streamlit as st
from datetime import date, timedelta

yesterday = (date.today() - timedelta(days=1)).isoformat()

api_key = st.secrets["nasa"]["api_key"]
api_url = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&start_date={yesterday}'

request = rq.get(api_url)
data = request.json()


if "button" not in st.session_state:
    st.session_state.button = False

if st.session_state.button == False:
    # ---Regular APOD or today's picture---
    try:
        st.title('Astronomy picture of the day')
        st.subheader(data[-1]['title'])
        st.image(data[-1]['hdurl'])
        st.write("")
        st.write(data[-1]['explanation'])
        st.button("⇽ Yesterday's picture", on_click=lambda: st.session_state.update(button=True), key='button-y')

    except IndexError :
    # ---Recalls the API for 1 day instead of 2---
        
        api_url_for_error = f'https://api.nasa.gov/planetary/apod?api_key={api_key}&date={yesterday}'
        request_for_error = rq.get(api_url_for_error)
        data2 = request_for_error.json()

        st.title('Astronomy picture of the day')
        st.subheader(data2['title'])
        st.image(data2['hdurl'])
        st.write("")
        st.write(data2['explanation'])
        st.button("⇽ Yesterday's picture", on_click=lambda: st.session_state.update(button=True), key='button-y')

if st.session_state.button == True:
    # ---Yesterday's picture if the usre clicks the button---

    st.title('Astronomy picture of the day')
    st.subheader(data[0]['title'])
    st.image(data[0]['hdurl'])
    st.write("")
    st.write(data[0]['explanation'])
    st.button("⇾ Today's picture", on_click=lambda: st.session_state.update(button=False), key='button-t')

