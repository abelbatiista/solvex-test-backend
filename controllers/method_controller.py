from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.method_model import Method

def get(id: int):
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM method WHERE user = ?'
        cursor.execute(query, [id])
        data = cursor.fetchall()
        list = []
        for _data in data:
            dictionary = dict(id=_data[0], user=[1], brand=_data[2], number=_data[3], expiration=_data[4], cvv=_data[5])
            list.append(dictionary)
        response = dict(ok=True, message='Successfully', methods=list, total=len(list))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def insert():
    try:
        method_details = request.get_json()
        method = Method(method_details['user'], method_details['brand'], method_details['number'],
                        method_details['expiration'], method_details['cvv'])
        database = get_database()
        cursor = database.cursor()
        query =  'INSERT INTO method(user, brand, number, expiration, cvv)  VALUES (?, ?, ?, ?, ?)'
        cursor.execute(query, [method.user, method.brand, method.number, method.expiration, method.cvv])
        database.commit()
        dictionary = dict(id=method.id, user=method.user, brand=method.brand, number=method.number,
                          expiration=method.expiration, cvv=method.cvv)
        response = dict(ok=True, message='Successfully', method=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)