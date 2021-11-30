# Edge detection on an example image

import numpy as np
import cv2

# define a window name
window_name = 'Canny edge detection demo'

trackbarValue_blur = 'Blur'
trackbarValue_upper = 'T-upper'
trackbarValue_lower = 'T-lower'

# TODO: load example image as grayscale
img = cv2.imread('images\\nl_clown.jpg',cv2.IMREAD_GRAYSCALE)
# resize if needed
img = cv2.resize(img,(400,400), interpolation=cv2.INTER_CUBIC)
# clone if needed
clone = img.copy()

def showImagesSideBySide(img_A, img_B):
    '''Helper function to draw two images side by side'''
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# TODO: Define callback function
def sliderCallBack(x):
    '''callback function for the sliders'''
    global trackbarValue_blur
    global trackbarValue_upper
    global trackbarValue_lower
    global window_name
    global img
    global clone
    # read slider positions
    position_blur= cv2.getTrackbarPos(trackbarValue_blur,window_name)
    position_upper= cv2.getTrackbarPos(trackbarValue_upper,window_name)
    position_lower= cv2.getTrackbarPos(trackbarValue_lower,window_name)
    # blur the image
    if(position_blur==0):
        position_blur+=1
    kernel_size = (position_blur,position_blur)
    img = cv2.blur(img, kernel_size)
    # img = cv2.GaussianBlur(img,kernel_size,sigmaX=0,borderType=cv2.BORDER_DEFAULT)
    
    # run Canny edge detection with thresholds set by sliders
    canny = cv2.Canny(img,position_lower, position_upper)
    # show the resulting images in one window
    showImagesSideBySide(clone,canny)


defaultvalue = 0
# TODO: initial Canny edge detection result creation
canny = cv2.Canny(img,defaultvalue, defaultvalue)

# show the resulting images in one window
showImagesSideBySide(img, canny)

# create trackbars (sliders) for the window and define one callback function
scaleFactor = 100

maxblur = 10
slider_blur=cv2.createTrackbar(trackbarValue_blur, window_name, defaultvalue,maxblur,sliderCallBack)
slider_t_upper = cv2.createTrackbar(trackbarValue_upper, window_name, defaultvalue, scaleFactor,sliderCallBack)
slider_t_lower = cv2.createTrackbar(trackbarValue_lower, window_name, defaultvalue, scaleFactor,sliderCallBack)

# TODO: create window with sliders


# wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()