from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.user_model import User

app = Flask(__name__)

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
    finally:
        database.close()

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
    finally:
        database.close()


def insert():
    try:
        user_details = request.get_json()
        user = User(user_details['name'], user_details['lastname'],
                    user_details['email'], user_details['password'],
                    user_details['role'], user_details['image'])
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO user(name, lastname, email, password, role, image) VALUES (?, ?, ?, ?, ?, ?)'
        cursor.execute(query, [user.name, user.lastname, user.email, user.password, user.role, user.image])
        database.commit()
        dictionary = dict(id=user.id, name=user.name, lastname=user.lastname, email=user.email, password=user.password,
                          role=user.role, image=user.image)
        response = dict(ok=True, message='Successfully', user=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        database.close()

def update(id: int):
    try:
        user_details = request.get_json()
        user = User(user_details['name'], user_details['lastname'],
                    user_details['email'], user_details['password'],
                    user_details['role'], user_details['image'], id)
        database = get_database()
        cursor = database.cursor()
        query = 'UPDATE user SET name = ?, lastname = ?, email = ?, password = ?, role = ?, image = ? WHERE id = ?'
        cursor.execute(query, [user.name, user.lastname, user.email, user.password, user.role, user.image, user.id])
        database.commit()
        dictionary = dict(id=user.id, name=user.name, lastname=user.lastname, email=user.email, password=user.password,
                          role=user.role, image=user.image)
        response = dict(ok=True, message='Successfully', user=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        database.close()

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
    finally:
        database.close()