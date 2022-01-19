from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.order_model import Order

def get(id: int):
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM _order WHERE user = ?'
        cursor.execute(query, [id])
        data = cursor.fetchall()
        list = []
        for _data in data:
            dictionary = dict(id=_data[0], location=_data[1], method=_data[2], user=_data[3], product=_data[4],
                              order=_data[5])
            list.append(dictionary)
        response = dict(ok=True, message='Successfully', orders=list, total=len(list))
        return make_response(jsonify(response), 200)
    except (Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def insert():
    try:
        order_details = request.get_json()
        order = Order(order_details['location'], order_details['method'], order_details['user'], order_details['product'],
                      order_details['order'])
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO _order(location, method, user, product, _order) VALUES (?, ?, ?, ?, ?)'
        cursor.execute(query, [order.location, order.method, order.user, order.product, order.order])
        database.commit()
        dictionary = dict(id=order.id, location=order.location, method=order.method, user=order.user,
                          product=order.product, order=order.order)
        response = dict(ok=True, message='Successfully', order=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)