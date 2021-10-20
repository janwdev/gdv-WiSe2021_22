import cv2
import math
import operator

# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Width: ", width)
print("Height: ", height)

# helper variables for drawing
# thickness
thick = 10
thin = 3

# color
blue = (255, 0, 0)  # BGR
green = (0, 255, 0)
red = (0, 0, 255)

# points
ptTopLeft = (0, 0)
ptTopRight = (width, 0)
ptBottomLeft = (0, height)
ptBottomRight = (width, height)

# fonts

# variables for moving rectangle


def circle_path(t, scale, offset):
    res = (int(scale*math.cos(t)+offset), int(scale*math.sin(t)+offset))
    return res


timer = 0
speed = 0.01

title = "Video image"
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
print("Press q to close Window")

# start a loop
while True:
    # capture the image
    ret, frame = cap.read()
    # check if capture succeeded
    if(ret):
        # draw a blue diagonal cross over the image
        cv2.line(frame, (0, 0), ptBottomRight, blue, thin)
        cv2.line(frame, ptBottomLeft, ptTopRight, blue, thin)
        # draw a circle

        # write some text

        # draw arrows (potential assignment)

        # draw a rectangle that moves on a circular path
        timer += speed
        pt1 = circle_path(timer, 100, 300)
        pt2 = (width//2, height//2)
        cv2.rectangle(frame, pt1, pt2, red, thin)

        # display the image
        cv2.imshow(title, frame)
        # press q to close the window
        if cv2.waitKey(10) == ord("q"):
            break
    else:
        print("Cant get a Picture from Camera")
        break

# release the video capture object and window
cap.release()
cv2.destroyAllWindows()
