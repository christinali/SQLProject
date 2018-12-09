createdb bookbagging; echo "hello";
psql bookbagging -af sqlFiles/create.sql;
psql bookbagging -af sqlFiles/department.sql;
psql bookbagging -af sqlFiles/student.sql;
psql bookbagging -af sqlFiles/class.sql;
psql bookbagging -af sqlFiles/professor.sql;
psql bookbagging -af sqlFiles/comment.sql;
psql bookbagging -af sqlFiles/teaches.sql;
psql bookbagging -af sqlFiles/taken.sql;

#after this you should run app.py in the server folder
#right now only the the /departments route is set up, but as we add more x.sql files more routes should become available
