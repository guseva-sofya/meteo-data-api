from flask import Flask, jsonify


app = Flask(__name__)


# add endpoint
@app.route("/api", methods=["POST"])
def my_endpoint():
    response_data = {"message": "Hello from API"}
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
