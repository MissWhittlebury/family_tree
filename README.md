To run the app:

NOTE: While the app should work with other databases, it has only been tested with a postgres database.

1) create a database for the app
2) create a virtual environment and install the packages in the requirements.txt file.
3) Set your environment variables. The below are needed.
* DB_USER=username_to_access_db
* DB_PWD=pwd_for_username
* DB_HOST=localhost (these are postgres defaults)
* DB_PORT=5432
* DB_NAME=your_db_name
* PYTHONPATH=family_tree/ (i.e. set to family_tree folder)
* FLASK_APP=family_tree.py
4) run alembic upgrade head from the root of the project to initialize the db
5) flask run
