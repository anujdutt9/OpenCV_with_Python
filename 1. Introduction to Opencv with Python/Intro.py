# Input Image, Convert to Grayscale, Write to current folder
# Show Image using Matplotlib and OpenCV

import cv2                                              # Import OpenCV
import matplotlib.pyplot as plt                         # Import pyplot from Matplotlib
import numpy as np                                      # Import Numpy

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)     # Read in the Image and Convert it to Grayscale


#---------------- Show Image using OpenCV ---------------#
cv2.imshow('image',img)                                 # Show the image with name 'image'
cv2.imwrite('gray_image.png',img)                       # Write Image to current folder
cv2.waitKey(0)                                          # Wait till key is pressed
cv2.destroyAllWindows()                                 # Destroy all Windows and exit


#---------- Show Image Using Matplotlib ------------------#
plt.imshow(img, cmap='gray', interpolation='bicubic')   # Show Image in Grayscale
#plt.plot([50,100],[80,100], 'g',linewidth=5)           # Prints a line on the Image og "green" color, line width = 5
plt.show()                                              # Show Image

#------------------ EOC ------------------#
