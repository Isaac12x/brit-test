# Brit Test

This tech test demonstrates Python programming skills featuring a login screen, signup, an items page and a summary page.

Here's an accompanying video of part of the tech test while I was reasoning about certain parts (pardon the quality! I'm not a streamer): [![techtestvid](https://i.vimeocdn.com/video/1759558131-6f119add17324fc3bba9c2454f5068d35e8a691551e22f11b08ca5b0a630b084-d?mw=80&q=85)](https://vimeo.com/888434078/ac7bd05345)

### Explanation

I have chosen Django as I could have chosen any other. Because I wanted the capability to do this well with email verification (as it should be when doing authentication) the easiest was to go through it using Django.
Otherwise, for the test, I would have gone with Cherrypy.

### TL;DR

To run the app copy and paste the following commands in a UNIX-like terminal.


`python3 -m venv env/ && source env/bin/activate && createdb brit_test`

`pip intall -r requirements/local.txt`

`python manage.py migrate && python manage.py runserver`

The app uses a Python command I have written to load any data in the Data folder into memory as long as it follows the right JSON structure.
To do so, set your Django app and run.

`python manage.py loaddata demodata.json`

Where demodata.json is the file in `brit_test/data/NAME.json`.

### Limitations

For the front end, given the app's simplicity, I chose to go with the basic templating instead of doing React (my usual go-to) but having to compile and serve the React app compressed, etc.

If you're to run the app as in production, you will need to create a .env file and pass all the valid env variables required to run it successfully.

### Authentication

Cookiecutter sets up authentication out-of-the-box via django-allauth. It can be easily extended to use social accounts to log in, as I have done previously. This will require longer as you need to go through the Oauth2 flow and get the tokens from the social platforms, etc.

### "Shortcuts"

I have used cookiecutter with the Django template from Daniel&Audrey Fieldroy to quickstart the project.

It adds all the configuration as the basis of the application and adds a few libraries off-the-bat so it's very easy to do all the basics (authentication, emailing, remote logging, etc.).

- I haven't taken any more shortcuts.
