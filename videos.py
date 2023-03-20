import cv2

# creating instance of video capture
cap = cv2.VideoCapture(0) # 0 argmnt is for video capturing through webcam
opened = cap.isOpened()

# codec -> decides the reading and writing the compressed video
# For video writing => instance or image i.e cap,4 character code fourcc, width,height,fps,vid.avi is required
# fourcc cc-character code c1,c2,c3,c4 or *
fourcc = cv2.VideoWriter_fourcc(*'MJPG') # or write as('m','j','p','g')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fps = cap.get(cv2.CAP_PROP_FPS)
# video writer
out = cv2.VideoWriter('nbn.avi',fourcc,fps,(int(width),int(height)))

print(height)
print(width)
print(f"frames are {fps}")

if opened:
    while(cap.isOpened()):
        ret, frame = cap.read()  # video is always captures in frames which returns continuously and ret is boolean value if frame is 0 returns false and gives error
        if ret == True:
            cv2.imshow('winname', frame)
            out.write(frame)
            if cv2.waitKey(2) == 27:  # 27 is value of esc button.
                break
out.release()  # save the video and release the memory usage
cap.release()
cv2.destroyAllWindows()



