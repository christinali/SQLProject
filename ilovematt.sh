dropdb bookbagging; createdb bookbagging; psql bookbagging -af create.sql
<<<<<<< HEAD
psql bookbagging -af department.sql; psql bookbagging -af professor.sql; psql bookbagging -af comment.sql
=======
psql bookbagging -af department.sql;
psql bookbagging -af student.sql;

>>>>>>> 6ce3ff94b91f275b515508e33a911343ba0fe651

#after this you should run app.py in the server folder
#right now only the the /departments route is set up, but as we add more x.sql files more routes should become available

