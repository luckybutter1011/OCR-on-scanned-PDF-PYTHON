import glob
import cv2
  
image_counter = 1
#path="C:\Users\HASSAN\OneDrive\CompVision\Textmine\rotating"
# images = glob.glob("./rotating/*.jpg")
images = glob.glob("./Retrieve/*.jpg")


# x = 6000
# y = 100
# w = 2000
# h = 4200
# image for cropping the description and size
# description, size, ITEMCODE, QTY
x = [6100, 7125, 7300, 7665]
y = [500, 500, 500, 500]
w = [1000, 175, 365, 250]
h = [3750, 3750, 3750, 3750]

for image in images:
        img=cv2.imread(image,1)

        height, width, channels = img.shape

        print("Image width:", width)
        print("Image height:", height)       

        for i in range(4):
                crop_img = img[y[i]:y[i]+h[i], x[i]:x[i]+w[i]]
                filename = "./Cropped/crop"+str(image_counter)+"_"+str(i)+".jpg"        
                cv2.imwrite(filename,crop_img)
        #cv2.imshow('windo',crop_img)
        image_counter = image_counter + 1
