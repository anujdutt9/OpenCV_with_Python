# Show real time video from Camera
# Write the Video to .avi file

import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)               						# Access Default Webcam : 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))     # Output File; Codec; 20fps; Window Size 


while True:
    ret, frame = cap.read()             						# Open the camera and Start Viewing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  			# Convert color to Grayscale
    out.write(gray)                     						# Write the Video File
    cv2.imshow('frame',frame)           						# Colored Video
    cv2.imshow('gray',gray)             						# Grayscale Video
    
    # If Key Pressed, Break out of code
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()                           						# Release Camera Capture
out.release()                           						# Release Video Writing
cv2.destroyAllWindows()                 						#Destroy all Windows
