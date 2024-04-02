import streamlit as st
import requests

# Hier API-Schlüssel einfügen
API_KEY = "AIzaSyCczAYQAMPwcBfIM6R6ncLpwrK_-lE8BF8"

# Funktion zur Abfrage von Routen und Anzeige auf der Karte
def display_route_on_map(origin, destination, color):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extrahiere Koordinaten für die Routenpunkte
        route_points = []
        for step in data['routes'][0]['legs'][0]['steps']:
            for point in decode_polyline(step['polyline']['points']):
                route_points.append({'lat': point[0], 'lon': point[1]})

        # Zeige die Route auf der Karte an
        st.map(route_points, zoom=12, color=color)

# Funktion zur Dekodierung der Polylines
def decode_polyline(polyline_str):
    # Die Funktion decode_polyline hier einfügen

# Hauptprogramm
def main():
    st.title("Directions App")
    
    # Inputfelder für Start- und Zielorte
    origin = st.text_input("Enter a starting point:")
    destination = st.text_input("Enter your destination:")
    
    # Farben für verschiedene Routen festlegen
    colors = ['red', 'blue', 'green']

    # Zeige die Route auf der Karte für jede eingegebene Farbe
    for i, color in enumerate(colors):
        display_route_on_map(origin, destination, color)

if __name__ == "__main__":
    main()