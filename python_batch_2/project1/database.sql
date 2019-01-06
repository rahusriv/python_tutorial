CREATE DATABASE ecomm;

USE ecomm;

CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255),phone_no VARCHAR(255),pwd VARCHAR(255), data VARCHAR(255), PRIMARY KEY (phone_no));

CREATE TABLE products (product_id VARCHAR(255), product_name VARCHAR(255),category VARCHAR(255),price DEC, quantity INT, PRIMARY KEY (product_id));

CREATE TABLE orders (order_id INT AUTO_INCREMENT PRIMARY KEY , phone_no VARCHAR(255),product_id VARCHAR(255), quantity INT);
