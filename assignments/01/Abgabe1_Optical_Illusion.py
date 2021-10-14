import cv2
import numpy as np
import math
import copy

# Aufgabe https://github.com/uhahne/gdv-WiSe2021_22/blob/main/assignments/Assignement01_OpticalIllusion.md

# Variablen definieren
width = 400
height = 300
partHeight = 40
partWidth = 40
border = 50

# Erstellen des Farbverlaufsbild durch einen Array welches Pixel generiert von 1(Weiß) bis 0(Schwarz), width gibt an wie viele Pixel generiert werden
img_org = np.tile(np.linspace(1, 0, width), (height, 1))

# Bildteil erstellen, durch Kopieren eines Bildabschnitts des orginal Bild
partImg = img_org[math.ceil(height/2-partHeight/2):math.ceil(height/2+partHeight/2),
                  math.ceil(width/2-partWidth/2):math.ceil(width/2+partWidth/2)]


# Fenster erstelen und benennen
title = "Illusion"  # Titel zum Anzeigen (Fenster)
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)

# Variablen definieren für die Schleife
position = border
right = True
firstRun = True
imgArray = []

while True:
    img = copy.copy(img_org)  # Kopie des orginal Bild erstellen

    # Bildauschnitt welcher sich bewegt wird auf das  orginal Bild gelegt
    img[math.ceil(height/2-partHeight/2):math.ceil(height/2 +
                                                   partHeight/2), position:partWidth+position] = partImg

    if firstRun:  # Code wird nur fuer ersten durchlauf geaendert, weil nur wichtig zum erzeugen des Videos
        # Die erstellte Kopie des orginal Bildes wird an den imgArray anhängen
        imgArray.append(img)
        # Größe des Bilds wird in der Variable gespeichert
        size = (img.shape[1], img.shape[0])

    # Der Bildauschnitt der sich bewegen soll rückt immer um eine position nach rechts
    if right:
        position = position+1

    # Der Bildauschnitt der sich bewegen soll rückt immer um eine position nach links
    else:
        position = position-1

    # Wenn der Ausschnitt sich am rechten Rand befindet ändert sich die Variable um ihn dann nach links laufen zu lassen
    if position == width-partWidth-border:
        right = False

    # Wenn der Ausschnitt sich am linken Rand befindet ändert sich die VAriable um ihn dann nach rechts laufen zu lassen
    if position == border:
        right = True

        # Wenn wir uns am Ende des ersten Durchlauf befinden soll ein Video aus dem Bilderarray erstellt werden
        if firstRun:
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            fps = 30
            video_filename = 'output/A1_Optical_Illusion_Video.avi'
            video = cv2.VideoWriter(
                video_filename, fourcc, fps, (width, height), False)

            # Jedes Bild im Array wird aneinander gehängt um ein Video zu erstellen
            for i in range(len(imgArray)):
                video.write(np.uint8(255 * imgArray[i]))

            # Videodatei wird freigegeben
            video.release()
            firstRun = False
            print("Video done")

    # Bildteile werden auf das Bild gelegt, diese bewegen sich nicht
    img[border:border+partHeight, width-border-partWidth:width-border] = partImg
    img[border:border+partHeight, border:border+partWidth] = partImg

    # Animation wird angezeigt
    cv2.imshow(title, img)
    if cv2.waitKey(5) == ord("q"):  # Programm schliessen
        break

cv2.destroyAllWindows()
