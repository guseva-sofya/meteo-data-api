def test_default_endpoint(client):
    response = client.get("/")
    assert b"<h1>Welcome to my API.</h1>" in response.data


def test_post_temperature_record(client):
    json_data = {"location": "Wien", "temperature": -10.1}
    response = client.post("/temperature", json=json_data)
    assert response.status_code == 204

    response = client.get("/temperature/Wien")
    assert response.status_code == 200

    assert len(response.json) == 1
    assert response.json[0]["temperature"] == -10.1


# TODO:
# test get locations
# test multiple records for one location
