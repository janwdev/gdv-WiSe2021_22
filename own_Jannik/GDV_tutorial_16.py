# Corner detection on example image inspired by
# https://docs.opencv.org/4.5.3/dc/d0d/tutorial_py_features_harris.html

import numpy as np
import cv2


# display two images side by side
def showImagesSideBySide(img_A, img_B):
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# do a non-maximum suppression
def doNonMaximaSuppression(img, window_size):
    # loop over each pixel in the image and keep pixel only if
    # it is maximal in a window with window_size
    img2 = np.zeros(img.shape, np.uint8)
    if(window_size % 2 != 1):
        window_size += 1
    rows, cols = img.shape
    offset = int((window_size-1/2))
    for x in range(offset, rows):
        for y in range(offset, cols):
            window = img[x-offset:x+offset+1, y-offset:y+offset+1]
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(window)
            if(max_loc[0] == offset and max_loc[1] == offset):
                img2[x, y] = img[x, y]
    return img2


# load example image
imgname = 'images/chessboard-contrast-squares.jpg'
img = cv2.imread(imgname, cv2.IMREAD_COLOR)
# resize if needed
img = cv2.resize(img, None, fx=0.1, fy=0.1)

# define parameters for Harris corner detection
blockSize = 2
ksize = 3
k = 0.04
# create a greyscale image for the corner detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert to floating point image
gray = np.float32(gray)

# harris corner detection using OpenCV method cornerHarris
corner_detection = cv2.cornerHarris(gray, blockSize, ksize, k)

# run non-maximum suppression to find isolated corner pointss
window_size = 5
corner_detection = doNonMaximaSuppression(corner_detection, window_size)
# dilate resulting image for increasing the corner size so that
# they become more visible than a single pixel
corner_detection = cv2.dilate(corner_detection, None)

# threshold for an optimal value, it may vary depending on the image
# and set corner pixels in the original image to a distinct color
# HINT: use something like "img[corner_img > threshold] = color" instead
# of a draw function to keep it simple
img[corner_detection > 0.01*corner_detection.max()] = [0, 0, 255]


# create window
window_name = 'Corner demo'
cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)

# show resulting images
# replace second image with the corner response image
showImagesSideBySide(img, cv2.cvtColor(corner_detection, cv2.COLOR_GRAY2BGR))

# wait for key to be pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
