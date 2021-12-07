'''
Assignement 03: Hybrid Imaging
Group: Gruppe 1
Names: Lara Franke, Jannik Weisser
Date: 24.11.2021
Sources:
https://yxw.cs.illinois.edu/course/CS445/F21/projects/hybrid/ComputationalPhotography_ProjectHybrid.html
https://docs.opencv.org/4.5.4/de/dbc/tutorial_py_fourier_transform.html
https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/
https://stackoverflow.com/questions/50508452/implementing-photoshop-high-pass-filter-hpf-in-opencv
https://www.kellyyangfan.com/hybridimage
'''
# imports
import cv2
import numpy as np

# Define variables
img1Name = 'images/happy.jpg'
img2Name = 'images/sad.jpg'
imgResizeSize = (400, 400)
# Arrays for the clicked part in the picture with coordinates
refPtSrc1 = []
refPtSrc2 = []
# Kernel sizes for rendered the high and low frequency pictures
ksize_imglow = 21
ksize_imghigh = 31
# Set titles for pictures and the sliders
titleOrig1 = "Original1"
titleOrig2 = "Original2"
titleHybrid = "hybrid"
titleWarped = "Warped2Img"
titleHighFreq = "high"
dragbarnamehigh = "ksize_high_freq"
dragbarnamelow = "ksize_low_freq"

''' Click function to select three points in the first image '''


def clickSrc1(event, x, y, flags, param):
    # grab references to the global variables
    global refPtSrc1
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN and len(refPtSrc1) < 3:
        pos = len(refPtSrc1)
        if (pos == 0):
            refPtSrc1 = [(x, y)]
        else:
            refPtSrc1.append((x, y))
        # draw a circle around the clicked point
        cv2.circle(img, refPtSrc1[pos], 4, (0, 255, 0), 2)
        cv2.imshow(titleOrig1, img)


''' Click function to select three points in the second image '''


def clickScr2(event, x, y, flags, param):
    # grab references to the global variables
    global refPtSrc2
    # if the left mouse button was clicked, add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN and len(refPtSrc2) < 3:
        pos = len(refPtSrc2)
        if (pos == 0):
            refPtSrc2 = [(x, y)]
        else:
            refPtSrc2.append((x, y))
        # draw a circle around the clicked point
        cv2.circle(img2, refPtSrc2[pos], 4, (0, 255, 0), 2)
        cv2.imshow(titleOrig2, img2)


''' Function to create a High and a Low Frequency Picture'''


def createLowAndHighFrequencyImg(imgLow, imgHigh, ksizelow, ksizehigh):
    # Low image gets created with the gaussian blur
    lowFrequencyImg = cv2.GaussianBlur(imgLow, ksizelow, cv2.BORDER_DEFAULT)
    # High frequency image gets created by subtracting the original image and the low frequency image
    highFrequencyimg = cv2.subtract(imgHigh, cv2.GaussianBlur(
        imgHigh, ksizehigh, sigmaX=0, borderType=cv2.BORDER_DEFAULT))
    return lowFrequencyImg, highFrequencyimg


''' Function to set sliders values for the warped picture and get the sliders position '''


def sliderCallBack(x):
    # Import global variables
    global computationDone
    global ksize_imghigh
    global ksize_imglow

    # read slider positions
    position_high = cv2.getTrackbarPos(dragbarnamehigh, titleHybrid)
    position_low = cv2.getTrackbarPos(dragbarnamelow, titleHybrid)
    # make kSize odd (because computation method)
    if(position_high % 2 != 1):
        position_high += 1
    if(position_low % 2 != 1):
        position_low += 1
    # Set new kernel sizes with the position of the sliders
    ksize_imghigh = position_high
    ksize_imglow = position_low
    computationDone = False


# Load image in a gray scale and resize for better display
img = cv2.imread(img1Name, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, imgResizeSize, interpolation=cv2.INTER_CUBIC)

img2 = cv2.imread(img2Name, cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2, imgResizeSize, interpolation=cv2.INTER_CUBIC)

# initialize needed variables and windows
rows, cols = img2.shape
resetImg2 = img2.copy()
resetImg1 = img.copy()

hybridImg = np.zeros(img.shape, np.uint8)
cv2.imshow(titleHybrid, hybridImg)

warpedSecondImg = np.zeros(img2.shape, np.uint8)

# Shows the two original pictures & calls the click function to select three points
cv2.imshow(titleOrig1, img)
cv2.setMouseCallback(titleOrig1, clickSrc1)
cv2.imshow(titleOrig2, img2)
cv2.setMouseCallback(titleOrig2, clickScr2)

# creates the sliders
scaleFactorSlider = 100
slider_ksize_high = cv2.createTrackbar(
    dragbarnamehigh, titleHybrid, ksize_imghigh, scaleFactorSlider, sliderCallBack)
slider_ksize_low = cv2.createTrackbar(
    dragbarnamelow, titleHybrid, ksize_imglow, scaleFactorSlider, sliderCallBack)

# keep looping until the 'q' key is pressed
computationDone = False
while True:
    # if there are three reference points, then compute the transform and apply the transformation
    if not(computationDone) and (len(refPtSrc1) == 3 and len(refPtSrc2) == 3):
        T_affine = cv2.getAffineTransform(
            np.float32(refPtSrc2), np.float32(refPtSrc1))
        print('\nAffine transformation:\n', '\n'.join(
            ['\t'.join(['%03.3f' % cell for cell in row]) for row in T_affine]))
        warpedSecondImg = cv2.warpAffine(resetImg2, T_affine, (cols, rows))
        warpedSecondImg = resetImg2
        computationDone = True
        # Shows the warped image
        cv2.imshow(titleWarped, warpedSecondImg)
        # Creates low and high frequency images
        lowimg, highImg = createLowAndHighFrequencyImg(
            resetImg1, warpedSecondImg, (ksize_imglow, ksize_imglow),
            (ksize_imghigh, ksize_imghigh))
        # Shows high frequency image
        cv2.imshow(titleHighFreq, highImg)
        # Creates hybrid image out of the low and high frequency image
        hybridImg = cv2.add(lowimg, highImg)
        # Shows hybrid image
        cv2.imshow(titleHybrid, hybridImg)

        hybrid_small = hybridImg.copy()
        hybrid_small = cv2.resize(hybrid_small, (80, 80))
        hybrid_big = hybridImg.copy()
        hybrid_big = cv2.resize(hybrid_big, (800, 800))
        cv2.imshow(titleHybrid + "small", hybrid_small)
        cv2.imshow(titleHybrid + "big", hybrid_big)
        # cv2.imshow("gegenüberstellung", np.concatenate((hybrid_small, hybrid_big), axis=1))

    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        warpedSecondImg = np.zeros(img.shape, np.uint8)
        img2 = resetImg2.copy()
        img = resetImg1.copy()
        refPtSrc1 = []
        refPtSrc2 = []
        computationDone = False
        cv2.imshow(titleOrig1, img)
        cv2.imshow(titleOrig2, img2)
        cv2.imshow(titleWarped, warpedSecondImg)
    # if the 'q' key is pressed, break from the loop
    elif key == ord("q"):
        break

cv2.destroyAllWindows()
