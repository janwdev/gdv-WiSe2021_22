# Imports
import cv2

# Load image from File
img = cv2.imread("images/img1_Blocwald.jpg", cv2.IMREAD_COLOR)

# TODO bearbeiten
# groesse aendern
newWidth = 640
newHeight = 480
newSize = (newWidth, newHeight)
img = cv2.resize(img, newSize)

# Save Image again
cv2.imwrite("images/img1_Blocwald_out.jpg", img)

# Show image
title = "Hello OpenCV"  # Titel zum Anzeigen
cv2.namedWindow(title, cv2.WINDOW_GUI_NORMAL)
cv2.imshow(title, img)
# Warten damit Fenster nicht direkt geschlossen wird (0 wartet 0 ms bevor reagiert bei Fenster schliessen)
cv2.waitKey(0)
cv2.destroyAllWindows()  # schliesst alle Fenster (zur Sicherheit)
