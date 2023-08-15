from flask import Flask, request, jsonify, make_response


app = Flask(__name__)

data = [2]


# add endpoint
@app.route("/get-data", methods=["GET"])
def get_data():
    response_data = {"data": data}
    return jsonify(response_data)


@app.route("/post-data", methods=["POST"])
def post_data():
    request_data = request.get_json()
    data.extend(request_data["data"])
    return make_response("Data received", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
