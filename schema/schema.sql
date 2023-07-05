CREATE TABLE requests (
    id int not null unique,
    kad_number varchar(30) not null,
    latitude varchar(30) not null,
    longitude varchar(30) not null,
    calculate varchar(5) not null
);