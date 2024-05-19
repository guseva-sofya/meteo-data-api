# Create image based on the prebuilt python image
FROM python:3.12

# Create new folder and cd (enter) into it
WORKDIR /meteo-api/

# Copy file to the current working directory (meteo-api)
COPY main.py .