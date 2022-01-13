import sqlite3

DATABASE_NAME = 'database.db'


def get_database():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def create_tables():
    tables = [
        """
            CREATE TABLE IF NOT EXISTS user 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL,
                image TEXT NOT NULL
            )
        """,
        """

        """
    ]
    database = get_database()
    cursor = database.cursor()
    for table in tables:
        cursor.execute(table)