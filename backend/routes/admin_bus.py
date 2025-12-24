from flask import Blueprint, request, jsonify
from db import get_db

admin_bus = Blueprint("admin_bus", __name__)

# GET ALL BUSES
@admin_bus.route("/all", methods=["GET"])
def get_buses():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM buses")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(result)

# ADD BUS
@admin_bus.route("/add", methods=["POST"])
def add_bus():
    data = request.json
    bus_number = data["bus_number"]
    capacity = data["capacity"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO buses (bus_number, capacity) VALUES (%s, %s)",
        (bus_number, capacity)
    )
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Bus added successfully"})

# DELETE BUS
@admin_bus.route("/delete/<int:bus_id>", methods=["DELETE"])
def delete_bus(bus_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM buses WHERE bus_id = %s", (bus_id,))
    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Bus deleted"})
