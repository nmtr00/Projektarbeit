import cv2
import numpy as np
from object_detector import *
img = cv2.imread("test2.tiff")

#Load Object Detector

detector = HomogeneousBgDetector()

contours = detector.detect_object(img)
#print(contours)

#Countour indizes list
contours_idx = []

#Draw object Boundaries

for cnt in contours:
    #Draw polygon for boundary contours with blue lines
    cv2.polylines(img, [cnt], True, (255, 0, 0), 0)

    # #Get rectangle
    # rect = cv2.minAreaRect(cnt)
    # (x, y), (w, h) , angle = rect
    # cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

    # box = cv2.boxPoints(rect)
    # box = np.int0(box)

    # cv2.polylines(img, [box], True, (0, 255, 0), 2) # Draw a box outside the contour
    # print(box)
contours = sorted(contours, key = lambda x: cv2.boundingRect(x)[0])

#List contours
for idx, contour in enumerate(contours):
    contours_idx.append(idx)
    print("Contours:", idx)
print(contours_idx)

if len(contours_idx)>>1:
    # Identify left and right contours
    left_contour = contours[0]
    right_contour = contours[len(contours_idx)-1]

    # Find the rightmost point of the left contour
    left_rightmost = tuple(left_contour[left_contour[:, :, 0].argmax()][0])
    right_leftmost = tuple(right_contour[right_contour[:, :, 0].argmin()][0])

    # Add marker to the rightmost point
    cv2.circle(img, left_rightmost, 1, (125, 125, 0), -1)
    cv2.circle(img, right_leftmost, 1, (125, 125, 0), -1)

    # Draw a red line connecting two points
    cv2.line(img, left_rightmost, right_leftmost, (0, 0, 255), 1)

    # Calculate distance between two points
    distance_pixels = np.sqrt((right_leftmost[0] - left_rightmost[0])**2 + (right_leftmost[1] - left_rightmost[1])**2)

    print("Distance between points in pixels:", distance_pixels)
# Save the output image as JPG
output_file = "output_image.tiff"
cv2.imwrite(output_file, img)
cv2.imshow("Image", img)
cv2.waitKey(0)
