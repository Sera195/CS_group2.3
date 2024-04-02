import streamlit as st
import requests
import gmaps

# API key for accessing the Google Maps API
API_KEY = "AIzaSyCczAYQAMPwcBfIM6R6ncLpwrK_-lE8BF8"

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
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        display_directions(data)
    else:
        st.error("Error in request:", response.status_code)

def show_directions_multiple_origins(destination, origin1, origin2):
    url_origin1 = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin1}&destination={destination}&key={API_KEY}"
    url_origin2 = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin2}&destination={destination}&key={API_KEY}"
    
    response_origin1 = requests.get(url_origin1)
    response_origin2 = requests.get(url_origin2)
    
    if response_origin1.status_code == 200 and response_origin2.status_code == 200:
        data_origin1 = response_origin1.json()
        data_origin2 = response_origin2.json()
        
        display_directions(data_origin1, color="blue")
        display_directions(data_origin2, color="red")
    else:
        st.error("Error in request:", response_origin1.status_code, response_origin2.status_code)

def display_directions(data, color="blue"):
    if "routes" in data and data["routes"]:
        start_location = (
            data["routes"][0]["legs"][0]["start_location"]["lat"],
            data["routes"][0]["legs"][0]["start_location"]["lng"],
        )
        end_location = (
            data["routes"][0]["legs"][0]["end_location"]["lat"],
            data["routes"][0]["legs"][0]["end_location"]["lng"],
        )

        gmaps.configure(api_key=API_KEY)
        fig = gmaps.figure()
        transit_layer = gmaps.directions_layer(
            start=start_location,
            end=end_location,
            travel_mode="TRANSIT",
            stroke_color=color,
            stroke_weight=3.0,
            stroke_opacity=1.0,
        )
        fig.add_layer(transit_layer)
        st.write(fig)
    else:
        st.warning("No routes found.")

if __name__ == "__main__":
    main()