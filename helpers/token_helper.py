from strgen import StringGenerator
from database.database import get_database

def __token_exists(id: int):
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT * FROM user WHERE token IS NOT NULL AND token = ?'
    cursor.execute(query, [id])
    data = cursor.fetchone()
    if data != None:
        __remove_token(data[0])

def __remove_token(id: int):
    database = get_database()
    cursor = database.cursor()
    query = 'UPDATE user SET token = NULL WHERE id = ?'
    cursor.execute(query, [id])
    database.commit()

def get_token_user():
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT id FROM user WHERE token IS NOT NULL'
    cursor.execute(query, [])
    data = cursor.fetchone()
    return None if data == None else data[0]

def get_user_by_token(token: str):
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT * FROM user WHERE token IS NOT NULL AND token = ?'
    cursor.execute(query, [token])
    data = cursor.fetchone()
    return None if data == None else data

def get_token(id: int):
    __token_exists(id)
    token = StringGenerator(r"[\w]{50}").render()
    database = get_database()
    cursor = database.cursor()
    query = 'UPDATE user SET token = ? WHERE id = ?'
    cursor.execute(query, [token, id])
    database.commit()
    return token

def verify_token():
    pass