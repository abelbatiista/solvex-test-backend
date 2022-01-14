from flask import Flask
from flask_cors import CORS
import controllers.user_controller as user_controller
import controllers.product_controller as product_controller
import controllers.file_controller as file_controller
from database.database import create_tables

app = Flask(__name__)
CORS(app, supports_credentials=True)

# User Routes

@app.route('/api/user', methods=['GET'])
def get_users():
    data = user_controller.get()
    return data

@app.route('/api/user/<id>', methods=['GET'])
def find_user_by_id(id):
    data = user_controller.find_by_id(id)
    return data

@app.route('/api/user', methods=['POST'])
def insert_user():
    data = user_controller.insert()
    return data

@app.route('/api/user/<id>', methods=['PUT'])
def update_user(id):
    data = user_controller.update(id)
    return data

@app.route('/api/user/<id>', methods=['DELETE'])
def delete_user(id):
    data = user_controller.delete(id)
    return data

'''******************************************'''

# Products Routes

@app.route('/api/product', methods=['GET'])
def get_products():
    data = product_controller.get()
    return data

@app.route('/api/product/<id>', methods=['GET'])
def find_product_by_id(id):
    data = product_controller.find_by_id(id)
    return data

@app.route('/api/product', methods=['POST'])
def insert_product():
    data = product_controller.insert()
    return data

@app.route('/api/product/<id>', methods=['PUT'])
def update_product(id):
    data = product_controller.update(id)
    return data

@app.route('/api/product/<id>', methods=['DELETE'])
def delete_product(id):
    data = product_controller.delete(id)
    return data

'''******************************************'''

# Uploads Routes

@app.route('/api/file/upload/user/<id>', methods=['POST'])
def upload_file(id):
    return file_controller.upload_file(id)

@app.route('/api/file/download/user/<id>', methods=['GET'])
def download_file(id):
    return file_controller.download_file(id)

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