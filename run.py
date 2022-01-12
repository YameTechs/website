from dotenv import load_dotenv

load_dotenv()


import os

from src import app

DEVMODE = os.environ["DEVMODE"] == "True"

if __name__ == "__main__":
    app.run(debug=DEVMODE)
