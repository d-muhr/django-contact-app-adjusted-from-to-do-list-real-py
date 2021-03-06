# contact app adjusted from to do list real py
  I adjusted the to do list app by Real-Python.com and extended it to make it a contact app. This was a training project which I did after having done the official Django-Tutorial in order to get to know CRUD and Django in general better to enable me to make an entirely own project in Django soon. I also used this training project to regularly "break things on purpose" to better understand the inner workings of Django.
  
Link of the original To Do List App:
https://github.com/realpython/materials/tree/master/django-todo-list

Statement that the original To Do List App (as the other material) has a MIT License:
https://github.com/realpython/materials


## Setup Instructions (copied from original)

These instructions have been tested in Ubuntu Linux and macOS. They should also work in Windows, but note that you'll need to use a different command to activate your virtual environment as described in Step 3. Please consult the [`venv` documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for greater detail on the use of virtual environments.

1. Navigate into the project directory (`source_code/`).
2. Create a virtual environment in a `venv/` folder by typing `python -m venv venv` in your console.
3. Activate the venv using `source venv/bin/activate` (Linux, MacOS) or `venv\Scripts\activate.bat` (Windows).
4. Install the dependencies with `python -m pip install -r requirements.txt`
5. Generate the empty SQLite database and tables using `python manage.py migrate`
5. Run the app with `python manage.py runserver`
6. Browse to the [app home page](http://localhost:8000/) to see the list of todo lists, which will initially be empty. 

You can now start using the UI to add your to-do lists and to-do items to the database. The data will be stored in a new `db.sqlite3` file in the root of your project directory.

You can also use Django's auto-generated [admin interface](https://realpython.com/customize-django-admin-python/#setting-up-the-django-admin) at `http://localhost:8000/admin/` to view, add, and edit the data.
