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
def crop_image(filename):
        x = [6060, 7140, 7300, 7660, 7300]
        y = [150, 150, 150, 150, 150]
        w = [1080, 160, 360, 250, 610]
        h = [4250, 4250, 4250, 4250, 4250]
        image_counter = 1
        # global image_counter
        images = glob.glob("./retrieve/"+filename+"/*.jpg")
        os.makedirs('cropped/'+filename, exist_ok=True)
        for image in images:
                # image = images[j]
                img=cv2.imread(image,1)

                height, width, channels = img.shape

                print("Image width:", width)
                print("Image height:", height)       

                for i in range(5):
                        crop_img = img[y[i]:y[i]+h[i], x[i]:x[i]+w[i]]
                        filename = "cropped/"+filename+"/crop"+str(image_counter)+"_"+str(i)+".jpg"        
                        cv2.imwrite(filename,crop_img)
                #cv2.imshow('windo',crop_img)
                image_counter = image_counter + 1


crop_image("03GI-27.1_C02_REV0.pdf")