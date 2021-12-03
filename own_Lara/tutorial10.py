''' This code is based on the stackoverflow answer from Fred Weinhaus: https://stackoverflow.com/a/59995542  '''
import cv2
import numpy as np

# global helper variables
window_width = 640
window_height = 480

def getFrequencies(image):
    """ Compute spectral image with a DFT
    """    
    # convert image to floats and do dft saving as complex output
    dft = cv2.dft(np.float32(image), flags = cv2.DFT_COMPLEX_OUTPUT)

    # apply shift of origin from upper left corner to center of image
    dft_shift = np.fft.fftshift(dft)
    
    # extract magnitude and phase images
    mag, phase = cv2.cartToPolar(dft_shift[:,:,0], dft_shift[:,:,1])
    min_Value,max_Value,min_location,max_location=cv2.minMaxLoc(mag)
    print(min_Value,max_Value,min_location,max_location)
    
    # get spectrum for viewing only
    spec = ((1/20) * np.log(mag))
    
    # Return the resulting image (as well as the magnitude and phase for the inverse)
    return spec, mag, phase

def changedFrequence(mag,phase):
    mag[:,319:322] = 0
    result = ((1/20) * np.log(mag))
    return  result,mag, phase 


def createFromSpectrum(mag,phase):
    # convert magnitude and phase into cartesian real and imaginary components
    real, imag = cv2.polarToCart(mag, phase)

    # combine cartesian components into one complex image
    back = cv2.merge([real, imag])

    # shift origin from center to upper left corner
    back_ishift = np.fft.ifftshift(back)

    # do idft saving as complex output
    img_back = cv2.idft(back_ishift)

    # combine complex components into original image again
    img_back = cv2.magnitude(img_back[:,:,0], img_back[:,:,1])

    # re-normalize to 8-bits
    min, max = np.amin(img_back, (0,1)), np.amax(img_back, (0,1))
    print(min,max)
    img_back = cv2.normalize(img_back, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    return img_back

def main():
    """ Load an image, compute frequency domain image from it and display both or vice versa """
    image_name = 'own_Lara\img\garden.PNG'

    # Load the image.
    image = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (window_width,window_height))

    # show the original image
    title_original = 'Original image'
    cv2.namedWindow(title_original, cv2.WINDOW_NORMAL) # Note that window parameters have no effect on MacOS
    cv2.resizeWindow(title_original,window_width,window_height)
    cv2.imshow(title_original,image)  
    result,mag,phase = getFrequencies(image)
    
    # show the resulting image
    title_result = 'Frequencies image'
    cv2.namedWindow(title_result, cv2.WINDOW_NORMAL) # Note that window parameters have no effect on MacOS
    cv2.resizeWindow(title_result,window_width,window_height)
    cv2.imshow(title_result,result)

    result,mag,phase = changedFrequence(mag,phase)
    back = createFromSpectrum(mag,phase)


    # and compute image back from frequencies
    title_back = 'Reconstructed image'
    cv2.namedWindow(title_back, cv2.WINDOW_NORMAL) # Note that window parameters have no effect on MacOS
    cv2.resizeWindow(title_back,window_width,window_height)
    cv2.imshow(title_back,back)

    # show the resulting image
    title_result = 'Frequencies changed image'
    cv2.namedWindow(title_result, cv2.WINDOW_NORMAL) # Note that window parameters have no effect on MacOS
    cv2.resizeWindow(title_result,window_width,window_height)
    cv2.imshow(title_result,result)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()

if (__name__ == '__main__'):
    main()

