from flask import Blueprint, request, jsonify
from db import get_db

admin_driver = Blueprint("admin_driver", __name__)

# GET ALL DRIVERS
@admin_driver.route("/all", methods=["GET"])
def get_drivers():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM drivers")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(result)

# ADD DRIVER
@admin_driver.route("/add", methods=["POST"])
def add_driver():
    data = request.json
    name = data["name"]
    phone = data["phone"]
    username = data["username"]
    password = data["password"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO drivers (name, phone, username, password)
        VALUES (%s, %s, %s, %s)
    """, (name, phone, username, password))

    db.commit()
    cursor.close()
    db.close()
    return jsonify({"message": "Driver added"})

# ASSIGN DRIVER TO BUS
@admin_driver.route("/assign", methods=["POST"])
def assign_driver():
    data = request.json
    driver_id = data["driver_id"]
    bus_id = data["bus_id"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute("UPDATE drivers SET assigned_bus = %s WHERE driver_id = %s", (bus_id, driver_id))
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Driver assigned"})
