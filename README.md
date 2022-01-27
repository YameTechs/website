# Website

The official website for YameTechs

## Todos

### other features

- [x] captcha
- [ ] security stuff

### codes

- [ ] events

### routes

- [x] home
- [ ] admin
- [ ] about
- [ ] contacts
- [ ] game
- [ ] portfolio
  - [ ] projects
- [ ] services
  - [ ] bots (discord)
  - [ ] websites
- [ ] users
  - [ ] account
  - [x] forgotten password
    - [x] verify email (email)
  - [x] login
  - [x] logout
  - [x] register
    - [x] verify account (email)

## Setting Up Instructions

### 1. Setup the files

```bash
# Clone the repo
git clone https://github.com/YameTechs/website.git

# cd to the project
cd website

# make .env file
touch .env

# edit your .env file ( you could use an editor to edit this file btw )
nano .env
```

#### sample layout of `.env` file

```python
DEVMODE='True'
FLASK_SECRET_KEY='your secret key'
DATABASE_URI='sqlite:///test.db'
EMAIL_USER='youremail@gmail.com'
EMAIL_PASSWORD='your_password'
RECAPTCHA_PUBLIC_KEY='site_key_from_google_recaptcha'
RECAPTCHA_PRIVATE_KEY='private_key_from_google_recaptcha'
```

### 2. Setup virtual environment

```bash
# For installing the virtual environment
pip install pipenv

# Now setup pipenv (add --dev if you will be developing code)
pipenv install --dev

# Start the shell
pipenv shell
```

### 3. Setup the database

```bash
# Go into python cli
python

# Import db and the models
>>> from src import db, create_app
>>> from src.models import *

# Create the db
>>> db.create_all(app=create_app())

# Exit python cli
>>> exit()
```

you are now ready to edit the code!

### 4. Pushing

After making changes to your code run the following

```bash
# To fix the code in a certain format do:
pipenv run format

# Please check flake8 messages for the errors that the code might have
# Try to fix those errors to! if the errors persist just leave it.
```
