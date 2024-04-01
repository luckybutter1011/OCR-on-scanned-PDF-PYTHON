import glob
import cv2
import os
  

path = 'cropped'
os.makedirs(path, exist_ok=True)
#path="C:\Users\HASSAN\OneDrive\CompVision\Textmine\rotating"
# images = glob.glob("./rotating/*.jpg")
# images = glob.glob("./Retrieve/*.jpg")

# x = 6000
# y = 100
# w = 2000
# h = 4200
# image for cropping the description and size
# description, size, ITEMCODE, QTY


# for image in images:
def crop_image(pdf_name):
        flag = 0
        image_counter = 1
        # global image_counter
        images = glob.glob("./retrieve/"+pdf_name+"/*.jpg")
        os.makedirs('cropped/'+pdf_name, exist_ok=True)
        for image in images:
                # image = images[j]
                img=cv2.imread(image,1)

                height, width, channels = img.shape

                print("Image width:", width)
                print("Image height:", height)  

                # Set the crop width and height
                if width > 9000:     
                        x = [9060, 8760, 10300, 11100]
                        y = [150, 150, 150, 150]
                        w = [2100, 380, 610, 300]
                        h = [7000, 7000, 7000, 7000]
                        flag = 1
                else:
                        x = [6060, 7140, 7300, 7660]
                        y = [150, 150, 150, 150]
                        w = [1080, 160, 610, 250]
                        h = [4100, 4100, 4100, 4100]
                        flag = 2
                # Crop the image   
                try:
                        for i in range(4):
                                crop_img = img[y[i]:y[i]+h[i], x[i]:x[i]+w[i]]
                                filename = "cropped/"+pdf_name+"/crop"+str(image_counter)+"_"+str(i)+".jpg"        
                                cv2.imwrite(filename,crop_img)
                                image_counter = image_counter + 1
                except:
                        return False 
        return flag


# crop_image("upload.pdf")