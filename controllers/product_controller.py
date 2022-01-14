from flask import Flask, request, make_response, jsonify
from database.database import get_database
from models.product_model import Product

app = Flask(__name__)

def get():
    try:
        database = get_database()
        cursor = database.cursor()
        query = 'SELECT * FROM product'
        cursor.execute(query)
        data = cursor.fetchall()
        list = []
        for _data in data:
            dictionary = dict(id=_data[0], name=_data[1], price=_data[2], image=data[3])
            list.append(dictionary)
        response = dict(ok=True, message='Successfully', products=list, total=len(list))
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
        query = 'SELECT * FROM product WHERE id = ?'
        cursor.execute(query, [id])
        data = cursor.fetchone()
        list = []
        dictionary = dict(id=data[0], name=data[1], price=data[2], image=data[3])
        list.append(dictionary)
        response = dict(ok=True, message='Successfully', product=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        database.close()


def insert():
    try:
        product_details = request.get_json()
        product = Product(product_details['name'], product_details['price'], product_details['image'])
        database = get_database()
        cursor = database.cursor()
        query = 'INSERT INTO product(name, price, image) VALUES (?, ?, ?)'
        cursor.execute(query, [product.name, product.price, product.image])
        database.commit()
        dictionary = dict(id=product.id, name=product.name, price=product.price, image=product.image)
        response = dict(ok=True, message='Successfully', product=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        database.close()

def update(id: int):
    try:
        product_details = request.get_json()
        product = Product(product_details['name'], product_details['price'], product_details['image'], id)
        database = get_database()
        cursor = database.cursor()
        query = 'UPDATE product SET name = ?, price = ?, image = ? WHERE id = ?'
        cursor.execute(query, [product.name, product.price, product.image, product.id])
        database.commit()
        dictionary = dict(id=product.id, name=product.name, price=product.price, image=product.image)
        response = dict(ok=True, message='Successfully', product=dictionary)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        database.close()

def delete(id: int):
    try:
        product = find_by_id(id)['product']
        database = get_database()
        cursor = database.cursor()
        query = 'DELETE FROM product WHERE id = ?'
        cursor.execute(query, [id])
        database.commit()
        response = dict(ok=True, message='Successfully', product=product)
        return make_response(jsonify(response), 200)
    except(Exception):
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        database.close()