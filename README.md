nukely_shows
============

a spyre web interface for showing what unlimited show are available on nukely

Requirements
-----
nukely.py grabs the shows from nukely and only requires python.
To launch the web app you'll need spyre which has some dependencies of it's own.

Setup
-----
This application requires nukely user credentials for someone signed up for nukely's unlimited shows account.
You'll need to supply your credentials by created a credentials.py file (these are included in .gitignore). credentials .py will have two lines

````
username = 'yourusername'
password = 'yourpassword'
````

replace yourusername with your nukely username and yourpassword with your nukely password.

Launching the web app
----
Once you've created the credentials.py file with your credentials, launch the web app with

````
> python nukely_app.py
````

By default the app will launch locally at 127.0.0.1:8080