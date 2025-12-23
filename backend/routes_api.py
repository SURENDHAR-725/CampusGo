from flask import Blueprint, request, jsonify
from db import get_db

routes_api = Blueprint("routes_api", __name__)

@routes_api.route("/api/routes")
def routes_list():
    conn = get_db()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM routes")
    return jsonify(cur.fetchall())
