import psycopg2


class TemperatureDao:
    def __init__(self, db_connection: psycopg2.extensions.connection):
        self.db_connection = db_connection

    def insert_temperature_record(self, location: str, temperature: float):
        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO temperature_records (location, temperature, recorded_at) VALUES (%s, %s, now())",
            (location, temperature),
        )
        self.db_connection.commit()
