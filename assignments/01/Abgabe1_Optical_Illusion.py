import cv2
import numpy as np
import math
import copy
import os

# task https://github.com/uhahne/gdv-WiSe2021_22/blob/main/assignments/Assignement01_OpticalIllusion.md

#Define variables
width = 400
height = 300
partHeight = 40
partWidth = 40
border = 50

#Create a picture of a gradient with an array. That array generates pixels from 0(white) to 1(black), width indicates how many pixels need to get generated
img_org = np.tile(np.linspace(1, 0, width), (height, 1))

#Create picture parts by making a copy of the original picture
partImg = img_org[math.ceil(height/2-partHeight/2):math.ceil(height/2+partHeight/2),
                  math.ceil(width/2-partWidth/2):math.ceil(width/2+partWidth/2)]


#Name and create window
title = "Illusion"  #Title is shown
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)

#Define variables for loop
position = border
runInRightDirection = True
firstRunFLeftToRightABack = True
imgArray = []

while True:
    img = copy.copy(img_org)  #Making a copy of the original picture

    #Laying the moving picture part on the background (original picture)
    img[math.ceil(height/2-partHeight/2):math.ceil(height/2 +
                                                   partHeight/2), position:partWidth+position] = partImg

    if firstRunFLeftToRightABack: #Code gets changed for the first run, just important for the creation of the video
        #Copy of the original picture gets append to imgArray
        imgArray.append(img)
        #Size of the picture gets saved 
        size = (img.shape[1], img.shape[0])

    #The part of the picture that’s supposed to move, moves one position to the right
    if runInRightDirection:
        position = position+1

   #The part of the picture that’s supposed to move, moves one position to the left
    else:
        position = position-1

    #If the moving picture hits the border on the right side, the variable changes so the part moves to the left
    if position == width-partWidth-border:
        runInRightDirection = False

    #If the moving picture hits the border on the left side, the variable changes so the part moves to the right
    if position == border:
        runInRightDirection = True

        #At the end of the first run, a video gets created from the picture array
        if firstRunFLeftToRightABack:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 30
            foldername = 'output'
            if not os.path.exists(foldername):
                os.makedirs(foldername)
            video_filename = foldername + '/A1_Optical_Illusion_Video.avi'
            video = cv2.VideoWriter(
                video_filename, fourcc, fps, (width, height), False)

            #Each picture in the array gets append to each other to create a video
            for i in range(len(imgArray)):
                video.write(np.uint8(255 * imgArray[i]))

            #Video file gets released
            video.release()
            firstRunFLeftToRightABack = False
            print("Video done")

    #Static picture parts get laid on top of the background 
    img[border:border+partHeight, width-border-partWidth:width-border] = partImg
    img[border:border+partHeight, border:border+partWidth] = partImg

     #Animation is shown
    cv2.imshow(title, img)
    if cv2.waitKey(5) == ord("q"):  #Programm gets closed
        break

cv2.destroyAllWindows()
