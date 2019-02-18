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
  title TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);

CREATE TABLE relation (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  of_user_id INTEGER NOT NULL,
  to_user_id INTEGER NOT NULL,
  relation INTEGER NOT NULL,
  FOREIGN KEY (of_user_id) REFERENCES user (id),
  FOREIGN KEY (to_user_id) REFERENCES user (id)
);