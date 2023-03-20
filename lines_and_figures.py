import cv2
import numpy as np

# Creating Canvas  500X500 ( 3 channels)
canvas = np.zeros((500,500,3))

# Drawing a line
cv2.line(canvas,(100,100),(250,255),(0,0,255),2,cv2.LINE_4)
cv2.line(canvas,(50,50),(100,100),(255,0,0),2,cv2.LINE_AA)
# line-4 and line-8 - bresenham algo
# line-AA - Gausian filtering

# Drawing a Rectangle
cv2.rectangle(canvas,(300,350),(400,450),(0,255,0),1)

# Drawing a Circle
cv2.circle(canvas,(200,200),50,(255,0,0),-1)

# Drawing a Arrowed Line
cv2.arrowedLine(canvas,(200,300),(400,400),(0,255,0),tipLength=0.3)
# Showing the canvas
cv2.imshow('winname',canvas)
cv2.waitKey(20000)