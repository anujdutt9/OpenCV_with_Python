# Input Image, Convert to Grayscale, Write to current folder
# Show Image using Matplotlib and OpenCV

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE)
#---------------- Show Image using OpenCV ---------------#
cv2.imshow('image',img)
cv2.imwrite('gra_image.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#---------- Show Image Using Matplotlib ------------------#

plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80,100], 'g',linewidth=5)
plt.show()


