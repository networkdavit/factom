DROP TABLE IF EXISTS facts;

CREATE TABLE facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    fact TEXT NOT NULL
);
