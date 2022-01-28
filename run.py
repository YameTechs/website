from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


import os  # noqa: E402

from src import create_app  # noqa: E402

DEVMODE = os.environ["DEVMODE"] == "True"

if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEVMODE)
