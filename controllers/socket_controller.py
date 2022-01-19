from flask import Flask, request, make_response, jsonify
from database.database import get_database

app = Flask(__name__)

def users():
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

def messages():
    database = get_database()
    cursor = database.cursor()
    query = 'SELECT * FROM message'
    cursor.execute(query)
    data = cursor.fetchall()
    list = []
    for _data in data:
        dictionary = dict(id=_data[0], to=_data[2], message=_data[3], date=_data[4])
        dictionary['from'] = _data[1]
        list.append(dictionary)
    return list