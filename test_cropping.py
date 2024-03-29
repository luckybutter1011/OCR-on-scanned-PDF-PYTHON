import glob
import cv2
import os
  

path = 'cropped2'
os.makedirs(path, exist_ok=True)



# for image in images:
def crop_image(pdf_name):
        
        image_counter = 1
        # global image_counter
        images = glob.glob("./retrieve/"+pdf_name+"/*.jpg")
        os.makedirs('cropped2/'+pdf_name, exist_ok=True)
        for image in images:
                # image = images[j]
                img=cv2.imread(image,1)

                height, width, channels = img.shape

                print("Image width:", width)
                print("Image height:", height)  

                # Set the crop width and height
                if width > 9000:     
                        x = [9060, 8590, 8590, 11100]
                        y = [380, 500, 390, 390]
                        w = [2000, 2790, 2790, 300]
                        h = [7000, 3400, 7000, 7000]
                else:
                        x = [6060, 7140, 7300, 7660]
                        y = [150, 150, 150, 150]
                        w = [1080, 160, 1980, 250]
                        h = [4100, 4100, 4100, 4100]
                
                # Crop the image   
                try:
                        for i in range(4):
                                crop_img = img[y[i]:y[i]+h[i], x[i]:x[i]+w[i]]
                                filename = "cropped2/"+pdf_name+"/crop"+str(image_counter)+"_"+str(i)+".jpg"        
                                cv2.imwrite(filename,crop_img)
                                image_counter = image_counter + 1
                except:
                        return False 
        return True


crop_image("upload.pdf")