import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('image.png')               # Load Image
##cv2.imshow('image', img)
##gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##cv2.imshow('grayscale',gray)

# Image; Staring point; Ending point; BGR Color (255,255,255); Line Width  
cv2.line(img,(100,120),(200,230),(120,200,50), 15)          # Print a Line on Image

# Rectangle: Top Left; Bottom Right; Color; Line Width
cv2.rectangle(img, (15,25), (200,15), (220,150,50), 5)

# Circle: center; radius; color; line width (-1: Fills in the circle)
cv2.circle(img, (200,300), 55, (20,150,50), -1)

# Polygon:
pts =  np.array([[100,50],[250,100],[220,230],[270,220]], np.int32)
#pts = pts.reshape((-1,1,2))                                 # Reshapes the Array to 1:2
cv2.polylines(img, [pts], True, (0,255,255), 3)

# Write text on Image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Hello OpenCV !!', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)            # 1: Font Size;  2: Thickness

cv2.imwrite('new_image.png',img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
