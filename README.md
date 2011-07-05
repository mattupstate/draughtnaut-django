# DraughtNaut

DraughtNaut is a hypothetical website concept I use to learn new languages and frameworks. In this case, Python and Django

You must have Django, and South installed for this application to run properly. To install Django visit the [Django website](https://docs.djangoproject.com/en/dev/topics/install/).

To install South use easy_install:

    sudo easy_install South

To run the application, rename the folder you cloned the repository into to 'draughtnaut' and from the command line run the following commands:

    python manage.py syncdb
    python manage.py migrate beer
    python manage.py migrate venues
    python manage.py runserver

Lastly, use test-data.sql to juice up the database with some data if its a new install

