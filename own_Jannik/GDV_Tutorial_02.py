import cv2
import copy

# loading images in grey and color
img_grey = cv2.imread('images/hfu_klein.jpeg', cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread('images/hfu_klein.jpeg', cv2.IMREAD_COLOR)
img = copy.copy(img_grey)  # copy erstellt Kopie, anstatt = nur die Referenz

# do some print out about the loaded data
print(type(img))
print(img.shape)

# Extract the size or resolution of the image
width = img.shape[1]
height = img.shape[0]

# Abschnitt funktioniert nicht!
# print first row
# print(img[0])
# print first column
# von jeder Zeile nur der 0te Wert (Doppelpunkt ist besonderer Operatorn (start:ende), nur : ist von Anfang bis Ende)
# print(img[0:height-1][0])

# set area of the image to black
for i in range(50, 80):
    # for j in range(40, 80, 3): # Von 40 bis 80 im Abstand 3
    for j in range(40, 80):
        img[i][j] = 0 # bei Graubildern
        # bei Farbbildern (BGR als Farbwerte, nicht RGB)
        # img[i][j] = (255, 0, 0)

# find all used colors in the image (Beispiel fuer Grayscale)
colors = []
for i in range(0, width):
    for j in range(0, height):
        currentColor = img[j][i]
        if colors.count(currentColor) == 0:
            colors.append(currentColor)
colors.sort() # sortiert array
print(colors)

# copy one part of an image into another one
partImg = img[30:105, 5:130]
img[115:190,150:275] = partImg


# save image

# show the image
title = "Tutorial 2"  # Titel zum Anzeigen (Fenster)
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()