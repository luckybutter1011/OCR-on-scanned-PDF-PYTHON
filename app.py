from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename
import os
from ocr.readpdf import pdf_to_img
from ocr.cropping import crop_image
from ocr.ocr import ocr_image
from ocr.getarray import *
from ocr.getarray_table import *

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
        filename = "upload.pdf"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], "upload.pdf"))
        pdf_to_img(filename)
        flag = crop_image(filename)
        
        if flag is False:
            return render_template('upload.html', error=True)
        ocr_image(filename)
        
        if flag == 1:
            length, size_array = get_size_table()
            des_shop_array, des_field_array = get_des_table(length)
            qty_array = get_itemcode_table()
            return render_template('show.html', des_shop_array=des_shop_array, des_field_array=des_field_array, qty_array=qty_array, size_array=size_array)
        
        if flag == 2:
            des_shop_array, des_field_array = get_des()
            itemcode_array, qty_array = get_itemcode()
            size_array = get_size()
            return render_template('show.html', des_shop_array=des_shop_array, des_field_array=des_field_array, itemcode_array=itemcode_array, size_array=size_array, qty_array=qty_array)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)