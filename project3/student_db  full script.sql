create database student_db;

CREATE TABLE results (
	id int auto_increment primary key,
    name VARCHAR(50),
    Physics INT,
    Bio INT,
    Maths INT,
    Chemistry INT,
    English INT,
    Nepali INT,
    total INT,
    percentage FLOAT,
    division VARCHAR(20),
	output enum('Pass','Fail')
);


select * from results;

