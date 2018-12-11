dropdb bookbagging; createdb bookbagging;
psql bookbagging -af sqlFiles/create.sql;
psql bookbagging -af sqlFiles/department.sql;
psql bookbagging -af sqlFiles/student.sql;