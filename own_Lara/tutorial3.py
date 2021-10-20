import numpy as np
import cv2

# capture webcam image
cap = cv2.VideoCapture(0)


# get camera image parameters from get()
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height:' ,height)
print('width:',width)
print('codec:', cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))


# create a window for the video
title ='Video image'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
print('Press q to close window')
 

# start a loop
while True:

    # read a camera frame
    ret,frame = cap.read()
    if (ret):
    
        # create four flipped tiles of the image
        img = np.zeros(frame.shape, np.uint8)
        small_frame = cv2.resize(frame,(0,0), fx=0.5, fy=0.5 )
        img[:height//2,:width//2] = small_frame 
        img[height//2:,:width//2] = cv2.flip(small_frame, 0)#x-Achse
        img[height//2:,width//2:] = cv2.flip(small_frame, -1)#y-Achse
        img[:height//2,width//2:] = cv2.flip(small_frame, 1)#y-Achse


        # display the image
        cv2.imshow(title, img)
    
         # press q to close the window  
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not retrieve frame.')
        break

# release the video capture object and window
cap.release()
cv2.destroyAllWindows()
