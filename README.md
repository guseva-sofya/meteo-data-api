## Start docker database:
```
docker compose up -d
```

[Start Docker Desktop on Windows/Mac.]

Show all containers:
```
docker ps -a
```

Connect to the database:
```
docker exec -it meteo-data-api-db-1 psql -U baloo -d meteo-data
```
Show all tables:
\d

Create new table:
CREATE TABLE my_table (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

Show table's columns:
\d my_table

INSERT INTO my_table (id, name) VALUES (1, 'Alex');

SELECT * FROM my_table;

Exit database:
\q 

Stop DB without removing it:
docker compose stop

Stop DB and remove the container (all data will be lost!!!)
docker compose down

Open adminer DB dashboard in browser: [localhost:3333](http://localhost:3333/)

## Alembic 

Alembic is a database migration tool.

To add alembic to the project:
```
poetry add alembic
```

To initialize alembic in your project:
```
alembic init alembic
```
This creates alembic files in the alembic directory.

Connect alembic to your DB by setting the `sqlalchemy.url` in alembic.ini file.

To add a new versioning script:
```
alembic revision -m "create_new_table"
```
This creates a new versioning script in alembic/versions. Edit the upgrade/downgrade
functions inside the script.

To run alembic migration:
```
alembic upgrade head
```

To downgrade (for example, delete table):
```
alembic downgrade -1
```

DAO (temperature_dao.py) - database access object.