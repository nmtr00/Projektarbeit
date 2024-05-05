import cv2
class HomogeneousBgDetector():
    def __init__(self):
        pass
    def detect_object(self, frame, min_area, mask_min, mask_max):
        #Convert to gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

        #Create a Mask with adaptive threshold
        # mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 21)  
        mask = cv2.inRange(gray, mask_min, mask_max)   
        # cv2.imshow("gray", gray)
        # cv2.imshow("mask", mask)
        
        #Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        object_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > min_area:
                object_contours.append(cnt)
        return object_contours