# Bookbaggregator
CS 316 Course Project

Install PostgreSQL via your Operating System's package manager (brew, apt-get, etc.).

Run the command `./setup.sh`
This may take a few minutes as it is loading all the data we have (quite a lot) into a PostgreSQL database. 

To start the frontend server run the following commands:

`cd frontend` 

`npm install`

`npm start`

Go back into root sqlproject directory (`cd ..`)

Start the backend Flask server (which will provide a REST API for the frontend and interface with the PostgreSQL database) by running `python3 server/app.py`

Open localhost:3000 in browser and enjoy!