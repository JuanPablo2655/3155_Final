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

CREATE TABLE Game(
    gaming_id SERIAL NOT NULL, 
    title VARCHAR(255) NOT NULL, 
    genre VARCHAR(255) NOT NULL, 
    PRIMARY KEY (gaming_id)
)

CREATE TABLE Community(
    community_id SERIAL NOT NULL, 
    community_name VARCHAR(255) NOT NULL
    PRIMARY KEY (community_id)
)

CREATE TABLE Post(
    post_id SERIAL NOT NULL, 
    title VARCHAR(255) NOT NULL, 
    author VARCHAR(255) NOT NULL, 
    content VARCHAR(255) NOT NULL, 
    comment VARCHAR(255) NOT NULL, 
    PRIMARY KEY (post_id)
)