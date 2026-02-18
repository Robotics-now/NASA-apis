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

st.title(f'Astronomy picture of {data["date"]}')
st.subheader(data['title'])
st.image(data['hdurl'])
st.divider()
st.write(data['explanation'])
st.write('')
st.session_state["date"] = st.date_input("Select previous date", max_value=date.today(), key="date_picker", on_change=update_date)
