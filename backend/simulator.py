import requests
import time
import random

bus_id = 1
lat = 12.9716
lng = 77.5946

while True:
    lat += random.uniform(-0.0005, 0.0005)
    lng += random.uniform(-0.0005, 0.0005)

    requests.post("http://localhost:5000/api/update-location", json={
        "bus_id": bus_id,
        "lat": lat,
        "lng": lng,
        "speed": random.randint(20, 40)
    })

    print("GPS sent:", lat, lng)
    time.sleep(2)
