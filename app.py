pip install streamlit-gmaps

import streamlit as st
import streamlit_gmaps as sg
from streamlit_gmaps import generate_static_map, configs

def main():
    st.title("Directions App")
    
    # Input fields
    destination = st.text_input("Enter your destination:")
    origin = st.text_input("Enter a starting point:")
    origin2 = st.text_input("Enter a second starting point (leave blank if not applicable):")

    # Check if second origin provided
    if origin2:
        show_directions_multiple_origins(destination, origin, origin2)
    else:
        show_directions_single_origin(destination, origin)

def show_directions_single_origin(destination, origin):
    # Code for directions with single origin

def show_directions_multiple_origins(destination, origin1, origin2):
    # Code for directions with multiple origins

def display_directions(data, color="blue"):
    # Code for displaying directions

if __name__ == "__main__":
    main()