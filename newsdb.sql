--
-- File generated with SQLiteStudio v3.3.3 on Tue Jun 1 15:32:35 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: category
CREATE TABLE category (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name VARCHAR (50) NOT NULL, url VARCHAR (255) NOT NULL);

-- Table: Comment
CREATE TABLE Comment (id INTEGER PRIMARY KEY AUTOINCREMENT, content TEXT, news_id INTEGER REFERENCES news (id));

-- Table: news
CREATE TABLE news (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, subject VARCHAR (255) NOT NULL, description TEXT, image VARCHAR (255) NOT NULL, original_url VARCHAR (255), category_id INTEGER REFERENCES category (id));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
