from flask import Flask
from flask_cors import CORS
from socket_manager import socketio

# Admin APIs
from routes.admin_bus import admin_bus
from routes.admin_route import admin_route
from routes.admin_stop import admin_stop
from routes.admin_driver import admin_driver

app = Flask(__name__)
CORS(app)

app.register_blueprint(admin_bus, url_prefix="/admin/bus")
app.register_blueprint(admin_route, url_prefix="/admin/route")
app.register_blueprint(admin_stop, url_prefix="/admin/stop")
app.register_blueprint(admin_driver, url_prefix="/admin/driver")

@app.route("/")
def home():
    if "user_id" not in session:
        return redirect("/login")
    return redirect("/dashboard")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    return render_template("dashboard.html")


if __name__ == "__main__":
    socketio.init_app(app)
    socketio.run(app, host="0.0.0.0", port=5000)
