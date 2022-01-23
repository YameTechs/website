import os
from src import app
from dotenv import load_dotenv

load_dotenv()
DEVMODE = os.environ["DEVMODE"] == "True"

if __name__ == "__main__":
    app.run(debug=DEVMODE)
