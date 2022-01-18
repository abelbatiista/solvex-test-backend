from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.user_model import User
from helpers.token_helper import get_token, get_token_user, get_user_by_token
app = Flask(__name__)

def login():
    try:
        auth_details = request.get_json()
        email = auth_details['email']
        password = auth_details['password']
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM user WHERE email = ? AND password = ?'
        cursor.execute(query, [email, password])
        data = cursor.fetchone()
        if data == None:
            response = dict(ok=False, message='User not found.')
            return make_response(jsonify(response), 404)
        dictionary = dict(id=data[0], name=data[1], lastname=data[2], email=data[3], password=data[4],
                          role=data[5], image=data[6])
        token = get_token(dictionary['id'])
        response = dict(ok=True, message='Successfully', user=dictionary, token=str(token))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def login_check():
    try:
        token = str(request.headers['x-token'])
        data = get_user_by_token(token)
        if (data == None):
            response = dict(ok=False, message='No user found.')
            return make_response(jsonify(response), 400)
        dictionary = dict(id=data[0], name=data[1], lastname=data[2], email=data[3], password=data[4],
                          role=data[5], image=data[6])
        response = dict(ok=True, message='Successfully', user=dictionary, token=str(data[7]))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def logout():
    try:
        if(get_token_user() == None):
            response = dict(ok=False, message='Unknown error.')
            return make_response(jsonify(response), 400)
        id = get_token_user()
        database = get_database()
        cursor = database.cursor()
        query = 'UPDATE user SET token = NULL WHERE id = ?'
        cursor.execute(query, [id])
        database.commit()
        response = dict(ok=True, message='Successfully')
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)