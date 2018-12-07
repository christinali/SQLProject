CREATE TABLE Department
(    name VARCHAR(100) NOT NULL,
    department_id INTEGER NOT NULL,
 PRIMARY KEY(department_id));

CREATE TABLE Professor
(	name VARCHAR(100) NOT NULL,
	professor_id INTEGER NOT NULL,
	PRIMARY KEY(professor_id));

CREATE TABLE Student
(	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	student_id INTEGER NOT NULL,
	major VARCHAR(100) NOT NULL,
	PRIMARY KEY(student_id));

CREATE TABLE Comment
(	text VARCHAR(1000) NOT NULL,
	upvotes INTEGER NOT NULL,
	downvotes INTEGER NOT NULL,
	student_id INTEGER NOT NULL,
	comment_id INTEGER NOT NULL,
	FOREIGN KEY(student_id) REFERENCES Student(student_id),
	PRIMARY KEY(comment_id));

CREATE TABLE Teaches
(	class_id INTEGER NOT NULL,
	professor_id INTEGER NOT NULL,
	semester VARCHAR(4) NOT NULl,
	PRIMARY KEY(class_id, professor_id));

CREATE TABLE Class
(	name VARCHAR(100) NOT NULL,
	class_id INTEGER NOT NULL,
	department_id INTEGER NOT NULL,
	PRIMARY KEY(class_id));