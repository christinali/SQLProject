CREATE TABLE Department
(    name VARCHAR(100) NOT NULL,
    department_id VARCHAR(100) NOT NULL,
 PRIMARY KEY(department_id));

CREATE TABLE Professor
(	name VARCHAR(100) NOT NULL,
	professor_id INTEGER NOT NULL,
	PRIMARY KEY(professor_id));

#CREATE TABLE Student
#(	name VARCHAR(100) NOT NULL,
#	email VARCHAR(100) NOT NULL,
#	student_id INTEGER NOT NULL,
#	PRIMARY KEY(student_id));

CREATE TABLE Comment
(	comment_id INTEGER NOT NULL,
	text_content VARCHAR(100) NOT NULL,
	student_id INTEGER NOT NULL, #foreign key later
	upvotes INTEGER NOT NULL,
	downvotes INTEGER NOT NULL,
	PRIMARY KEY(comment_id));