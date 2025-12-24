from flask import Flask, jsonify
from flask_cors import CORS
from socket_manager import socketio

# Tracking (GPS updates)
from tracking import tracking

# Admin APIs
from routes.admin_bus import admin_bus
from routes.admin_route import admin_route
from routes.admin_stop import admin_stop
from routes.admin_driver import admin_driver

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(tracking)                              # /update_location
app.register_blueprint(admin_bus, url_prefix="/admin/bus")     # bus management
app.register_blueprint(admin_route, url_prefix="/admin/route") # route management
app.register_blueprint(admin_stop, url_prefix="/admin/stop")   # stop management
app.register_blueprint(admin_driver, url_prefix="/admin/driver") # driver management

@app.route("/")
def home():
    return jsonify({"message": "CampusGo Backend Running"})


if __name__ == "__main__":
    socketio.init_app(app, cors_allowed_origins="*")
    socketio.run(app, host="0.0.0.0", port=5000)
