#!/bin/bash

# rm db.sqlite3
# touch db.sqlite3

python manage.py makemigrations
python manage.py migrate

python manage.py addtops --filename ./test_clothes.json
python manage.py addpants --filename ./test_clothes.json
python manage.py addshoes --filename ./test_clothes.json

python manage.py updateTopMatrix
# python manage.py updatePantsMatrix
# python manage.py updateShoesMatrix