import cv2
import numpy as np
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_table(file):
    im1 = cv2.imread(file)
    im = cv2.imread(file)
    gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    coordinates = []
    cells = []
    k=0
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        coordinates.append((x, y, w, h))
        
        if (file == "./cropped/upload.pdf\crop4_3.jpg" and ((w>200 and w<300) and (h>200 and h<500))):
            k+=1
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cell = thresh[y:y+h, x:x+w]
            cell = cell[10:-10, 10:-10]
            kernel = np.ones((5,5), np.uint8)
            dilated_value = cv2.dilate(cell, kernel, iterations=1)
            edges = cv2.morphologyEx(dilated_value, cv2.MORPH_GRADIENT, kernel)

            # Find contours in the edge map
            contours1, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            # Create a mask to remove the cloud shape
            mask = np.zeros(cell.shape, dtype=np.uint8)
            for cnt1 in contours1:
                x1, y1, w1, h1 = cv2.boundingRect(cnt1)
                if y1 > int(h/2)-40 and y1 < int(h/2)+40 and 60 > h1:
            
                    cv2.drawContours(mask, [cnt1], -1, (255, 255, 255), thickness=cv2.FILLED)
            result = cv2.bitwise_and(cell, mask)
            cells.append(result)
        
        elif (file == "./cropped/upload.pdf\crop2_1.jpg" and ((w>50 and w<500) and (h>100 and h<500))):
            k+=1
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cell = thresh[y:y+h, x:x+w]
            cell = cell[10:-10, 10:-10]
            cells.append(cell)
        elif (file == "./cropped/upload.pdf\crop1_0.jpg" and ((w>1500 and w<2200) and (h>200 and h<500))):
            k+=1
            cv2.rectangle(im, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cell = thresh[y:y+h, x:x+w]
            cell = cell[2:-2, 2:-2]
            cells.append(cell)
    ocr_text = []
    j = 0
    for cell in cells:
        kernel = np.ones((5,7), np.uint8)
        dilated_cell = cv2.dilate(cell, kernel, iterations=1)
        eroded_cell = cv2.erode(dilated_cell, kernel, iterations=1)
        if file == "./cropped/upload.pdf\crop2_1.jpg":
            image = dilated_cell
        elif file == "./cropped/upload.pdf\crop4_3.jpg":
            image = eroded_cell
        elif file == "./cropped/upload.pdf\crop1_0.jpg":
            image = cell
        j+=1        
        text = pytesseract.image_to_string(image, config='--oem 3 -l eng --psm 6')
        ocr_text.append(text) 
    return "\n".join(ocr_text)

