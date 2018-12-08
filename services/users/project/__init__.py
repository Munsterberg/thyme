import os
from flask import Flask, jsonify

app = Flask(__name__)

app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)


@app.route("/users/ping", methods=["GET"])
def ping():
    return jsonify({"status": "success"})
