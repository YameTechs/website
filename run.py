from dotenv import load_dotenv

load_dotenv()


import os

from src import create_app

if __name__ == "__main__":
    DEVMODE = os.environ["DEVMODE"] == "True"

    app = create_app()
    app.run(debug=DEVMODE)
