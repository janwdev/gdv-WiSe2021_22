import numpy as np
import cv2

# Load image and resize for better display
img = cv2.imread('images\\nl_clown.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img,(400,400), interpolation=cv2.INTER_CUBIC)
rows,cols,dims = img.shape

# define translation matrix
T_translation = np.float32([
    [1,0,0],
    [0,1,0]
    ])
print('\nTranslation\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_translation]))
# apply translation matrix on image
dst_translation = np.zeros(img.shape,np.uint8)

# define anisotropic scaling matrix
T_anisotropic_scaling = np.float32([
    [1,0,0],
    [0,1,0]
    ])
print('\nAnisotropic scaling\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_anisotropic_scaling]))
# apply anisotropic scaling matrix on image
dst_anisotropic_scaling = np.zeros(img.shape,np.uint8)

# define rotation matrix

T_rotation = np.float32([
    [1,0,0],
    [0,1,0]
    ])
print('\nRotation\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_rotation]))
# apply translation matrix on image
dst_rotation = np.zeros(img.shape,np.uint8)

# Rotate around image center

T_rotation_around_center = np.float32([
    [1,0,0],
    [0,1,0]
    ])
print('\nRotation around center\n','\n'.join(['\t'.join(['%03.3f' % cell for cell in row]) for row in T_rotation_around_center]))
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