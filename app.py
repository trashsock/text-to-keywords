# pip install pdfminer.six
# pip install flask

import urllib.request
import os
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

# make sure folder exists beforehand
UPLOAD_FOLDER = 'uploads'        # folder where uploaded files are stored (can be changed)

app = Flask(__name__)
app.secret_key = "secret key"       # secret key for flash to run
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024     # max file size is 10MB (can be changed)


ALLOWED_EXTENSIONS = {'docx', 'pdf'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('File not found')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            return redirect('/')
        else:
            flash('Allowed file types are .docx and .pdf')
            return redirect(request.url)


if __name__ == "__main__":
    app.run()

