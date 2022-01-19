from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.user_model import User

app = Flask(__name__)

def __users():
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT * FROM user'
    cursor.execute(query)
    data = cursor.fetchall()
    list = []
    for _data in data:
        dictionary = dict(id=_data[0], name=_data[1], lastname=_data[2], email=_data[3], password=_data[4],
                          role=_data[5], image=_data[6])
        list.append(dictionary)
    return list

def get():
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM user'
        cursor.execute(query)
        data = cursor.fetchall()
        list = []
        for _data in data:
            dictionary = dict(id=_data[0], name=_data[1], lastname=_data[2], email=_data[3], password=_data[4],
                              role=_data[5], image=_data[6])
            list.append(dictionary)
        response = dict(ok=True, message='Successfully', users=list, total=len(list))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def find_by_id(id: int):
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM user WHERE id = ?'
        cursor.execute(query, [id])
        data = cursor.fetchone()
        list = []
        dictionary = dict(id=data[0], name=data[1], lastname=data[2], email=data[3], password=data[4],
                          role=data[5], image=data[6])
        list.append(dictionary)
        response = dict(ok=True, message='Successfully', user=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def insert():
    try:
        users = __users()
        user_details = request.get_json()
        user = User(user_details['name'], user_details['lastname'],
                    user_details['email'], user_details['password'],
                    None, None)
        for u in users:
            if(u['email'] == user.email):
                response = dict(ok=False, message='Email exists.')
                return make_response(jsonify(response), 200)
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO user(name, lastname, email, password) VALUES (?, ?, ?, ?)'
        cursor.execute(query, [user.name, user.lastname, user.email, user.password])
        database.commit()
        dictionary = dict(id=user.id, name=user.name, lastname=user.lastname, email=user.email, password=user.password,
                          role=user.role, image=user.image)
        response = dict(ok=True, message='Successfully', user=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def update(id: int):
    try:
        users = __users()
        user_details = request.get_json()
        user = User(user_details['name'], user_details['lastname'],
                    user_details['email'], None, None, None, id)
        for u in users:
            if (u['email'] == user.email):
                response = dict(ok=False, message='Email exists.')
                return make_response(jsonify(response), 200)
            if (u['id'] == int(id)):
                database = get_database()
                cursor = database.cursor()
                query = 'UPDATE user SET name = ?, lastname = ?, email = ? WHERE id = ?'
                cursor.execute(query, [user.name, user.lastname, user.email, user.id])
                database.commit()
                for u in users:
                    if (u['id'] == int(id)):
                        user.id = u['id']
                        user.password = u['password']
                        user.image = u['image']
                        user.image = u['role']
                dictionary = dict(id=user.id, name=user.name, lastname=user.lastname, email=user.email,
                                  password=user.password,
                                  role=user.role, image=user.image)
                response = dict(ok=True, message='Successfully', user=dictionary)
                return make_response(jsonify(response), 200)
        response = dict(ok=False, message='User not exists.')
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def delete(id: int):
    try:
        user = find_by_id(id)['user']
        database = get_database()
        cursor = database.cursor()
        query = 'DELETE FROM user WHERE id = ?'
        cursor.execute(query, [id])
        database.commit()
        response = dict(ok=True, message='Successfully', user=user)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)