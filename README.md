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

## SQL commands

Update name of the field in a table:
```
update temperature_records set location='Munich' where id in (1,2);
```

Start database transaction (opportunity to go back to a state before transaction);
```
begin;
```

Make commands. Then rollback:

```
rollback;
```

To commit changes (without opportunity to rollback):
```
commit
```

## Testing

To run all tests use 
```
pytest
```

To show print messages in tests run

```
pytest -s
```

## Docker

Build image using Dockerfile in the repo:
```
docker build .
```

Create image with name:

```
docker build -t meteo-data-api .
```

Show all Docker images in the system:

```
docker image ls
```

Run image, connect to it in interactive mode and run bash (this - Ubuntu):
```
docker run -it <image_id> bash
```

One image is an image of system that I run. Container is a runnig copy of an image.
Image is a recipy, container is a cooked dish.

Shows all containers in the system:
```
docker ps -a
```

Remove container:
```
docker rm <container_id>
```

Remove image:
```
docker image rm <image_id>
```

Remove all unused images and containers:
```
docker system prune
```