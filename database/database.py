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
                from_id INTEGER NOT NULL,
                to_id INTEGER NOT NULL,
                message TEXT NOT NULL,
                date TEXT NOT NULL
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS method 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user INTEGER NOT NULL,
                brand TEXT NOT NULL,
                number TEXT NOT NULL,
                expiration TEXT NOT NULL,
                cvv TEXT NOT NULL
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS location 
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user INTEGER NOT NULL,
                label TEXT NOT NULL,
                adress TEXT NOT NULL,
                street TEXT NOT NULL,
                number TEXT NOT NULL,
                sector TEXT NOT NULL,
                city TEXT NOT NULL,
                province TEXT NOT NULL,
                country TEXT NOT NULL,
                code TEXT NOT NULL
            )
        """,
        """
            CREATE TABLE IF NOT EXISTS _order
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user INTEGER NOT NULL,
                product INTEGER NOT NULL,
                location INTEGER NOT NULL,
                method INTEGER NOT NULL,
                _order TEXT NOT NULL
            )
        """
    ]
    database = get_database()
    cursor = database.cursor()
    for table in tables:
        cursor.execute(table)