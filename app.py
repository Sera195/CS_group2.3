import streamlit as st

import requests
import gmaps

# API key for accessing the Google Maps API
API_KEY = "AIzaSyCczAYQAMPwcBfIM6R6ncLpwrK_-lE8BF8"

# Destination point
destination = input("Enter your destination: ")

# Start and destination points
origin = input("Enter a starting point: ")
origin2 = input("Enter a second starting point (leave blank if not applicable): ")

# Determine if the second starting point is provided
if origin2:
    # URL for the Directions API request for the first starting point
    url_origin = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"

    # URL for the Directions API request for the second starting point
    url_origin2 = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin2}&destination={destination}&key={API_KEY}"

    # Send HTTP GET requests
    response_origin = requests.get(url_origin)
    response_origin2 = requests.get(url_origin2)

    # Check if the requests were successful (Status Code 200)
    if response_origin.status_code == 200 and response_origin2.status_code == 200:
        # Extract data from the responses (JSON format)
        data_origin = response_origin.json()
        data_origin2 = response_origin2.json()

        # Configure gmaps
        gmaps.configure(api_key=API_KEY)
        fig = gmaps.figure()

        # Check if routes exist for the first starting point
        if "routes" in data_origin and data_origin["routes"]:
            # Add direction layers for the first starting point
            start_location_origin = (
                data_origin["routes"][0]["legs"][0]["start_location"]["lat"],
                data_origin["routes"][0]["legs"][0]["start_location"]["lng"],
            )
            end_location_origin = (
                data_origin["routes"][0]["legs"][0]["end_location"]["lat"],
                data_origin["routes"][0]["legs"][0]["end_location"]["lng"],
            )
            transit_layer_origin = gmaps.directions_layer(
                start=start_location_origin,
                end=end_location_origin,
                travel_mode="TRANSIT",
                stroke_color="blue",
                stroke_weight=3.0,
                stroke_opacity=1.0,
            )
            fig.add_layer(transit_layer_origin)
        else:
            print("No routes found between the first starting point and the destination.")

        # Check if routes exist for the second starting point
        if "routes" in data_origin2 and data_origin2["routes"]:
            # Add direction layers for the second starting point
            start_location_origin2 = (
                data_origin2["routes"][0]["legs"][0]["start_location"]["lat"],
                data_origin2["routes"][0]["legs"][0]["start_location"]["lng"],
            )
            end_location_origin2 = (
                data_origin2["routes"][0]["legs"][0]["end_location"]["lat"],
                data_origin2["routes"][0]["legs"][0]["end_location"]["lng"],
            )
            transit_layer_origin2 = gmaps.directions_layer(
                start=start_location_origin2,
                end=end_location_origin2,
                travel_mode="TRANSIT",
                stroke_color="red",
                stroke_weight=3.0,
                stroke_opacity=1.0,
            )
            fig.add_layer(transit_layer_origin2)
        else:
            print("No routes found between the second starting point and the destination.")

    else:
        print("Error in request:", response_origin.status_code, response_origin2.status_code)

else:
    # URL for the Directions API request for the single starting point
    url_origin = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"

    # Send HTTP GET request
    response_origin = requests.get(url_origin)

    # Check if the request was successful (Status Code 200)
    if response_origin.status_code == 200:
        # Extract data from the response (JSON format)
        data_origin = response_origin.json()

        # Configure gmaps
        gmaps.configure(api_key=API_KEY)
        fig = gmaps.figure()

        # Check if routes exist for the single starting point
        if "routes" in data_origin and data_origin["routes"]:
            # Add direction layer for the single starting point
            start_location_origin = (
                data_origin["routes"][0]["legs"][0]["start_location"]["lat"],
                data_origin["routes"][0]["legs"][0]["start_location"]["lng"],
            )
            end_location_origin = (
                data_origin["routes"][0]["legs"][0]["end_location"]["lat"],
                data_origin["routes"][0]["legs"][0]["end_location"]["lng"],
            )
            transit_layer_origin = gmaps.directions_layer(
                start=start_location_origin,
                end=end_location_origin,
                travel_mode="TRANSIT",
                stroke_color="blue",
                stroke_weight=3.0,
                stroke_opacity=1.0,
            )
            fig.add_layer(transit_layer_origin)
        else:
            print("No routes found between the starting point and the destination.")


    else:
        print("Error in request:", response_origin.status_code)



fig