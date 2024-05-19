# Create image based on the prebuilt python image
FROM python:3.12

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

# Create new folder and cd (enter) into it
WORKDIR /meteo-api/

COPY poetry.lock pyproject.toml /
RUN poetry install

# Copy file to the current working directory (meteo-api)
COPY main.py .