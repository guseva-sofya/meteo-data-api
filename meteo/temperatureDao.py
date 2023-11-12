from dataclasses import dataclass
from typing import List
import psycopg2
from datetime import datetime


@dataclass
class TemperatureRecord:
    temperature: float
    time: datetime


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

    def find_available_locations(self) -> List[str]:
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT DISTINCT(location) FROM temperature_records")
        result = cursor.fetchall()

        locations = [row[0] for row in result]
        return locations

    def find_temperature_for_location(self, location: str) -> List[TemperatureRecord]:
        cursor = self.db_connection.cursor()
        cursor.execute(
            """
                SELECT temperature, recorded_at
                FROM temperature_records
                WHERE location=%s
                ORDER BY recorded_at
            """,
            (location,),
        )
        result = cursor.fetchall()
        return [TemperatureRecord(row[0], row[1]) for row in result]
