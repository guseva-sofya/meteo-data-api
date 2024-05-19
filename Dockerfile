# Create image base on the latest version of Ubuntu
FROM ubuntu:latest

RUN apt update
RUN apt install -y python3

# Create new folder and cd (enter) into it
WORKDIR /meteo-api/

# Copy file to the current working directory (meteo-api)
COPY main.py .