import cv2
import numpy as np

# Making an empty Black canvas
# Here canvas is of 3 layers
canvas = np.zeros((300,300,3))

# Required points we need to join
pts = np.array([[250,5],[220,80],[120,20],[110,250]],np.int32)

# Reshape the points to shape (number_vertex,1,2)
pts = pts.reshape((-1,1,2))

# Draw this polygon
# Here Boolean True and False determine if the figure is closed
cv2.polylines(canvas,[pts],True,(0,0,255),2)

# shhowing the canvas
cv2.imshow('winname',canvas)
cv2.waitKey(20000)