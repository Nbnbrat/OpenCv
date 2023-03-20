import cv2
import datetime
import math
from constants import COLORS,RADIUS,CENTER

def get_ticks():
    hours_init = []
    hours_dest = []

    for i in range(0,360,6):  # bcz there is a 6 degree b/n each tick
        x_coordinate = int(CENTER[0] + RADIUS * math.cos(i * math.pi / 180))  # x = r cos theta here i is the 6 degree for each tick need to convert it into radian so pi/180
        y_coordinate = int(CENTER[1] + RADIUS * math.sin(i * math.pi / 180))  # y = r sin theta

        hours_init.append((x_coordinate,y_coordinate))

    for i in range(0,360,6):
        x_coordinate = int(CENTER[0] + (RADIUS-20) * math.cos(i * math.pi / 180))
        y_coordinate = int(CENTER[1] + (RADIUS-20) * math.sin(i * math.pi / 180))

        hours_dest.append((x_coordinate,y_coordinate))

    return hours_init,hours_dest

def getDigitalTime(h,m,s):
    time = ""
    hour = ""
    minute = ""
    second = ""
    if h<10:
        hour = f"0{h}:"
    else:
        hour = f"{h}:"
    if m<10:
        minute = f"0{m}:"
    else:
        minute = f"{m}:"
    if s<10:
        second = f"0{s}"
    else:
        second = f"{s}"
    time = hour+minute+second
    return time


# for needle of the clock
def draw_time(image):
    # taking the time features
    time_now = datetime.datetime.now().time()
    hour = math.fmod(time_now.hour,12)
    minute = time_now.minute
    second = time_now.second

    # taking the angles(degree- theta value) for hour, second,minute
    second_angle = math.fmod(second*6+270, 360)
    minute_angle = math.fmod(minute*6+270, 360)
    hour_angle = math.fmod((hour*30)+(minute/2) + 270, 360)

    second_x = int(CENTER[0] + (RADIUS-25) * math.cos(second_angle * math.pi/180))
    second_y = int(CENTER[1] + (RADIUS-25) * math.sin(second_angle * math.pi/180))
    cv2.line(image, CENTER,(second_x,second_y),COLORS['black'],2)

    minute_x = int(CENTER[0] + (RADIUS - 60) * math.cos(minute_angle * math.pi / 180))
    minute_y = int(CENTER[1] + (RADIUS - 60) * math.sin(minute_angle * math.pi / 180))
    cv2.line(image, CENTER, (minute_x, minute_y), COLORS['amber'], 3)

    hour_x = int(CENTER[0] + (RADIUS - 100) * math.cos(hour_angle * math.pi / 180))
    hour_y = int(CENTER[1] + (RADIUS - 100) * math.sin(hour_angle * math.pi / 180))
    cv2.line(image, CENTER, (hour_x, hour_y), COLORS['amber'], 7)

    cv2.circle(image,CENTER,5,COLORS['blue'],-1)

    time = getDigitalTime(int(hour),minute,second)

    cv2.putText(image,time,(200,390),cv2.FONT_HERSHEY_DUPLEX,1.6,COLORS['red'],1,cv2.LINE_AA)

    return image



