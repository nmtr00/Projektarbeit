import cv2
import numpy as np
from object_detector import *
img = cv2.imread("obj.jpg")

#Load Object Detector

detector = HomogeneousBgDetector()

contours = detector.detect_object(img)
#print(contours)
#Draw object Boundaries

for cnt in contours:
    #Draw polygon for boundary contours
    cv2.polylines(img, [cnt], True, (255, 0, 0), 2)

    #Get rectangle
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h) , angle = rect
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.polylines(img, [box], True, (0, 255, 0), 2) # Draw a box outside the contour
    print(box)
cv2.imshow("Image", img)
cv2.waitKey(0)
