from flask import Flask, request, jsonify, make_response

from meteo import db

app = Flask(__name__)
db_connection = db.connect_to_db()

# TODO: 1. refactor DB connection
# 2. Design meteo-API
# 3. Deploy to cloud


# default endpoint
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to my API.</h1>"


@app.route("/get-data", methods=["GET"])
def get_data():
    cursor = db_connection.cursor()
    cursor.execute("SELECT id, name FROM my_table")
    result = cursor.fetchall()

    response_data = []
    for row in result:
        row_dict = {"id": row[0], "name": row[1]}
        response_data.append(row_dict)
    return jsonify(response_data)


@app.route("/post-data", methods=["POST"])
def post_data():
    # read request data and write them into the database
    request_data = request.get_json()
    name = request_data["name"]

    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO my_table (name) VALUES (%s)", (name,))
    db_connection.commit()

    return make_response("Data received", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
