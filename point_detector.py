import cv2
import numpy as np
class PointMeasure():
    def __int__(self):
        pass
    def distance_width(self, img, scaling, left, right, x_correction):
        delta_x = x_correction
        #Identify points
        left_point = tuple(left[left[:,:, 0].argmax()][0])
        
        right_point = tuple(right[right[:,:, 0].argmin()][0])

        left_point = (left_point[0] - delta_x, left_point[1])
        right_point = (right_point[0] + delta_x, right_point[1])

        #Add marker to both points
        cv2.circle(img, left_point, 1, (125, 125, 0), -1)
        cv2.circle(img, right_point, 1, (125, 125, 0), -1)
        
        cv2.line(img, left_point, right_point, (0, 0, 255), 1) #Draw a red line between two points
        # Calculate distance between two points
        distance_pixels = np.sqrt((right_point[0] - left_point[0])**2 + (right_point[1] - left_point[1])**2)
        distance_mm = distance_pixels / scaling
        cv2.putText(img, f'{distance_mm} mm', (left_point[0], right_point[1] -10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5) #Add measurement on the red line
        return distance_mm
    def distance_height(self, img, scaling, contour):
        
        # Calculate moments of the contour
        M = cv2.moments(contour)

        # Calculate centroid
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
        centroid_point = (x, y)
        # Get the dimensions of the image
        height, width = img.shape[:2]
        # Define the coordinates for the bottom edge
        reference_y = height
        reference_x = x
        reference_point = (reference_x, reference_y)
        cv2.line(img, centroid_point, reference_point, (0, 0, 255), 1) #Draw a red line between two points

        # Calculate distance between two points
        distance_pixels = y
        distance_mm = distance_pixels / scaling
        cv2.putText(img, f'{distance_mm} mm', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 5) #Add measurement on the red line

        return