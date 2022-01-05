# Website

The official website for YameTechs

## Setting Up Instructions

### 1.setup the files

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
```

### 2.setup virtual environment

```bash
# For installing the virtual environment
pip install pipenv

# Now setup pipenv (add --dev if you will be developing code)
pipenv install --dev

# Start the shell
pipenv shell

# Start the code
python run.py
```

you are now ready to edit the code!
