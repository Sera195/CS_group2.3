import streamlit as st
import gmaps

# API key for accessing the Google Maps API
API_KEY = "AIzaSyBpjEKrlbfkGbVUU8LgiaBFVPHvCADIVgY"

# Configure gmaps with your API key
gmaps.configure(api_key=API_KEY)

# Create a Google Maps figure
fig = gmaps.figure()

# Display the figure using Streamlit
st.write(fig)