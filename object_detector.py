import cv2
class HomogeneousBgDetector():
    def __init__(self):
        pass
    def detect_object(self, frame):
        #Convert to gray scale
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

        #Create a Mask with adaptive threshold
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 26)     

        #Find contours
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # cv2.imshow("mask", mask)
        object_contours = []

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 7000:
                object_contours.append(cnt)
        return object_contours