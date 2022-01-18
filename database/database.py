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
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                lastname TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT DEFAULT 'USER_ROLE' NOT NULL,
                image TEXT NULL,
                token TEXT NULL
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS product 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                image TEXT
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS message 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                image TEXT
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS product 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                price REAL NOT NULL,
                image TEXT
            )
        """
    ]
    database = get_database()
    cursor = database.cursor()
    for table in tables:
        cursor.execute(table)