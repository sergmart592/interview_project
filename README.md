# Interview Project
Project done for a interview process
(MongoDB + Flask + Vue + GIPHY API)
Python and Javascript

# AH!-ZOM Gif Searcher

This is a small web app for an interview process
It consist of the following

  - BACKEND - Python Flask Web Framework the web server
  - FRONTEND - Javascript Vue.JS For a more responsive site.
  - DATABASE - MongoDB serving as the database to store user data
NOTE:
This project was developed and run on Ubuntu 18.04 x64

### Python Requirements
Make sure the current working directory is `interview_project/`
A python virtual enviroment can be created by running the following:
```
python3.6 -m venv <name of enviroment>
```
Once the virtual enviroment is created, enable the enviroment by running the following.
```
source <name of enviroment>/bin/activate
```
Once the enviroment is enable. Run the following command with the specified file to install the packages listed below.
```
pip install -r requirements.txt
```
```
bcrypt==3.1.5
cffi==1.11.5
Click==7.0
Flask==1.0.2
Flask-Bcrypt==0.7.1
Flask-Cors==3.0.7
Flask-JWT-Extended==3.14.0
Flask-PyMongo==2.2.0
itsdangerous==1.1.0
Jinja2==2.10
MarkupSafe==1.1.0
pkg-resources==0.0.0
pycparser==2.19
PyJWT==1.7.1
pymongo==3.7.2
six==1.12.0
Werkzeug==0.14.1
```
### Javascript Requirements
The following applications/packages are needed to install the rest of the JS dependencies
```
Vue v3.2.1
Vue CLI v2.9.3
Node v8.10.0
npm v6.5.0
```
Packages Needed
```
"axios": "^0.18.0",
"bootstrap": "^4.2.1",
"jwt-decode": "^2.2.0",
"vue": "^2.5.2",
"vue-router": "^3.0.1"
```
To install the above dependencies run the following:
`npm install`

### Databas Requirements
```
MongoDB shell version v3.6.3
```

## How to Run


### Backend - Flask Server
To run the backend portion of the project, run the following
```
cd interview_project/
source <virtual enviroment name>/bin/activate
cd backend/
python giphyApp.py
```
Output:
```
 * Serving Flask app "giphyApp" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 249-288-666
```
This setup is the fast way of testing and looking at the web app functionality
The backend could also be tested by using tools such as `Postman` application that will send POST request. For more details:
`https://www.getpostman.com/`

### Frontend - Vue JS Framework

To run the front end of the application execute the following:
`npm start`
Output
```
 DONE  Compiled successfully in 8141ms                                           4:06:38 PM
 I  Your application is running here: http://localhost:8080
```

Once both the Backend and Frontend are correctly running. Access the website at `http://localhost:8080`

## How to Use

### Register
To register an account, 3 things are needed.
- first name
- last name
- email
- password
Once the information is entered correctly, the page will swtich to the Login page.

### Login
To login, the email and password need to be supplied.
If not valid, the page will displayed stating that the email or password are invalid
and will redirect to the login page to retry once again.

### Logout
To logout simply just click on the logout text in the navigation bar.

### Search Gifs
Input any related keywords to search for gifs.
If the user had any favorites already selected, they will appear below the search bar and above the searched gifs.
Below the `Remove Favorites` button and `Save Favorites` button, the gifs will appear.
Under each gif there will be a `Favorite` button that will add the gif to the favorites above. To delete the favorite from the list, simply click on the gif.
To save all the favorites to the database, click on the `Save Favorites` and to save the removed gifs, click on the `Remove Favorites` button to remove them also from the database.
The gifs that appear after the buttons are pressed will be the once that will appear if you log out and log back in for the specific user. 



# What was learned.
Most of the technologies here I have little to no experience in while doing this project.
- I am using the localStorage in the browser to hold the user information, even if the password is encrypted, the localStorage is vulnerable to CSRF attacks. This is something that I learned after implementing it on the project.
- I am using only POST methods to where it is better to implement methods that use and accept GET and DELETE.
- This entire project was a huge learning experience for me. 


