import glob
from PIL import Image
import pytesseract
import re
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
characters_to_remove = ['‘', '|', '-', '(', ';', '}', '+', '—', '”', '“', '°']
images = glob.glob("./Cropped/*.jpg")
image_counter = 1

for image in images:
    # preprocessing the image
    bgr_image = cv2.imread(image)
    gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    invert = 255 - thresh    
    img = Image.open(image)
    data = pytesseract.image_to_string(img, lang='eng', config='--psm 6')
    cleaned_data = data
    for char in characters_to_remove:
        cleaned_data = cleaned_data.replace(char, '')
    with open(f'extract/text_{image_counter}.txt', 'w') as file:
        file.write(cleaned_data)
    image_counter = image_counter + 1