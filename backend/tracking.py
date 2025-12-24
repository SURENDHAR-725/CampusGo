from flask import Blueprint, request, jsonify
from socket_manager import socketio
from db import get_db

tracking = Blueprint("tracking", __name__)

@tracking.route("/update_location", methods=["POST"])
def update_location():
    data = request.json
    bus_id = data["bus_id"]
    lat = data["latitude"]
    lng = data["longitude"]

    # save to DB
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO bus_location (bus_id, latitude, longitude)
        VALUES (%s, %s, %s)
    """, (bus_id, lat, lng))
    db.commit()

    cursor.close()
    db.close()

    # send to frontend via websocket
    socketio.emit("bus_location", {
        "bus_id": bus_id,
        "latitude": lat,
        "longitude": lng
    })

    return jsonify({"status": "ok"})
