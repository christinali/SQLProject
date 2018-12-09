CREATE TABLE Department
(    name VARCHAR(100) NOT NULL,
    department_id VARCHAR(100) NOT NULL,
 PRIMARY KEY(department_id));

CREATE TABLE Professor
(	professor_id INTEGER NOT NULL,
	name VARCHAR(100) NOT NULL,
	PRIMARY KEY(professor_id));


CREATE TABLE Professor1
(	professor_id1 INTEGER NOT NULL,
	name1 VARCHAR(100) NOT NULL);

CREATE TABLE Student
(	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) NOT NULL,
	student_id INTEGER NOT NULL,
	major VARCHAR(100) NOT NULL,
	FOREIGN KEY(major) REFERENCES Department(department_id),
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
	semester VARCHAR(100) NOT NULL,
	FOREIGN KEY(professor_id) REFERENCES Professor(professor_id),
	PRIMARY KEY(class_id, professor_id, semester));

CREATE TABLE Teaches1
(	class_id1 INTEGER NOT NULL,
	professor_id1 INTEGER NOT NULL,
	semester1 VARCHAR(100) NOT NULL,
	FOREIGN KEY(professor_id1) REFERENCES Professor(professor_id));

CREATE TABLE Class
(	name VARCHAR(100) NOT NULL,
	class_id INTEGER NOT NULL,
	department_id VARCHAR(100) NOT NULL,
	class_num VARCHAR(10) NOT NULL,
	cz INTEGER NOT NULL,
	ss INTEGER NOT NULL,
	cci INTEGER NOT NULL,
	alp INTEGER NOT NULL,
	ns INTEGER NOT NULL,
	qs INTEGER NOT NULL,
	ei INTEGER NOT NULL,
	fl INTEGER NOT NULL,
	r INTEGER NOT NULL,
	sts INTEGER NOT NULL,
	w INTEGER NOT NULL,
	FOREIGN KEY(department_id) REFERENCES Department(department_id),
	PRIMARY KEY(class_id));

CREATE TABLE Taken
(	semester VARCHAR(4) NOT NULL,
	star_number FLOAT NOT NULL,
	comment_id INTEGER,
	student_id INTEGER NOT NULL,
	class_id INTEGER NOT NULL,
	department_id VARCHAR(100) NOT NULL,
	difficulty FLOAT NOT NULL,
	FOREIGN KEY(department_id) REFERENCES Department(department_id),
	FOREIGN KEY(student_id) REFERENCES Student(student_id),
	FOREIGN KEY(class_id) REFERENCES Class(class_id),
	PRIMARY KEY(student_id,class_id,department_id));