import streamlit as st
import gmaps

API_KEY = "AIzaSyBpjEKrlbfkGbVUU8LgiaBFVPHvCADIVgY"

gmaps.configure(api_key=API_KEY)

fig = gmaps.figure()

st.write(fig)