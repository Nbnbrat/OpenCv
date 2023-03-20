import cv2
import numpy as np
from constants import CENTER,COLORS,RADIUS,CANVAS_SIZE
from helperfunctions import get_ticks,draw_time

image = np.zeros(CANVAS_SIZE)
image[:] = [255,255,255]

hours_init, hours_dest = get_ticks()
for i in range(len(hours_init)):
    if i % 5 == 0:
        cv2.line(image,hours_init[i],hours_dest[i],COLORS['black'],3)
    else:
        cv2.circle(image,hours_init[i],5,COLORS['black'],-1)

cv2.circle(image,CENTER,RADIUS+10,COLORS['yellow'],2)
cv2.putText(image,'GUESS',(215,230),cv2.FONT_HERSHEY_TRIPLEX,2,COLORS['dark_gray'],1,cv2.LINE_AA)

while True:
    image_original = image.copy()

    clock_face = draw_time(image_original)

    cv2.imshow('clock',image_original)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


