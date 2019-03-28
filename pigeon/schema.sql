DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS relation;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE relation (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  user_id_1 INTEGER NOT NULL,
  user_id_2 INTEGER NOT NULL,
  type INTEGER NOT NULL,
  FOREIGN KEY (user_id_1) REFERENCES user (id),
  FOREIGN KEY (user_id_2) REFERENCES user (id)
);

-- Add dummy data
INSERT INTO user values(1, 'admin', 'admin', 'Admin', 'Admin');
INSERT INTO user values(2, 'hnadeem', 'hnadeem', 'Hassan', 'Nadeem');
INSERT INTO user values(3, 'Pranavi', 'Pranavi', 'Pranavi', 'Rambhakta');
INSERT INTO user values(4, 'Sourabh', 'Sourabh', 'Sourabh', 'Shetty');
INSERT INTO user values(5, 'Lonely', 'Lonely', 'Lonely', 'Misanthrope');

INSERT INTO post values(NULL, 1, '2001-11-11 13:23:44', 'Hello, Admin here!');
INSERT INTO post values(NULL, 3, '2020-11-11 13:23:44', 'OMG, 5590 is so cool!');
INSERT INTO post values(NULL, 4, '2015-07-07 13:23:44', "A huge round of applause for what I can only describe as Eva Green's rap battle with Lucifer #PennyDreadful.");
INSERT INTO post values(NULL, 4, '2016-11-26 12:44:00', "I just let a family cut in line ahead of me at the airport so it wouldn't be awkward if we crashed and had to survive on an island together.");

INSERT INTO relation values(NULL, 2, 3, 1);
INSERT INTO relation values(NULL, 3, 2, 1);
INSERT INTO relation values(NULL, 3, 4, 1);
INSERT INTO relation values(NULL, 4, 2, 1);
INSERT INTO relation values(NULL, 4, 3, 1);
