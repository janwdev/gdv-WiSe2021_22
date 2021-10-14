import cv2

img = cv2.imread('own_Lara/img/garden.PNG', cv2.IMREAD_COLOR)
print(img)

# resize image with 'resize'
newWidth = 640
newHight = 480
newSize =(newWidth,newHight)
img = cv2.resize(img,newSize)

#rotate image 90°
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('own_Lara/img_out.jpg',img)

title = 'Hello OpenCV'
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img)
cv2.waitKey(0)  # wartet unendlich bis jemand taste drückt
cv2.destroyAllWindows()
