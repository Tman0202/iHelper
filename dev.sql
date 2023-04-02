-- This script that prepares a MySQL server for the project

-- creates the given database if it does not exist
CREATE DATABASE IF NOT EXISTS iHelper_dev_db;

-- creates the given user with its corresponding password if it doesn't exist
CREATE USER IF NOT EXISTS 'iHelper_dev'@'localhost' IDENTIFIED BY 'iHelper_dev_pwd';

-- grants all privileges on given db to just created user
GRANT ALL PRIVILEGES ON iHelper_dev_db.* TO 'iHelper_dev'@'localhost';

-- grants select privileges only on performance_schema to given user
GRANT SELECT ON performance_schema.* TO 'iHelper_dev'@'localhost';