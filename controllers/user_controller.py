from database.database import get_database
from models.user_model import User

def get():
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT * FROM user'
    cursor.execute(query)
    return cursor.fetchall()

def find_by_id(id: int):
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT * FROM user WHERE id = ?'
    cursor.execute(query, [id])
    return cursor.fetchone()

def insert(user: User):
    database = get_database()
    cursor = database.cursor()
    query = 'INSERT INTO user(name, lastname, email, password, role, image) VALUES (?, ?, ?, ?, ?, ?)'
    cursor.execute(query, [user.name, user.lastname, user.email, user.password, user.role, user.image])
    database.commit()
    return True

def update(user: User):
    database = get_database()
    cursor = database.cursor()
    query = 'UPDATE user SET name = ?, lastname = ?, email = ?, password = ?, role = ?, image = ? WHERE id = ?'
    cursor.execute(query, [user.name, user.lastname, user.email, user.password, user.role, user.image, user.id])
    database.commit()
    return True

def delete(user: User):
    database = get_database()
    cursor = database.cursor()
    query = 'DELETE FROM user WHERE id = ?'
    cursor.execute(query, [user.id])
    database.commit()
    return True