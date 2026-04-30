import sqlite3

CREATE_COMPANIONS_TABLE = """
CREATE TABLE IF NOT EXISTS companions (
    id INTEGER PRIMARY KEY,
    name TEXT,
    adventure TEXT,
    rating INTEGER
)
"""

INSERT_COMPANION = "INSERT INTO companions (name, adventure, rating) VALUES (?, ?, ?);"

GET_ALL_COMPANIONS = "SELECT * FROM companions;"
GET_COMPANIONS_BY_NAME = "SELECT * FROM companions WHERE name = ?;"
GET_BEST_ADVENTURE_FOR_COMPANION = """
SELECT * FROM companions
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;
"""

DELETE_COMPANION_BY_ID = "DELETE FROM companions WHERE id = ?;"
DELETE_COMPANION_BY_NAME = "DELETE FROM companions WHERE name = ?;"


def connect():
    return sqlite3.connect("companions.db")


def create_tables(connection):
    with connection:
        connection.execute(CREATE_COMPANIONS_TABLE)


def add_companion(connection, name, adventure, rating):
    with connection:
        connection.execute(INSERT_COMPANION, (name, adventure, rating))


def get_all_companions(connection):
    with connection:
        return connection.execute(GET_ALL_COMPANIONS).fetchall()


def get_companions_by_name(connection, name):
    with connection:
        return connection.execute(GET_COMPANIONS_BY_NAME, (name,)).fetchall()


def get_best_adventure_for_companion(connection, name):
    with connection:
        return connection.execute(GET_BEST_ADVENTURE_FOR_COMPANION, (name,)).fetchone()


def delete_companion_by_id(connection, companion_id):
    with connection:
        connection.execute(DELETE_COMPANION_BY_ID, (companion_id,))


def delete_companion_by_name(connection, name):
    with connection:
        connection.execute(DELETE_COMPANION_BY_NAME, (name,))