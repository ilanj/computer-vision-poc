# Python programe to illustrate
# arithmetic operation of
# addition of two images

# organizing imports
import cv2
import numpy as np

# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('136.JPG')
image2 = cv2.imread('137.JPG')
image3 = cv2.imread('qr_code.png')

# cv2.addWeighted is applied over the
# image inputs with applied parameters
weightedSum = cv2.add(image1, image2)

# the window showing output image
# with the weighted sum
cv2.imshow('Weighted Image', weightedSum)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()