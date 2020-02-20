CREATE TABLE sent (
    id INTEGER PRIMARY KEY,
    text TEXT UNIQUE
);

CREATE TABLE word (
    id INTEGER PRIMARY KEY,
    text TEXT UNIQUE
);

CREATE TABLE sent_word (
    sent_id INTEGER NOT NULL,
    word_id INTEGER NOT NULL,
    UNIQUE(sent_id, word_id),
    FOREIGN KEY (sent_id) REFERENCES sent(id),
    FOREIGN KEY (word_id) REFERENCES word(id)
);
