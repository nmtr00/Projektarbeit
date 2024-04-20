import cv2
import numpy as np
from object_detector import *
from contours_identifier import *
from point_detector import *
img = cv2.imread("test2.tiff")

#Load Object Detector

detector = HomogeneousBgDetector()

# Detect objects
contours = detector.detect_object(img)

# Instantiate ContourAnalyzer
analyzer = ContourAnalyzer()

# Get contour indices
contours_idx = analyzer.get_contour_indices(img, contours)
print(contours_idx)


if len(contours_idx)>>1:
    # Identify left and right contours
    left_contour, right_contour = analyzer.get_left_and_right_contours(contours)

    #Measure distance between two points
    measure = PointMeasure()
    distance = measure.distance_width(img, 30, left_contour, right_contour)
    # print("Distance between points in pixels:", distance)
# Save the output image as JPG
output_file = "output_image.tiff"
cv2.imwrite(output_file, img)
cv2.imshow("Image", img)
cv2.waitKey(0)
