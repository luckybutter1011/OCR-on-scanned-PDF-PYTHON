import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


path = 'aaa'
os.makedirs(path, exist_ok=True)

file = ('cropped/upload.pdf/crop2_1.jpg')


im1 = cv2.imread(file)
im = cv2.imread(file)
gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3,3), 0)
# blur = cv2.medianBlur(gray, 3)
# cv2.imshow("blur", blur)
# cv2.waitKey(0)

thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = np.ones((5,7), np.uint8)
dilated_value = cv2.dilate(thresh, kernel, iterations=1)
# eroded_value = cv2.erode(thresh, kernel, iterations=1)

contours, hierarchy = cv2.findContours(dilated_value, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

coordinates = []
cells = []
k=0
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    coordinates.append((x, y, w, h))
    # if y < 50: # This condition can be adjusted based on the position of the tables
    if (w>50 and w<500) and (h>100 and h<500):
        k+=1
        cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 3)
        cell = thresh[y:y+h, x:x+w]
        cells.append(cell)
        cv2.imwrite("aaa/aaa"+str(k)+".bmp", cell)

for cell in cells:
    kernel = np.ones((5,7), np.uint8)
    dilated_cell = cv2.dilate(cell, kernel, iterations=1)
    eroded_cell = cv2.erode(dilated_cell, kernel, iterations=1)
    # text = pytesseract.image_to_string(dilated_cell, config='--oem 3 --psm 6')
    text = pytesseract.image_to_string(dilated_cell, config='--oem 3 --psm 6', lang="eng")
    print(text)
        
# plt.imshow(cv2.cvtColor(hierarchy, cv2.COLOR_BGR2RGB))
# plt.show()

