from flask import Blueprint, request, jsonify
from db import get_db

buses = Blueprint("buses", __name__)

@buses.route("/api/buses")
def get_buses():
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM buses")
    return jsonify(cur.fetchall())

@buses.route("/api/buses/add", methods=["POST"])
def add_bus():
    data = request.json
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO buses (bus_number, route_id, capacity)
        VALUES (%s, %s, %s)
    """, (data["bus_number"], data["route_id"], data["capacity"]))

    conn.commit()
    return {"status": "Bus Added"}
