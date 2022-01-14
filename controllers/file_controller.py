import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, make_response, jsonify
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/user'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(id: int):
    try:
        if request.method == 'POST':
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
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                response = dict(ok=True, message='Successfully')
                return make_response(jsonify(response), 200)
                # *return redirect(url_for('download_file', name=filename))
        response = dict(ok=False, message='Not found method.')
        return make_response(jsonify(response), 400)
    except:
        response = dict(ok=False, message='Error in Database.')
        return make_response(jsonify(response), 500)
    finally:
        pass

def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], 'abel.jpg')