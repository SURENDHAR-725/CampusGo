from flask import Blueprint, request, jsonify
from db import get_db

admin_route = Blueprint("admin_route", __name__)

# GET ALL ROUTES
@admin_route.route("/all", methods=["GET"])
def get_routes():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM routes")
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify(result)

# ADD ROUTE
@admin_route.route("/add", methods=["POST"])
def add_route():
    data = request.json
    route_name = data["route_name"]

    db = get_db()
    cursor = db.cursor()
    cursor.execute("INSERT INTO routes (route_name) VALUES (%s)", (route_name,))
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Route added"})

# DELETE ROUTE
@admin_route.route("/delete/<int:route_id>", methods=["DELETE"])
def delete_route(route_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM routes WHERE route_id = %s", (route_id,))
    db.commit()
    cursor.close()
    db.close()

    return jsonify({"message": "Route deleted"})
