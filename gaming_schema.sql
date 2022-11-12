--Gaming tables to insert into the database and get the backend working. 

--Table for accounts
CREATE TABLE Account(
    account_id SERIAL NOT NULL, 
    user_name VARCHAR(255) NOT NULL, 
    full_Name VARCHAR(255) NOT NULL,
    gaming_password VARCHAR (255) NOT NULL
    email VARCHAR(255) NOT NULL
    PRIMARY KEY (account_id)
);