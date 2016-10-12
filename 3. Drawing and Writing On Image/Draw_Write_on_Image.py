# Drawing Line, Circle, Rectangle, Polygon on Image
# Writing on Image

import cv2                                                                          # Import OpenCV
import matplotlib.pyplot as plt                                                     # Import pyplot from Matplotlib
import numpy as np                                                                  # Import Numpy

img = cv2.imread('image.png')                                                       # Load Image
##cv2.imshow('image', img)                                                          # Show the Image
##gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                                       # Convert Image to Grayscale
##cv2.imshow('grayscale',gray)                                                      # Show Grayscale Image

# Image; Staring point; Ending point; BGR Color (255,255,255); Line Width  
cv2.line(img,(100,120),(200,230),(120,200,50), 15)                                  # Draw a Line on Image

# Rectangle: Top Left; Bottom Right; Color; Line Width
cv2.rectangle(img, (15,25), (200,15), (220,150,50), 5)                              # Draw a Rectangle on Image

# Circle: center; radius; color; line width (-1: Fills in the circle)
cv2.circle(img, (200,300), 55, (20,150,50), -1)                                     # Draw Circle on Image

# Polygon:
pts =  np.array([[100,50],[250,100],[220,230],[270,220]], np.int32)                 # Co-ordinates of side points of Polygon
#pts = pts.reshape((-1,1,2))                                                        # Reshapes the Array to 1:2
cv2.polylines(img, [pts], True, (0,255,255), 3)                                     # Draw Polygon on Image

# Write text on Image
font = cv2.FONT_HERSHEY_SIMPLEX                                                     # Set Font Style of Text
cv2.putText(img, 'Hello OpenCV !!', (0,130), font, 1, (200,255,255), 2, cv2.LINE_AA)# 1: Font Size;  2: Thickness

cv2.imwrite('new_image.png',img)                                                    # Write Image to current folder

cv2.imshow('image',img)                                                             # Show Image
cv2.waitKey(0)                                                                      # Wait till a key is pressed
cv2.destroyAllWindows()                                                             # Destroy All Windows and Exit

#----------------- EOC --------------------#


