import os, binascii
from flask import Flask, flash, request, redirect, url_for, send_from_directory, make_response, jsonify
from werkzeug.utils import secure_filename
from database.database import get_database

database = get_database()

def __user(id: int, collection: str):
    database = get_database()
    cursor = database.cursor()
    query = f'SELECT * FROM {collection} WHERE id = ?'
    cursor.execute(query, [id])
    data = cursor.fetchone()
    return data

def activate(collection: str):
    UPLOAD_FOLDER = f'uploads/{collection}'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    return app, ALLOWED_EXTENSIONS

def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(id: int, collection: str):
    try:
        [app, ALLOWED_EXTENSIONS] = activate(collection)
        if request.method == 'PUT':
            # check if the post request has the file part
            if 'file' not in request.files:
                response = dict(ok=False, message='File not exists.')
                return make_response(jsonify(response), 400)
                # *flash('No file part')
                # *return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                response = dict(ok=False, message='File not selected.')
                return make_response(jsonify(response), 400)
                # *flash('No selected file')
                # *return redirect(request.url)
            if file and allowed_file(file.filename, ALLOWED_EXTENSIONS):
                user = __user(id, collection)
                if(user == None):
                    response = dict(ok=False, message='Element not exists')
                    return make_response(jsonify(response), 404)
                extension = file.filename.split('.')[1]
                filename = secure_filename(f'{binascii.b2a_hex(os.urandom(10))}.{extension}')
                if(user[6] != None):
                    try:
                        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], user[6]))
                    except:
                        database = get_database()
                        cursor = database.cursor()
                        query = f'UPDATE {collection} SET image = NULL WHERE id = ?'
                        cursor.execute(query, [id])
                        database.commit()
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                database = get_database()
                cursor = database.cursor()
                query = f'UPDATE {collection} SET image = ? WHERE id = ?'
                cursor.execute(query, [filename, id])
                database.commit()
                response = dict(ok=True, message='Successfully')
                return make_response(jsonify(response), 200)
                # *return redirect(url_for('download_file', name=filename))
        response = dict(ok=False, message='Not found method.')
        return make_response(jsonify(response), 400)
    except:
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)

def download_file(collection: str, image: str):
    [app, ALLOWED_EXTENSIONS] = activate(collection)
    try:
        return send_from_directory(app.config["UPLOAD_FOLDER"], image)
    except:
        app.config["UPLOAD_FOLDER"] = f'uploads'
        return send_from_directory(app.config["UPLOAD_FOLDER"], 'no-image.png')