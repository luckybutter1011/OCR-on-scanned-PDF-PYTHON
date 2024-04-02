from pdf2image import convert_from_path
import os

path = 'retrieve'
os.makedirs(path, exist_ok=True)
 
# function to convert pdf to images
def pdf_to_img(pdf_name):
    PDF_file = 'uploads/'+pdf_name
    pages = convert_from_path(PDF_file, 500, poppler_path='poppler-24.02.0/Library/bin') 
    os.makedirs('retrieve/'+pdf_name, exist_ok=True)
    image_counter = 1

    for page in pages: 
        filename = "retrieve/"+pdf_name+"/page_"+str(image_counter)+".jpg"
        # Save the image of the page in system 
        page.save(filename, 'JPEG') 
        # Increment the counter to update filename 
        image_counter = image_counter + 1
 

