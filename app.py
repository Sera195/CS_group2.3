import requests
import gmaps

# API key für den Zugriff auf die Google Maps API
API_KEY = "AIzaSyBpjEKrlbfkGbVUU8LgiaBFVPHvCADIVgY"

# Funktion zum Abrufen der Koordinaten einer Adresse
def get_coordinates(place):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={place}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "results" in data and len(data["results"]) > 0:
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
    return None, None

# Start- und Zielpunkte
origins = input("Geben Sie Startpunkte durch Komma getrennt ein (z.B. Punkt1, Punkt2, Punkt3): ").split(",")
destination = input("Geben Sie Ihr Ziel ein: ")

# Überprüfen, ob mindestens ein Startpunkt angegeben wurde
if len(origins) < 1:
    print("Bitte geben Sie mindestens einen Startpunkt ein.")
    exit()

# Liste von Farben für die Routen
colors = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 165, 0), (128, 0, 128), (255, 192, 203)]

# Konfiguration der gmaps
gmaps.configure(api_key=API_KEY)
fig = gmaps.figure(layout = {"width": "1550px", "height": "600px"})

# Durchlaufe alle Startpunkte und füge Richtungsschichten hinzu
for i, origin in enumerate(origins):
    # Überprüfen, ob der Startpunkt eine Adresse mit Postleitzahl ist
    if ',' in origin:  # Wenn die Eingabe eine Adresse mit Postleitzahl ist
        place, postal_code = origin.split(',', 1)
        start_latlng = get_coordinates(place.strip())  # Koordinaten des Startpunkts abrufen
        if start_latlng[0] is None or start_latlng[1] is None:
            print(f"Koordinaten nicht gefunden für {place}")
            continue
    else:
        start_latlng = get_coordinates(origin.strip())  # Koordinaten des Startpunkts abrufen
        if start_latlng[0] is None or start_latlng[1] is None:
            print(f"Koordinaten nicht gefunden für {origin}")
            continue

    # URL für die Directions API Anfrage
    url_origin = f"https://maps.googleapis.com/maps/api/directions/json?origin={start_latlng[0]},{start_latlng[1]}&destination={destination}&key={API_KEY}"

    # Sende HTTP GET Anfrage
    response_origin = requests.get(url_origin)

    # Überprüfe, ob die Anfrage erfolgreich war (Status Code 200)
    if response_origin.status_code == 200:
        # Extrahiere Daten aus der Antwort (im JSON-Format)
        data_origin = response_origin.json()

        # Überprüfe, ob eine Route gefunden wurde
        if "routes" in data_origin and len(data_origin["routes"]) > 0:
            # Start- und Endpositionen der Route
            start_location_origin = (
                data_origin["routes"][0]["legs"][0]["start_location"]["lat"],
                data_origin["routes"][0]["legs"][0]["start_location"]["lng"],
            )
            end_location_origin = (
                data_origin["routes"][0]["legs"][0]["end_location"]["lat"],
                data_origin["routes"][0]["legs"][0]["end_location"]["lng"],
            )

            # Farbe der Route basierend auf dem Index festlegen
            color = colors[i % len(colors)]

            # Richtungsschicht hinzufügen
            transit_layer_origin = gmaps.directions_layer(
                start=start_location_origin,
                end=end_location_origin,
                travel_mode="TRANSIT",
                stroke_color=color,
                stroke_weight=3.0,
                stroke_opacity=1.0,
            )
            fig.add_layer(transit_layer_origin)
        else:
            print(f"Keine Route gefunden für Startpunkt {origin}")
    else:
        print(f"Fehler in Anfrage für Startpunkt {origin}: {response_origin.status_code}")

# Karte anzeigen
fig