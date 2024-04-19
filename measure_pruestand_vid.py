import cv2
import numpy as np
from object_detector import *
# Load the video file
cap = cv2.VideoCapture('your_video_file.mp4')  # Replace 'your_video_file.mp4' with your video file path

# Check if the video file opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()
#Load Object Detector

detector = HomogeneousBgDetector()
while True:
    #Read a frame from the vieeo
    ret, frame = cap.read()

    if not ret:
        print("End of video.")
        break

    contours = detector.detect_object(frame)
    #print(contours)

    #Countour indizes list
    contours_idx = []

    #Draw object Boundaries

    for cnt in contours:
        #Draw polygon for boundary contours with blue lines
        cv2.polylines(frame, [cnt], True, (255, 0, 0), 1)

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
    #     print("Contours:", idx)
    # print(contours_idx)

    if len(contours_idx)>>1:
        # Identify left and right contours
        left_contour = contours[0]
        right_contour = contours[len(contours_idx)-1]

        # Find the rightmost point of the left contour
        left_rightmost = tuple(left_contour[left_contour[:, :, 0].argmax()][0])
        right_leftmost = tuple(right_contour[right_contour[:, :, 0].argmin()][0])

        # Add marker to the rightmost point
        cv2.circle(frame, left_rightmost, 2, (125, 125, 0), -1)
        cv2.circle(frame, right_leftmost, 2, (125, 125, 0), -1)

        # Draw a red line connecting two points
        cv2.line(frame, left_rightmost, right_leftmost, (0, 0, 255), 1)

         # Calculate distance between two points
        distance_pixels = np.sqrt((right_leftmost[0] - left_rightmost[0])**2 + (right_leftmost[1] - left_rightmost[1])**2)
        scaling = 30
        distance_mm = distance_pixels / scaling
        cv2.putText(frame, f'{distance_mm} mm', (right_leftmost[0], left_rightmost[1] + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2) #Add measurement on the red line

        print("Distance between points in pixels:", distance_pixels)
        cv2.imshow("Image", frame)  #Display the frame

        # Check for key press; If 'q' is pressed, exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
