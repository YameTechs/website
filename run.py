from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


import os
from src import create_app

DEVMODE = os.environ["DEVMODE"] == "True"

if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEVMODE)
