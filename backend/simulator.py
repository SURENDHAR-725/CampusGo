import requests
import time

BUS_ID = 1   # change if multiple buses

coords = [
    (12.9716, 77.5946),
    (12.9721, 77.5950),
    (12.9730, 77.5960),
    (12.9740, 77.5970)
]

while True:
    for lat, lng in coords:
        requests.post("http://127.0.0.1:5000/update_location", json={
            "bus_id": BUS_ID,
            "latitude": lat,
            "longitude": lng
        })
        print("GPS sent:", lat, lng)
        time.sleep(2)
