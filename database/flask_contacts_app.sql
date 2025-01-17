create database flask_contacts_app;

use flask_contacts_app;

create table contacts(
    id int unsigned auto_increment primary key,
    fullname varchar(150),
    phone varchar(15),
    email varchar(100) not null unique
)