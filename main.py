from meteo import app

# # TODO
# # - Add linters ruff, add blackformatter
# # - Add tests
# # - Deploy to cloud

if __name__ == "__main__":
    meteo_app = app.build_app()
    meteo_app.run(host="0.0.0.0", port=8000)
