create database testwork;

use testwork;

create table user(
    id int,
    name varchar(10),
    account varchar(10),
    password varchar(20)
);

insert into user(id,name,account,password) values(1,'csu','820822','123456');