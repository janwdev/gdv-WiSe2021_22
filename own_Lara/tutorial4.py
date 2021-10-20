import cv2
import math
import operator

# capture webcam image
cap = cv2.VideoCapture(0)


# get camera image parameters from get()
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print('height:' ,height)
print('width:',width)
print('codec:', cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))

# drawing helper variables
pt_topleft=(0,0)
pt_bottomright= (width,height)
pt_bottomleft= (width,0)
pt_topright = (0,height)
## thickness
thick = 10
thin = 3

## color (BGR)
blue = (255,0,0)
red = (0,0,255)

## fonts

# variables for moving rectangle
def circle_path(t,scale,offset):
    res=(int(scale*math.cos(t)+offset),int(scale*math.sin(t)+offset))
    return res
timer = 0.0
# create a window for the video
title ='Drawing image'
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
print('Press q to close window')
 

# start a loop
while True:

    # check if capture succeeded
    ret,frame = cap.read()
    if (ret):
        
        # draw a blue diagonal cross over the image
        cv2.line(frame,pt_topleft,pt_bottomright, blue, thick)
        cv2.line(frame,pt_bottomleft,pt_topright, blue, thick)


        # draw a circle

        # write some text

        # draw arrows (potential assignment)

        # draw a rectangle that moves on a circular path
        timer +=0.05
        pt1=circle_path(timer, 100,300)
        pt2= (width//2, height//2)

        cv2.rectangle(frame,pt1,pt2,red,thin)
        
        # display the image
        cv2.imshow(title, frame)
    
         # press q to close the window  
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not retrieve frame.')
        break

# release the video capture object and window
cap.release()
cv2.destroyAllWindows()
