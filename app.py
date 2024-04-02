import streamlit as st
import gmaps

API_KEY = ""

gmaps.configure(api_key=API_KEY)

fig = gmaps.figure()

st.write(fig)