import os
from alembic.config import Config
from alembic import command
import psycopg2

connection = None


def connect_to_db() -> psycopg2.extensions.connection:
    global connection
    if connection is not None:
        return connection

    connection = psycopg2.connect(
        database="meteo-data",
        user="baloo",
        password="junglebook",
        host="localhost",  # use "localhost" for the local server
        port="5432",  # typically 5432 for PostgreSQL
    )
    print("Connected to PostgreSQL")

    run_alembic_migration()
    print("Finished Alembic migrations")
    return connection


def run_alembic_migration():
    # Set the ALEMBIC_CONFIG environment variable to point to your alembic.ini file.
    os.environ["ALEMBIC_CONFIG"] = "alembic.ini"

    # Load the Alembic configuration
    alembic_cfg = Config("alembic.ini")

    # Run the migrations
    command.upgrade(alembic_cfg, "head")


def clear():
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temperature_records")
    conn.commit()
