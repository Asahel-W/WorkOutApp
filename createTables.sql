CREATE TABLE User(username TEXT UNIQUE,
    password TEXT,
    email TEXT UNIQUE,
    uid INT PRIMARY KEY);