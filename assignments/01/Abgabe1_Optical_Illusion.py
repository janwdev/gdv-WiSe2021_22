import cv2
import numpy as np
import math
import copy

#Variablen definieren 
width = 400 
height = 300
partHeight = 40
partWidth = 40
border = 50

#Erstellen des Farbverlaufsbild durch einen Array welches Pixel generiert von 1(Weiß) bis 0(Schwarz), width gibt an wie viele generiert werden
img_org = np.tile(np.linspace(1, 0, width), (height, 1))

#Bildteile erstellen, durch kopieren eines Bildabschnitts im orginal Bild
partImg = img_org[math.ceil(height/2-partHeight/2):math.ceil(height/2+partHeight/2),
                  math.ceil(width/2-partWidth/2):math.ceil(width/2+partWidth/2)]


#Fenster öffnet sich
title = "Illusion"  # Titel zum Anzeigen (Fenster)
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)

#Variablen definieren für die Schleife
position = border
right = True
firstRun = True
imgArray = []

while True:
    img = copy.copy(img_org)#Kopie des orginal Bild erstellen
    #Bildteile auf das orginal Bild legen
    img[math.ceil(height/2-partHeight/2):math.ceil(height/2 +
                  partHeight/2), position:partWidth+position] = partImg

    if firstRun:
        imgArray.append(img)
        size = (img.shape[1], img.shape[0])

    if right:
        position = position+1
    else:
        position = position-1

    if position == width-partWidth-border:
        right = False
    if position == border:
        right = True
        if firstRun:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 30
            video_filename = 'output/A1_Optical_Illusion_Video.avi'
            video = cv2.VideoWriter(video_filename, fourcc, fps, (width, height), False)

            for i in range(len(imgArray)):
                video.write(np.uint8(255 * imgArray[i]))
            video.release()
            firstRun = False
            print("Video done")

    img[border:border+partHeight, width-border-partWidth:width-border] = partImg
    img[border:border+partHeight, border:border+partWidth] = partImg
    
    cv2.imshow(title, img)
    if cv2.waitKey(5) == ord("q"): # Programm schliessen
        break

cv2.destroyAllWindows()
