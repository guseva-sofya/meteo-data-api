import psycopg2

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
