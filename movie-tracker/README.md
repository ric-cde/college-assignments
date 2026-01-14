# Launching the app

1. Install npm, node, and mongodb. (Active mongodb service is required).
2. Navigate to movie-tracker directory and run: 'npm install'

## Build version
3. Type: 'npm run seed'. This runs a script to add a sample database to the db (converted from ratings.csv), creates unique indexes, etc. NB: If an error is encountered on first run, you may need to run this script twice. 
4. Type: 'npm start'. The website will now be available at http://localhost:8081

The full project can be used/accessed from this build version.

## Development version
This project utilises create-react-app, so two servers are required for development mode. 

If you encounter issues with the build version, after starting the node server as described above, you can also:

5. Navigate to movie-tracker/ui and run 'npm install' (installs necessary create-react-app packages).
6. Type: 'npm start'. (NB: running this in Powershell within VS Code sometimes caused issues; you may need to run it in a separate window). 

The development website will now also be available at http://localhost:3000

# Troubleshooting*

Running the database script a second time (clears existing documents) should work if issues/conflicts are encountered.

If the database script does not initialise at all, you can also manually create a database and a "recommends" collection in MongoDB Compass.

# References

I've utilised a number of tutorials & guides. Chief among these are the book, Pro MERN Stack 2, various documentation, and this guide for setting up user authentication with Node & React:

  https://icodemag.com/how-to-build-a-login-register-app-with-the-mern-stack-part-1-getting-started/

I've adapted/used code from this tutorial in several places; it's cited in e.g. server.js, ui/login.js