import os
from dotenv import load_dotenv
import pytest
from meteo import app as application
from meteo import db


@pytest.fixture()
def app():
    app = application.build_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    # other setup can go here

    yield app

    # clean up / reset resources here
    env = application.read_environment()
    db.clear(env.dbconfig())


@pytest.fixture()
def client(app):
    return app.test_client()
