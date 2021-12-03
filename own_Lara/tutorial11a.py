import numpy as np
import cv2
import math

# Load image and resize for better display
img = cv2.imread('images\\nl_clown.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(400,400), interpolation=cv2.INTER_CUBIC)
rows,cols,dims = img.shape

# define translation matrix for translation about 100 pixels to the right and 50 up
T_translation = np.float32([
    [1,0,100],
    [0,1,-50]
    ])
print('\nTranslation\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_translation]))
# apply translation matrix on image using cv2.warpAffine
dst_translation =cv2.warpAffine(img, T_translation(rows,cols))

# define anisotropic scaling matrix that stretches to double length horizontally 
# and squeezes vertically to the half height
T_anisotropic_scaling = np.float32([
    [2,0,0],
    [0,0.5,0]
    ])
print('\nAnisotropic scaling\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_anisotropic_scaling]))
# apply anisotropic scaling matrix on image using cv2.warpAffine
dst_anisotropic_scaling =cv2.warpAffine(img,T_anisotropic_scaling(rows*2,int(cols/2)))

# define rotation matrix for 45° clockwise rotation
deg = 45
rad = math.radians(deg)

T_rotation = np.float32([
    [math.cos(rad),-math.sin(rad),0],
    [math.sin(rad),math.cos(rad),0]
    ])
print('\nRotation\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_rotation]))
# apply rotatio matrix on image using cv2.warpAffine
dst_rotation = cv2.warpAffine(img,T_rotation(rows,cols))

# Rotate around image center for 45° counterclockwise using cv2.getRotationMatrix2D
center = (int((rows-1)/2), int((cols-1)/2))
T_rotation_around_center =  cv2.getRotationMatrix2D(center,deg,1)

#print('\nRotation around center\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_rotation_around_center]))
# apply rotatio matrix on image using cv2.warpAffine
dst_rotation_around_center = np.zeros(img.shape,np.uint8)

# show the original and resulting images
cv2.imshow('Original',img)
cv2.imshow('Translation',dst_translation)
cv2.imshow('Anisotropic scaling',dst_anisotropic_scaling)
cv2.imshow('Rotation',dst_rotation)
cv2.imshow('Rotation around center',dst_rotation_around_center)

# keep images open until key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()