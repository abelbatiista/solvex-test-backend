from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send
import controllers.auth_controller as auth_controller
import controllers.user_controller as user_controller
import controllers.product_controller as product_controller
import controllers.file_controller as file_controller
from database.database import create_tables

app = Flask(__name__)
app.config['SECRET_KET'] = 'secret'
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*")
cors = CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})

# Real Time with sockets

'''******************************************'''

users = {}
@socketio.on('connect')
def on_connect():
    print('Client connected')
    socketio.emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def on_disconnect():
    users.pop(request.sid,'No user found')
    socketio.emit('current_users', users)
    print("User disconnected!\nThe users are: ", users)

@socketio.on('sign_in')
def user_sign_in(user_name, methods=['GET', 'POST']):
    users[request.sid] = user_name['name']
    socketio.emit('current_users', users)
    print("New user sign in!\nThe users are: ", users)

@socketio.on('message')
def messaging(message, methods=['GET', 'POST']):
    print('received message: ' + str(message))
    message['from'] = request.sid
    socketio.emit('message', message, room=request.sid)
    socketio.emit('message', message, room=message['to'])

# Render

@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')

'''******************************************'''

# Auth Routes

@app.route('/api/auth', methods=['POST'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def login():
    data = auth_controller.login()
    return data

@app.route('/api/auth', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def login_check():
    data = auth_controller.login_check()
    return data

@app.route('/api/auth', methods=['PUT'])
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def logout():
    data = auth_controller.logout()
    return data

'''******************************************'''

# User Routes

@app.route('/api/user', methods=['GET'])
def get_users():
    data = user_controller.get()
    return data

@app.route('/api/user/<id>', methods=['GET'])
def find_user_by_id(id: int):
    data = user_controller.find_by_id(id)
    return data

@app.route('/api/user', methods=['POST'])
def insert_user():
    data = user_controller.insert()
    return data

@app.route('/api/user/<id>', methods=['PUT'])
def update_user(id: int):
    data = user_controller.update(id)
    return data

@app.route('/api/user/<id>', methods=['DELETE'])
def delete_user(id: int):
    data = user_controller.delete(id)
    return data

'''******************************************'''

# Products Routes

@app.route('/api/product', methods=['GET'])
def get_products():
    data = product_controller.get()
    return data

@app.route('/api/product/<id>', methods=['GET'])
def find_product_by_id(id: int):
    data = product_controller.find_by_id(id)
    return data

@app.route('/api/product', methods=['POST'])
def insert_product():
    data = product_controller.insert()
    return data

@app.route('/api/product/<id>', methods=['PUT'])
def update_product(id: int):
    data = product_controller.update(id)
    return data

@app.route('/api/product/<id>', methods=['DELETE'])
def delete_product(id: int):
    data = product_controller.delete(id)
    return data

'''******************************************'''

# Uploads Routes

@app.route('/api/file/upload/<collection>/<id>', methods=['PUT'])
def upload_file(collection: str, id: int):
    return file_controller.upload_file(id, collection)

@app.route('/api/file/download/<collection>/<image>', methods=['GET'])
def download_file(collection: str, image: str):
    return file_controller.download_file(collection, image)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, x-token"
    return response

if __name__ == '__main__':
    create_tables()
    """
       Here you can change debug and port
       Remember that, in order to make this API functional, you must set debug in False
    """
    # *app.run(host='0.0.0.0', port=8000, debug=False)
    socketio.run(app, host='0.0.0.0', port=8000, debug=True)