# PROJECT-1 >> Reversing the video (existing video)
# import the Library
import cv2

# Video capture Instance
cap = cv2.VideoCapture('test.mp4')

# Properties of video

# Total no. of frames in a video
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Frames per second of video
fps = cap.get(cv2.CAP_PROP_FPS)

# Height and width of the video
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Initiating the output writer for video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('reversed.avi',fourcc,fps,(int(width*0.5),int(height*0.5)))

print(f'no.of frames are:{total_frames}')
print(f'fps is {fps}')

# We get the index of the last frame of the video file
frame_index = total_frames - 1

# Checking if the video instance is ready
if cap.isOpened():
    # Reading till the end of the video
    while(frame_index != 0):
        # We set the current frame position to last frame.
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index) # starter loop
        ret, frame = cap.read()

        # Resize the frame
        frame = cv2.resize(frame,(int(width*0.5),int(height*0.5)))

        # Optional: To show the video i.e reversed
        cv2.imshow('winname', frame)

        # WRiting the reversed video
        out.write(frame)
        # Decrementing Frame index at each step, i.e feeding the loop
        frame_index -= 1

        # Printing the progress
        if frame_index % 100 == 0:
            print(frame_index)
            if cv2.waitKey(2) == ord('q'):
                break

out.release()
cap.release()
cv2.destroyAllWindows()






