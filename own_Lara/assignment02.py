'''
Assignement 02: Object counting
Group: Gruppe 1
Names: Lara Franke, Jannik Weisser
Date: 04.11.2021
Sources: <Sources of inspiration and collaboration (persons, videos, web pages, documents, books, ...)>
'''

import cv2
import glob  # for loading all images from a directory
import numpy as np

# Goal: Count the number of all colored balls in the images

# ground truth
num_yellow = 30
num_blue = 5
num_pink = 8
num_white = 10
num_green = 2
num_red = 6
gt_list = (num_red, num_green, num_blue, num_yellow, num_white, num_pink)

# define color ranges in HSV, note that OpenCV uses the following ranges H: 0-179, S: 0-255, V: 0-255
# hue_range = 10
# saturation_range = 100
# value_range = 100
hue_range = 5
saturation_range =50
value_range = 50
# rot in bild 3 wird zu klein, bei allen anderen wachsen die Kugeln zusammen 
# Values are RGB

# red
# hue_red = 359
# saturation_red = 66
# value_red = 68

hue_red = 179
saturation_red = 168
value_red = 173
lower_bound_red = (hue_red-hue_range, saturation_red -
                   saturation_range, value_red-value_range)
upper_bound_red = (hue_red+hue_range, saturation_red +
                   saturation_range, value_red+value_range)
# color = np.uint8([[[61,59,173]]]) # BGR
# hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# print("red: ",hsv_color)

# green
# hue_green = 92
# saturation_green = 71
# value_green = 66
hue_green = 46
saturation_green = 181
value_green = 168
lower_bound_green = (hue_green-hue_range, saturation_green -
                     saturation_range, value_green-value_range)
upper_bound_green = (hue_green+hue_range, saturation_green +
                     saturation_range, value_green+value_range)
# color = np.uint8([[[49,168,105]]]) # BGR
# hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# print("green: ",hsv_color)

# blue
# hue_blue = 198
# saturation_blue = 91
# value_blue = 67
hue_blue = 99
saturation_blue = 233
value_blue = 171
lower_bound_blue = (hue_blue-hue_range, saturation_blue -
                    saturation_range, value_blue-value_range)
upper_bound_blue = (hue_blue+hue_range, saturation_blue +
                    saturation_range, value_blue+value_range)
# color = np.uint8([[[171,124,15]]]) # BGR
# hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# print("blue: ",hsv_color)

# yellow
# hue_yellow = 55
# saturation_yellow = 81
# value_yellow = 100
hue_yellow = 28
saturation_yellow = 207
value_yellow = 255
lower_bound_yellow = (hue_yellow-hue_range, saturation_yellow -
                      saturation_range, value_yellow-value_range)
upper_bound_yellow = (hue_yellow+hue_range, saturation_yellow +
                      saturation_range, value_yellow+value_range)
# color = np.uint8([[[48,238,255]]]) # BGR
# hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# print("yellow: ",hsv_color)

# white
# hue_white = 59
# saturation_white = 12
# value_white = 100
hue_white = 29
saturation_white = 31
value_white = 255
lower_bound_white = (hue_white-hue_range, saturation_white -
                     saturation_range, value_white-value_range)
upper_bound_white = (hue_white+hue_range, saturation_white +
                     saturation_range, value_white+value_range)
# color = np.uint8([[[224,254,255]]]) # BGR
# hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# print("white: ",hsv_color)

# pink
# hue_pink = 14
# saturation_pink = 43
# value_pink = 98
hue_pink = 7
saturation_pink = 110
value_pink = 250
lower_bound_pink = (hue_pink-hue_range, saturation_pink -
                    saturation_range, value_pink-value_range)
upper_bound_pink = (hue_pink+hue_range, saturation_pink +
                    saturation_range, value_pink+value_range)
# color = np.uint8([[[142,168,250]]]) # BGR
# hsv_color = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# print("pink: ",hsv_color)

# morphological operations
# optional mapping of values with morphological shapes
def morph_shape(val):
    if val == 0:
        return cv2.MORPH_RECT
    elif val == 1:
        return cv2.MORPH_CROSS
    elif val == 2:
        return cv2.MORPH_ELLIPSE

# dilation with parameters
def dilatation(img, size, shape):
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.dilate(img, element)

# erosion with parameters
def erosion(img, size, shape):
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.erode(img, element)

# opening
def opening(img, size, shape):
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, element)

