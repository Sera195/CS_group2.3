API_KEY = "AIzaSyCczAYQAMPwcBfIM6R6ncLpwrK_-lE8BF8"

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
    index, lat, lng = 0, 0, 0
    coordinates = []
    changes = {'latitude': 0, 'longitude': 0}

    # Decode polyline
    while index < len(polyline_str):
        # Variables for decoding
        shift, result = 0, 0

        # Decode latitude
        while True:
            byte = ord(polyline_str[index]) - 63
            index += 1
            result |= (byte & 0x1f) << shift
            shift += 5
            if not byte >= 0x20:
                break
        lat += ~(result >> 1) if result & 1 else (result >> 1)
        changes['latitude'] = lat / 100000.0

        # Decode longitude
        shift, result = 0, 0
        while True:
            byte = ord(polyline_str[index]) - 63
            index += 1
            result |= (byte & 0x1f) << shift
            shift += 5
            if not byte >= 0x20:
                break
        lng += ~(result >> 1) if result & 1 else (result >> 1)
        changes['longitude'] = lng / 100000.0

        # Append the decoded coordinate to the list
        coordinates.append((changes['latitude'], changes['longitude']))

    return coordinates