from flask import Flask, jsonify, request
from flask_cors import CORS
import controllers.user_controller as controller
from database.database import create_tables
from models.user_model import User

app = Flask(__name__)
CORS(app, supports_credentials=True)

app.route('/api/user', methods=['GET'])
def get_users():
    users = controller.get()
    return jsonify(users)

app.route('/api/user/<id>', methods=['GET'])
def find_user_by_id(id):
    user = controller.find_by_id(id)
    return jsonify(user)

app.route('/api/user', methods=['POST'])
def insert_user():
    user_details = request.get_json()
    user = User(user_details['name'], user_details['lastname'],
                user_details['email'], user_details['password'],
                user_details['role'], user_details['image'])
    response = controller.insert(user)
    return jsonify(response)

app.route('/api/user/<id>', methods=['PUT'])
def update_user(id):
    user_details = request.get_json()
    user = User(user_details['name'], user_details['lastname'],
                user_details['email'], user_details['password'],
                user_details['role'], user_details['image'], id)
    response = controller.update(user)
    return jsonify(response)

app.route('/api/user/<id>', methods=['DELETE'])
def delete_user(id):
    response = controller.delete(id)
    return jsonify(response)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

if __name__ == '__main__':
    create_tables()
    """
       Here you can change debug and port
       Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)