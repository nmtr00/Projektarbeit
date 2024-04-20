import cv2
import numpy as np
class PointMeasure():
    def __int__(self):
        pass
    def distance_width(self, img, scaling, left, right):
        #Identify points
        left_point = tuple(left[left[:,:, 0].argmax()][0])
        right_point = tuple(right[right[:,:, 0].argmin()][0])

        #Add marker to both points
        cv2.circle(img, left_point, 1, (125, 125, 0), -1)
        cv2.circle(img, right_point, 1, (125, 125, 0), -1)
        
        cv2.line(img, left_point, right_point, (0, 0, 255), 1) #Draw a red line between two points
        # Calculate distance between two points
        distance_pixels = np.sqrt((right_point[0] - left_point[0])**2 + (right_point[1] - left_point[1])**2)
        distance_mm = distance_pixels / scaling
        cv2.putText(img, f'{distance_mm} mm', (left_point[0], right_point[1] -10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2) #Add measurement on the red line
        return distance_mm