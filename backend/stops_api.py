from flask import Blueprint, request, jsonify
from db import get_db

stops_api = Blueprint("stops_api", __name__)

@stops_api.route("/api/stops/<route_id>")
def get_stops(route_id):
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM stops WHERE route_id=%s ORDER BY stop_order", (route_id,))
    return jsonify(cur.fetchall())
