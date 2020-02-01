# Hamband Website
A django project for https://hamband.math.sharif.edu

## Installation
1. Create a virtualenv with `python -m env venv`
2. Activate virtualenv with `source venv/bin/activate`
3. Install requirements with `pip install -r requirements.txt`
4. Copy settings from `base/local_settings.sample.py` to `base/local_settings.py`.
5. Migrate database with `python3 manage.py migrate`.
6. You can also populate database for testing with `python3 manage.py seed`
7. Run it with `python3 manage.py runserver` :)
 