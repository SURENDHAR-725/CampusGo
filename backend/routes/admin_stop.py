from flask import Blueprint, request, jsonify
from db import get_db

admin_stop = Blueprint("admin_stop", __name__)

# GET ALL STOPS FOR ROUTE
@admin_stop.route("/all/<int:route_id>", methods=["GET"])
def get_stops(route_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM stops WHERE route_id = %s ORDER BY stop_order", (route_id,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(result)

# ADD STOP
@admin_stop.route("/add", methods=["POST"])
def add_stop():
    data = request.json
    route_id = data["route_id"]
    stop_name = data["stop_name"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    stop_order = data["stop_order"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO stops (route_id, stop_name, latitude, longitude, stop_order)
        VALUES (%s, %s, %s, %s, %s)
    """, (route_id, stop_name, latitude, longitude, stop_order))

    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Stop added"})

# DELETE STOP
@admin_stop.route("/delete/<int:stop_id>", methods=["DELETE"])
def delete_stop(stop_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM stops WHERE stop_id = %s", (stop_id,))
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Stop deleted"})
