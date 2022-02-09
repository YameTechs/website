# Website

[![Lints & Tests][lint_n_test.img]][lint_n_test.action]
[![Coverage][coverage.img]][coverage.coveralls]
[![Black][black.img]][black.github]

[lint_n_test.img]: https://github.com/YameTechs/website/actions/workflows/lint_n_test.yml/badge.svg
[lint_n_test.action]: https://github.com/YameTechs/website/actions?query=workflow%3A%22Lint+%26+Test%22+branch%3Amain++

[coverage.img]: https://coveralls.io/repos/github/YameTechs/website/badge.svg
[coverage.coveralls]: https://coveralls.io/github/YameTechs/website

[black.img]: https://img.shields.io/badge/code%20style-black-000000.svg
[black.github]: https://github.com/psf/black

The official website for YameTechs

## Todos

### other features

- [x] captcha
- [ ] security stuff
- [ ] clean email msg

### codes

- [ ] events

### routes

- [x] home
- [ ] admin
- [ ] about
- [ ] contacts
- [ ] portfolio
  - [ ] projects
- [ ] services
  - [ ] bots (discord)
  - [ ] websites
- [ ] users
  - [ ] settings
    - [ ] backend
    - [ ] frontend
  - [ ] account
    - [ ] UI
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
EMAIL_USER='your_email@mail.com'
EMAIL_PASS='your_password'
RECAPTCHA_PUBLIC_KEY='site_key_from_google_recaptcha'
RECAPTCHA_PRIVATE_KEY='private_key_from_google_recaptcha'
MAIN_ADMIN_EMAIL='youre_mail@mail.com'
MAIN_ADMIN_PASSWORD='your_password'
MAIN_ADMIN_USERNAME='your_username'
```

### 2. Setup virtual environment

```bash
# For installing the virtual environment
pip install pipenv

# Now setup pipenv (add --dev if you will be developing code)
pipenv sync --dev

# Start the shell
pipenv shell
```

### 3. Setup the database

```bash
# Go into python cli
python

# Import _db and the models
>>> from src import _db, create_app
>>> from src.models import *

# Create the db
>>> _db.create_all(app=create_app())

# Exit python cli
>>> exit()
```

you are now ready to edit the code!

### 4. Pushing

After making changes to your code run the following

```bash
# To fix the code in a certain format do:
pipenv run flake8 .
pipenv run python -m pytest --cov
```
