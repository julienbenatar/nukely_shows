jukely_shows
============

a spyre web interface for showing what unlimited show are available on jukely

Requirements
-----
jukely.py grabs the shows from Jukely and only requires python.
To launch the web app you'll need spyre which has some dependencies of it's own.

Setup
-----
This application requires Jukely user credentials for someone signed up for Jukely's unlimited shows account.
You'll need to supply your credentials by created a credentials.py file (these are included in .gitignore). credentials .py will have two lines

````
username = 'yourusername'
password = 'yourpassword'
````

replace yourusername with your Jukely username and yourpassword with your Jukely password.

Launching the web app
----
Once you've created the credentials.py file with your credentials, launch the web app with

````
> python jukely_app.py
````
