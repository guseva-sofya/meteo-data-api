from flask import Flask, request, jsonify, make_response

import psycopg2


app = Flask(__name__)

data = [2]


# defeult endpoint
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to my API.</h1>"


# add endpoint
@app.route("/get-data", methods=["GET"])
def get_data():
    # connect to PostgresSQL database
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name FROM my_table")
    result = cursor.fetchall()
    print(result)

    response_data = []
    for row in result:
        row_dict = {"id": row[0], "name": row[1]}
        response_data.append(row_dict)
    return jsonify(response_data)


@app.route("/post-data", methods=["POST"])
def post_data():
    request_data = request.get_json()
    data.extend(request_data["data"])
    return make_response("Data received", 200)


def connect_to_db():
    connection = psycopg2.connect(
        database="meteo-data",
        user="baloo",
        password="junglebook",
        host="localhost",  # use "localhost" for the local server
        port="5432",  # typically 5432 for PostgreSQL
    )
    print("Connected to PostgreSQL")
    return connection


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
