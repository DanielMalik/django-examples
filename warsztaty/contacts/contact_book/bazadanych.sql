CREATE DATABASE contacts;

CREATE TABLE Contacts (
    id int auto_increment,
    name varchar(255),
    surname varchar(255),
    mail varchar(255),
    phone_number varchar(32),
    PRIMARY KEY(id));

INSERT INTO Contacts VALUES (0, "Baba", "Jaga", "baba@jaga.pl", "91893712");

SELECT * FROM Contacts;
