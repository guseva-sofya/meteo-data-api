## Start docker database:
```
docker compose up -d
```

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
CREATE TABLE my_table (id integer, name text);

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