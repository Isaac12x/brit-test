# Brit Test

This tech test demonstrate python programming skills featuring a login screen, signup, an items page and a summary of items page.

### Explanation

I have choosen django as I could have choosen any other. Because I wanted the capability to do this well with email verification (as it should be when doing authentication) the easiest was to go through it using django.
Otherwise, for the test only would have gone with cherrypy.

### TL;DR

To run the app
`python3 -m venv env/ && source env/bin/activate && createdb brit_test`

`pip intall -r requirements/local.txt`

`python manage.py migrate && python manage.py runserver`

The app uses a python command I have written to load any data in the Data folder into memory as long as it follows the right json structure.
To do so, set your django app and run
`python manage.py loaddata demodata.json`

Where demodata.json is the file in `brit_test/data/NAME.json`.

### Limitations

For the frontend, given the simplicity of the app I chose to go with the basic templating instead of doing React (my usual go-to) but having to compile and have to serve the react app compressed, etc.

If you're to run the app as in production you will need to create a .env file and pass all the valid env variables required to run it successfully.

### Authentication

Cookiecutter sets up authentication out-of-the-box via django-allauth. It can be easily extended to use social accounts to log in as I have done previously. This will require longer as you need to go through the Oauth2 flow and get the tokens from the social platforms, etc.

### "Shortcuts"

I have used cookiecutter with the django template from Daniel&Audrey Fieldroy to quickstart the project.

It adds all the configuration as the basis of the application and adds a few libraries off-the-bat so it's very easy to do all the basics (authentication, emailing, remote logging, etc.).

- I haven't taken any more shortcuts.
