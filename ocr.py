import glob
from PIL import Image
import pytesseract
import re
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# characters_to_remove = ['‘', '|', '-', '(', ';', '}', '+', '—', '”', '“', '°']
characters_to_remove = ['‘', '|', ';', '}', '+', '“', '°', '”']
images = glob.glob("./Cropped/*.jpg")
image_counter = 1

for image in images:
    # preprocessing the image
    bgr_image = cv2.imread(image)
    gray = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    invert = 255 - thresh    
    # img = Image.open(invert)
    data = pytesseract.image_to_string(invert, lang='eng', config='--oem 3 --psm 6')
    cleaned_data = data
    for char in characters_to_remove:
        cleaned_data = cleaned_data.replace(char, '')
    with open(f'extract/text_{image_counter}.txt', 'w') as file:
        file.write(cleaned_data)
    image_counter = image_counter + 1