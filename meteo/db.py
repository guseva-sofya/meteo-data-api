import os
from dataclasses import dataclass
from alembic.config import Config
from alembic import command
import psycopg2

connection = None


@dataclass
class DbConfig:
    database: str
    user: str
    password: str
    host: str
    port: str


def connect_to_db(dbconfig: DbConfig) -> psycopg2.extensions.connection:
    global connection
    if connection is not None:
        return connection

    connection = psycopg2.connect(
        database=dbconfig.database,
        user=dbconfig.user,
        password=dbconfig.password,
        host=dbconfig.host,  # use "localhost" for the local server
        port=dbconfig.port,  # typically 5432 for PostgreSQL
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


def clear(dbconfig: DbConfig):
    conn = connect_to_db(dbconfig)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM temperature_records")
    conn.commit()