# closing
def closing(img, size, shape):
    element = cv2.getStructuringElement(shape, (2 * size + 1, 2 * size + 1),
                                        (size, size))
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, element)


# set color under test
num_colors = 6
color_names = ['red', 'green', 'blue', 'yellow', 'white', 'pink']


num_labels = 0  # TODO: implement something to set this variable
num_rejected = 1

# setting the parameters that work for all colors
color_lower_bound = [lower_bound_red, lower_bound_green, lower_bound_blue, lower_bound_yellow, lower_bound_white, lower_bound_pink]
color_upper_bound = [upper_bound_red, upper_bound_green, upper_bound_blue, upper_bound_yellow, upper_bound_white, upper_bound_pink]
# set individual (per color) parameters
# hsv_red = (hue_red, saturation_red, value_red)
# hsv_blue = (hue_blue, saturation_blue, value_blue)
# hsv_pink = (hue_pink, saturation_pink, value_pink)
# hsv_white = (hue_white, saturation_white, value_white)
# hsv_green = (hue_green, saturation_green, value_green)
# hsv_yellow = (hue_yellow, saturation_yellow, value_yellow)
# hsv = [hue_red, hsv_green, hsv_blue, hsv_yellow, hsv_white, hsv_pink]

kernel_size = 3
kernel_shape = morph_shape(2)
connectivity = 8

circle_size = 10
circle_thickness = 5
min_size = 10

def ownAlgorithm(img, height, width, c):
    global num_rejected
    global num_labels
    num_rejected = 1
    print(color_names[c])
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_img, color_lower_bound[c], color_upper_bound[c])
    cv2.imshow('Original image', img)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('Masked image',result)

    #mask = opening(mask,kernel_size, kernel_shape)
    #mask = closing(mask,kernel_size, kernel_shape)

    #mask = erosion(mask,kernel_size, kernel_shape)
    #mask = dilatation(mask,kernel_size, kernel_shape)
    #mask = closing(mask,kernel_size, kernel_shape)
    
    (numLabels, labels, stats, centroids) = cv2.connectedComponentsWithStats(mask,connectivity,cv2.CV_32S)
    num_labels = numLabels
    for i in range(1,numLabels):
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        if w < min_size or h < min_size:
            print ('Found a too small component.')
            num_rejected += 1
            continue # found component is too small to be correct 
        # #Rundheitspruefung
        # if w > h:
        #     roundness = 1.0 / (w/h)
        # elif h > w:
        #     roundness = 1.0 / (h/w)  
        # if (roundness < .9):
        #     print ('Found a component that is not round enough.')
        #     num_rejected += 1
        #     continue # ratio of width and height is not suitable

    print("labels ", numLabels-1)
    print("rejected ", num_rejected-1)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('Masked image later',result)

num_test_images_succeeded = 0
for img_name in glob.glob('images/chewing_gum_balls*.jpg'):
    # load image
    print('Searching for colored balls in image:', img_name)

    all_colors_correct = True

    for c in range(0, num_colors):

        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        height = img.shape[0]
        width = img.shape[1]

        # TODO: Insert your algorithm here
        ownAlgorithm(img, height, width, c)
        
        num_final_labels = num_labels-num_rejected

        success = (num_final_labels == int(gt_list[c]))

        if success:
            print('We have found all', str(num_final_labels), '/',
                  str(gt_list[c]), color_names[c], 'chewing gum balls. Yeah!')
            foo = 0
        elif (num_final_labels > int(gt_list[c])):
            print('We have found too many (', str(num_final_labels), '/',
                  str(gt_list[c]), ') candidates for', color_names[c], 'chewing gum balls. Damn!')
            all_colors_correct = False
        else:
            print('We have not found enough (', str(num_final_labels), '/',
                  str(gt_list[c]), ') candidates for', color_names[c], 'chewing gum balls. Damn!')
            all_colors_correct = False

        # debug output of the test images
        if ((img_name == 'images\chewing_gum_balls01.jpg')
            or (img_name == 'images\chewing_gum_balls04.jpg')
                or (img_name == 'images\chewing_gum_balls06.jpg')):
            # show the original image with drawings in one window
            # cv2.imshow('Original image', img)
            # show other images?

            cv2.waitKey(0)
            cv2.destroyAllWindows()

    if all_colors_correct:
        num_test_images_succeeded += 1
        print('Yeah, all colored objects have been found correctly in ', img_name)

print('Test result:', str(num_test_images_succeeded), 'test images succeeded.')
