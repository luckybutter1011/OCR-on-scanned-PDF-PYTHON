from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os

from readpdf import pdf_to_img
from cropping import crop_image

app = Flask(__name__)
path = 'uploads'
os.makedirs(path, exist_ok=True)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/uploadDoc', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        pdf_to_img(filename)
        crop_image(filename)
        print(filename)
        return 'File uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True)