'''
Assignement 03: Hybrid Imaging
Group: Gruppe 1
Names: Lara Franke, Jannik Weisser
Date: 24.11.2021
Sources: <Sources of inspiration and collaboration (persons, videos, web pages, documents, books, ...)>
'''
# imports 
import cv2
import numpy as np

refPtSrc1 = []
refPtSrc2 = []

def clickSrc1(event, x, y, flags, param):
    # grab references to the global variables
    global refPtSrc1
    # if the left mouse button was clicked, add the point to the source array
    if event == cv2.EVENT_LBUTTONDOWN and len(refPtSrc1) < 3:
        pos = len(refPtSrc1)
        if (pos == 0):
            refPtSrc1 = [(x,y)]
        else:
            refPtSrc1.append((x, y))	
        # draw a circle around the clicked point
        cv2.circle(img, refPtSrc1[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Original1',img)

def clickScr2(event, x, y, flags, param):
    # grab references to the global variables
    global refPtSrc2
    # if the left mouse button was clicked, add the point to the destination array
    if event == cv2.EVENT_LBUTTONDOWN and len(refPtSrc2) < 3:
        pos = len(refPtSrc2)
        if (pos == 0):
            refPtSrc2 = [(x,y)]
        else:
            refPtSrc2.append((x, y))	
        # draw a circle around the clicked point
        cv2.circle(img2, refPtSrc2[pos], 4, (0, 255, 0), 2)
        cv2.imshow('Original2',img2)

def createLowAndHighFrequencyImg(imgLow, imgHigh, ksize):
    lowFrequencyImg = cv2.GaussianBlur(imgLow,ksize,cv2.BORDER_DEFAULT)
    highFrequencyimg = imgHigh - cv2.GaussianBlur(imgHigh,ksize,cv2.BORDER_DEFAULT)
    return lowFrequencyImg, highFrequencyimg

def getFrequencies(image):
    """ Compute spectral image with a DFT
    """
    # convert image to floats and do dft saving as complex output
    dft = cv2.dft(np.float32(image), flags = cv2.DFT_COMPLEX_OUTPUT)

    # apply shift of origin from upper left corner to center of image
    dft_shift = np.fft.fftshift(dft)
    
    # extract magnitude and phase images
    mag, phase = cv2.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(mag)
    print(min_val,max_val, min_loc, max_loc)
    # get spectrum for viewing only
    spec = ((1/20) * np.log(mag))
    
    # Return the resulting image (as well as the magnitude and phase for the inverse)
    return spec, mag, phase

# Load image and resize for better display
img = cv2.imread('images/DerekPicture.jpg',cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(400,400), interpolation=cv2.INTER_CUBIC)

img2 = cv2.imread('images/nutmeg.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.resize(img2,(400,400), interpolation=cv2.INTER_CUBIC)

# initialize needed variables and windows
rows,cols = img2.shape
resetImg2 = img2.copy()
resetImg1 = img.copy()
warpedSecondImg = np.zeros(img2.shape,np.uint8)
cv2.imshow('Original1',img)
cv2.setMouseCallback('Original1', clickSrc1)
cv2.imshow('Original2',img2)
cv2.setMouseCallback('Original2', clickScr2)


# keep looping until the 'q' key is pressed
computationDone = False
while True:
    # if there are three reference points, then compute the transform and apply the transformation
    if not(computationDone) and (len(refPtSrc1) == 3 and len(refPtSrc2) == 3):
        T_affine = cv2.getAffineTransform(np.float32(refPtSrc2), np.float32(refPtSrc1))
        print('\nAffine transformation:\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_affine]))
        warpedSecondImg = cv2.warpAffine(resetImg2,T_affine,(cols,rows))
        computationDone = True
        cv2.imshow('Warped2Img',warpedSecondImg)
        lowimg,highImg = createLowAndHighFrequencyImg(resetImg1, warpedSecondImg, (21,21))
        cv2.imshow('high',highImg)
        hybridImg = lowimg+highImg
        cv2.imshow('hybrid',hybridImg)

    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the transformation
    if key == ord("r"):
        warpedSecondImg = np.zeros(img.shape,np.uint8)
        img2 = resetImg2.copy()
        img = resetImg1.copy()
        refPtSrc1 = []
        refPtSrc2 = []
        computationDone = False
        cv2.imshow('Original1',img)
        cv2.imshow('Original2',img2)
        cv2.imshow('Warped2Img',warpedSecondImg)
    # if the 'q' key is pressed, break from the loop
    elif key == ord("q"):
        break

cv2.destroyAllWindows()