import cv2
import numpy as np
import copy

# load image in color and in gray
img_color = cv2.imread('gdv_ws_21-22/img/pic.jpg',cv2.IMREAD_COLOR)
img_gray = cv2.imread('gdv_ws_21-22/img/pic.jpg',cv2.IMREAD_GRAYSCALE)

img = copy.copy(img_gray)#Copy erzeugt

# print out some loaded data
print(type(img))
print(img.shape)

# extract size and resolution of image
width = img.shape[1]
height = img.shape[0]

#print first row
print(img[0])

#print first column
print(img[0:height-1][0])  # : von allen Zeilen nur der erste Wert ausgeben

#set area of the image black
#img=np.zeros((800,800)) schwarzes bild erzeugen, arrey mit nullen
#for i in range (30,60,2): #startet bei 30 endet bei 60, jedes 2 pixel nur schwarz
    #for j in range (20,40,3):
        #img[i][j] = (0,255,0) # werte für bgr


#find all used colors in the image#
colors = []
for i in range (width):
    for j in range (height):
        current_color = img[j][i]
        if colors.count(current_color) == 0:
            colors.append(current_color)
colors.sort()
print(colors)


#copy one part of the image into another
part = img [70:105,5:130]
img[115:150,85:210] = part 

#show image
title = 'Hello OpenCV'
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img_gray)
cv2.waitKey(0)  # wartet unendlich bis jemand taste drückt
cv2.destroyAllWindows()
