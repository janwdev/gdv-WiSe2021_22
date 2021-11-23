# Inspired by https://www.pyimagesearch.com/2015/03/09/capturing-mouse-click-events-with-python-and-opencv/
import numpy as np
import cv2

# define arrays for the clicked points

# define one callback functions for each image window
def clickSrc(event, x, y, flags, param):
    # grab references to the global variables
    
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # draw a circle around the clicked point
        
        # redraw the image
        cv2.imshow('Original',img)

def clickDst(event, x, y, flags, param):
    # grab references to the global variables
    
    # if the left mouse button was clicked, add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN:
        
        # draw a circle around the clicked point
        
         # redraw the image
        cv2.imshow('Transformed image',dst_transform)

# Load image and resize for better display
img = cv2.imread('images\\nl_clown.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(400,400), interpolation=cv2.INTER_CUBIC)

# initialize needed variables and windows
rows,cols,dim = img.shape
clone = img.copy()
dst_transform = np.zeros(img.shape,np.uint8)
cv2.namedWindow('Original')
cv2.setMouseCallback('Original', clickSrc)
cv2.namedWindow('Transformed image')
cv2.setMouseCallback('Transformed image', clickDst)


# keep looping until the 'q' key is pressed

while True:
    # if there are three reference points, then compute the transform and apply the transformation
    
    
    # display the image and wait for a keypress
    cv2.imshow('Original', img)
    cv2.imshow('Transformed image',dst_transform)
    key = cv2.waitKey(1) & 0xFF
    
    # if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        dst_transform = np.zeros(img.shape,np.uint8)
        img = clone.copy()
        refPtSrc = []
        refPtDst = []
        
    # if the 'q' key is pressed, break from the loop
    elif key == ord("q"):
        break

cv2.destroyAllWindows()