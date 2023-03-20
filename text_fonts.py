import cv2
import numpy as np

# Creating a canvas of 800X500 (3 channels)
canvas = np.zeros((800,500,3))

# List of all fonts in cv2
fonts = [
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX
]

position = (40,50)
for i in range(0,8):
    cv2.putText(canvas,'THIS IS OPENCV !',position,fonts[i],1,(255,255,255),2,cv2.LINE_AA)
    position = (position[0],position[1] + 40)
    cv2.putText(canvas,'THIS IS OPENCV !'.lower(),position,fonts[i],1,(255,255,255),2,cv2.LINE_AA)
    position = (position[0], position[1] + 40)

# Displaying canvas
cv2.imshow('winname',canvas)
cv2.waitKey(20000)
