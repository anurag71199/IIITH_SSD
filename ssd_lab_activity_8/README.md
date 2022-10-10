###Lab 8 MERN STACK

Backend (server):

setup the backend using express JS and mongo db. Used mongo db's connection string to establish a connection on my local 3000 port (inside the .env folder). Made 2 routes for login and query records. Made 2 models, one which contained user info (roll,pass,role) and the other one for queries. Wrote the main connection code in app.js. Run the server using node app.js

Once the server ran successfully, moved on to the frontend in REACT.

Frontend (client):

Set the routes for Login, Signup and Profile Page in App.js. Made a folder called components which contains individual js pages for each mentioned functionalities. These files act as the front end information sender to the backend where the info is processed in the routes.

## HOW TO RUN

Go to the server folder:

Install the dependencies using npm - 
    express
    mongoose
    dotenv
    cors
    body-parser
    bcrypt
    express-session
    connect-mongodb-session

Run : node app.js

Go to the client>mern-client folder and run: npm install

Then run: npm start to launch the website. (Press y for the prompt for running the client on another port)
 
