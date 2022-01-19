from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.message_model import Message

def _insert(message: Message):
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO message(from_id, to_id, message, date) VALUES (?, ?, ?, ?)'
        cursor.execute(query, [message.frm, message.to, message.message, message.date])
        database.commit()
    except(Exception):
        pass

def get():
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM message'
        cursor.execute(query, [])
        data = cursor.fetchall()
        list = []
        for _data in data:
            dictionary = dict(id=_data[0], to=_data[2], message=_data[3], date=_data[4])
            dictionary['from'] = _data[1]
            list.append(dictionary)
        response = dict(ok=True, message='Successfully', methods=list, total=len(list))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def insert():
    try:
        message_details = request.get_json()
        message = Message(message_details['from'], message_details['to'], message_details['message'],
                          message_details['date'])
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO message(from_id, to_id, message, date) VALUES (?, ?, ?, ?)'
        cursor.execute(query, [message.frm, message.to, message.message, message.date])
        database.commit()
        dictionary = dict(id=message.id, to=message.to, message=message.message, date=message.date)
        dictionary['from'] = message.frm
        response = dict(ok=True, message='Successfully', method=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)