import glob
from PIL import Image
import pytesseract
import re
import cv2
import os
from ocr.ocr_table import ocr_table

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
characters_to_remove = ['‘', '|', ';', '}', '+', '“', '°', '”', '=']

def ocr_image(pdf_name):

    path = 'cropped'
    os.makedirs(path, exist_ok=True)
    path2 = 'extract'
    os.makedirs(path2, exist_ok=True)
    images = glob.glob("./cropped/"+pdf_name+"/*.jpg")
    image_counter = 1
    
    for image in images:
        bgr_image = cv2.imread(image)
        height, width, channels = bgr_image.shape

        if height > 5000:
            data = ocr_table(image)
        else:
            gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (3,3), 0)
            thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            invert = 255 - thresh    
            data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6 --oem 3')

        cleaned_data = data

        for char in characters_to_remove:
            cleaned_data = cleaned_data.replace(char, '')
            
        with open(f'extract/text_{image_counter}.txt', 'w') as file:
            file.write(cleaned_data)
            
        image_counter = image_counter + 1