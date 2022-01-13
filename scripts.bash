printf "\n[isort]\n"
isort .

printf "\n[black]\n"
black .

printf  "\n[flake8]\n"
flake8 .
