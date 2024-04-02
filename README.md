# OCR_Project
This project is for e-drawing pdf OCR.
## Requirement
- Environment: Windows 10/11
- RAM: minimum 4GB

## Installation
- Install the tesseract-ocr-w64-setup-5.3.3.20231005.exe
- Ensure the path for:
   ##### In ocr.py file, `pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'`
   ##### In readpdf.py file, `pages = convert_from_path(PDF_file, 500, poppler_path='poppler-24.02.0/Library/bin') `
- `pip install -r requirements.txt`
- `flask run` or `python app.py`

## Usage
- http://localhost:5000
- Upload the pdf.

# Variables
- size_array : Array for size 
- des_shop_array : Array for shop description
- des_field_array : Array for field description
- qty_array : Array for QTy
- item_array : Array for itemcode

If you have a problem, please feel free to contact me. `smart163410@gmail.com`

