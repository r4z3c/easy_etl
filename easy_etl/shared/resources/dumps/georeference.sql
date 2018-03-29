DROP DATABASE IF EXISTS easy_etl;

CREATE DATABASE easy_etl;

USE easy_etl;

CREATE TABLE states (
    id INT,
    name VARCHAR(3)
);

CREATE TABLE cities (
    id INT,
    state_id INT,
    name VARCHAR(255)
);

INSERT INTO states (id, name) VALUES
    (1, 'MG'),
    (2, 'RJ'),
    (3, 'SP');

INSERT INTO cities (id, state_id, name) VALUES
    (11, 1, 'Ipatinga'),
    (12, 1, 'São Vicente'),
    (21, 2, 'Angra dos Reis'),
    (22, 2, 'Paraty'),
    (31, 3, 'Franca'),
    (32, 3, 'São Paulo');
