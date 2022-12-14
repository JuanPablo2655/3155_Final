CREATE TABLE account(
    account_id SERIAL NOT NULL, 
    user_name VARCHAR(255) NOT NULL, 
    full_Name VARCHAR(255) NOT NULL,
    gaming_password VARCHAR (255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    PRIMARY KEY (account_id)
);

CREATE TABLE community (
    community_id SERIAL NOT NULL, 
    community_name VARCHAR(255) NOT NULL,
    description VARCHAR(255) NOT NULL,
    PRIMARY KEY (community_id)
);

CREATE TABLE account_community(
    account_id INT, 
    community_id INT,
    PRIMARY KEY (account_id, community_id), 
    FOREIGN KEY (account_id) REFERENCES account(account_id),
    FOREIGN KEY (community_id) REFERENCES community(community_id)
);

CREATE TABLE post (
    post_id SERIAL NOT NULL, 
    title VARCHAR(255) NOT NULL, 
    author VARCHAR(255) NOT NULL, 
    content VARCHAR(4096) NOT NULL,
    community_name VARCHAR(255) NOT NULL,  
    votes INT DEFAULT 0, 
    date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP, 
    account_id INT NOT NULL, 
    community_id INT NOT NULL, 
    PRIMARY KEY (post_id),
    FOREIGN KEY (account_id) REFERENCES account(account_id),
    FOREIGN KEY (community_id) REFERENCES community(community_id)
);

CREATE TABLE comment (
    comment_id SERIAL NOT NULL,
    author VARCHAR(255) NOT NULL, 
    date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    content VARCHAR(4096) NOT NULL, 
    votes INT DEFAULT 0, 
    post_id INT NOT NULL, 
    account_id INT NOT NULL, 
    PRIMARY KEY (comment_id),
    FOREIGN KEY (post_id) REFERENCES post(post_id),
    FOREIGN KEY (account_id) REFERENCES account(account_id)
);

INSERT INTO community VALUES (1, 'communty', 'communty description');