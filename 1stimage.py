import numpy as np
import cv2

image = np.zeros((500,500))
image[:,:] = 100 # setting all the rows and all the columns into 100
image = image[:,:]+10 # and adding 10 to each pixel values
image[100:200,200:300] = 255 # selecting indexing 100 to 200 rows and 200 to 300 colmns to set it to white color

cv2.imwrite('sample.jpg', image) # imwrite creates an image
img1=cv2.imread('sample.jpg') # load the existing image
# function to show the image until we press any key
cv2.imshow('test img',img1) # img shows at a blink of an eye so need to use wait function
cv2.waitKey(5000) #   here wait till 5000 milisecond, if we dont give time argmnt then show the image until we press any key

img2 = cv2.imread('hills.webp',cv2.IMREAD_GRAYSCALE)
cv2.imshow('test img',img2)
cv2.waitKey()