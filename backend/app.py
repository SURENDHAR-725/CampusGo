from flask import Flask, render_template, session, redirect
from auth import auth
from buses import buses
from routes_api import routes_api
from stops_api import stops_api
from tracking import tracking
from socket_manager import socketio

app = Flask(__name__)
app.secret_key = "SECRET123"

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(buses)
app.register_blueprint(routes_api)
app.register_blueprint(stops_api)
app.register_blueprint(tracking)


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
