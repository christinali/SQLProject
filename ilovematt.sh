dropdb bookbagging; createdb bookbagging; psql bookbagging -af create.sql
psql bookbagging -af department.sql

#after this you should run app.py in the server folder
#right now only the the /departments route is set up, but as we add more x.sql files more routes should become available