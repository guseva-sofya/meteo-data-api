import os
from flask import Flask, Response, request, jsonify, make_response
from dataclasses import dataclass

from dotenv import load_dotenv
from meteo import db
from meteo import temperatureDao


def build_app() -> Flask:
    app = Flask(__name__)
    env = read_environment()
    db_connection = db.connect_to_db(env.dbconfig())
    temperature_dao = temperatureDao.TemperatureDao(db_connection)

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
        temperature_records = temperature_dao.find_temperature_for_location(
            location.lower()
        )
        return jsonify(temperature_records)

    return app


@dataclass
class Environment:
    database: str
    user: str
    password: str
    host: str
    port: str

    def dbconfig(self) -> db.DbConfig:
        return db.DbConfig(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
        )


def read_environment() -> Environment:
    load_dotenv()

    database = os.getenv("DATABASE", "")
    if database == "":
        raise ValueError("DATABASE environment error not set")

    user = os.getenv("USER", "")
    if user == "":
        raise ValueError("USER environment error not set")

    password = os.getenv("PASSWORD", "")
    if password == "":
        raise ValueError("PASSWORD environment error not set")

    host = os.getenv("HOST", "")
    if host == "":
        raise ValueError("HOST environment error not set")

    port = os.getenv("PORT", "")
    if port == "":
        raise ValueError("PORT environment error not set")

    return Environment(
        database=database, user=user, password=password, host=host, port=port
    )
