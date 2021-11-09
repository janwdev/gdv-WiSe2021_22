# Template matching, originally with objects from the image. Typical example is counting blood cells
import cv2

use_color = True

if use_color:
    # load image and template image, note that the template has been manually cut out of the image
    img = cv2.imread("images/chewing_gum_balls06.jpg", cv2.IMREAD_COLOR)
    template = cv2.imread("images/cgb_pink.jpg", cv2.IMREAD_COLOR)
    # read shape of the template and original image
    H,W,C = img.shape
    h,w,c = template.shape
else:
    # load image and template image, note that the template has been manually cut out of the image
    img = cv2.imread("images/chewing_gum_balls06.jpg", cv2.IMREAD_GRAYSCALE)
    template = cv2.imread("images/cgb_pink.jpg", cv2.IMREAD_GRAYSCALE)
    # read shape of the template and original image
    H,W,C = img.shape
    h,w,c = template.shape

# Define template matching methods, see https://docs.opencv.org/4.5.3/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the math behind each method
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
method_names = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

# loop over all methods in order to compare them
for method,method_name in zip(methods,method_names): # Anstatt Zip koennte man auf 2x for
    # work on a new image each time
    img2 = img.copy() 
    # do the template matching
    result = cv2.matchTemplate(img2, template, method)
    # get the best match location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val,max_val, min_loc, max_loc)
    # draw rectangle at found location
    bestmatch = min_loc # gruen
    bestmatch_tuple = (bestmatch[0] + w, bestmatch[1] + h)
    cv2.rectangle(img2, bestmatch, bestmatch_tuple, (0,255,0), 3)
    bestmatch = max_loc # blau
    bestmatch_tuple = (bestmatch[0] + w, bestmatch[1] + h)
    cv2.rectangle(img2, bestmatch, bestmatch_tuple, (255,0,0), 3)

    #rot ist das richtige
    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        bestmatch = min_loc
    else:
        bestmatch = max_loc
    bestmatch_tuple = (bestmatch[0] + w, bestmatch[1] + h)
    cv2.rectangle(img2, bestmatch, bestmatch_tuple, (0,0,255), 3)

    # show original image with found location
    cv2.imshow('Location', img2)
    # show image with the template matching result for all pixels
    result_title = 'Result with %s' % method_name # % im String wird im String durch das ersetzt, was nach % steht
    cv2.imshow(result_title, result)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()