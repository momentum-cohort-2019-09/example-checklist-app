CHECKLISTS = {
    '1': {
        'title': 'Django setup checklist',
        'items': [
            "Create a virtualenv: `pipenv --three`",
            "Install Django: `pipenv install django`",
            "Enter the virtualenv: `pipenv shell`",
            """Create a Django project: `django-admin startproject config .` The `.` is **very important**. See below for more information about `startproject`.""",
            "Create a Django app: `./manage.py startapp <your_app_name>`.",
            "Edit `config/settings.py` and add the name of your app to `INSTALLED_APPS`."
        ]
    },
    '2': {
        'title': "Using Git branches",
        'items': [
            "In master, run `git pull`", "Run `git checkout -b <branch-name>`",
            "Make your changes, running `git add` and `git commit` after each change.",
            "Before pushing, run `git fetch origin master` and `git merge master` and resolve all conflicts.",
            "Run `git push origin <branch-name>`", "Make a pull request"
        ]
    }
}
