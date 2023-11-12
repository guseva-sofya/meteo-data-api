from typing import List
from flask import Flask, Response, request, jsonify, make_response

from meteo import db
from meteo import temperatureDao

app = Flask(__name__)
db_connection = db.connect_to_db()
temperature_dao = temperatureDao.TemperatureDao(db_connection)

# TODO
# - refactor DB connection
# - Get temperature for location
# - Add linters ruff, add blackformatter
# - Add tests
# - Design meteo-API
# - Deploy to cloud


# default endpoint
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to my API.</h1>"


@app.route("/temperature", methods=["POST"])
def save_temperature_record() -> Response:
    request_data = request.get_json()
    location: str = request_data["location"].lower()
    temperature: float = request_data["temperature"]

    temperature_dao.insert_temperature_record(location, temperature)

    return make_response("", 204)


@app.route("/temperature/locations", methods=["GET"])
def get_temperature_locations() -> Response:
    locations = temperature_dao.find_available_locations()
    return jsonify(locations)


@app.route("/temperature/<location>", methods=["GET"])
def get_temperature_for_location(location: str) -> Response:
    temperature_records = temperature_dao.find_temperature_for_location(location.lower())
    return jsonify(temperature_records)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
