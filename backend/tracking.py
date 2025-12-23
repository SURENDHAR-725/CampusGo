from flask import Blueprint, request, jsonify
from socket_manager import socketio
from db import get_db

tracking = Blueprint("tracking", __name__)

@tracking.route("/api/update-location", methods=["POST"])
def update_location():
    data = request.json
    bus_id = data["bus_id"]
    lat = data["lat"]
    lng = data["lng"]
    speed = data["speed"]

    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bus_locations (bus_id, latitude, longitude, speed)
        VALUES (%s, %s, %s, %s)
    """, (bus_id, lat, lng, speed))
    conn.commit()

    socketio.emit("bus_location", data)

    return {"status": "ok"}
