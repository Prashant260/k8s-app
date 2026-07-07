from flask import Flask, jsonify
import socket
import os

app = Flask(__name__)

healthy = True
broken = False

@app.route("/")
def home():
    if broken:
        raise Exception("Production Bug")

    return {
        "message": "Application Running",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "4.0")
    }

@app.route("/health")
def health():
    if healthy:
        return {"status": "UP"}, 200
    return jsonify({"status": "DOWN"}), 503

@app.route("/fail")
def fail():
    global healthy
    healthy = False
    return {"message": "Readiness failed"}

@app.route("/recover")
def recover():
    global healthy
    healthy = True
    return {"message": "Application recovered"}

@app.route("/break")
def break_app():
    global broken
    broken = True
    return {"message": "Application will now throw 500 errors"}

@app.route("/fix")
def fix_app():
    global broken
    broken = False
    return {"message": "Application fixed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)