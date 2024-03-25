from pdf2image import convert_from_path
 
PDF_file = '03GI-27.1_C02_REV0.pdf'
pages = convert_from_path(PDF_file, 500, poppler_path='/poppler-24.02.0/Library/bin') 

image_counter = 1

for page in pages: 
   
    filename = "Retrieve/page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
    image_counter = image_counter + 1
 

