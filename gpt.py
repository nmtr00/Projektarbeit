import cv2
import numpy as np

# Load the image
image = cv2.imread('obj_2.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image to isolate the red areas
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
thresh = cv2.bitwise_not(thresh)
# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by their x-coordinate
contours = sorted(contours, key=lambda x: cv2.boundingRect(x)[0])
print("Contours:")
for idx, contour in enumerate(contours):
    print("Contour", idx)
# Identify left and right contours
left_contour = contours[0]
right_contour = contours[1]

# Draw contours
cv2.drawContours(image, [left_contour], -1, (0, 255, 0), 2)
cv2.drawContours(image, [right_contour], -1, (0, 255, 0), 2)

# Find the rightmost point of the left contour
left_rightmost = tuple(left_contour[left_contour[:, :, 0].argmax()][0])

# Add marker to the rightmost point
cv2.circle(image, left_rightmost, 5, (125, 125, 0), -1)

# Find topmost and bottommost points of left contour
left_top = tuple(left_contour[left_contour[:, :, 1].argmin()][0])
left_bottom = tuple(left_contour[left_contour[:, :, 1].argmax()][0])

# Find topmost and bottommost points of right contour
right_top = tuple(right_contour[right_contour[:, :, 1].argmin()][0])
right_bottom = tuple(right_contour[right_contour[:, :, 1].argmax()][0])

# Add text annotations to the image
cv2.putText(image, 'Left Object', (left_top[0], left_top[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
cv2.putText(image, 'Right Object', (right_top[0], right_top[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

print("Rightmost point of the left contour:", left_rightmost)
# Show the image with contours, annotations, and marker
cv2.imshow('Image with Contours, Object Names, and Marker', image)
#cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
