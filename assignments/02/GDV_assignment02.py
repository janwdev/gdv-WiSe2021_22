'''
Assignement 02: Object counting
Group: Gruppe 1
Names: Lara Franke, Jannik Weisser
Date: 04.11.2021
Sources: <Sources of inspiration and collaboration (persons, videos, web pages, documents, books, ...)>
'''
# imports 
import cv2
import glob  # for loading all images from a directory

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

hue_range = 5
saturation_range = 50
value_range = 50

# setting colour values in RGB for the different bubble gum color
#red
hue_red = 179
saturation_red = 168
value_red = 173
lower_bound_red = (hue_red-hue_range, saturation_red -
                   saturation_range, value_red-value_range)
upper_bound_red = (hue_red+hue_range, saturation_red +
                   saturation_range, value_red+value_range)
#green
hue_green = 46
saturation_green = 181
value_green = 168
lower_bound_green = (hue_green-hue_range, saturation_green -
                     saturation_range, value_green-value_range)
upper_bound_green = (hue_green+hue_range, saturation_green +
                     saturation_range, value_green+value_range)
#blue
hue_blue = 99
saturation_blue = 233
value_blue = 171
lower_bound_blue = (hue_blue-hue_range, saturation_blue -
                    saturation_range, value_blue-value_range)
upper_bound_blue = (hue_blue+hue_range, saturation_blue +
                    saturation_range, value_blue+value_range)
#yellow
hue_yellow = 28
saturation_yellow = 207
value_yellow = 255
lower_bound_yellow = (hue_yellow-hue_range, saturation_yellow -
                      saturation_range, value_yellow-value_range)
upper_bound_yellow = (hue_yellow+hue_range, saturation_yellow +
                      saturation_range, value_yellow+value_range)
#white
hue_white = 29
saturation_white = 31
value_white = 255
lower_bound_white = (hue_white-hue_range, saturation_white -
                     saturation_range, value_white-value_range)
upper_bound_white = (hue_white+hue_range, saturation_white +
                     saturation_range, value_white+value_range)
#pink
hue_pink = 7
saturation_pink = 110
value_pink = 250
lower_bound_pink = (hue_pink-hue_range, saturation_pink -
                    saturation_range, value_pink-value_range)
upper_bound_pink = (hue_pink+hue_range, saturation_pink +
                    saturation_range, value_pink+value_range)

# array with the lower bound of each colour
color_lower_bound = [lower_bound_red, lower_bound_green, lower_bound_blue,
                     lower_bound_yellow, lower_bound_white, lower_bound_pink]
# arrays with the higher bound of each colour
color_upper_bound = [upper_bound_red, upper_bound_green, upper_bound_blue,
                     upper_bound_yellow, upper_bound_white, upper_bound_pink]

# sets morph shape
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

# define over all number of color and an array of the colour names
num_colors = 6
color_names = ['red', 'green', 'blue', 'yellow', 'white', 'pink']

# define counters 
num_labels = 0
num_rejected = 1

# define kernelsize
kernel_size = 3
kernel_shape = morph_shape(2)
connectivity = 8

# define when the size of gum gets to small
min_size = 10

# define mask
mask = None

# method to count one colour of the bubble gum 
def color_counter(img, height, width, c):
    # use global variables inside of the method
    global num_rejected
    global num_labels
    global mask
    # reseting the rejects to 1 because of the background always gets counted 
    num_rejected = 1
    # bgr image to hsv 
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # create a mask
    mask = cv2.inRange(hsv_img, color_lower_bound[c], color_upper_bound[c])
    
    # change mask for different color 
    if c == 0:  # red
        mask = opening(mask, kernel_size-1, kernel_shape)
        mask = dilatation(mask, kernel_size+1, kernel_shape)
        mask = closing(mask, kernel_size, kernel_shape)
    if c == 3:  # yellow
        mask = opening(mask, kernel_size-1, kernel_shape)
    else: # all the other color 
        mask = opening(mask, kernel_size, kernel_shape)
        mask = closing(mask, kernel_size, kernel_shape)

    # Check for too small components
    (num_labels, labels, stats, centroids) = cv2.connectedComponentsWithStats(
        mask, connectivity, cv2.CV_32S)
    for i in range(1, num_labels):
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]
        if w < min_size or h < min_size:
            print('Found a too small component.')
            num_rejected += 1
            continue  # found component is too small to be correct

# check how many testimages completed successfully
num_test_images_succeeded = 0
# loop through all images
for img_name in glob.glob('images/chewing_gum_balls*.jpg'):
    print('Searching for colored balls in image:', img_name)
    all_colors_correct = True
    # loop through all color
    for c in range(0, num_colors):
        img = cv2.imread(img_name, cv2.IMREAD_COLOR)
        height = img.shape[0]
        width = img.shape[1]
        # call own function
        color_counter(img, height, width, c)
        # check if number of found elements is correct
        num_final_labels = num_labels-num_rejected
        success = (num_final_labels == int(gt_list[c]))

        # output if the correct quantity of gums got counted  
        if success:
            print('We have found all', str(num_final_labels), '/',
                  str(gt_list[c]), color_names[c], 'chewing gum balls. Yeah!')
            foo = 0
        # output if too many gums got counted
        elif (num_final_labels > int(gt_list[c])):
            print('We have found too many (', str(num_final_labels), '/',
                  str(gt_list[c]), ') candidates for', color_names[c], 'chewing gum balls. Damn!')
            all_colors_correct = False
        # output if too little gums got counted
        else:
            print('We have not found enough (', str(num_final_labels), '/',
                  str(gt_list[c]), ') candidates for', color_names[c], 'chewing gum balls. Damn!')
            all_colors_correct = False

        # debug output of the test images
        if ((img_name == 'images\chewing_gum_balls01.jpg')
            or (img_name == 'images\chewing_gum_balls04.jpg')
                or (img_name == 'images\chewing_gum_balls06.jpg')):
            # show images
            cv2.imshow('Original image', img)
            result = cv2.bitwise_and(img, img, mask=mask)
            cv2.imshow('Masked image', result)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

    # counting in how many pictures all color got counted correctly
    if all_colors_correct:
        num_test_images_succeeded += 1
        print('Yeah, all colored objects have been found correctly in ', img_name)

print('Test result:', str(num_test_images_succeeded), 'test images succeeded.')
