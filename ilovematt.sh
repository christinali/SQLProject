dropdb bookbagging; createdb bookbagging;
psql bookbagging -af sqlFiles/create.sql;
psql bookbagging -af sqlFiles/department.sql;
# psql -U cheesecake -d bookbagging -c "COPY department FROM '/home/cheesecake/sqlproject/csv_copies/departmentsunique.csv' DELIMITERS ',' CSV;"
psql bookbagging -af sqlFiles/student.sql;
psql bookbagging -af sqlFiles/class.sql;
# psql -U cheesecake -d bookbagging -c "COPY class FROM '/home/cheesecake/sqlproject/csv_copies/classescleaned.csv' DELIMITERS ',' CSV;"
psql bookbagging -af sqlFiles/professor.sql;
# psql -U cheesecake -d bookbagging -c "COPY professor FROM '/home/cheesecake/sqlproject/csv_copies/profsunique.csv' DELIMITERS ',' CSV;"
psql bookbagging -af sqlFiles/comment.sql;
psql bookbagging -af sqlFiles/teaches.sql;
# psql -U cheesecake -d bookbagging -c "COPY teaches FROM '/home/cheesecake/sqlproject/csv_copies/teachesunique.csv' DELIMITERS ',' CSV;"
psql bookbagging -af sqlFiles/taken.sql;



#after this you should run app.py in the server folder
#right now only the the /departments route is set up, but as we add more x.sql files more routes should become available