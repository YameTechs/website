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
  - [x] database view
- [ ] about
- [ ] contacts
- [ ] portfolio
  - [ ] projects
- [ ] services
  - [x] CRUD operation on service post
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
# Only set this to true if you are developing
DEVMODE='True'

# This could be anything
FLASK_SECRET_KEY='your secret key'

# You could keep this if you don't know what else to put in here
DATABASE_URI='sqlite:///test.db'

# This must be a real email!
EMAIL_USER='your_email@mail.com'
# THis must be the password for your email above!
EMAIL_PASS='your_password'

# Get you key in google recaptcha (just google it)
RECAPTCHA_PUBLIC_KEY='site_key_from_google_recaptcha'
RECAPTCHA_PRIVATE_KEY='private_key_from_google_recaptcha'

# This is the main user that will be added as the main admin
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

### 3. Pushing

After making changes to your code run the following

```bash
# To fix the code in a certain format do:
pipenv run isort .
pipenv run black .

# To lint the code do:
pipenv run flake8 .

# To test the code do:
pipenv run python -m pytest --cov
```
