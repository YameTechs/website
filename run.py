import os

from dotenv import load_dotenv

from src import app

load_dotenv()
DEVMODE = os.environ["DEVMODE"] == "True"

if __name__ == "__main__":
    app.run(debug=DEVMODE)
