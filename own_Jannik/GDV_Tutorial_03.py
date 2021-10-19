import numpy as np
import cv2

# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Width: " , width)
print("Height: ", height)

# create a window for the video
title = "Video image"
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
print("Press q to close Window")

# start a loop
while True:
    # read a camera frame
    ret, frame = cap.read()
    if(ret):
        # create four flipped tiles of the image
        img = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy = 0.5)
        img[0:int(height/2), 0: int(width/2)] = smaller_frame
        img[int(height/2): height, 0: int(width/2)] = cv2.flip(smaller_frame, 0) # flip x-axis
        img[0:int(height/2), int(width/2): width] = cv2.flip(smaller_frame, 1) # flip y-axis
        img[int(height/2): height, int(width/2): width] = cv2.flip(smaller_frame, -1) # flip both axis

        # display the image
        cv2.imshow(title, img)
        # press q to close the window
        if cv2.waitKey(10) == ord("q"):
            break
    else:
        print("Cant get a Picture from Camera")
        break

# release the video capture object and window
cap.release()
cv2.destroyAllWindows()
