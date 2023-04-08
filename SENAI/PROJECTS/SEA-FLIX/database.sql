create database seaflix2;

USE seaflix2;

create table users (
idUsers INT auto_increment primary key,
user_name varchar(50),
user_age int,
user_email varchar(50),
user_plan varchar(50),
user_type varchar(50),
user_id int
);

create table movies (
idmovies int auto_increment primary key,
movie_name varchar(50),
movie_desc varchar(150),
movie_plan varchar(50),
movie_class int
);
