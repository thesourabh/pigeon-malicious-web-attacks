#### Install Dependencies
`sudo su`

`apt-get install sqlite3 libsqlite3-dev`

`pip install -r requirements.txt`

#### Export Environment Variables
##### Ubuntu
`export FLASK_APP=pigeon && export FLASK_ENV=development`

#### Initialize Database
`flask init-db`

#### Run
`flask run`

#### SQL Injection
`a','1');DROP TABLE user;`

#### Cross-site scripting
Code needs to be sanitized for SQL
[SQL Escape](https://www.freeformatter.com/sql-escape.html)

`<script type='application/javascript'>alert('xss');</script>`